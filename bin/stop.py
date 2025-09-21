#!/usr/bin/env python3

from subprocess import Popen, run

from valkey import Valkey
from valkey.exceptions import ConnectionError

from project.default import get_homedir, get_socket_path


def main() -> None:
    get_homedir()
    p = Popen(['shutdown'])
    p.wait()
    try:
        r = Valkey(unix_socket_path=get_socket_path('cache'), db=1)
        r.delete('shutdown')
        print('Shutting down databases...')
        p_backend = run(['run_backend', '--stop'])
        p_backend.check_returncode()
        print('done.')
    except ConnectionError:
        # Already down, skip the stacktrace
        pass


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import logging

from valkey import ConnectionPool, Valkey
from valkey.connection import UnixDomainSocketConnection

from .default import get_config, get_socket_path


class ProjectName():

    def __init__(self) -> None:
        self.logger = logging.getLogger(f'{self.__class__.__name__}')
        self.logger.setLevel(get_config('generic', 'loglevel'))

        self.valkey_pool: ConnectionPool = ConnectionPool(connection_class=UnixDomainSocketConnection,
                                                          path=get_socket_path('cache'), decode_responses=True)

    @property
    def valkey(self) -> Valkey:
        return Valkey(connection_pool=self.valkey_pool)

    def check_valkey_up(self) -> bool:
        return self.valkey.ping()  # type: ignore[return-value]

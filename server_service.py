#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: server_service.py
@time: 16-3-10 下午4:26
"""


import time
from rpyc import Service
from tools.logger import Logger
log = Logger('server_service', 'logs/server_service.log').get()


class ServerService(Service):
    def exposed_get_utc(self):
        return time.time()

    def exposed_get_time(self):
        log.debug('test debug')
        log.info('test info')
        return time.ctime()

    def exposed_bar(self):
        return self._conn.root.foo() + "bar"

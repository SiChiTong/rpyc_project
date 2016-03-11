#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: client_service.py
@time: 16-3-10 下午7:57
"""


from rpyc import Service


class ClientService(Service):
    def exposed_foo(self):
        return "foo"

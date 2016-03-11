#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: client.py
@time: 16-3-10 下午4:25
"""


import rpyc
from client_service import ClientService
from config import server_web


c = rpyc.connect(server_web['host'], server_web['port'], service=ClientService)
print("server's time is", c.root.get_time())
print("remote's bar result is", c.root.bar())

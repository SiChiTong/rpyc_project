#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: server.py
@time: 16-3-10 下午4:25
"""


from rpyc.utils.server import ThreadedServer
from server_service import ServerService
from config import server_web
import logging
# 日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(filename)s - [line:%(lineno)d] - %(levelname)s - %(message)s',
    filename='logs/server.log'
)


if __name__ == "__main__":
    s = ThreadedServer(ServerService, port=server_web['port'], auto_register=True)
    s.start()

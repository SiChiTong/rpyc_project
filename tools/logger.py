#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: logger.py
@time: 16-3-10 下午6:26
"""


import logging


class Logger(object):
    def __init__(self, logger, log_name):
        """
        日志初始化
        from tools.logger import Logger
        log = Logger('app', log_name='app.log').get()
        log.info('info message')
        :param logger:
        :param log_name:
        :return:
        """
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        logger_fmt = '%(asctime)s - %(name)s - %(filename)s - [line:%(lineno)d] - %(levelname)s - %(message)s'
        formatter = logging.Formatter(logger_fmt)
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get(self):
        return self.logger


if __name__ == '__main__':
    log = Logger('app', log_name='app.log').get()
    log.info('info message')

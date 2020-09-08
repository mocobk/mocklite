#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : flask_logger.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/7/16 19:37
import logging
from logging.handlers import RotatingFileHandler
from flask import request


class CustomFormatter(logging.Formatter):
    """自定义格式化类"""

    def format(self, record):
        """每次输出日志时都会调用"""
        # 获取请求的 path
        record.path = request.path
        # 获取请求的 method
        record.method = request.method
        # 获取客户端的ip
        record.remote_ip = request.remote_addr

        return super().format(record)


def init_logger(app):
    """
    配置 flask 日志, 可在 config 中配置如下 key

    # 配置 console 输出的日志级别 （默认）
    LOG_LEVEL = logging.WARNING

    # 配置 file 输出的日志路径和日志级别 （可选）
    FILE_LOGGER = {
        'path': os.path.join(os.path.dirname(__file__), 'flask.log'),
        'log_level': logging.DEBUG
    }

    没有 app 上下文的情况下调用：
    from app.libs.flask_logger import logger
    logger.info('我的日志')

    有 app 上下文的情况下调用：
    app.logger.info('我的日志')

    输出：
    [2020-07-16 20:34:27,874] 127.0.0.1 GET /v1/test   INFO: console 日志
    [2020-07-16 20:34:39,364] 127.0.0.1 GET /v1/test TestFlyServer/app/api/v1/test.py 27   INFO: file 日志
    """
    # 创建flask.app日志器
    flask_logger = logging.getLogger('flask.app')
    # 设置全局级别
    flask_logger.setLevel(app.config.get('LOG_LEVEL', 'WARNING'))

    # 创建控制台处理器
    console_handler = logging.StreamHandler()

    # 设置输出格式
    console_formatter = CustomFormatter(
        fmt='[%(asctime)s] %(remote_ip)s %(method)s %(path)s %(levelname)6s: %(message)s'
    )
    console_handler.setFormatter(console_formatter)

    # 日志器添加处理器
    flask_logger.addHandler(console_handler)

    file_logger = app.config.get('FILE_LOGGER')
    if file_logger:
        # 创建文件处理器, 当达到限定的文件大小时, 将日志转存到其他文件中
        file_handler = RotatingFileHandler(filename=file_logger['path'], encoding='utf-8', maxBytes=100 * 1024 * 1024,
                                           backupCount=10)

        # 给处理器设置输出格式
        file_formatter = CustomFormatter(
            fmt='[%(asctime)s] %(remote_ip)s %(method)s %(path)s %(pathname)s %(lineno)d %(levelname)6s: %(message)s'
        )
        file_handler.setFormatter(file_formatter)
        # 单独设置文件处理器的日志级别
        file_handler.setLevel(file_logger.get('log_level', 'WARNING'))

        # 日志器添加处理器
        flask_logger.addHandler(file_handler)


logger = logging.getLogger('flask.app')

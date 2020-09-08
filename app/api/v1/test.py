#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : user.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/1/8 14:39
import socket
import time

from flask import Blueprint

from app.libs.flask_logger import logger
from app.libs.flask_restful import Api, Resource
from app.libs.response import Success

blueprint = Blueprint('test', __name__)

api = Api(blueprint)


@api.resource('')
class DemoTest(Resource):
    method_decorators = []

    def get(self):
        logger.info('收到测试请求')
        hostname = socket.gethostname()
        data = {
            'hostname': socket.gethostname(),
            'ip': socket.gethostbyname(hostname),
            'say': 'Hi mocobk',
            'time': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        return Success(data=data)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/9/8 9:53
from flask import Blueprint

from app.libs.flask_restful import Api, Resource, RequestParser
from app.libs.response import Success
from proxy import ProxyManager

blueprint = Blueprint('proxy', __name__)

api = Api(blueprint)


@api.resource('/')
class ProxyManagerResource(Resource):

    def get(self):
        parser = RequestParser()
        parser.add_argument('option', location='args', choices=('start', 'restart', 'stop'))
        arg = parser.parse_args()
        is_success = getattr(PROXY, arg.option)()
        if is_success:
            return Success(data={'option': arg.option, 'status': 1})
        else:
            return Success(data={'option': arg.option, 'status': 0})

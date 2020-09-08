#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : flask_restful.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/1/9 15:44
from flask import current_app
from flask_restful import Api as _Api, Resource as __Resource
from flask_restful.reqparse import RequestParser as _RequestParser
from werkzeug.exceptions import HTTPException
from marshmallow import ValidationError

from app.libs.response import APIException, BadRequest, ServiceInternalError
from traceback import print_exc

class Resource(__Resource):
    pass

class Api(_Api):
    def handle_error(self, e):
        """
        用于处理 flask_restful Api 内部抛出的所有错误
        包括 RequestParser Marshmallow参数校验异常等
        替代了注册全局异常: app.register_error_handler(Exception, global_error)

        Error handler for the API transforms a raised exception into a Flask
        response, with the appropriate HTTP status code and body.

        :param e: the raised Exception object
        :type e: Exception

        """
        print_exc()  # 打印所有异常栈，方便分析日志
        # 自定义的异常抛出 HTTPException，有 e.response
        # RequestParser 参数校验异常也会抛出 HTTPException，但 e.response
        if isinstance(e, HTTPException):
            if e.response is None:
                message = e.data.get('message', e.data) if hasattr(e, 'data') and isinstance(getattr(e, 'data'),
                                                                                             dict) else e.description
                e = APIException(
                    message=message,
                    code=e.code,
                    error_code=e.name.replace(' ', '')
                )

        # Marshmallow参数校验异常会抛出 ValidationError
        elif isinstance(e, ValidationError):
            e = BadRequest(
                message=e.messages,
                error_code='SchemaValidationError'
            )

        else:
            # 如果不属于 HTTPException 或 ValidationError 则打印错误并抛出默认的 ServiceInternalError
            e = ServiceInternalError()

        return super().handle_error(e)


class RequestParser(_RequestParser):
    def add_argument(self, name, default=None, dest=None, required=True,
                     ignore=False, type=str, location=('json', 'values',),
                     choices=(), action='store', help=None, operators=('=',),
                     case_sensitive=True, store_missing=False, trim=False,
                     nullable=True):
        """Adds an argument to be parsed.

        Accepts either a single instance of Argument or arguments to be passed
        into :class:`Argument`'s constructor.

        See :class:`Argument`'s constructor for documentation on the
        available options.
        """

        return super().add_argument(name, default=default, dest=dest, required=required,
                                    ignore=ignore, type=type, location=location,
                                    choices=choices, action=action, help=help, operators=operators,
                                    case_sensitive=case_sensitive, store_missing=store_missing, trim=trim,
                                    nullable=nullable)

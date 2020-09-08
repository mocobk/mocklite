#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : response.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/1/9 10:17

from flask import request as _request, json
from werkzeug.datastructures import Headers
from werkzeug.exceptions import HTTPException
from werkzeug.wrappers import Response as ResponseBase



"""
APISuccess APIException 都使用了 flask.json 来序列化 response, 其与内置 json 参数一致，
支持在 config 中配置参数（JSON_AS_ASCII JSON_SORT_KEYS）以及更多的对象支持：

The default Flask JSON encoder. This one extends the default
encoder by also supporting ``datetime``, ``UUID``, ``dataclasses``,
and ``Markup`` objects.
"""


class APISuccess(ResponseBase):
    """成功响应，flask_restful 直接返回 Response 对象给 flask 处理
    Response -> flask_restful.Resource.dispatch_request
    """
    code = 200

    def __init__(self, data=None, code=None, headers: dict = None):
        if code:
            self.code = code
        self._headers = headers if headers is not None else {}
        super().__init__(
            response=json.dumps(data, ensure_ascii=False) if data is not None else data,
            status=self.code,
            headers=Headers(self._headers),
            content_type='application/json',
        )


class APIException(HTTPException):
    """
    异常响应，返回错误 code 和 message
    继承 HTTPException 主要是为了统一处理自定义库和第三方库抛出的异常
    HTTPException -> flask_restful.Api.handle_error
    """
    code = 500
    error_code = 'ServiceInternalError'
    message = 'Unknow service internal error.'
    _headers = {}

    def __init__(self, message=None, code=None, error_code=None, headers: dict = None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if message:
            self.message = message
        if headers:
            self._headers = headers

        self._data = {
            'message': self.message,
            'code': self.error_code,
        }

        super().__init__(
            self.message,
            response=ResponseBase(
                response=json.dumps(self._data, ensure_ascii=False),
                status=self.code,
                headers=Headers(self._headers),
                content_type='application/json',
            ))


"""
| code | message               | method            | description                                                              |
|------|-----------------------|-------------------|--------------------------------------------------------------------------|
| 200  | OK                    | [GET]             | 服务器成功返回用户请求的数据，该操作是幂等的（Idempotent）               |
| 201  | CREATED               | [POST/PUT/PATCH]  | 用户新建或修改数据成功                                                   |
| 202  | Accepted              | [*]               | 表示一个请求已经进入后台排队（异步任务）                                 |
| 204  | NO CONTENT            | [DELETE]          | 用户删除数据成功                                                         |
| 400  | INVALID REQUEST       | [POST/PUT/PATCH]  | 用户发出的请求有错误，服务器没有进行新建或修改数据的操作，该操作是幂等的 |
| 401  | Unauthorized          | [*]               | 表示用户没有权限（令牌、用户名、密码错误）                               |
| 403  | Forbidden             | [*]               | 表示用户得到授权（与401错误相对），但是访问是被禁止的                    |
| 404  | NOT FOUND             | [*]               | 用户发出的请求针对的是不存在的记录，服务器没有进行操作，该操作是幂等的   |
| 406  | Not Acceptable        | [GET]             | 用户请求的格式不可得（比如用户请求JSON格式，但是只有XML格式）            |
| 410  | Gone                  | [GET]             | 用户请求的资源被永久删除，且不会再得到的                                 |
| 422  | Unprocesable entity   | [POST/PUT/PATCH]  | 当创建一个对象时，发生一个验证错误                                       |
| 500  | INTERNAL SERVER ERROR | [*]               | 服务器发生错误，用户将无法判断发出的请求是否成功                         |
"""


class Success(APISuccess):
    code = 200


class CreateSuccess(APISuccess):
    code = 201


class UpdateSuccess(APISuccess):
    code = 201


class DeleteSuccess(APISuccess):
    code = 204


class BadRequest(APIException):
    code = 400
    error_code = 'BadRequest'
    message = 'Bad request parameters or illegal request.'


class NotFound(APIException):
    code = 404
    error_code = 'NotFound'
    message = 'The resource are not found.'


class ServiceInternalError(APIException):
    code = 500
    error_code = 'ServiceInternalError'
    message = 'Unknow service internal error.'

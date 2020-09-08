#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : __init__.py.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/1/15 11:07
from contextlib import contextmanager

from marshmallow import ValidationError

from app.libs.response import BadRequest


@contextmanager
def auto_validate():
    """反序列化为模型时异常校验"""
    try:
        yield
    except ValidationError as err:
        raise BadRequest(message=err.messages)

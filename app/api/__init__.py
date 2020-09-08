#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : __init__.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/1/8 14:39

from app.api.v1 import mock, test
from app.libs.blueprint import NestableBlueprint


def create_blueprint(name, views: list, **kwargs):
    # 使用嵌套蓝图划分版本
    blueprint = NestableBlueprint(name, __name__, url_prefix=f'/{name}', **kwargs)

    for view in views:
        # 子蓝图未配置 url_prefix 则取其 name 为 url_prefix
        url_prefix = view.blueprint.url_prefix or f'/{view.blueprint.name}'
        blueprint.register_blueprint(view.blueprint, url_prefix=url_prefix, endpoint='v1')
    return blueprint


v1_blueprint = create_blueprint('v1', [mock, test])

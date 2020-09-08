#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : redprint.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/1/8 15:20
from flask import Blueprint


class NestableBlueprint(Blueprint):
    def register_blueprint(self, blueprint, **options):
        def deferred(state):
            # 将 NestableBlueprint.name 与 blueprint.name 合并 eg.  v1.user
            blueprint.name = f'{self.name}.{blueprint.name}'
            url_prefix = (state.url_prefix or u"") + (options.get('url_prefix', blueprint.url_prefix) or u"")
            if 'url_prefix' in options:
                del options['url_prefix']
            state.app.register_blueprint(blueprint, url_prefix=url_prefix, **options)
        self.record(deferred)

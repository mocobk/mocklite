#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : __init__.py.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/1/8 14:34

from flask import Flask

from app.extensions import register_extensions
from config import CONFIG


def register_blueprints(_app):
    from app.api import v1_blueprint
    _app.register_blueprint(v1_blueprint)

# 创建 app 的工厂函数
def create_app(_config=CONFIG):
    # 创建app实例对象
    app = Flask(__name__)

    # 加载配置
    app.config.from_object(_config)
    # 注册蓝本（需要在 db.create_all 之前，以便先加载 models，然后创建表）
    register_blueprints(app)
    # 注册扩展
    register_extensions(app)
    return app

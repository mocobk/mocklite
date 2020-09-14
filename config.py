#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import logging
import os

PROJECT_DIR = os.path.dirname(__file__)

print('__file__', __file__)
print('PROJECT_DIR', PROJECT_DIR)


class _Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    LOG_LEVEL = logging.INFO

    def __getitem__(self, item):
        return getattr(self, item)


class ProductionConfig(_Config):
    """生产环境"""
    SQLALCHEMY_DATABASE_URI = f"sqlite:////usr/src/sqlite3.db?charset=utf8mb4"


class DevelopmentConfig(_Config):
    """开发环境"""
    ENV = 'Development'
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{PROJECT_DIR}/sqlite3.db?charset=utf8mb4"

    SQLALCHEMY_ECHO = True  # 开启 sqlalchemy 调试模式，可输出 sql 语句
    DEBUG = False
    LOG_LEVEL = logging.DEBUG


__CONFIG = {
    'development': DevelopmentConfig(),
    'production': ProductionConfig()
}

CONFIG = __CONFIG[os.getenv('FLASK_ENV', 'development')]

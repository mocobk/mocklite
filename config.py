#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import logging
import os

PROJECT_DIR = os.path.dirname(__file__)


class _Config:
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    LOG_LEVEL = logging.WARNING

    def __getitem__(self, item):
        return getattr(self, item)


class ProductionConfig(_Config):
    """生产环境"""
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://admin:admin@mysql:3306/test_fly?charset=utf8mb4"


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

CONFIG = __CONFIG[os.getenv('MOCK_ENV', 'development')]

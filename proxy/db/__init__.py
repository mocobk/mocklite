#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/8/19 18:14
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from config import CONFIG

"""
connect 参数：check_same_thread = False，避免 mitmdump 使用并发模式时报错 
(sqlite3.ProgrammingError) SQLite objects created in a thread can only be used in that same thread.
"""
engine = create_engine(
    CONFIG.SQLALCHEMY_DATABASE_URI,
    echo=CONFIG.SQLALCHEMY_ECHO,
    connect_args={'check_same_thread': False}
)

# 创建对象的基类:
Base = declarative_base(bind=engine)

session: Session = sessionmaker(bind=engine)()


@contextmanager
def auto_commit():
    """通过 with db.auto_commit() 管理上下文，失败自动回滚"""
    try:
        yield
        session.commit()
    except Exception as e:
        session.rollback()
        raise e

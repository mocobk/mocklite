#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : user.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/1/8 16:08
from sqlalchemy import func

from app.models.base import ModelBase, db, SQLAlchemyAutoSchema


class MockProject(ModelBase):
    __tablename__ = 'mock_project'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(512))
    color = db.Column(db.String(50), comment='项目主题色')
    status = db.Column(db.Integer, server_default='1', comment='状态：1 正常，-1 删除')
    create_time = db.Column(db.DateTime, server_default=func.datetime('now', 'localtime'))
    update_time = db.Column(db.DateTime, server_default=func.datetime('now', 'localtime'),
                            server_onupdate=func.datetime('now', 'localtime'))

    def __repr__(self):
        return '<MockProject: id={} name={}>'.format(self.id, self.name)


class MockProjectSchema(SQLAlchemyAutoSchema):
    """orm 模型序列化"""

    class Meta:
        model = MockProject


class MockData(ModelBase):
    __tablename__ = 'mock_data'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, nullable=False)
    method = db.Column(db.String(10), nullable=False, server_default='GET')
    url = db.Column(db.String(2048), index=True, nullable=False)
    response = db.Column(db.Text)
    code = db.Column(db.Integer, server_default='200', comment='http 响应状态码：200（默认）')
    content_type = db.Column(db.String(30), server_default='application/json')
    headers = db.Column(db.Text)
    match_type = db.Column(db.Integer, server_default='0', comment='URL 匹配模式：0普通模式（默认），1 正则模式')
    status = db.Column(db.Integer, server_default='0', comment='Mock 数据状态：0关闭（默认），1 打开，-1 删除')
    description = db.Column(db.String(512))
    create_time = db.Column(db.DateTime, server_default=func.datetime('now', 'localtime'))
    update_time = db.Column(db.DateTime, server_default=func.datetime('now', 'localtime'),
                            server_onupdate=func.datetime('now', 'localtime'))

    def __repr__(self):
        return '<MockData: id={} method={} url={}>'.format(self.id, self.method, self.url)


class MockDataSchema(SQLAlchemyAutoSchema):
    """orm 模型序列化"""

    class Meta:
        model = MockData
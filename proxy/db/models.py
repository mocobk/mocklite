#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/8/19 18:15
from sqlalchemy import Column, String, Integer, DateTime, Text, func
from proxy.db import Base


class MockData(Base):
    __tablename__ = 'mock_data'

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, nullable=False)
    method = Column(String(10), nullable=False, server_default='GET')
    url = Column(String(2048), index=True, nullable=False)
    response = Column(Text)
    code = Column(Integer, server_default='200', comment='http 响应状态码：200（默认）')
    content_type = Column(String(30), server_default='application/json')
    headers = Column(Text)
    match_type = Column(Integer, server_default='0', comment='URL 匹配模式：0普通模式（默认），1 正则模式')
    status = Column(Integer, server_default='0', comment='Mock 数据状态：0关闭（默认），1 打开，-1 删除')
    description = Column(String(512))
    create_time = Column(DateTime, server_default=func.datetime('now', 'localtime'))
    update_time = Column(DateTime, server_default=func.datetime('now', 'localtime'),
                         server_onupdate=func.datetime('now', 'localtime'))

    def __repr__(self):
        return '<MockData: id={} method={} url={}>'.format(self.id, self.method, self.url)

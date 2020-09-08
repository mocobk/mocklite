#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/8/20 12:50

# 创建User类实例
from proxy import db
from proxy.db.models import MockData

db.Base.metadata.drop_all()
db.Base.metadata.create_all()

mock_data1 = MockData(project_id=1, method='GET', url='/v1/login',code=201, response='{"name":"@cname"}', status=1)
mock_data2 = MockData(project_id=1, method='GET', url='/v1/user', response='{a: 2}', status=0)
mock_data3 = MockData(project_id=1, method='GET', url='/v1/user', response='{a: 2}', status=-1)

if __name__ == '__main__':
    with db.auto_commit():
        db.session.add(mock_data1)
        db.session.add(mock_data2)
        db.session.add(mock_data3)
    print(db.session.query(MockData).filter_by(method='GET', status=1).all())
    # print(db.session.query(MockData).filter(MockData.method=='GET', MockData.status!=-1).all())

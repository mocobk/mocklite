#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : user.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/5/25 20:04
import re

from flask import Blueprint
from pymock import Mock
from sqlalchemy import or_, text, func

from app.extensions import db
from app.libs.flask_restful import Api, Resource, RequestParser
from app.libs.response import Success, CreateSuccess, UpdateSuccess, DeleteSuccess, DeleteFaild
from app.models.mock import MockData, MockDataSchema, MockProject, MockProjectSchema, MockDataWithCountSchema

blueprint = Blueprint('mock', __name__)

api = Api(blueprint)


class CommonRequestParser(RequestParser):
    def __init__(self):
        super().__init__()
        self.add_argument('page_size', required=False, type=int, location='args', default=100, store_missing=True)
        self.add_argument('page', required=False, type=int, location='args', default=1, store_missing=True)
        self.add_argument('search_words', required=False, type=str, location='args')


@api.resource('/projects')
class ProjectsResource(Resource):
    parser = RequestParser(trim=True)
    parser.add_argument('name')
    parser.add_argument('description', required=False)
    parser.add_argument('color', required=False)

    def get(self):
        args = CommonRequestParser().parse_args()
        search_words = args.get('search_words')
        projects_paginate = MockProject.query.filter(MockProject.status != -1,
                                                     or_(MockProject.name.like(f'%{search_words}%'),
                                                         MockProject.description.like(f'%{search_words}%')
                                                         ) if search_words else text('')
                                                     ).paginate(page=args.page, per_page=args.page_size)

        data = MockProjectSchema().dump(projects_paginate.items, many=True)
        return Success(data={
            'page': projects_paginate.page,
            'pages': projects_paginate.pages,
            'total': projects_paginate.total,
            'data': data,
        })

    def post(self):
        args = self.parser.parse_args()
        projects = MockProjectSchema().load(args)
        with db.auto_commit():
            db.session.add(projects)
        return CreateSuccess()


@api.resource('/projects/<int:id_>')
class ProjectDetailResource(Resource):

    def get(self, id_):
        project = MockProject.query.filter(MockProject.status != -1, MockProject.id == id_).first_or_404()
        data = MockProjectSchema().dump(project)
        return Success(data=data)

    def put(self, id_):
        args = ProjectsResource.parser.parse_args()
        project = MockProject.query.filter(MockProject.status != -1, MockProject.id == id_).first_or_404()
        project = MockProjectSchema().load(args, instance=project)

        with db.auto_commit():
            db.session.add(project)
        return UpdateSuccess()

    def delete(self, id_):
        project: MockProject = MockProject.query.filter(MockProject.status != -1, MockProject.id == id_).first_or_404()
        has_mock_data = MockData.query.filter(MockData.project_id == id_, MockData.status != -1).all()
        if has_mock_data:
            raise DeleteFaild(message='请先删除该项目下的所有 Mock 数据')
        project.status = -1
        with db.auto_commit():
            db.session.add(project)
        return DeleteSuccess()


@api.resource('/data')
class DataResource(Resource):
    parser = RequestParser(trim=True)
    parser.add_argument('project_id', type=int)
    parser.add_argument('method', choices=('GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'))
    parser.add_argument('url')
    parser.add_argument('match_type', type=int)
    parser.add_argument('request', required=False)
    parser.add_argument('content_type')
    parser.add_argument('headers', required=False)
    parser.add_argument('code', required=False)
    parser.add_argument('response', required=False)
    parser.add_argument('status', required=False)
    parser.add_argument('description', required=False)

    def get(self):
        """
        select a.*,b.count
        from mock_data a join
        (select max(id) as id,count(*) as count  from  mock_data  where project_id = 6 group by method,url) b
        on a.id=b.id ORDER BY a.create_time DESC;
        """
        parser: RequestParser = CommonRequestParser()
        parser.add_argument('project_id', type=int)
        args = parser.parse_args()

        search_words = args.get('search_words')

        sub_query = db.session.query(
            func.max(MockData.id).label('id'),
            func.count('*').label('count')
        ).filter(
            MockData.status != -1,
            MockData.project_id == args.project_id,
            or_(MockData.url.like(f'%{search_words}%'),
                MockData.description.like(f'%{search_words}%')
                ) if search_words else text('')
        ).group_by(MockData.method, MockData.url, MockData.match_type).subquery()

        mock_data_paginate = db.session.query(MockData, sub_query.c.count) \
            .join(sub_query, MockData.id == sub_query.c.id).paginate(page=args.page,
                                                                     per_page=args.page_size,
                                                                     error_out=False)

        data = MockDataWithCountSchema().dump(mock_data_paginate.items, many=True)
        return Success(data={
            'page': mock_data_paginate.page,
            'pages': mock_data_paginate.pages,
            'total': mock_data_paginate.total,
            'data': data,
        })

    def post(self):
        args = self.parser.parse_args()
        mock_data = MockDataSchema().load(args)
        with db.auto_commit():
            db.session.add(mock_data)
        return CreateSuccess()

    def delete(self):
        parser = RequestParser()
        parser.add_argument('ids', type=int, action='append')
        args = parser.parse_args()
        mock_data = MockData.query.filter(MockData.id.in_(args.ids)).all()
        for item in mock_data:
            db.session.delete(item)
        db.session.commit()
        return DeleteSuccess()


@api.resource('/data/filter')
class DataFilterResource(Resource):
    parser = RequestParser(trim=True)
    parser.add_argument('project_id', type=int)
    parser.add_argument('method', choices=('GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'), required=False)
    parser.add_argument('url', required=False)
    parser.add_argument('match_type', type=int, required=False)
    parser.add_argument('parent_id', type=int, required=False)

    def get(self):
        args = self.parser.parse_args()
        mock_data = MockData.query.filter(
            MockData.status != -1,
            MockData.project_id == args.project_id,
            (MockData.id != args.parent_id) if args.parent_id else text(''),
            (MockData.method == args.method) if args.method else text(''),
            (MockData.url == args.url) if args.url else text(''),
            (MockData.match_type == args.match_type) if args.match_type else text(''),
        ).all()
        data = MockDataSchema().dump(mock_data, many=True)
        return Success(data=data)


@api.resource('/data/<int:id_>')
class DataDetailResource(Resource):

    def get(self, id_):
        mock_data = MockData.query.filter(MockData.status != -1, MockData.id == id_).first_or_404()
        data = MockDataSchema().dump(mock_data)
        return Success(data=data)

    def put(self, id_):
        args = DataResource.parser.parse_args()
        mock_data = MockData.query.filter(MockData.status != -1, MockData.id == id_).first_or_404()
        mock_data = MockDataSchema().load(args, instance=mock_data)

        with db.auto_commit():
            db.session.add(mock_data)
        return UpdateSuccess()

    def delete(self, id_):
        mock_data: MockData = MockData.query.filter(MockData.status != -1, MockData.id == id_).first_or_404()
        mock_data.status = -1

        with db.auto_commit():
            db.session.add(mock_data)
        return DeleteSuccess()


@api.resource('/test')
class MockTest(Resource):
    parser = RequestParser(trim=True)
    parser.add_argument('url')
    parser.add_argument('match_type', required=False, default=0, store_missing=True)
    parser.add_argument('content_type', required=False)
    parser.add_argument('headers', required=False)
    parser.add_argument('response', required=False)
    parser.add_argument('target_url', required=False)

    mock = Mock().mock_js

    def post(self):
        args = self.parser.parse_args()
        if args.get('target_url'):
            is_match = args.url in args.target_url if args.match_type == 0 else bool(
                re.search(args.url, args.target_url, re.IGNORECASE))
        else:
            is_match = True

        headers = self.mock(args.headers) if args.get('headers') else {}
        response = self.mock(args.response) if args.get('response') else {}
        content_type = {"Content-Type": args.content_type} if args.get('content_type') else {}

        return Success(data={
            'is_match': is_match,
            'headers': {'Access-Control-Allow-Origin': '*', **content_type, **headers},
            'response': response,
        })

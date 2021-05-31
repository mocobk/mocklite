#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/8/20 16:43
import json
import re
import typing

from ilogger import logger
from mitmdump import DumpMaster, Options
from mitmproxy import ctx, http
from mitmproxy.script import concurrent
from mitmproxy.utils import human
from pymock import Mock
from jsonpath import jsonpath

from proxy import db
from proxy.db.models import MockData
from enum import Enum


class RuleType(Enum):
    FORM_DATA = 'form-data'
    X_WWW_FORM_URLENCODED = 'x-www-form-urlencoded'
    QUERY = 'query'
    HEADERS = 'headers'
    JSON = 'json'
    GraphQL = 'GraphQL'
    NULL = None


class FlowInterceptor:

    def __init__(self):
        self.mock = Mock().mock_js
        logger.info('FlowInterceptor init...')

    @staticmethod
    def running():
        logger.info('FlowInterceptor is running, proxy server listening at http://{}'.format(
            human.format_address(ctx.master.server.address)
        ))

    @staticmethod
    def get_json(text):
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return None

    @staticmethod
    def is_key_value_matched(flow_data: dict, key, value, match_type):
        flow_value = str(flow_data.get(key, ''))
        if match_type == 0:
            if value != flow_value:
                return False
        else:
            if not re.search(value, flow_value, re.IGNORECASE):
                return False
        return True

    def is_matched_request_data(self, flow: http.HTTPFlow, request_rules: list):
        flow_data_map = {
            RuleType.FORM_DATA: flow.request.multipart_form,
            RuleType.X_WWW_FORM_URLENCODED: flow.request.urlencoded_form,
            RuleType.HEADERS: flow.request.headers,
            RuleType.QUERY: flow.request.query
        }
        for item in request_rules:
            type_, key, value, match_type = (
                RuleType(item.get('type')),
                item.get('key'),
                item.get('value'),
                item.get('match_type')
            )
            if flow_data_map.get(type_):
                if not self.is_key_value_matched(flow_data_map[type_], key, value, match_type):
                    return False

            elif type_ == RuleType.JSON:
                flow_value = jsonpath(self.get_json(flow.request.text), key)
                if flow_value:
                    if not self.is_key_value_matched({key: flow_value[0]}, key, value, match_type):
                        return False
            elif type_ == RuleType.GraphQL:
                flow_json = self.get_json(flow.request.text) or {}
                if flow_json.get('operationName'):
                    query_name = flow_json.get('operationName')
                else:
                    query_list = re.findall(r'\S+', flow_json.get('query', ''), re.IGNORECASE)
                    try:
                        query_name = query_list[1].split('(')[0]
                    except IndexError:
                        return False
                if not self.is_key_value_matched({key: query_name}, key, value, match_type):
                    return False
            else:
                return False
        return True

    def get_matched_data(self, flow: http.HTTPFlow, mock_data: typing.List[MockData]) -> MockData:
        """用请求中的 URL 与数据库查询出的数据逐个匹配"""
        for mock_data in mock_data:
            if mock_data.match_type == 0:
                if mock_data.url in flow.request.url:
                    if mock_data.request:
                        if self.is_matched_request_data(flow, json.loads(mock_data.request)):
                            return mock_data

                    else:
                        return mock_data
            else:
                if re.search(mock_data.url, flow.request.url, re.IGNORECASE):
                    if mock_data.request:
                        if self.is_matched_request_data(flow, json.loads(mock_data.request)):
                            return mock_data

                    else:
                        return mock_data

    @concurrent  # 使用并发模式时，不能使用 ctx.log
    def request(self, flow: http.HTTPFlow):
        method, url = flow.request.method, flow.request.url
        mock_data = db.session.query(MockData).filter_by(method=method, status=1).all()

        match_data = self.get_matched_data(flow, mock_data)
        if match_data:
            logger.info('%s%6s %s', '▶', method, flow.request.path)
            content = json.dumps(self.mock(match_data.response), ensure_ascii=False) if match_data.response else ''
            content_type = {"Content-Type": match_data.content_type} if match_data.content_type else {}
            headers = self.mock(match_data.headers) if match_data.headers else {}

            logger.debug('Mock data: %s', content)
            flow.response = http.HTTPResponse.make(
                match_data.code,  # (optional) status code
                content,  # (optional) content
                {'Access-Control-Allow-Origin': '*', **content_type, **headers}
            )
        else:
            logger.info('%-2s%6s %s', '•', method, flow.request.path[:200] + (flow.request.path[200:] and '...'))


if __name__ == '__main__':
    opts = Options(listen_host='0.0.0.0', listen_port=8888, termlog_verbosity='warn', flow_detail=0, scripts=None,
                   block_global=False)
    m = DumpMaster(opts)
    m.addons.add(FlowInterceptor())
    m.run()

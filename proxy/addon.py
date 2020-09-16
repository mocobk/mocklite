#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/8/20 16:43
import json
import re
import typing

from mitmdump import DumpMaster, Options
from mitmproxy import ctx, http
from mitmproxy.script import concurrent
from mitmproxy.utils import human
from pymock import Mock

from proxy import db
from proxy.db.models import MockData
from ilogger import logger


class FlowInterceptor:

    def __init__(self):
        self.mock = Mock().mock_js
        logger.info('FlowInterceptor init...')

    def running(self):
        logger.info('FlowInterceptor is running, proxy server listening at http://{}'.format(
            human.format_address(ctx.master.server.address)
        ))

    def get_matched_data(self, url, mock_datas: typing.List[MockData]) -> MockData:
        """用请求中的 URL 与数据库查询出的数据逐个匹配"""
        for mock_data in mock_datas:
            if mock_data.match_type == 0:
                if mock_data.url in url:
                    return mock_data
            else:
                if re.match(mock_data.url, url, re.IGNORECASE):
                    return mock_data

    @concurrent  # 使用并发模式时，不能使用 ctx.log
    def request(self, flow: http.HTTPFlow):
        method, url = flow.request.method, flow.request.url
        mock_datas = db.session.query(MockData).filter_by(method=method, status=1)
        match_data = self.get_matched_data(url, mock_datas)
        if match_data:
            logger.info('%s%6s %s', '▶', method, flow.request.path)
            response_data = self.mock(match_data.response)
            response_headers = self.mock(match_data.headers) if match_data.headers else {}

            logger.debug('Mock data: %s', response_data)
            flow.response = http.HTTPResponse.make(
                match_data.code,  # (optional) status code
                json.dumps(response_data, ensure_ascii=False),  # (optional) content
                {"Content-Type": match_data.content_type, 'Access-Control-Allow-Origin': '*', **response_headers}
            )
        else:
            logger.info('%-2s%6s %s', '•', method, flow.request.path)


if __name__ == '__main__':
    addons = [
        FlowInterceptor()
    ]

    opts = Options(listen_host='0.0.0.0', listen_port=8888, termlog_verbosity='warn', flow_detail=0, scripts=None)
    m = DumpMaster(opts)
    m.addons.add(*addons)
    m.run()

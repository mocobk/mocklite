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

from proxy import db
from proxy.db.models import MockData


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
                if re.search(mock_data.url, url, re.IGNORECASE):
                    return mock_data

    @concurrent  # 使用并发模式时，不能使用 ctx.log
    def request(self, flow: http.HTTPFlow):
        method, url = flow.request.method, flow.request.url
        mock_datas = db.session.query(MockData).filter_by(method=method, status=1).all()

        match_data = self.get_matched_data(url, mock_datas)
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
    opts = Options(listen_host='0.0.0.0', listen_port=8888, ssl_insecure=True, termlog_verbosity='warn', flow_detail=0,
                   scripts=None)
    m = DumpMaster(opts)
    m.addons.add(FlowInterceptor())
    m.run()

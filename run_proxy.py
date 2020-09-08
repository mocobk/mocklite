#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/9/8 18:49

from mitmdump import DumpMaster, Options

from proxy.addon import addons

if __name__ == '__main__':

    opts = Options(listen_host='0.0.0.0', listen_port=8080, termlog_verbosity='warn', flow_detail=0, scripts=None)
    m = DumpMaster(opts)
    m.addons.add(*addons)
    m.run()

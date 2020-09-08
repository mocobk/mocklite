#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/8/22 20:47
from multiprocessing import Process

from mitmdump import DumpMaster, Options

from app.libs.response import ServiceInternalError
from proxy.addon import addons


class Proxy(Process):
    PORT = 8080
    TERMLOG_VERBOSITY = 'warn'
    FLOW_DETAIL = 0

    def run(self) -> None:
        opts = Options(listen_host='0.0.0.0', listen_port=self.PORT, termlog_verbosity=self.TERMLOG_VERBOSITY,
                       flow_detail=self.FLOW_DETAIL)
        m = DumpMaster(opts)
        m.addons.add(*addons)
        m.run()


class ProxyManager:
    def __init__(self):
        self.p = None

    def start(self):
        if self.p is not None and self.p.is_alive():
            raise ServiceInternalError(message='代理进程已是启动状态，请先停止')
        self.p = Proxy()
        self.p.daemon = True
        self.p.start()
        print(self.p.is_alive(), '=============')
        return self.p.is_alive()

    def stop(self):
        if not self.p.is_alive():
            return True
        self.p.terminate()
        self.p.join(timeout=10)
        return self.p.is_alive()

    def restart(self):
        is_alive = self.stop()
        if is_alive:
            return False
        return self.start()

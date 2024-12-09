#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = 'test py ctp of se'
__author__ = 'HaiFeng'
__mtime__ = '2022/09/11'

from py_ctp.quote import CtpQuote
from py_ctp.enums import *


def onLogin(obj, info):
    print(info)
    obj.ReqSubscribeMarketData(["rb2505"])


def main():
    q = CtpQuote()
    q.OnConnected = lambda obj: q.ReqUserLogin("203824", "q1621572449!", "9999")
    q.OnUserLogin = onLogin
    q.OnTick = lambda obj, t: print(t)
    q.ReqConnect('tcp://180.168.146.187:10212')

    input()
    q.Release()
    input()


if __name__ == '__main__':
    main()

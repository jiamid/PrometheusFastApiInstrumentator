# -*- coding: utf-8 -*-
# @Time    : 2022/9/13 9:14
# @Author  : JIAMID
# @Email   : jiamid@qq.com
# @File    : __init__.py.py
# @Software: PyCharm
from .instrumentation import PrometheusFastApiInstrumentator

__version__ = "5.9.1"

"""
普罗米修斯中间件
prometheus_client 作为基础
相比于常见的监控，加了一个监控 返回数据包{’code‘:200,'msg':'success'}中 code的情况
"""
Instrumentator = PrometheusFastApiInstrumentator
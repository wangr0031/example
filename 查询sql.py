#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wangrong'
from request_ssc import SscRequest

ssc=SscRequest('10.45.80.26','18280')
###查询结果 1924,1916,1922,1925,
jobList=[1933]
for onejob in jobList:
    ssc.queryJobExecStatus(onejob)



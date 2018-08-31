#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wangrong'
from request_ssc import SscRequest

ssc=SscRequest('10.45.80.26','18280')
###查询结果
jobList=[1879]
for onejob in jobList:
    ssc.queryJobExecStatus(onejob)


#ssc.queryJobExecStatus(1020)
#ssc.queryJobExecStatus(1014)

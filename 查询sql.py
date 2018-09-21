#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wangrong'
from request_zcm import ZcmRequest

ssc=ZcmRequest('10.45.80.26','18280')
###查询结果 1924,1916,1922,1925,2015,2019
##2033,2034,2035,2036,2037
jobList=[3032]
for onejob in jobList:
    ssc.queryJobExecStatus(onejob)



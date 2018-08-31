#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wangrong'
from request_ssc import SscRequest

ssc=SscRequest('10.45.80.26','18280')
##执行sql.zip
## fileName, filePath, ftpHost, userName, passWord
#ssc.ExecuteSqlZipFromServer("string","string","string","string","string")
################################################################################
##########批量执行sql###################################################
##########################################
## skip ,"dabp" sett
#product_name=["balc","bcc","charging","cic","cpc","csc","custc","drm","eshop","irc","jobserver","med","oc","payc","pcrf","pot","src"]
product_name=["dabp"]
script_home='/lvdata/appserver/kunpeng42/app_stateless'
for product in product_name:
    filePath=script_home+'/'+product+'/sql'
    ssc.ExecuteSqlZipFromServer("sql.zip", filePath, "172.16.17.21", "appserver", "appserver")
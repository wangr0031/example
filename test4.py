#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wangrong'
import requests,os


def GetDnsString(dbuser):
    DbConDnsInfo = {
        'instance': {'cc': ['apig', 'ftf', 'cic', 'cpc', 'cpc_flow', 'custc', 'oc', 'drm', 'ebc', 'pos', 'sa', 'src'],
                     'pmt': ['ab', 'bc', 'pcc'],
                     'rb': ['pcb', 'inv', 'rb'],
                     'sett': ['med', 'sett'],
                     'stbp': ['stbp', 'etl', 'dap']},
        'dburl': {'cc': ['172.16.80.11', '11521'],
                  'pmt': ['172.16.80.12', '11521'],
                  'sett': ['172.16.80.13', '11521'],
                  'stbp': ['172.16.80.14', '11521']}
    }
    for one_instance in DbConDnsInfo['instance']:
        if isinstance(DbConDnsInfo['instance'][one_instance], list):
            for one_value in DbConDnsInfo['instance'][one_instance]:
                if one_value == dbuser:
                    db_instance = one_instance
                    db_string = 'jdbc:oracle:thin:@' + DbConDnsInfo['dburl'][db_instance][0] + ':' + \
                                DbConDnsInfo['dburl'][db_instance][1] + '/' + db_instance
                    return db_string
                else:
                    continue
oneapp=r'E:/Workspace/鲲鹏项目/一键部署server/临时版本/20180809-01-演示/sett/sql/balc-web-product.zip'
print (os.path.split(oneapp)[1].split('-')[0])
a=db_con_dns = {
        'instance': {
            'cc': ['apig', 'ftf', 'cic', 'cpc', 'cpc_flow', 'custc', 'oc', 'drm', 'ebc', 'pos', 'sa', 'src'],
            'pmt': ['ab', 'bc', 'pcc'],
            'rb': ['pcb', 'inv', 'rb'],
            'sett': ['med', 'sett'],
            'stbp': ['stbp', 'etl', 'dap']},
        'dburl': {'cc': ['172.16.80.11', '11521'],
                  'pmt': ['172.16.80.12', '11521'],
                  'rb': ['172.16.80.13', '11521'],
                  'sett': ['172.16.80.14', '11521'],
                  'stbp': ['172.16.80.15', '11521']},
        'password':''
    }
print (a['password'].__len__())
if not a['password']:
    print (1)
else:
    print (2)
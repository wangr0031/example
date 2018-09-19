#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wangrong'
from gen_json_ora import GenJson4Ora


# db_con_dns = {
#     'instance': {
#         'cc': ['apig', 'ftf', 'cic', 'cpc', 'cpc_flow', 'custc', 'oc', 'drm', 'ebc', 'pos', 'sa', 'src'],
#         'pmt': ['ab', 'bc', 'pcc'],
#         'rb': ['pcb', 'inv', 'rb'],
#         'sett': ['med', 'sett'],
#         'stbp': ['stbp', 'etl', 'dap']},
#     'dburl': {'cc': ['172.16.80.11', '11521'],
#               'pmt': ['172.16.80.12', '11521'],
#               'rb': ['172.16.80.13', '11521'],
#               'sett': ['172.16.80.14', '11521'],
#               'stbp': ['172.16.80.15', '11521']},
#     'password': '1jian8Shu!'
# }
db_con_dns = {
    'instance': {
        'cc': ['apig', 'ftf', 'cic', 'cpc', 'cpc_flow', 'custc', 'oc', 'drm', 'ebc', 'pos', 'sa', 'src', 'ab', 'bc',
               'pcc', 'pcb', 'inv', 'rb', 'med', 'sett', 'stbp', 'etl', 'dap']},
    'dburl': {'cc': ['10.45.69.191', '1521']},
    'password': ''
}
# db_con_dns = {
#     'instance': {
#         'dbepdb': ['apig', 'ftf', 'cic', 'cpc', 'cpc_flow', 'custc', 'oc', 'drm', 'ebc', 'pos', 'sa', 'src', 'ab', 'bc',
#                'pcc', 'pcb', 'inv', 'rb', 'med', 'sett', 'stbp', 'etl', 'dap']},
#     'dburl': {'dbepdb': ['172.16.24.172', '1521']},
#     'password': ''
# }
script_home = r'C:\Users\cc\Desktop\性能环境\ok0917\app_stateless'
gen = GenJson4Ora(script_home, db_con_dns)
gen.MainProcess()



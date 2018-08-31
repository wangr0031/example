#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wangrong'
from gen_json_ora import GenJson4Ora

script_home = r'C:\Users\cc\Desktop\20180830\ok0829\app_stateless'
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
    'dburl': {'cc': ['172.16.80.42', '11521']},
    'password': ''
}
# db_con_dns = {
#     'instance': {
#         'cc': ['apig', 'ftf', 'cic', 'cpc', 'cpc_flow', 'custc', 'oc', 'drm', 'ebc', 'pos', 'sa', 'src','ab', 'bc', 'pcc','pcb', 'inv', 'rb'],
#         'sett': ['med', 'sett','stbp', 'etl', 'dap']},
#     'dburl': {'cc': ['10.10.88.211', '11521'],
#               'sett': ['10.10.88.212', '11521']},
#     'password': '1jian8Shu!'
# }
gen = GenJson4Ora(script_home, db_con_dns)
gen.MainProcess()

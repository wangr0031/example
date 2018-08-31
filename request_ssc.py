#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wangrong'
import requests
import json
import datetime
import os
import re


class SscRequest():
    def __init__(self, request_ip, port, IsHttps='N'):
        self.global_header = {'Content-Type': 'application/json;charset=UTF-8',
                              "Accept": "*/*"}
        if IsHttps.upper() == 'Y':
            self.request_url = 'https://' + request_ip + ':' + port
        else:
            self.request_url = 'http://' + request_ip + ':' + port
        # self.current_day=datetime.datetime.now().strftime('%Y%m%d-%H')
        self.log_path = './log/{}'.format(datetime.datetime.now().strftime('%Y%m%d-%H'))
        if not os.path.exists(self.log_path):
            os.makedirs(self.log_path)

    def ExecuteSqlZipFromServer(self, fileName, filePath, ftpHost, userName, passWord, ftpPort=22):
        payload = {}
        payload['fileName'] = fileName
        payload['filePath'] = filePath
        payload['ftpHost'] = ftpHost
        payload['userName'] = userName
        payload['passWord'] = passWord
        payload['ftpPort'] = ftpPort
        requests_url = self.request_url + '/DeployManage/deploy'
        r = requests.post(requests_url, headers=self.global_header,
                          data=json.dumps(payload))
        print("\033[1;32msscInstanceId ==>\033[0m  {} ".format(r.json()['data']['sscInstanceId']))

    def queryJobExecStatus(self, instanceId):
        payload = {"execType": 1}
        payload['instanceId'] = instanceId
        requests_url = self.request_url + '/jobManage/queryJobExecStatus'
        log_file = './log/{}'
        response = []
        r = requests.post(requests_url, headers=self.global_header,
                          data=json.dumps(payload))
        #print (r.json())
        if r.json()['status'] == 'running':
            print("\033[1;33mJob {} is running...\033[0m".format(instanceId))
            # print (json.dumps(r.json(), indent=1))
        elif r.json()['status'] == 'fail':
            #print (r.json()['data'])
            total_files = 0
            total_sql_rows = 0
            for one_row in r.json()['data']:
                temp_response = {}
                temp_response['url'] = one_row['url']
                temp_response['script'] = one_row['script']
                temp_response['status'] = one_row['status']
                temp_response['success'] = one_row['success']
                temp_response['fail'] = one_row['fail']
                temp_response['executed'] = one_row['executed']
                temp_response['total'] = one_row['total']
                temp_response['sqlDetail'] = one_row['sqlDetail']
                response.append(temp_response)
                total_files = total_files + 1
                total_sql_rows = total_sql_rows + one_row['total']
            errlog = '{}/err_{}.log'.format(self.log_path, instanceId)
            print("Execute error, log in {},Execute total < {} > files,Execute total < {} > sql rows".format(errlog,total_files,total_sql_rows))
            json.dump(response, open(errlog, "w"), indent=1)
        elif r.json()['status'] == 'success':
            total_files = 0
            total_sql_rows = 0
            for one_row in r.json()['data']:
                total_files = total_files + 1
                total_sql_rows = total_sql_rows + one_row['total']
            oklog = '{}/success_{}.log'.format(self.log_path, instanceId)
            json.dump(r.json(), open(oklog, "w"), indent=1)
            print('Execute successfully,log in {},Execute total files is < {} > files,Execute total < {} > sql rows'.format(oklog,total_files,total_sql_rows))
        else:
            print(json.dumps(r.json(), indent=1))

    def checkFile(self, filePath, fileName, ftpHost='172.16.17.21', userName='appserver', passWord='appserver',
                  ftpPort=22, scriptType='oracle'):
        payload = {}
        payload['filePath'] = filePath
        payload['fileName'] = fileName
        payload['ftpHost'] = ftpHost
        payload['userName'] = userName
        payload['passWord'] = passWord
        payload['ftpPort'] = ftpPort
        payload['scriptType'] = scriptType
        requests_url = self.request_url + '/parser/checkFile'
        r = requests.post(requests_url, headers=self.global_header, params=payload)
        if r.json()['data'] == 'parse success!':
            print('Parse Result:\033[1;32m{}\033[0m'.format('Pass'))
        else:
            print('Parse Result:\033[1;31m{},\n{}\033[0m'.format(r.json()['data'], r.json()['msg']))

    def ParseSqlByRegExp(self, RegExp, filePath):

        pass


if __name__ == '__main__':
    ssc = SscRequest('10.45.80.26', '18280')
    ###查询结果
    ssc.queryJobExecStatus(1100)
    ###执行sql.zip
    ### fileName, filePath, ftpHost, userName, passWord
    # ssc.ExecuteSqlZipFromServer("string","string","string","string","string")
    #################################################################################
    ###########批量执行sql###################################################
    ###########################################
    # product_name=['sett']
    # script_home='/lvdata/appserver/kunpeng42'
    # for product in product_name:
    #     filePath=script_home+'/'+product+'/sql'
    #     ssc.ExecuteSqlZipFromServer("sql.zip", filePath, "172.16.17.21", "appserver", "appserver")

    #################################################################################
    ###checkfile(default ftpHost='172.16.17.21',userName='appserver',passWord='appserver')#
    #################################################################################
    # ssc.checkFile('/lvdata/appserver/kunpeng/balc/sql','balc_balc_bc_oracle.sql')

    #################################################################################
    ####################checkfile in cycle##########################################
    #################################################################################
    # realpath_dir = r'C:/Users/cc/Desktop/解析sql'
    # prefix_path='/lvdata/appserver/parsesql'
    # match_postfix = ['.sql']
    # skip_keyword = ['qmdb']
    # sql_file_list = []
    # for dirpath, dirnames, filenames in os.walk(realpath_dir):
    #     fpath = dirpath.replace(realpath_dir, '')
    #     for filename in filenames:
    #         if os.path.splitext(filename)[1] in match_postfix:
    #             if skip_keyword:
    #                 for skip_key in skip_keyword:
    #                     if not re.search(skip_key, filename.lower()):
    #                         print ("checkFile \033[1;33m{}\033[0m ...".format(filename))
    #                         ssc.checkFile(prefix_path, filename)
    #                         #sql_file_list.append(filename)
    #                         # print (prefix_path+'/'+filename)
    #             else:
    #                 print("checkFile \033[1;33m{}\033[0m  ...".format(filename))
    #                 ssc.checkFile(prefix_path, filename)

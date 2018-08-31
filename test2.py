#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wangrong'

import json
import os
import re
import chardet
import zipfile

class config_json:
    def __init__(self):
        '''
        初始化字典
        '''
        self.ExecCfg={}
        self.ExecCfg['fileSeq']=''
        self.ExecCfg['dataSourceType'] = ''
        self.ExecCfg['url'] = ''
        self.ExecCfg['username'] = ''
        self.ExecCfg['password'] = ''
        self.ExecCfg['sqlFileList']=list()
    def setfileseq(self,fileseq):
        self.ExecCfg['fileSeq']=fileseq
    def setdatasourcetype(self,datasourcetype):
        self.ExecCfg['dataSourceType']=datasourcetype
    def seturl(self,url):
        self.ExecCfg['url']=url
    def setusername(self,username):
        self.ExecCfg['username']=username
    def setpassword(self,password):
        self.ExecCfg['password']=password
    def setsqlfilelist(self,sqlfilelist):
        self.ExecCfg['sqlFileList'].append(sqlfilelist)

class GenJson4Ora(config_json):
    def __init__(self, script_home, db_con_dns):
        '''
        :param script_home: script_home = r'E:/Python3Project/testdir'
        :param db_con_dns: db_con_dns = '172.16.80.41:11521:cc'
        '''
        super().__init__()
        if script_home[-1] == '/':
            self.ScriptHome = script_home[:-1]
        else:
            self.ScriptHome = script_home
        self.DbConDnsInfo = db_con_dns

    def GetUsernameFromFile(self, file_name, split_filter='_'):
        try:
            temp_username = os.path.splitext(file_name)[0].split(split_filter)[-3] + '_' + \
                            os.path.splitext(file_name)[0].split(split_filter)[-2]
        except IndexError:
            temp_username = 'NA'
        if temp_username == 'cpc_flow':
            username = 'cpc_flow'
        elif temp_username == 'NA':
            username = 'NA'
        else:
            username = os.path.splitext(file_name)[0].split(split_filter)[-2]
        return username
    #
    # def UpdateDictValues(self, dict, keys, input_values):
    #     temp_values = dict[keys]
    #     if isinstance(temp_values, (str, int, float, bool)):
    #         temp_values = input_values
    #     elif isinstance(temp_values, list):
    #         if isinstance(input_values, (str, int, float, bool)):
    #             temp_values.append(input_values)
    #         else:
    #             temp_values = temp_values + input_values
    #     dict[keys] = temp_values
    #     return dict
    #
    def CheckFileEncoding(self, fullpath_file_name):
        '''
        :param fullpath_file_name: 文件的全路径 'E:/Python3Project/testdir/balc/sql/balc_product_init_balc_bc_oracle.sql'
        :return:
        '''
        f = open(fullpath_file_name, 'rb')
        data = f.read()
        code_result = chardet.detect(data)
        if code_result['encoding'] != 'utf-8':
            print(
                "\033[0;31m[{}] Character Set Error\033[0m,current Character set is \033[1;31;42m{}\033[0m,Expected \033[1;31;42mUTF-8\033[0m character set ".format(
                    fullpath_file_name, code_result['encoding'].upper()))
    #
    # def GetDictFromDir(self, fullpath_dir):
    #     user_dir_dict = {}
    #     no_user_file = []
    #     last_db_username = ''
    #     for dirpath, dirname, filenames in os.walk(fullpath_dir):
    #         for file_name in filenames:
    #             if os.path.splitext(file_name)[1] == '.sql':
    #                 # print('process file:{}'.format(file_name))
    #                 if re.search('qmdb', file_name.lower()):
    #                     continue
    #                 else:
    #                     fullpath_file = fullpath_dir + '/sql/' + file_name
    #                     self.CheckFileEncoding(fullpath_file)
    #                     db_username = self.GetUsernameFromFile(file_name)
    #                     if db_username == 'NA':
    #                         no_user_file.append(file_name)
    #                         continue
    #
    #                     if db_username in user_dir_dict.keys():
    #                         user_dir_dict = self.UpdateDictValues(user_dir_dict, db_username, file_name)
    #                     else:
    #                         user_dir_dict[db_username] = file_name.split()
    #                     last_db_username = db_username
    #     if no_user_file:
    #         user_dir_dict = self.UpdateDictValues(user_dir_dict, last_db_username, no_user_file)
    #     return user_dir_dict
    #
    # def SortList(self, input_list):
    #     '''
    #     :param input_list: 文件列表['balc_product_init_balc_bc_oracle.sql','balc_product_balc_bc_oracle.sql']
    #     :return:
    #     '''
    #     # 定义5个临时变量，用来存储5种条件过滤出来的内容
    #     tmpfile1 = []
    #     tmpfile2 = []
    #     tmpfile3 = []
    #     tmpfile4 = []
    #     tmpfile5 = []
    #     for onefile in input_list:
    #         if re.search('core', onefile.lower()) and not re.search('init', onefile.lower()):
    #             tmpfile1.append(onefile)
    #         elif re.search('core', onefile.lower()) and re.search('init', onefile.lower()):
    #             tmpfile2.append(onefile)
    #         elif re.search('prod', onefile.lower()) and not re.search('init', onefile.lower()):
    #             tmpfile3.append(onefile)
    #         elif re.search('prod', onefile.lower()) and re.search('init', onefile.lower()):
    #             tmpfile4.append(onefile)
    #         else:
    #             tmpfile5.append(onefile)
    #     ## core >> core_init >> product >> product_init >> others
    #     tmpfile = tmpfile1 + tmpfile2 + tmpfile3 + tmpfile4 + tmpfile5
    #     return tmpfile
    #
    # def SortFileList(self, sql_file_list):
    #     sorted_file_list = self.SortList(sql_file_list)
    #     sqlFileList = []
    #     seqnum = 1
    #     for one_sql_file in sorted_file_list:
    #         one_dict = {}
    #         one_dict['fileName'] = one_sql_file
    #         one_dict['seqnum'] = seqnum
    #         seqnum += 1
    #         sqlFileList.append(one_dict)
    #     return sqlFileList
    #
    # def WriteJsonConfigFile(self, json_file_path, json_data):
    #     with open(json_file_path, "w", encoding='utf-8') as f:
    #         json.dump(json_data, f, indent=1)
    #         print("\033[1;32m[2]\033[0mDump json to file {} \033[1;32msuccess\033[0m".format(json_file_path))
    #
    # def ZipProductionSqlDir(self, zipdir, zip_filename='sql.zip', skip_keyword=['qmdb'], skip_postfix=['.zip']):
    #     ## formate zipdir path,remove '/'
    #     if zipdir[-1] == '/':
    #         zipdir = zipdir[:-1]
    #     zip_filename = zipdir + '/' + zip_filename
    #     zip_handle = zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED)
    #     for dirpath, dirnames, filenames in os.walk(zipdir):
    #         fpath = dirpath.replace(zipdir, '')  ##remove the parent dir path
    #         for filename in filenames:
    #             if os.path.splitext(filename)[1] not in skip_postfix:
    #                 if skip_keyword:
    #                     for skip_key in skip_keyword:
    #                         if not re.search(skip_key, filename.lower()):
    #                             zip_handle.write(os.path.join(dirpath, filename), fpath + '/' + filename)
    #                 else:
    #                     zip_handle.write(os.path.join(dirpath, filename), fpath + '/' + filename)
    #     print('\033[1;32m[3]\033[0mCompress file [{}] \033[1;32msuccess\033[0m'.format(zip_filename))
    #     zip_handle.close()
    #
    # def MainProcess(self):
    #     for production_dir in os.listdir(self.ScriptHome):
    #         fileSeq = 1
    #         fullpath_dir = self.ScriptHome + '/' + production_dir
    #         print('\033[1;32m[1]\033[0mProcess production \033[1;32m[directory]\033[0m:{}'.format(fullpath_dir))
    #         if not os.path.isdir(fullpath_dir):
    #             print("\033[1;33m[Warning]Skip file\033[0m {}".format(fullpath_dir))
    #             continue
    #         user_file_dict = self.GetDictFromDir(fullpath_dir)
    #         #print(user_file_dict,fullpath_dir,len(user_file_dict))
    #         if not len(user_file_dict):
    #             print ("\033[1;33m[Warning]Skip product\033[0m[{}]".format(production_dir))
    #             continue
    #         config_json = []
    #         for one_user_name in user_file_dict:
    #             # print (one_user_name)
    #             # print (user_file_dict[one_user_name])
    #             tmp_config_json = {}
    #             tmp_config_json["fileSeq"] = fileSeq
    #             tmp_config_json["dataSourceType"] = 'oracle'
    #             tmp_config_json["url"] = 'jdbc:oracle:thin:@' + self.DbConDnsInfo
    #             tmp_config_json["username"] = one_user_name
    #             tmp_config_json["password"] = one_user_name
    #             # print (user_file_dict[one_user_name])
    #             sqlFileList = self.SortFileList(user_file_dict[one_user_name])
    #             tmp_config_json["sqlFileList"] = sqlFileList
    #             config_json.append(tmp_config_json)
    #             fileSeq += 1
    #         ## write json string to file
    #         json_file_path = self.ScriptHome + '/' + production_dir + '/sql/config.json'
    #         self.WriteJsonConfigFile(json_file_path, config_json)
    #         ##compress to sql.zip
    #         compress_dir = self.ScriptHome + '/' + production_dir + '/sql'
    #         self.ZipProductionSqlDir(compress_dir)


if __name__ == '__main__':
    script_home = r'E:/Python3Project/testdir'
    db_con_dns = '172.16.80.41:11521:cc'
    gen = GenJson4Ora(script_home, db_con_dns)
    #gen.MainProcess()

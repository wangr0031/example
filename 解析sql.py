#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wangrong'
from request_ssc import SscRequest
import os, re
import paramiko
import stat


class sftpCmdClass(object):
    def __init__(self,ip,username,password,port=22):
        self.ip=ip
        self.username=username
        self.password=password
        self.port=port

    def __get_all_file_in_remote_dir(self,sftpHandle,remote_dir):
        all_files=list()
        if remote_dir[-1]=='/':
            remote_dir=remote_dir[:-1]
        try:
            files_attr=sftpHandle.listdir_attr(remote_dir)
        except FileNotFoundError as errfile:
            print ("\033[1;33mremote directory\033[0m {} \033[1;31mnot found!\033[0m".format(remote_dir))
            exit()
        except Exception as err:
            print ("errinfo:{}".format(err))

        for file_attr in files_attr:
            filename=remote_dir+'/'+file_attr.filename
            #print ("filename={},file_mode={}".format(filename,file_attr.st_mode))
            if stat.S_ISDIR(file_attr.st_mode):
                all_files.extend(self.__get_all_file_in_remote_dir(sftpHandle,filename))
            else:
                all_files.append(filename)
        return all_files

    def sftp_get_dir(self,remote_dir):
        trans=paramiko.Transport((self.ip,self.port))
        trans.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(trans)
        all_files = self.__get_all_file_in_remote_dir(sftp, remote_dir)
        return all_files
        #print ("all_files:\n",all_files)


sftp_info={"ip":"172.16.17.21",
      "user":"appserver",
      "password":"appserver"
      }
remote_path = '/lvdata/appserver/kunpeng41/app_stateless'
#remote_path = '/home/v9crm/shenxia'
match_postfix = ['.sql']
skip_keyword = ['qmdb']
s=sftpCmdClass(sftp_info['ip'],sftp_info['user'],sftp_info['password'])
#s=sftpCmdClass('172.16.22.139','v9crm','v9crm')
ssc = SscRequest('10.45.80.26', '18280')
#ssc = SscRequest('10.45.16.87', '8090')
sql_file_list=s.sftp_get_dir(remote_path)

for file in sql_file_list:
    if os.path.splitext(file)[1] in match_postfix:
        if skip_keyword:
            for skip_key in skip_keyword:
                if not re.search(skip_key, file.lower()):
                    print("checkFile \033[1;33m{}\033[0m...  ".format(file),end="")
                    try:
                        ## ftpHost='172.16.17.21', userName='appserver', passWord='appserver'
                        ssc.checkFile(os.path.split(file)[0], os.path.split(file)[1],sftp_info['ip'],sftp_info['user'],sftp_info['password'])
                    except ConnectionError as conerr:
                        print ("\033[1;31mConnection Error:\033[0m {}".format(conerr))
                    except Exception as err:
                        print ("\033[1;31mRequest Error:\033[0m\n{}".format(err))

        else:
            print("checkFile \033[1;33m{}\033[0m...  ".format(file),end="")
            ssc.checkFile(os.path.split(file)[0], os.path.split(file)[1],sftp_info['ip'],sftp_info['user'],sftp_info['password'])


# for dirpath, dirnames, filenames in os.walk(realpath_dir):
#     fpath = dirpath.replace(realpath_dir, '')
#     for filename in filenames:
#         if os.path.splitext(filename)[1] in match_postfix:
#             if skip_keyword:
#                 for skip_key in skip_keyword:
#                     if not re.search(skip_key, filename.lower()):
#                         print("checkFile \033[1;33m{}\033[0m ...".format(filename))
#                         ssc.checkFile(prefix_path, filename)
#                         # sql_file_list.append(filename)
#                         # print (prefix_path+'/'+filename)
#             else:
#                 print("checkFile \033[1;33m{}\033[0m  ...".format(filename))
#                 ssc.checkFile(prefix_path, filename)

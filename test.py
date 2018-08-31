#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wangrong'

import os
import sys
import re
#prefix_path='/lvdata/appserver/kunpeng'
realpath_dir=r'E:/Python3Project/testdir'
match_postfix=['.sql']
skip_keyword=['qmdb']
sql_file_list=[]
for dirpath, dirnames, filenames in os.walk(realpath_dir):
    fpath = dirpath.replace(realpath_dir, '')  ##remove the parent dir path
    for filename in filenames:
        if os.path.splitext(filename)[1]  in match_postfix:
            if skip_keyword:
                for skip_key in skip_keyword:
                    if not re.search(skip_key, filename.lower()):
                        sql_file_list.append(filename)
                        #print (prefix_path+'/'+filename)
            else:
                sql_file_list.append(filename)
                #print (prefix_path+'/'+filename, fpath + '/' + filename)
print (sql_file_list)


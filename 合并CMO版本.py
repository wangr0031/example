#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wangrong'
'''
-
'''
import os, re
import sys, shutil
import zipfile


class CombineCMOversion():
    def __init__(self, srcdirname, destdirname):
        srcdirname = srcdirname.replace('\\', '/')
        destdirname = destdirname.replace('\\', '/')
        self.statful_app = ['med-backend-product', 'olc-all-product', 'sett-backend-product',
                            'cg-dbep-webservice-server-core', 'cg-dbep-ussdxml-server-core']
        if srcdirname[-1] == '/':
            self.dirname = srcdirname[:-1]
        else:
            self.dirname = srcdirname

        if destdirname[-1] == '/':
            self.dstdir = destdirname[:-1]
        else:
            self.dstdir = destdirname

        if not os.path.exists(self.dstdir):
            # os.makedirs(self.dstdir)
            os.makedirs(self.dstdir + '/app_stateless')
            os.makedirs(self.dstdir + '/app_stateful')

    def get_sql_file(self, full_dirpath, skip_file=['qmdb'], match_postfix=['.sql']):
        all_sql_file = []
        skip_sql_file = []
        for dirpath, dirnames, filenames in os.walk(full_dirpath):
            for file in filenames:
                if os.path.splitext(file)[1] in match_postfix:
                    if skip_file:
                        for skip_key in skip_file:
                            if not re.search(skip_key, file.lower()):
                                # print ('dirpath=',dirpath,'dirnames=',dirnames,'file=',file)
                                fullfile = (dirpath + '/' + file).replace('\\', '/')
                                all_sql_file.append(fullfile)
                            else:
                                fullfile = (dirpath + '/' + file).replace('\\', '/')
                                skip_sql_file.append(fullfile)
                    else:
                        fullfile = (dirpath + '/' + file).replace('\\', '/')
                        all_sql_file.append(fullfile)

        return all_sql_file, skip_sql_file

    def get_app_file(self, full_dirpath, skip_file=['sql.zip'], match_postfix=['.zip']):
        all_app_file = []
        skip_app_file = []
        for dirpath, dirnames, filenames in os.walk(full_dirpath):
            for file in filenames:
                if os.path.splitext(file)[1] in match_postfix:
                    if skip_file:
                        for skip_key in skip_file:
                            if not re.search(skip_key, file.lower()):
                                fullfile = (dirpath + '/' + file).replace('\\', '/')
                                all_app_file.append(fullfile)
                            else:
                                fullfile = (dirpath + '/' + file).replace('\\', '/')
                                skip_app_file.append(fullfile)
                    else:
                        fullfile = (dirpath + '/' + file).replace('\\', '/')
                        all_app_file.append(fullfile)
        return all_app_file

    def checkzipfile(self, i_zipfile, check_postfix=['.zip']):
        zip_handle = zipfile.ZipFile(i_zipfile)
        for onefile in zip_handle.filelist:
            if os.path.splitext(onefile.filename)[1] in check_postfix:
                print("\033[1;31m zipfile <{}> contain illege file {}\033[0m".format(i_zipfile, onefile.filename))

    def combine_sql(self, sqldir):
        sqldir = sqldir.replace('\\', '/')
        for onelist in os.listdir(sqldir):
            src_full_dir_path = sqldir + '/' + onelist
            if os.path.isdir(src_full_dir_path):
                ##生成目标产品目录
                dstsqldir = (self.dstdir + '/app_stateless/' + onelist + '/sql').lower()
                if not os.path.exists(dstsqldir):
                    os.makedirs(dstsqldir)
                sql_list, skip_sql_file = self.get_sql_file(src_full_dir_path)
                if sql_list:
                    for onesql in sql_list:
                        try:
                            shutil.copy(onesql, dstsqldir)
                            # print(
                            #     "\033[1;33mcopy file\033[0m {} \033[1;33mto\033[0m {} \033[1;32msuccess!\033[0m".format(
                            #         onesql, dstsqldir))
                        except Exception as err:
                            print(
                                "\033[1;33mcopy SQL file\033[0m {} \033[1;33mto\033[0m {} \033[1;31mfailed!\033[0m errinfo:\n{}".format(
                                    onesql, dstsqldir, err))
                            exit()
                if skip_sql_file:
                    for onesql in skip_sql_file:
                        try:
                            skip_dir = (self.dstdir + '/qmdb/' + onelist).lower()
                            os.makedirs(skip_dir)
                            shutil.copy(onesql, skip_dir)
                        except Exception as err:
                            print(
                                "\033[1;33mcopy QMDB file\033[0m {} \033[1;33mto\033[0m {} \033[1;31mfailed!\033[0m errinfo:\n{}".format(
                                    onesql, dstsqldir, err))
                            exit()
            else:
                continue

    def combine_app(self, appdir):
        appdir = appdir.replace('\\', '/')
        if not os.path.isdir(appdir):
            print('{} is not a direcotry!'.format(appdir))
            exit()
        app_list = self.get_app_file(appdir)
        if app_list:
            for oneapp in app_list:
                self.checkzipfile(oneapp)
                filename = os.path.split(oneapp)[1]
                # print ("=======>{}<==========".format(filename))
                if filename.split('.')[0].lower() in self.statful_app:
                    dstappdir = (self.dstdir + '/app_stateful/' + filename.split('-')[0].lower() + '/app')
                else:
                    dstappdir = (self.dstdir + '/app_stateless/' + filename.split('-')[0].lower() + '/app')
                if not os.path.exists(dstappdir):
                    os.makedirs(dstappdir)
                try:
                    shutil.copy(oneapp, dstappdir)
                    # print(
                    #     "\033[1;33mcopy file\033[0m {} \033[1;33mto\033[0m {} \033[1;32msuccess!\033[0m".format(
                    #         oneapp, dstappdir))
                except Exception as err:
                    print(
                        "\033[1;33mcopy file\033[0m {} \033[1;33mto\033[0m {} \033[1;31mfailed!\033[0m errinfo:\n{}".format(
                            oneapp, dstappdir, err))
                    exit()
        else:
            print("\033[1;31mNo app file found!\033[0m")

    def MainProcess(self):
        for one in os.listdir(self.dirname):
            src_full_dir_path = self.dirname + '/' + one
            if os.path.isdir(src_full_dir_path):
                if one == '脚本':
                    self.combine_sql(src_full_dir_path)
                    print("\033[1;32mcopy SQL file success!\033[0m")
                elif one == '应用':
                    self.combine_app(src_full_dir_path)
                    print("\033[1;32mcopy APP file success!\033[0m")
                else:
                    print("\033[1;31mskip object {}!\033[0m".format(self.dirname))

            else:
                print("\033[1;33mskip object\033[0m {}".format(one))
                continue


if __name__ == '__main__':
    com = CombineCMOversion(r'C:\Users\cc\Desktop\格鲁版本\B', r'C:\Users\cc\Desktop\格鲁版本\ok0919')
    # com.combine_sql(r'C:\Users\cc\Desktop\20180809部署tmp\0816全量脚本')
    com.combine_app(r'C:\Users\cc\Desktop\格鲁版本\B')
    # com.MainProcess()

#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wangrong'

import xlrd, os, re


class com_excel_app():
    def __init__(self, excel, app):
        self.excel_path = excel.replace('\\', '/')
        self.app_path = app.replace('\\', '/')

    def get_app_name_from_excel_app_midware(self):
        excelfile = xlrd.open_workbook(self.excel_path)
        apptable = excelfile.sheet_by_name('app midware')
        totalrows = apptable.nrows
        totalcols = apptable.ncols
        col_num = -1
        for rows in range(totalrows):
            for cols in range(totalcols):
                if apptable.row_values(rows)[cols] == 'app_name':
                    col_num = cols
        if col_num >= 0:
            col_values = apptable.col_values(col_num)
            while '' in col_values:
                col_values.remove('')
            if col_values:
                col_values.remove('app_name')
        return col_values

    def get_app_name_from_excel(self):
        app_dict_from_excel = {}
        excelfile = xlrd.open_workbook(self.excel_path)
        apptable = excelfile.sheet_by_name('app info')
        totalrows = apptable.nrows
        for i in range(totalrows):
            if i in [0, 1]:
                continue
            app_dict_from_excel[apptable.row_values(i)[0]] = apptable.row_values(i)[1]
        return app_dict_from_excel

    def get_app_name_from_dir(self, skip_file=['sql.zip'], match_postfix=['.zip']):
        all_app_file = list()
        skip_app_file = list()
        for dirpath, dirnames, filenames in os.walk(self.app_path):
            for file in filenames:
                if os.path.splitext(file)[1] in match_postfix:
                    if skip_file:
                        for skip_key in skip_file:
                            if not re.search(skip_key, file.lower()):
                                fullfile = (dirpath + '/' + file).replace('\\', '/')
                                all_app_file.append(file)
                            else:
                                fullfile = (dirpath + '/' + file).replace('\\', '/')
                                skip_app_file.append(fullfile)
                    else:
                        fullfile = (dirpath + '/' + file).replace('\\', '/')
                        all_app_file.append(fullfile)
        return all_app_file, skip_app_file

    def compare(self):
        '''以目录对比文档'''
        app_dict = self.get_app_name_from_excel()
        # print(app_dict.keys())
        (all_app_file, skip_app_file) = self.get_app_name_from_dir()
        for one_app in all_app_file:
            if os.path.splitext(one_app)[0] in app_dict.keys():
                # print ("{} match".format(one_app))
                pass
            else:
                print("\033[1;31mdirectory {} APP {} not match with Excel,please confirm & modify\033[0m".format(self.app_path, one_app))

    def compare2(self):
        '''以文档对比目录'''
        app_dict = self.get_app_name_from_excel()
        # print(app_dict.keys())
        (all_app_file, skip_app_file) = self.get_app_name_from_dir()
        for one_app in app_dict:
            if one_app + '.zip' in all_app_file:
                # print ("{} match".format(one_app))
                pass
            else:
                print("\033[1;31mexcel APP info {} not match,please modify Excel {}\033[0m".format(one_app,self.excel_path))

    def compare3(self):
        app_dict = self.get_app_name_from_excel()
        app_list = self.get_app_name_from_excel_app_midware()
        for oneapp in app_list:
            if oneapp in app_dict.keys():
                pass
            else:
                print("\033[1;31mexcel APP info {} not match with APP midware,please modify Excel {}\033[0m".format(
                    oneapp, self.excel_path))


if __name__ == '__main__':
    excel_file = r'C:\Users\cc\Desktop\格鲁版本\midware.xlsx'
    app_dir = r'C:\Users\cc\Desktop\格鲁版本\ok0919'
    c = com_excel_app(excel_file, app_dir)
    c.compare()
    c.compare2()
    c.compare3()

#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wangrong'

from openpyxl.reader.excel import load_workbook
import os


class read_midware_excel():
    def __init__(self, src_path):
        ''' format src path'''
        src_path = src_path.replace('\\', '/')
        if src_path[-1] == '/':
            src_path = src_path[:-1]
        # check file
        if os.path.exists(src_path):
            if not os.path.isfile(src_path):
                self.src_excel_path = src_path + '/' + 'midware.xlsx'
                if not os.path.isfile(self.src_excel_path):
                    exit()
            else:
                self.src_excel_path = src_path
        else:
            print('Directory {} not found'.format(src_path))
            exit()

    def open_excel_file(self):
        '''open excel file'''
        try:
            wb = load_workbook(filename=self.src_excel_path)
            print (type(wb))
        except Exception as err:
            print ('Error Excel File:{}'.format(os.path.abspath(self.src_excel_path)))
            exit()
        return wb

    def load_db_info(self,work_book):
        db_sheet=work_book['db info']
        print ("Work Sheet Titile:", db_sheet.title)





if __name__ == '__main__':
    r = read_midware_excel('./data/')
    b=r.open_excel_file()
    r.load_db_info(b)

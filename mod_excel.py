#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wangrong'
import xlrd,os,re
## https://blog.csdn.net/u013045749/article/details/49910695/
# 想要，往已经存在的xls文件中，写入新的行，新的数据，对应的逻辑为：
#
# 用xlrd.open_workbook打开已有的xsl文件
# 注意添加参数formatting_info=True，得以保存之前数据的格式
# 然后用，from xlutils.copy import copy;，之后的copy去从打开的xlrd的Book变量中，拷贝出一份，成为新的xlwt的Workbook变量
# 然后对于xlwt的Workbook变量，就是正常的：
# 通过get_sheet去获得对应的sheet
# 拿到sheet变量后，就可以往sheet中，写入新的数据
# 写完新数据后，最终save保存

class excel_func():
    def __init__(self,src_xlsx_path):
        self.src_xlsx=src_xlsx_path.replace('\\', '/')
        self.excel_instance = xlrd.open_workbook(self.src_xlsx)

    def get_excel_instacne(self):
        pass

    def load_db_info_data(self):
        dbinfo_data=self.excel_instance.sheet_by_name('db info')
        pass


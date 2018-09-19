#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wangrong'
import xlrd

def read_excel():
    excelfile_path='./data/midware.xlsx'
    excelfile=xlrd.open_workbook(excelfile_path)

    table=excelfile.sheets()[3]
    #print(type(table))
    nrows=table.nrows
    print (nrows)
    for i in range(nrows):
        if i in [0,1]:
            continue
        print(table.row_values(i)[0])


    # print (excelfile.sheet_names())
    # sheet=excelfile.sheet_by_name('app info')
    # print(type(sheet),sheet)
    # print(sheet.name,sheet.nrows,sheet.ncols)
    # for i in range(sheet.nrows):
    #     print (sheet.cell(1, 0).value.encode('utf-8'))

read_excel()

#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wangrong'
class Animal:
    '''
    人和狗都是动物，所以创造一个Animal基类
    '''
    def __init__(self, name, aggressivity, life_value):
        self.name = name  # 人和狗都有自己的昵称;
        self.aggressivity = aggressivity  # 人和狗都有自己的攻击力;
        self.life_value = life_value  # 人和狗都有自己的生命值;

    def eat(self):
        print('%s is eating'%self.name)
class Dog(Animal):
    def __init__(self,name,breed,aggressivity,life_value):
        super().__init__(name, aggressivity, life_value)

import zipfile
import  os

file=r'C:/Users/cc/Desktop/20180829/CMO/应用/jobserver-all-core.zip'
file=file.replace('\\', '/')
zip_handle=zipfile.ZipFile(file)
for onezipfile in zip_handle.filelist:
    if onezipfile.file_size:
        print (onezipfile.filename)
print (zip_handle.namelist())
print (zip_handle.infolist())
print (zip_handle.filename)
print (type(zip_handle.filelist[1]))
print (zip_handle.filelist[7])
print (os.path.splitext(zip_handle.filelist[7].filename)[1])


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
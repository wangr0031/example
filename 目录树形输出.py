#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wangrong'
import os
import os.path

def dfs_showdir(path, depth):
    path=path.replace('\\','/')
    if depth == 0:
        print("root:[" + path + "]")

    for item in os.listdir(path):
        if '.git' not in item:
            print("|      " * depth + "+--" + item)

            newitem = path +'/'+ item
            if os.path.isdir(newitem):
                dfs_showdir(newitem, depth +1)

if __name__ == '__main__':
    dfs_showdir(r'C:\Users\cc\Desktop\20180827\ok0827', 0)
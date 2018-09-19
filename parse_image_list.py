#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wangrong'
import zipfile
import os,re,shutil
import json

class ZFile():
    def __init__(self,src_zip_path):
        self.exact_tmp_dir=os.path.join(os.path.dirname(os.path.abspath(__file__)),'tmp')
        if os.path.exists(self.exact_tmp_dir):
            shutil.rmtree(self.exact_tmp_dir)
            os.makedirs(self.exact_tmp_dir)
        else:
            os.makedirs(self.exact_tmp_dir)

        src_zip_path=src_zip_path.replace('\\','/')
        if src_zip_path[-1] == '/':
            self.src_path = src_zip_path[:-1]
        else:
            self.src_path = src_zip_path

    def is_correct_zip_file(self,zipinstance):
        res=zipinstance.testzip()
        if res is None:
            return True
        else:
            return False

    def load_json_file(self,json_file):
        json_dict=json.loads(json_file)
        application_name=json_dict['applicationName']
        image=json_dict['appInfo']['images'][0]['image']
        print('app_name:{},image:{}'.format(application_name,image))
        print (json_dict.keys())
        print (json_dict['appInfo']['images'][0]['image'])

        return json_dict

    def unzip_zip_file(self,zip_file,match_file='app.json',mode='r'):
        zfile = zipfile.ZipFile(zip_file, mode, compression=zipfile.ZIP_DEFLATED)
        res_code=self.is_correct_zip_file(zfile)
        if not res_code:
            print ("Zip File is error")
            exit()
        all_file_list=zfile.namelist()
        for one in all_file_list:
            if re.search(match_file.lower(),one.lower()):
                print ('match file:',one)
                zfile.extract(one,self.exact_tmp_dir)
                json_file=zfile.open(one,'r').read()
                #print (str(json_file,encoding='utf-8'))
                json_file=self.load_json_file(str(json_file,encoding='utf-8'))
                #print (json_file)



if __name__ == '__main__':
    a=ZFile(r'C:\Users\cc\Desktop\格鲁版本\B')
    a.unzip_zip_file(r'C:\Users\cc\Desktop\格鲁版本\B\irc-web-product.zip')
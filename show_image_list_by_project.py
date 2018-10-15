#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wangrong'
from request_zcm import ZcmRequest

app=ZcmRequest('10.45.80.26')
app.get_app_image_list('dbeptest5')


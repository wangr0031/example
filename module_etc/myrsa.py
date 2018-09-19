#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wangrong'
import base64
import rsa

message='BGYTmUioo6qPzwbTmVNNtJlIuCQlxsFnEIdJcBDa0wA='
with open('./key/OCSPublicKey.pem') as publickfile:
    p = publickfile.read()
    print(type(p))
    pubkey = rsa.PublicKey.load_pkcs1(p.encode('utf-8'))

# with open('./key/OCSPrivateKey.pem') as privatefile:
#     p = privatefile.read()
#     print(type(p))
#     privkey = rsa.PrivateKey.load_pkcs1(p.encode('utf-8'))
# 用公钥加密、再用私钥解密
crypto = rsa.encrypt(message.encode('utf-8'), pubkey)
print(crypto)
print("---- 5 ----")
print('crypto:', type(crypto))
print('cry_base64:', base64.encodestring(crypto))
print('cry_base64_utf8:', base64.encodestring(crypto).decode('utf-8'))

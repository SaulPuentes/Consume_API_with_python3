#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

client_id = '938931884f579516ae9d'
client_secret = 'f57ec67a7f8deac51f1100600dcd6e809a4e917b'

code = '8c619dcb7c1a87f86dcc'
access_token = '5497bac0fb549dd9240922a788ce8ace59269054'
#https://github.com/login/oauth/authorize?client_id=938931884f579516ae9d&scope=repo

url = 'https://api.github.com/user/repos'
headers = { 'Authorization' : 'token 4cd6e4d36aaff008dcc600fb2e3abdfb0a4f6163'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    payload = response.json()

    for project in payload:
        name = project['name']
        print(name)
else:
    print(response.content)

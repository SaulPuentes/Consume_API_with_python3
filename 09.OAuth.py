#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

client_id = '938931884f579516ae9d'
client_secret = 'f57ec67a7f8deac51f1100600dcd6e809a4e917b'

code = '8c619dcb7c1a87f86dcc'
access_token = '5497bac0fb549dd9240922a788ce8ace59269054'
#https://github.com/login/oauth/authorize?client_id=938931884f579516ae9d&scope=repo

url = 'https://github.com/login/oauth/access_token'
payload = {'client_id': client_id, 'client_secret': client_secret, 'code': code}
headers = {'Accept' : 'application/json'}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    response_json = response.json()

    access_token = response_json['access_token']
    print(access_token)
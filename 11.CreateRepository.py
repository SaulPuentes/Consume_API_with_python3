#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

client_id = '938931884f579516ae9d'
client_secret = 'f57ec67a7f8deac51f1100600dcd6e809a4e917b'

code = '8c619dcb7c1a87f86dcc'
access_token = '5497bac0fb549dd9240922a788ce8ace59269054'
#https://github.com/login/oauth/authorize?client_id=938931884f579516ae9d&scope=delete_repo

url = 'https://api.github.com/user/repos'
paylod = { 'name':'Consume_API_with_python3' }
headers = { 'Accept' : 'application/vnd.github.baptiste-preview+json', 'Authorization': 'token ' + access_token}

response = requests.delete(url, headers=headers, json=paylod)

if response.status_code == 200:
    print(response.json())
else:
    print(response.content)
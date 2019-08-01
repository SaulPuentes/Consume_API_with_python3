#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json

url = 'https://httpbin.org/post'
payload = { 'nombre': 'Eduardo', 'curso': 'python', 'nivel': 'intermedio'}

#response = requests.post(url, json=payload)
response = requests.post(url, data=json.dumps(payload))
print(response.url)

if response.status_code == 200: 
    print(response.content)
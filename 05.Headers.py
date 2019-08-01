#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json

url = 'https://httpbin.org/post'
payload = { 'nombre': 'Eduardo', 'curso': 'python', 'nivel': 'intermedio'}
headers = { 'Content-Type': 'applicaction/json', 'access-token': '12345'}

response = requests.post(url, data=json.dumps(payload), headers=headers)
print(response.url)

if response.status_code == 200:
    headers_response = response.headers # Dictionary
    #print(headers_response)
    server = headers_response['Server']
    print(server)
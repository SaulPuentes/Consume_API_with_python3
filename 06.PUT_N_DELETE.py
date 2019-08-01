#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json

#url = 'https://httpbin.org/put'
url = 'https://httpbin.org/delete'
payload = { 'nombre': 'Eduardo', 'curso': 'python', 'nivel': 'intermedio'}
headers = { 'Content-Type': 'applicaction/json', 'access-token': '12345'}

#response = requests.put(url, data=json.dumps(payload), headers=headers)
response = requests.delete(url, data=json.dumps(payload), headers=headers)
print(response.url)

if response.status_code == 200: 
    headers_response = response.headers # Dictionary
    server = headers_response['Server']
    print(server)
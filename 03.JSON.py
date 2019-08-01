#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json

url = 'https://httpbin.org/get'
args = { 'nombre': 'Eduardo', 'curso': 'python', 'nivel': 'intermedio'}

response = requests.get(url, params=args)
print(response.url)

if response.status_code == 200: 
    """
    response_json = response.json() # dictionary
    origin = response_json['origin']
    print(origin)
    """

    response_json = json.loads(response.text)
    origin = response_json['origin']
    print(origin)
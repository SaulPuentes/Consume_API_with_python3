#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

url = 'https://httpbin.org/get'
args = { 'nombre': 'Eduardo', 'curso': 'python', 'nivel': 'intermedio'}

response = requests.get(url, params=args)

if response.status_code == 200:
    content = response.content
    print(content)
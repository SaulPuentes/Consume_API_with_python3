#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

url = 'https://www.google.com.mx/'
response = requests.get(url)

if response.status_code == 200:
    content = response.content
    file = open('google.html', 'wb')
    file.write(content)
    file.close()
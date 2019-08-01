#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

url = 'https://httpbin.org/cookies'
cookies = { 'my-cookie' : 'true' }

response = requests.get(url, cookies=cookies)

if response.status_code == 200:
    cookies = response.cookies
    print(cookies)

    print("The content is :")
    print(response.content)
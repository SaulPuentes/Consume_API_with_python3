#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

url = 'https://api.github.com/user'

session = requests.session()
session.auth = ( 'your_email@example.com', 'password' )

response = session.get(url)

if response.ok:    
    response = session.get('https://github.com/YourUserName')
    if response.ok:
        print(response.cookies)
        #print(response.content)
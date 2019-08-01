#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

url = 'https://i.imgur.com/pTPvZdx.jpg'

response = requests.get(url, stream=True) #Make the requests without save the content

with open('image.jpg', 'wb') as file:
    for chunk in response.iter_content():
        file.write(chunk)

response.close()
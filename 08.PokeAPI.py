#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests


def get_pokemons(url='http://pokeapi.co/api/v2/pokemon-form/', offset=0):
    args = {'offset': offset} if offset else {}

    response = requests.get(url, params=args)

    if response.status_code == 200:
        payload = response.json()
        results = payload.get('results', [])

    if results:
        for pokemon in results:
            name = pokemon['name']
            print(name)

    next = input("Continue listing? [Y/N]").lower()
    if next == 'y':
        get_pokemons(offset=offset+20)

get_pokemons()
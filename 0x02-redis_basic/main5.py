#!/usr/bin/env python3
""" Main file """
from redis import Redis


get_page = __import__('web').get_page


r = Redis()
url = 'http://slowwly.robertomurray.co.uk'
get_page(url)

name = f'count:{url}'
print(int(r.get(name)))


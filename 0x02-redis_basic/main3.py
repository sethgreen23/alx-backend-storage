#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache
replay = __import__('exercise').replay
cache = Cache()
cache.store("first")
cache.store("second")

replay(cache.store)


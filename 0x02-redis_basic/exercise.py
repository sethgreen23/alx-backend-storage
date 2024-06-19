#!/usr/bin/env python3
"""
Basic Redis operations
"""
import redis
from uuid import uuid4
from typing import Callable, Union
from functools import wraps


class Cache:
    """ Cache class"""

    def __init__(self) -> None:
        """ Init method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[bytes, str, float, int]) -> str:
        """ Store method """
        key = str(uuid4())
        data = data.decode('utf-8')
        self._redis.set(key, data)
        return key

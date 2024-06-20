#!/usr/bin/env python3
"""
Basic Redis operations
"""
import redis
from uuid import uuid4
from typing import Callable, Union
from functools import wraps


def count_calls(fn: Callable) -> Callable:
    """ Count Cache class method calls"""
    @wraps(fn)
    def wrapper(self, *args: object, **kwargs: object) -> Callable:
        """ Wrapper function """
        self._redis.incr(f'{fn.__qualname__}')
        return fn(self, *args, **kwargs)
    return wrapper


class Cache:
    """ Cache class"""

    def __init__(self) -> None:
        """ Init method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store method """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        """ Get method"""
        if fn is None:
            return self._redis.get(key)
        return fn(self._redis.get(key))

    def get_str(self, key: str) -> str:
        """Get string method"""
        return str(key)

    def get_int(self, key: str) -> int:
        """Get int method"""
        return int(key)

#!/usr/bin/env python3
"""
Basic Redis operations
"""
import redis
from uuid import uuid4
from typing import Callable, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Count Cache class method calls"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function """
        key = method(self, *args, **kwargs)
        self._redis.incr(method.__qualname__)
        return key
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Call history method"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function """
        key = method(self, *args, **kwargs)
        self._redis.rpush(f'{method.__qualname__}:outputs', key)
        self._redis.rpush(f'{method.__qualname__}:inputs', str(args))
        return key
    return wrapper


def replay(method: Callable) -> None:
    """Replay method"""
    r = redis.Redis()
    method_name = method.__qualname__
    call_time = int(r.get(method_name))
    output_l_n = r.lrange(f'{method_name}:outputs', 0, -1)
    input_l_n = r.lrange(f'{method_name}:inputs', 0, -1)
    print(f'{method_name} was called {call_time} times:')
    output_index = 0
    input_index = 0
    while output_index < len(output_l_n) and input_index < len(input_l_n):
        output_value = output_l_n[output_index]
        input_value = input_l_n[input_index]
        input_index += 1
        output_index += 1
        left = f'{method_name}((*{input_value.decode("utf-8")})'
        right = f'{output_value.decode("utf-8")})'
        print(f'{left} -> {right}')


class Cache:
    """ Cache class"""

    def __init__(self) -> None:
        """ Init method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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

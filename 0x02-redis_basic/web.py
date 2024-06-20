#!/usr/bin/env python3
"""Web server"""

import requests
from redis import Redis
from functools import wraps
from typing import Callable


def track_url(method: Callable) -> Callable:
    """Track URL"""

    @wraps(method)
    def wrapper(*args, **kwargs):
        """wrapper function"""
        r = Redis()
        r.incr(f'count:{args[0]}', exp=10)
        return method(*args, **kwargs)
    return wrapper


@track_url
def get_page(url: str) -> str:
    """Get page"""
    r = requests.get(url)
    return r.text

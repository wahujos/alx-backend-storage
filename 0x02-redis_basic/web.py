#!/usr/bin/env python3
"""
In this tasks, we will implement a get_page
function(prototype: def get_page(url: str) -> str:). The core
of the function is very simple. It uses the requests
module to obtain the HTML content of a particular URL
and returns it.
"""

import redis
import requests
from typing import Callable
from functools import wraps


redis_client = redis.Redis()


def cache_result(method: Callable) -> Callable:
    """
    cache results method
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """
        checks if the result is already cached
        """
        cached_result = redis_client.get(f"cache:{url}")
        if cached_result:
            return cached_result.decode('utf-8')
        result = method(url)
        redis_client.setex(f"cache:{url}", 10, result)
        return result
    return wrapper


def count_requests(method: Callable) -> Callable:
    """
    Count requests method
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """
        increment the count of the counter
        """
        redis_client.incr(f"count:{url}")
        return method(url)
    return wrapper


@cache_result
@count_requests
def get_page(url: str) -> str:
    """
    The get page method
    """
    response = requests.get(url)
    return response.text

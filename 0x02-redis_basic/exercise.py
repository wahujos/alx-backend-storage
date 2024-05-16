#!/usr/bin/env python3
"""
Writing strings to Redis
"""

import redis
import uuid
import functools
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """
    counts number of times the method are called num
    """
    key = method.__qualname__

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        increment call count and return original method
        """
        # key = f"{method.__qualname__}:calls"
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """
    call_history has a single parameter named method
    that is a Callable and returns a Callable.
    """
    # input_key = method.__qualname__
    # output_key = method.__qualname__
    
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Generate keys for input and output lists
        """
        # input_key = f"{method.__qualname__}:inputs"
        # output_key = f"{method.__qualname__}:outputs"
        # input = str(args)
        # self._redis.rpush(input_key, input)
        # output = method(self, *args, **kwargs)
        # self._redis.rpush(output_key, output)
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output
    return wrapper


class Cache:
    """
    Create a Cache class.
    """
    def __init__(self):
        """
        In the __init__ method, store an instance of the Redis
        client as a private variable named _redis
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Create a store method that takes a data argument and returns string
        The method should generate a random key (e.g. using uuid), store the
        input data in Redis using the random key and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str,
            fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float, None]:
        """
        In this exercise we will create a get method that take a key
        string argument and an optional Callable argument named fn.
        This callable will be used to convert the data back to the
        desired format.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """
        Also, implement 2 new methods: get_str and get_int that will
        automatically parametrize Cache.get with the correct
        conversion function.
        """
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        """
        Also, implement 2 new methods: get_str and get_int that will
        automatically parametrize Cache.get with the correct
        conversion function.
        """
        return self.get(key, fn=int)

#!/usr/bin/env python3
"""
Writing strings to Redis
"""

import redis
import uuid
from typing import Union, Callable, Optional


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

    def get_int(self, key: int) -> Union[int, None]:
        """
        Also, implement 2 new methods: get_str and get_int that will
        automatically parametrize Cache.get with the correct
        conversion function.
        """
        return self.get(key, fn=int)

#!/usr/bin/python3
"""
A  class LRUCache that inherits from BaseCaching and is a caching system.
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    A class MRUCache that inherits from BaseCaching and is a caching system.
    """
    def __init__(self):
        """
        A method to add an item to the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        A method to add an item to the cache.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key = next(iter(self.cache_data))
                print("DISCARD:", mru_key)
                del self.cache_data[mru_key]

            self.cache_data[key] = item
        else:
            del self.cache_data[key]
            self.cache_data[key] = item

    def get(self, key):
        """
        A method to add an item to the cache.
        """
        if key is not None and key in self.cache_data:
            value = self.cache_data[key]
            del self.cache_data[key]
            self.cache_data[key] = value
            return value
        return None

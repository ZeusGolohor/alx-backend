#!/usr/bin/python3
"""
A  class LRUCache that inherits from BaseCaching and is a caching system.
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    A class LRUCache that inherits from BaseCaching and is a caching system.
    """

    def __init__(self):
        """
        A method to initialize the class.
        """
        super().__init__()
        self.key_times = {}

    def put(self, key, item):
        """
        A method to add an item to the cache.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discarded_key = min(self.key_times, key=self.key_times.get)
                del self.cache_data[discarded_key]
                del self.key_times[discarded_key]

            self.cache_data[key] = item
            self.key_times[key] = 0  # Reset usage count

    def get(self, key):
        """
        A method used to get a record from the cache.
        """
        if key is not None:
            if key in self.cache_data:
                self.key_times[key] += 1
                return self.cache_data.get(key)
        else:
            return None

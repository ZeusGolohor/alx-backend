#!/usr/bin/python3
"""
A class LIFOCache that inherits from BaseCaching and is a caching system.
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    A class LIFOCache that inherits from BaseCaching and is a caching system.
    """

    def __init__(self):
        """
        A method to initialize the class.
        """
        super().__init__()

    def put(self, key, item):
        """
        A method to add an item to the cache.
        """
        if key is not None and item is not None:
            # Check if cache is full
            if len(self.cache_data) >= self.MAX_ITEMS:
                if self.last_key:
                    if (self.cache_data.get(key) is None):
                        discarded_key = self.last_key
                        del self.cache_data[discarded_key]
                        print("DISCARD: {}".format(discarded_key))
            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """
        A method used to get a record from the cache.
        """
        if key is not None:
            return self.cache_data.get(key)
        else:
            return None

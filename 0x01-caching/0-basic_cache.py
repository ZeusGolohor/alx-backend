#!/usr/bin/python3
"""
A class BasicCache that inherits from BaseCaching and is a caching system.
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    A class BasicCache that inherits from BaseCaching and is a caching system.
    """
    def __init__(self):
        """
        A method to initial the class.
        """
        super().__init__()

    def put(self, key, item):
        """
        To assign to the dictionary self.cache_data the
        item value for the key key.
        """
        if (key is not None or item is not None):
            self.cache_data[key] = item

    def get(self, key):
        """
        To return the value in self.cache_data linked to key.
        """
        if (key is not None):
            return (self.cache_data.get(key))
        else:
            return None

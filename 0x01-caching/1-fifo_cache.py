#!/usr/bin/python3
"""
A class FIFOCache that inherits from BaseCaching and is a caching system.
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    A class FIFOCache that inherits from BaseCaching and is a caching system.
    """
    def __init__(self):
        """
        A method to initialize the class.
        """
        super().__init__()

    def put(self, key, item):
        """
        A method used to add to the cache.
        """
        if (key is not None and item is not None):
            new_dict = {}
            if (super().MAX_ITEMS == len(self.cache_data)):
                if (key is not None and item is not None):
                    if (self.cache_data.get(key) is not None):
                        self.cache_data[key] = item
                    else:
                        i = 0
                        for key1, value in self.cache_data.items():
                            if (i != 0 and i < super().MAX_ITEMS):
                                new_dict[key1] = value
                            else:
                                print("DISCARD: {}".format(key1))
                            i += 1
                        new_dict[key] = item
                        self.cache_data = new_dict
            else:
                if (key is not None and item is not None):
                    self.cache_data[key] = item

    def get(self, key):
        """
        A method used to get a record from the cache.
        """
        if (key is not None):
            return (self.cache_data.get(key))
        else:
            return (None)

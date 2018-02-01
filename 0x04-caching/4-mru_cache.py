#!/usr/bin/python3
""" MRUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """MRU Caching technique with BaseCaching.MAX_ITEMS keys"""
    recently_used = None

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache using MRU Caching technique and
        pop if number of items in cache data is higher (LIFO)
        that BaseCaching.MAX_ITEMS

        :param key: key to be added
        :param item: value to be added

        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self.recently_used in self.cache_data:
                    del self.cache_data[self.recently_used]
                print("DISCARD:", self.recently_used)
            if key in self.cache_data:
                del self.cache_data[key]
            self.cache_data[key] = item
            self.recently_used = key

    def get(self, key):
        """Get an item by key

        :param key: key to be looked for

        """
        if key is not None:
            self.recently_used = key
            return self.cache_data.get(key)
        return None

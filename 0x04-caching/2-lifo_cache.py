#!/usr/bin/python3
""" LIFOCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """LIFO Caching technique which BaseCaching.MAX_ITEMS keys"""

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache using LIFO Caching technique and
        pop if number of items in cache data is higher (LIFO)
        that BaseCaching.MAX_ITEMS

        :param key: key to be added
        :param item: value to be added

        """
        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                print("DISCARD:", self.cache_data.popitem(last=True)[0])
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key

        :param key: key to be looked for

        """
        if key is not None:
            return self.cache_data.get(key)
        return None

#!/usr/bin/python3
""" LFUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """LFU Caching technique which BaseCaching.MAX_ITEMS keys"""
    lfu_data = None
    index = None

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.lfu_data = OrderedDict()
        self.index = 0

    def put(self, key, item):
        """Add an item in the cache using LFU Caching technique and
        pop if number of items in cache data is higher (LIFO)
        that BaseCaching.MAX_ITEMS

        :param key: key to be added
        :param item: value to be added

        """
        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]
                self.lfu_data[key] += 1
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                sorted_index = [
                    (k,
                     self.lfu_data[k]) for k in sorted(
                        self.lfu_data,
                        key=self.lfu_data.get,
                        reverse=False)][0][0]
                print("DISCARD:", sorted_index)
                del self.cache_data[sorted_index]
                del self.lfu_data[sorted_index]
            self.cache_data[key] = item
            if key not in self.lfu_data:
                self.lfu_data[key] = 0

    def get(self, key):
        """Get an item by key

        :param key: key to be looked for

        """
        if key is not None:
            if key in self.lfu_data:
                self.lfu_data[key] += 1
            return self.cache_data.get(key)
        return None

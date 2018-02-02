#!/usr/bin/python3
""" LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU Caching technique which BaseCaching.MAX_ITEMS keys"""
    lru_data = None
    index = None

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.lru_data = dict()
        self.index = 0

    def put(self, key, item):
        """Add an item in the cache using LRU Caching technique and
        pop if number of items in cache data is higher (LIFO)
        that BaseCaching.MAX_ITEMS

        :param key: key to be added
        :param item: value to be added

        """
        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # print(self.lru_data)
                sorted_index = [
                    (k,
                     self.lru_data[k]) for k in sorted(
                        self.lru_data,
                        key=self.lru_data.get,
                        reverse=False)][0][0]
                print("DISCARD:", sorted_index)
                del self.cache_data[sorted_index]
                del self.lru_data[sorted_index]
            self.cache_data[key] = item
            self.lru_data[key] = self.index
            self.index += 1

    def get(self, key):
        """Get an item by key

        :param key: key to be looked for

        """
        if key is not None:
            if key in self.lru_data:
                self.lru_data[key] = self.index
                self.index += 1
            return self.cache_data.get(key)
        return None

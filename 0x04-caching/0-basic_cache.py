#!/usr/bin/python3
""" BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """basic caching technique which stores unlimited keys"""

    def put(self, key, item):
        """Add an item in the cache

        :param key: key to be added
        :param item: value to be added

        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key

        :param key: key to be looked for

        """
        if key is not None:
            return self.cache_data.get(key)
        return None

#!/usr/bin/python3
""" 9-insert_school """
import pymongo


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection based on kwargs

    :param mongo_collection: pymongo collection object
    :param **kwargs: attributes to be included

    """
    return mongo_collection.insert(kwargs)

#!/usr/bin/python3
""" 8-all """
import pymongo


def list_all(mongo_collection):
    """lists all documents in a collection

    :param mongo_collection: pymongo collection object

    """
    return mongo_collection.find()

#!/usr/bin/python3
""" 12-log_stats """
from pymongo import MongoClient


def count_all(mongo_collection):
    """counts all documents in a collection

    :param mongo_collection: pymongo collection object

    """
    return mongo_collection.count()


def count_method(mongo_collection, method):
    """counts all documents in a collection with particular method

    :param mongo_collection: pymongo collection object
    :param method: method to be searched

    """
    return mongo_collection.count({"method": method})


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    ngnix = client.logs.ngnix
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print("{} logs".format(count_all(ngnix)))
    print("Methods:")
    for method in methods:
        print("\t method {}: {}".format(method, count_method(ngnix, method)))
    print("{} status check".format(ngnix.count(
        {"method": "GET", "path": "/status"})))

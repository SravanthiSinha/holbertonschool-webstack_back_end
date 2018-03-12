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
    nginx = client.logs.nginx
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print("{} logs".format(count_all(nginx)))
    print("Methods:")
    for method in methods:
        print("\tmethod {}: {}".format(method, count_method(nginx, method)))
    print("{} status check".format(nginx.count(
        {"method": "GET", "path": "/status"})))

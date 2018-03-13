#!/usr/bin/python3
""" 102-log_stats """
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


def top_10_ips(mongo_collection):
    """
    print top 10 of the most present IPs in the collection nginx of the
    database logs
    :param mongo_collection: pymongo collection object
    """
    criteria = [{"$group": {"_id": "$ip", "count": {"$sum": 1}}},
                {"$sort": {"count": -1}}, {"$limit": 10}]
    ips = mongo_collection.aggregate(criteria)
    print("IPs:")
    for ip in ips:
        print("\t{}: {}".format(ip.get('_id'), ip.get('count')))


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
    top_10_ips(nginx)

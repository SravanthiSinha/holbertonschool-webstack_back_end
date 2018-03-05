#!/usr/bin/python3
""" 11-schools_by_topic """
import pymongo


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic

    :param mongo_collection: the pymongo collection object
    :param topic: topic  to be searched

    """
    return mongo_collection.find({"topics": {"$eq": topic}})

#!/usr/bin/python3
""" 10-update_topics """
import pymongo


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document based on the name

    :param mongo_collection: pymongo collection object
    :param name: the school name to update
    :param topics: the list of topics approached in the school

    """
    mongo_collection.update({"name": name},
                            {"$set": {"topics": topics}},
                            multi=True,
                            upsert=False)

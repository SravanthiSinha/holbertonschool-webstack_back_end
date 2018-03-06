#!/usr/bin/python3
""" 101-students """
import pymongo


def top_students(mongo_collection):
    """returns all students sorted by average score

    :param mongo_collection: pymongo collection object

    """
    criteria = [{"$unwind": "$topics"},
                {"$group": {"_id": "$_id",
                            "name": {"$first": "$name"},
                            "averageScore": {"$avg": "$topics.score"}}},
                {"$sort": {"averageScore": -1}}]
    return mongo_collection.aggregate(criteria)

#!/usr/bin/env python3
"""return all students sorted by average score"""


def top_students(mongo_collection):
    """return all students sorted by average score"""
    pipeline = [{"$project": {"name": "$name",
                              "averageScore": {"$avg": "$topics.score"}}},
                {'$sort': {'averageScore': -1}}]

    results = mongo_collection.aggregate(pipeline)
    # Convert the aggregation cursor to a list and return it
    return list(results)

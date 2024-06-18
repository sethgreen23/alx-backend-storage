#!/usr/bin/env python3
"""update all topics of a school document based on the name()"""


from pymongo import MongoClient



def update_topics(mongo_collection, name, topics):
	"""update all topics of a school document based on the name()"""
	query = {"name": name}
	newValues = {'$set': {"topics": topics}}
	return mongo_collection.update_many(query, newValues)

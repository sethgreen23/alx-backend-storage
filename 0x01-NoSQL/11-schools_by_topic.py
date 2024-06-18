#!/usr/bin/env python3
"""update all topics of a school document based on the name()"""


from pymongo import MongoClient



def schools_by_topic(mongo_collection, topic):
	"""update all topics of a school document based on the name()"""
	query = {"topics": topic}
	return mongo_collection.find(query)

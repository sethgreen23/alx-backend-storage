#!/usr/bin/env python3
"""list all documents in a collection"""


from pymongo import MongoClient



def list_all(mongo_collection):
	"""Return all documents in a collection"""
	documents = mongo_collection.find()
	return documents if documents is not None else []

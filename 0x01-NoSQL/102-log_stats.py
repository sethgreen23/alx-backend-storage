#!/usr/bin/env python3
"""update all topics of a school document based on the name()"""


from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    print("{} logs".format(collection.count_documents({})))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))
    status_check = collection.count_documents({"path": "/status"})
    print("{} status check".format(status_check))
    print("IPs:")
    ips = collection.distinct("ip")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    results = collection.aggregate(pipeline)
    for result in results:
        print("\t{}: {}".format(result.get("_id"), result.get("count")))

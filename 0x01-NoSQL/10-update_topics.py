#!/usr/bin/env python3
"""
Write a Python function that changes all topics of a school
document based on the name:
"""

from pymongo import MongoClient

def update_topics(mongo_collection, name, topics):
    """
    Prototype: def update_topics(mongo_collection, name, topics):
    mongo_collection will be the pymongo collection object
    name (string) will be the school name to update
    topics (list of strings) will be the list of topics approached in the school
    """
    result = mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
    return result

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")
    db = client["mydatabase"]
    collection = db["mycollection"]
    new_id = update_topics(collection, name = "test", topics = ["topic1"])
    client.close()
    
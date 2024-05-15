#!/usr/bin/env python3
"""
Write a Python function that returns the list of school having a specific topic:
"""

from pymongo import MongoClient

def schools_by_topic(mongo_collection, topic):
    """
    Prototype: def schools_by_topic(mongo_collection, topic):
    mongo_collection will be the pymongo collection object
    topic (string) will be topic searched
    """
    result = mongo_collection.find({"topics": topic})
    return result

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")
    db = client["mydatabase"]
    collection = db["mycollection"]
    result = schools_by_topic(collection, topic = "topic")
    client.close()
    
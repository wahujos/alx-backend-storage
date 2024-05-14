#!/usr/bin/env python3
"""
Write a Python function that inserts a new document in a collection based on kwargs:
"""

from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):
    """
    Prototype: def insert_school(mongo_collection, **kwargs):
    mongo_collection will be the pymongo collection object
    Returns the new _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")
    db = client["mydatabase"]
    collection = db["mycollection"]
    new_id = insert_school(collection, name = "test")
    client.close()
    
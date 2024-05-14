#!/usr/bin/env python3
"""
Write a Python function that lists all documents in a collection:
"""

from pymongo import MongoClient

def list_all(mongo_collection):
        """
        Prototype: def list_all(mongo_collection):
        Return an empty list if no document in the collection
        mongo_collection will be the pymongo collection object
        """
        results = list(mongo_collection.find())
        return results

if __name__ == "__main__":
    
    client = MongoClient("mongodb://localhost:27017/")
    db = client["mydatabase"]
    collection = db["mycollection"]
    documents = list_all(collection)
    print(documents)
    client.close()

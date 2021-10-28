import pandas as pd
from pymongo import MongoClient

# mongo_client = MongoClient('localhost', 27017)
# db = mongo_client.some_database
# col = db.some_collection
# cursor = col.find()
# print("total docs returned by find():", len( list(cursor) ))
client = MongoClient("mongodb://localhost:27017/")
 
# Database Name
db = client["main_data"]
 
# Collection Name
col = db["pradeep"]
 
x = col.find()
 
for data in x:
    print(data['director_name'])
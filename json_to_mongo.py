import pymongo
from pymongo import MongoClient
import pandas as pd
import json

#連線mongoDB
mongoclient = MongoClient(host='localhost', port=27017)
db = mongoclient.test
collection = db.test

with open('test.json') as f:
    file_data = json.load(f)
    print(file_data)
    print(type(file_data))

collection.insert(file_data )





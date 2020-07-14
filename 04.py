from bson.json_util import loads, dumps
import pymongo
from pymongo import MongoClient
import pandas as pd
import json

#連線mongoDB
mongoclient = MongoClient(host='localhost', port=27017)
db = mongoclient.test
collection = db.test

record = db.test.find_one()
json_str = dumps(record)
print(json_str)
record2 = loads(json_str)
print(record2)
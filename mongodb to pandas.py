import pymongo
from pymongo import MongoClient
import pandas as pd

#連線mongoDB
mongoclient = MongoClient(host='localhost', port=27017)
db = mongoclient.test
collection = db.test

results = collection.find()
for result in results:
    print(result)

print("----------------------------")

list_tmp = []
for r in collection.find({}, {'_id':0}):
    list_tmp.append(r)
data = pd.DataFrame(list_tmp)
print(data)

import pymongo
from pymongo import MongoClient
import pandas as pd
import json

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.test

student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}

#result = collection.insert_one(student)
#print(result)

# result = collection.insert_many([student1, student2])
# print(result)
# print(result.inserted_ids)

# result = collection.find_one({'name': 'Mike'})
# print(type(result))
# print(result)
#
# from bson.objectid import ObjectId
#
# result = collection.find_one({'_id': ObjectId('5f09c9333b85a1e99a3246c9')})
# print(result)

# results = collection.find({'age': 20})
# print(results)
# for result in results:
#     print(result)
#
# results = collection.find({'age': {'$gt': 20}})
# for result in results:
#     print(result)
#
# results = collection.find({'name': {'$regex': '^s.*'}})
# print(results)
# for i in results:
#     print(i)

# count = collection.find().count()
# print(count)
#
# count = collection.find({'age': 20}).count()
# print(count)

# results1 = collection.find().sort('name', pymongo.ASCENDING)
# print([result['name'] for result in results1])
# results2 = collection.find().sort('age', pymongo.DESCENDING)
# for result in results2:
#     print(result)

# results = collection.find().sort('name', pymongo.ASCENDING).skip(2)
# print([result['name'] for result in results])
#
# results = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(2)
# print([result['name'] for result in results])
#
# condition = {'name': 'Kevin'}
# student = collection.find_one(condition)
# student['age'] = 25
# result = collection.update(condition, student)
# print(result)

# condition = {'name': 'Jordan'}
# student = collection.find_one(condition)
# student = { "$set": { "age": "123" } }
# result = collection.update_one(condition, student)
# print(result)
#
# for x in collection.find({'name': 'Jordan'}):
#     print(x)
#
# condition = {'name': 'Jordan'}
# result = collection.update_many(condition, { "$set": { "age": "123" } })
# print(result)
#
# for x in collection.find({'name': 'Jordan'}):
#     print(x)
#
# result = collection.delete_one({'name': 'Jordan'})
# print(result)
#
# for x in collection.find({'name': 'Jordan'}):
#     print(x)
#
# results = collection.find_one_and_delete({'name': '123'})
# print(results)
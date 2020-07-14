import pymongo
from pymongo import MongoClient
import pandas as pd
import json

myclient = pymongo.MongoClient()
df = pd.read_csv('test.csv',encoding = 'utf-8')
df.to_json('test.json')
jdf = open('test.json').read()
data = json.loads(jdf)
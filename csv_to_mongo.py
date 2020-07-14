import pymongo
from pymongo import MongoClient
import pandas as pd

#連線mongoDB
mongoclient = MongoClient(host='localhost', port=27017)
db = mongoclient.test
collection = db.test

#export csv to mongodb
def InsertData(path=None):

    df = pd.read_csv(path)
    data = df.to_dict('records')

    collection.insert_many(data, ordered=False)
    print("All the Data has been Exported to Mongo DB Server .... ")

if __name__ == "__main__":
    InsertData(path="test.csv")


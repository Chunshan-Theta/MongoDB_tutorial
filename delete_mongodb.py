from collections import OrderedDict
import time
from pymongo import MongoClient
from pymongo.results import InsertOneResult

myclient: MongoClient = \
    MongoClient("mongodb+srv://root:root@cluster0-u9yg3.mongodb.net/test?retryWrites=true&w=majority")

mydb = myclient["FirstDatabase"]
mycol = mydb["customers"]
mydict = { "name": "John", "address": "Highway 37" }
insert_result: InsertOneResult = mycol.insert_one(mydict)
print(insert_result)
mycol.delete_one(filter={ "_id": insert_result.inserted_id})

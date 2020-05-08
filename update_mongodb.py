from collections import OrderedDict
import time
from pymongo import MongoClient

myclient: MongoClient = \
    MongoClient("mongodb+srv://root:root@cluster0-u9yg3.mongodb.net/test?retryWrites=true&w=majority")

mydb = myclient["FirstDatabase"]
mycol = mydb["customers"]
x = mycol.find_one()
print(x)

query_where = { "_id": x['_id'] }
updated_value = { "$set": { "name": f"Canyon 123, {int(time.time()*1000)}" } }
mycol.update_one(query_where, updated_value)

x = mycol.find_one()
print(x)
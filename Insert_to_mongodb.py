from pymongo import MongoClient
from pymongo.results import InsertOneResult, InsertManyResult

myclient: MongoClient = \
    MongoClient("mongodb+srv://root:root@cluster0-u9yg3.mongodb.net/test?retryWrites=true&w=majority")
print(myclient.list_database_names())




mydb = myclient["FirstDatabase"]
mycol = mydb["customers"]


# auto generate id column called "_id"
mydict = { "name": "John", "address": "Highway 37" }
x: InsertOneResult = mycol.insert_one(mydict)
print(x, x.inserted_id)


mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

x: InsertManyResult = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x, x.inserted_ids)
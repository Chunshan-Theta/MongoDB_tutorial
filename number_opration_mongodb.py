from pymongo import MongoClient
from pymongo.results import InsertOneResult, InsertManyResult

myclient: MongoClient = \
    MongoClient("mongodb+srv://root:root@cluster0-u9yg3.mongodb.net/test?retryWrites=true&w=majority")
print(myclient.list_database_names())




mydb = myclient["FirstDatabase"]
if "goods" in mydb.list_collection_names():
  mycol = mydb["goods"]
  mycol.drop()

mycol = mydb["goods"]


# auto generate id column called "_id"

mylist = [
  { "name": "goods1", "number": 12,"order_people":["a","b"]},
  { "name": "goods2", "number": 6,"order_people":["b"]},
  { "name": "goods3", "number": 32,"order_people":[]},
  { "name": "goods4", "number": 12,"order_people":["c"]},
  { "name": "goods5", "number": 11,"order_people":[]},
  { "name": "goods6", "number": 15,"order_people":[]},
  { "name": "goods7", "number": 23,"order_people":[]},
  { "name": "goods8", "number": 35,"order_people":[]},
  { "name": "goods9", "number": 21,"order_people":[]},
  { "name": "goods10", "number": 23,"order_people":[]},
  { "name": "goods11", "number": 40,"order_people":[]},
  { "name": "goods12", "number": 25,"order_people":[]}
]

insert_results: InsertManyResult = mycol.insert_many(mylist)


# >
result = mycol.find(filter={
  "number":{
    "$gt":15
  }
})

for i in result:
  print(i)

print("-"*6)

# <
result = mycol.find(filter={
  "number": {
    "$lt": 15
  }
})

for i in result:
  print(i)

print("-" * 6)

# >=
result = mycol.find(filter={
  "number": {
    "$gte": 15
  }
})

for i in result:
  print(i)

print("-" * 6)

# <=
result = mycol.find(filter={
  "number": {
    "$lte": 15
  }
})

for i in result:
  print(i)

print("-" * 6)

# <=
result = mycol.find(filter={
  "number": {
    "$gte": 15,
    "$lte": 30
  }
})

for i in result:
  print(i)

print("-" * 6)


# in
# 1
result = mycol.find(filter={
  "number": {
    "$in": [5,10,15,20,25,30,35,40]
  }
})

for i in result:
  print(i)

print("-" * 6)

# 2
result = mycol.find(filter={
  "order_people": {
    "$in": ["a", "b"]
  }
})

for i in result:
  print(i)

print("-" * 6)
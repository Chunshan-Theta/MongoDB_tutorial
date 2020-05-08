from collections import OrderedDict

from pymongo import MongoClient

myclient: MongoClient = \
    MongoClient("mongodb+srv://root:root@cluster0-u9yg3.mongodb.net/test?retryWrites=true&w=majority")


print(myclient.list_database_names())
mydb = myclient["FirstDatabase"]
mycol = mydb["customers"]

# Find
x = mycol.find_one()

# 1
print("="*6)
print(x)

# 2
print("="*6)
for x in mycol.find():
    print(x)

# 3
print("="*6)
for x in mycol.find({}, {"_id": 0, "name": 1, "address": 1}):
    print(x)


# Find with filter

# 1
print("="*6)
myquery = { "address": "Highway 37" }
mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

# 2 https://transbiz.com.tw/regex-regular-expression-ga-%E6%AD%A3%E8%A6%8F%E8%A1%A8%E7%A4%BA%E5%BC%8F/ 正規表示式
print("="*6)

myquery = {
    "address": {
        "$regex": "^Y|^S",
    }
}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)


# sort
# 1
'''
sort("name", 1) #ascending
sort("name", -1) #descending
'''
print("="*6)

myquery = {
    "address": {
        "$regex": "^Y|^S",
    }
}
mydoc = mycol.find(myquery).sort("address")
for x in mydoc:
    print(x)
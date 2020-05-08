from pymongo import MongoClient

myclient: MongoClient = \
    MongoClient("mongodb+srv://root:root@cluster0-u9yg3.mongodb.net/test?retryWrites=true&w=majority")


print(myclient.list_database_names())
mydb = myclient["FirstDatabase"]
mycol = mydb["customers"]

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


# count
# 1
print("="*6)
find_all_count = mycol.count_documents(filter={})
print(f"SUM COUNT: {find_all_count}")

# 2
print("="*6)
find_all_count = mycol.count_documents(filter={
    "address": {
        "$regex": "^Y|^S",
    }
})
print(f"SUM COUNT: {find_all_count}")

# limit
# 1
print("="*6)
mydoc = mycol.find().sort("address").limit(10)
for i,x in enumerate(mydoc):
    print(i,x)

# 2
print("="*6)
mydoc = mycol.find(limit=10).sort("address")
for i,x in enumerate(mydoc):
    print(i,x)

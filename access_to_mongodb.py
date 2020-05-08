from pymongo import MongoClient

myclient: MongoClient = \
    MongoClient("mongodb+srv://root:root@cluster0-u9yg3.mongodb.net/test?retryWrites=true&w=majority")
print(myclient.list_database_names())

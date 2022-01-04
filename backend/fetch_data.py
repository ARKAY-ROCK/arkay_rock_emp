from pymongo import MongoClient as mg

db_cli = mg ()

doc = db_cli['users']['users'].find()


for i in doc:
    print(i)
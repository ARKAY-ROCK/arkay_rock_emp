from pymongo import MongoClient as mg

db_cli = mg()


old_value = {"sq_ft": "0"}
up_value = {"$set": {"sq_ft": 123}, "$set": {"month": "jan"}}


db_cli['salary_log']['monthly'].update_one(old_value, up_value)


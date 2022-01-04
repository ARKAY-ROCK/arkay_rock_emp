from pymongo import MongoClient as mg

cli = mg ()

all_employee = cli.list_database_names()

#all_employee = ['Kannan_402']

print(all_employee)

for i in all_employee:
    for j in cli[i].monthly_sq_feet.find({}):
        print(  i , " " , j["_id"] , "   " , j["month"])
        id_name = j["_id"]+"_"+"2020"
        month = j["_id"]+"_"+"2020"
       # month = j["_id"]
        print (id_name , " " , month)
        cli[i].monthly_sq_feet.update({"_id":'december'},{"$set":{'month':'december_2020'}})
       # cli[i].monthly_sq_feet.update({"month":j['month']},{"$set":{'_id':id_name}})


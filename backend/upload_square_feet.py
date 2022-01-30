from pymongo import MongoClient as mg

db_cli = mg()


class AddSquareFeet:
    def __init__(self, employee_name, month, year, sq_ft):
        self.employee_name = employee_name
        self.month = month
        self.year = str(year)
        self.sq_ft = str(sq_ft)

    def add_sq_ft(self):
        che_month = self.month+"_"+str(self.year)
        print(che_month)
        check_exist = db_cli[self.employee_name]['monthly_sq_feet'].count_documents(
            {'month': che_month})
        if (check_exist):
            id_check = {'month':che_month}
            new_value = { "$set": {'total_sq_feet' : self.sq_ft}}
            db_cli[self.employee_name]['monthly_sq_feet'].update_one(id_check,new_value)
            return "updated"
        else:
            sqtft = {"_id": che_month,
                     "month": che_month,
                     "employee_name": self.employee_name,
                     "total_sq_feet": self.sq_ft
                     }
            db_cli[self.employee_name]['monthly_sq_feet'].insert_one(sqtft)
            return "Added"

        return "error"


#print(AddSquareFeet('raj_001', 'january', '2021', 13).add_sq_ft())

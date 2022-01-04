from pymongo import MongoClient as mg

db_cli = mg ()

class Employee_details:
    def __init__ (self,req):
        self.req = req
    def get_employee_details(self):
        ab = {}
        bc = []
        all_employees = db_cli.list_database_names()
        for j in all_employees:
            for i in db_cli[j].details.find({}, {"_id": False}):
                ab.update(i)
                bc.append(i)
        
        print(bc)


emp_det = Employee_details('req').get_employee_details()

print(emp_det)
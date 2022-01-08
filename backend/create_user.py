from pymongo import MongoClient as mg
from convert_mon_list import *

db_con = mg()
users_table = db_con["users"]["users"]

class create_user:
    def __init__(self, user_name, role, password):
        self.user_name = user_name
        self.role = role
        self.password = password

    def create_account(self):
        create_account = users_table.insert_one({
            'user_name': self.user_name,
            'role': "admin",  # admin for default login
            'password': self.password,
            'user_role': self.role+"_"+"role" , # to restrict action
            'show_role':self.role
        })
        return (create_account)


class reterive_info:
    def __init__(self, user_name):
        self.user_name = user_name

    def reterive_information(self):
        user_info = users_table.find({'user_name': self.user_name},{"_id":False})
        list_converter = convert_mon_list(user_info)
        return list_converter.convert_to_list()
    
    def reterive_employee_info(self):
        emp_info = db_con[self.user_name].details.find_one({'EmployeeCode':self.user_name.split("_")[1]},{'_id':False})
        
        return emp_info



class reterive_users:
    def __init__(self, table):
        self.table = table

    def active_user_list(self):
        users = []
        user_list = db_con['users']['users'].find()
        list_converter = convert_mon_list(user_list)
        for i in list_converter.convert_to_list():
            users.append({'users': i["user_name"]})
        return users


class CheckUserExist:
    def __init__ (self,user_name):
        self.user_name = user_name
    
    def check_user_exist(self):
       user_ex = 0  
       user_ex =  users_table.count_documents({'user_name':self.user_name})

       return str(user_ex)

class DeleteUser:
    def __init__ (self,employee_name):
        self.employee_name = employee_name
    def delete_employee(self):
        db_con.drop_database(self.employee_name)

        return "Employee Removed"

#c_u = create_user('ram2','user','ram')
# print(c_u.create_account())

#cus_ret = reterive_info("ram")
# print(cus_ret.reterive_information())
#print(CheckUserExist('admins').check_user_exist())

#DeleteUser('firstone_001').delete_employee()
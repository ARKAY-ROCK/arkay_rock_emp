from pymongo import MongoClient as mg

db_cli = mg()


class enroll_employee:
    def __init__(self, req):
        self.req = req

    def create_account(self):

        emp_db_path = db_cli[self.req['FirstName'] +
                            "_"+self.req['EmployeeCode']].details
        print(self.req)
        emp_details = {
            "FirstName": self.req['FirstName'].lower(),
            "MiddleName": self.req['MiddleName'].lower(),
            "LastName": self.req['LastName'].lower(),
            "Email": self.req['Email'].lower(),
            "EmployeeCode": self.req['EmployeeCode'],
            "DOB": self.req['DOB'],
            "ContactNo": self.req['ContactNo'],
            "role": self.req['EmployeeType'].lower(),
            "department": self.req['DepartmentID'].lower(),
            "DateOfJoining": self.req['DateOfJoining'],
            "position": self.req['PositionID'].lower(),
            "TerminateDate": self.req['TerminateDate'],
            "Bloodgroup": self.req['BloodGroup'].lower(),
            "EmergencyContact": self.req['EmergencyContact'],
            "ESINumber": self.req['ESINumber'],
            "EPFNumber": self.req['EPFNumber']

        }


        emp_db_path.insert_one(emp_details)

        return "Employee Enrolled"
    
    def update_employee (self):

        return None

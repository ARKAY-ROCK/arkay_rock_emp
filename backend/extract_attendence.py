from pymongo import MongoClient as mg

db_cli = mg()


class ExtractAttendence:
    def __init__(self, date=None, month_year=None):
        self.date = date
        self.month_year = month_year

    def extract_attendence_date(self):
        print(self.date)
        attendence = []
        db_date = self.date['date'][-2:] + "/"+self.date['date'][5:7] + "/" + self.date['date'][:4]
        all_emp = db_cli.list_database_names()
        for j in all_emp:
            k = db_cli[j].attendence.find_one({"_id": db_date})
            if (k != None):
                 attendence.append(k)

        return attendence
    
    def extract_attendence_month_year(self):
            print(self.month_year)
            attendence = []
            all_emp = db_cli.list_database_names()
            for j in all_emp:
                k = db_cli[j].attendence.find({"month": self.month_year})
                for i in k:
                    print(i)
                    attendence.append(i)
            
            return attendence


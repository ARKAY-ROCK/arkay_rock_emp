from pymongo import MongoClient as mg 
from datetime import datetime

db_cli = mg ()
months_list_post = ["january", "february", "march", "april", "may",
                    "june", "july", "august", "september", "october", "november", "december"]


class add_attendence:
    def __init__ (self,req):
        self.req = req
    
    def add_mannual_attendence (self):

        if (str(self.req['employee_name']) == 'all'):
            print("all_attendence")
            all_employees = db_cli.list_database_names()
            print(all_employees)
            if (len(str(self.req['in_time'])) == 5 and len(str(self.req['out_time'])) == 5 and len(str(self.req['delay'])) >= 1 and len(str(self.req['advance'])) >= 1 and len(str(self.req['overtime'])) >= 1):
                new_date = str(self.req['date'][-2:]) + "/" + str(
                    self.req['date'][5:7])+"/" + str(self.req['date'][:4])
                total_hours = abs(int(str(self.req['out_time'])[
                              0:2])-int(str(self.req['in_time'])[0:2]))
                total_min = abs(int(str(self.req['out_time'])[
                            3:5])-int(str(self.req['in_time'])[3:5]))
                total_hours_worked = datetime.strptime(
                    str(total_hours)+":"+str(total_min), "%H:%M").time()
                month = months_list_post[int(
                    new_date[3:5])-1]+"_"+str(new_date[-4:])
                for i in all_employees:
                    db_cli[i].attendence.delete_one({'_id': new_date})
                    att_format = {'_id': new_date, 'status': 'present', 'total_hours': str(total_hours_worked), 'month': month,
                              'date': new_date, 'employee_name': i, 'in_time': str(self.req['in_time']),
                              'out_time': str(self.req['out_time']), 'delay': str(self.req['delay']),
                              'advance': str(self.req['advance']), 'overtime': str(self.req['overtime'])}

                    db_cli[i].attendence.insert_one(att_format)
            if (str(self.req['in_time']) == "0" and str(self.req['out_time']) == "0" and str(self.req['delay']) == "0" and str(self.req['advance']) == "0" and str(self.req['overtime']) == "0"):
                for i in all_employees:
                    new_date = str(self.req['date'][-2:]) + "/" + str(
                    self.req['date'][5:7])+"/" + str(self.req['date'][:4])
                    db_cli[i].attendence.delete_one({'_id': new_date})
                    status = 'success'

        if (str(self.req['employee_name']) != 'all'):
            print("att delete")
            if (str(self.req['in_time']) == "0" and str(self.req['out_time']) == "0" and str(self.req['delay']) == "0" and str(self.req['advance']) == "0" and str(self.req['overtime']) == "0"):

                new_date = str(self.req['date'][-2:]) + "/" + str(self.req['date'][5:7])+"/" + str(self.req['date'][:4])
                db_cli[str(self.req['employee_name'])].attendence.delete_one({'_id': new_date})
                status = 'deleted'
                return "deleted"

        prev_overtime = 0
        if (self.req['in_time'] is None):
            print("None")
        if (len(str(self.req['in_time'])) == 5 and len(str(self.req['out_time'])) == 5 and len(str(self.req['delay'])) >= 1 and len(str(self.req['advance'])) >= 1 and len(str(self.req['overtime'])) >= 1):
            status = 'success'
            if(1 == 1):
                new_date = str(self.req['date'][-2:]) + "/" + str(
                self.req['date'][5:7])+"/" + str(self.req['date'][:4])
                count = db_cli[str(self.req['employee_name'])].attendence.count_documents({'date': new_date})
                print('count     ', count)

                month = months_list_post[int(
                new_date[3:5])-1]+"_"+str(new_date[-4:])
                print(month)
                total_hours = abs(int(str(self.req['out_time'])[
                              0:2])-int(str(self.req['in_time'])[0:2]))
                total_min = abs(int(str(self.req['out_time'])[
                            3:5])-int(str(self.req['in_time'])[3:5]))
                print(total_hours, total_min)
                total_hours_worked = datetime.strptime(
                str(total_hours)+":"+str(total_min), "%H:%M").time()
                print(total_hours_worked)
                att_format = {'_id': new_date, 'status': 'present', 'total_hours': str(total_hours_worked), 'month': month,
                          'date': new_date, 'employee_name': str(self.req['employee_name']), 'in_time': str(self.req['in_time']),
                          'out_time': str(self.req['out_time']), 'delay': str(self.req['delay']),
                          'advance': str(self.req['advance']), 'overtime': str(self.req['overtime'])}
                status = 'success'
                print(att_format)
                if (count == 1):
                    for ot in db_cli[str(self.req['employee_name'])].attendence.find({'_id': new_date}):

                        prev_overtime = float(ot['overtime'])
                    att_format.update(
                    {'overtime': prev_overtime+float(self.req['overtime'])})
                    print('new overtime', prev_overtime +
                      float(self.req['overtime']))
                    print(att_format)
                    db_cli[str(self.req['employee_name'])
                       ].attendence.delete_one({'_id': new_date})
                    db_cli[str(self.req['employee_name'])
                       ].attendence.insert_one(att_format)
                if (count == 0):
                    db_cli[str(self.req['employee_name'])
                       ].attendence.insert_one(att_format)

            if(1 == 2):
                status = 'error'

        if (len(str(self.req['in_time'])) < 5 or len(str(self.req['out_time'])) < 5 or len(str(self.req['delay'])) < 1 or len(str(self.req['advance'])) < 1 or len(str(self.req['overtime'])) < 1):
            status = 'error'

        return status
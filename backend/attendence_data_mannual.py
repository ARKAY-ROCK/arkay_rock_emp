from pymongo import MongoClient as mg 
from calendar import monthcalendar, monthrange , weekday , SUNDAY

db_cli = mg ()
months_list_post = ["january", "february", "march", "april", "may",
                    "june", "july", "august", "september", "october", "november", "december"]

class attendence_data_mannual:
    def __init__ (self,emp_name,month=None,year=1998,date=None):
        self.emp_name = emp_name
        self.month = month
        self.year = int(year)
        self.date = date
    
    def get_month_report (self):

        if (self.month=='feburary'):
            m = months_list_post.index('february') + 1
            fetch_month = "february"
        if (self.month != 'feburary'):
            m = months_list_post.index(self.month) + 1
            fetch_month =self.month
        dc = SUNDAY
        matrix = monthcalendar(self.year, m)
        final_sunday = []
        present_day = []
        sundays = sum(1 for x in matrix if x[dc] != 0)
        sunday_list = list(x for x in matrix if x[dc] != 0)
        for s in sunday_list:
            for sun in s[-1:]:
                final_sunday.append(sun)
        all_doc = db_cli[self.emp_name].attendence.find({'month': fetch_month+"_"+str(self.year)})
        days_in_month = monthrange(int(self.year), m)[1]
        overtime = 0 
        for k in all_doc:
            if (int(k['date'][0:2]) in final_sunday):
                 print("sunday")
            if (int(k['date'][0:2]) not in final_sunday):
                present_day.append(int(k['date'][0:2]))
            try:
                 overtime = overtime + float(k['overtime'])
            except:
                print("e")
        for ss in final_sunday:
            present_day.append(int(ss))
        present_day.sort()
        all_days_month = []
        for dm in range(1, days_in_month+1):
            all_days_month.append(dm)
        absent_list = []
        for ab in all_days_month:
            if ab not in present_day:
                 absent_list.append(ab)
        present_day = 0
        absent_day = 0
        present_days = db_cli[self.emp_name].attendence.find({'month': fetch_month+"_"+str(self.year)})
        for i in present_days:
            if (int(i['date'][:2]) not in final_sunday):
                 present_day = present_day + 1
        if (present_day):
             present_day = present_day + sundays
        if (present_day == 0):
            present_day = 0
        absent_day = days_in_month - present_day
        final_list = {'present_day': present_day, 'absent_day': str(
        absent_day)+"  -  "+str(absent_list), 'overtime': overtime}

        return final_list
    
    def selected_day_report(self):
        details = db_cli[self.emp_name].attendence.find({'date': self.date})
        department = 'None'
        in_time = '00:00'
        out_time = '00:00'
        advance = '0'
        overtime = '0'
        delay = '00:00:00'        
        for j in db_cli[self.emp_name].details.find({}):
            department = j['FirstName'] + " " + j['LastName'].upper() + \
            " : " + j['department']+" "+j['position']
        for i in details:
            if 'in_time' in i:
                in_time = i['in_time']
                out_time = i['out_time']
                advance = i['advance']
                delay = i['delay']
                overtime = i['overtime']
            else:
                in_time = '00:00'
                out_time = '00:00'
                advance = '0'
                overtime = '0'
                delay = '00:00:00'
        final_list = {'department': department, 'in_time': in_time,
                   'out_time': out_time, 'advance': advance, 'overtime': overtime, 'delay': delay}
 
        
        return final_list
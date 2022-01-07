from pymongo import MongoClient as mg
from attendence_data_mannual import *
from slip_download_html import * 

db_cli = mg()

class salary_slip_details:
    def __init__ (self,emp_name,month,year):
        self.emp_name = emp_name
        self.month = month
        self.year = year
    
    def get_salary_details(self):
        month_details = attendence_data_mannual(self.emp_name,self.month,self.year).get_month_report()
       
        document = str(self.month)+ "_" + str(self.year)
        salary_table = db_cli[self.emp_name]['salary_history'].find_one({'month':document})
        employee_details = db_cli[self.emp_name].details.find_one({'EmployeeCode':self.emp_name.split("_")[1]})
        employee_salary_details = db_cli[self.emp_name].salary_details.find_one({'employee_name':self.emp_name})
        slip_details = {
            'employee_name':salary_table['employee_name'].split("_")[0].upper(),
            'employee_id':salary_table['employee_name'].split("_")[1],
            'month' : salary_table['month'].split("_")[0],
            'conveyance' : round(float( salary_table['conveyence']),1),
            'esi': salary_table['esi_employee_share'],
            'epf' : salary_table['epf_employee_share'],
            'year' : salary_table['month'].split("_")[1],
            'present_days' : month_details['present_day'],
            'absent_days' : month_details['absent_day'].split("-")[0].replace(" ",""),
            'employee_dep': employee_details['department'].upper(),
            'employee_design' : employee_details['position'].upper(),
            'employee_pf_no': employee_details['EPFNumber'],
            'employee_bank' : employee_salary_details['bank_name'],
            'employee_account' : employee_salary_details['account_no'],
            'emp_basic' : salary_table['basic_salary'],
            'emp_pf' : round(float(salary_table['epf_employee_share']),1),
            'emp_hr': round(float(salary_table['hra']),1),
            'emp_wl' : round(float(salary_table['wl_allowence']),1),
            'emp_esi':round(float(salary_table['esi_employee_share']),1),
            'emp_net' : salary_table['net_salary'],
            'emp_det' : round(float(salary_table['epf_employee_share']) + float(salary_table['esi_employee_share']),1),
            'emp_fin' : salary_table['final_salary'],
            'emp_month': self.month.upper(),
            'emp_year':self.year
        }
        for i in slip_details:
            print(i , "  : ",slip_details[i])
        replace_value = SlipDownloadHtml(slip_details).replace_html()
        return replace_value


#https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_msvc2015-win64.exe
#ob = salary_slip_details('id_name','month','year')
#print(ob.get_salary_details())


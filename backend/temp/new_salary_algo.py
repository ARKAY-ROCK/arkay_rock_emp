## roll = admin-admin (Aadmin)
## unrolll = adminrollunroll (user&pw) (Admin A)

## 100 to 9000 
### all small case

## drop down

# mc = Admin
# ec = 
# dc = 
# bp = 
# hp = 
# carving =
# packing =
# maintanence= 
# clean = 
# drivers = 
# admin = 


## esi form
   # s.no , esi_no , name, D.O.j, working_days , wages , esi 
   
## epf form 
   # s.no , epf_no, name , ncs , basicpay , employee_share , employeer_share , employeer_pension   
   


from flask import Flask,jsonify,request,send_file
from threading import Thread
import time
import hashlib
from flask_pymongo import PyMongo
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager,create_access_token
from pymongo import MongoClient as mg
from datetime import datetime
from calendar import monthrange, weekday, SUNDAY
import os
print("pdf export")
from flask import send_from_directory
import webbrowser
import calendar
from operator import itemgetter
#from upload_essl_file_in_out_auto_seperate import *
import upload_essl_file_in_out_auto_seperate
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, \
    Table, TableStyle


months_list_post = ["january","february","march","april","may","june","july","august","september","october","november","december"]

sal = mg()

ali = 'CENTER'
dim = (900.0,1000.0)

class DataToPdf():
    """
    Export a list of dictionaries to a table in a PDF file.
    """

    def __init__(self, fields, data, sort_by=None, title=None):
        """
        Arguments:
            fields - A tuple of tuples ((fieldname/key, display_name))
                specifying the fieldname/key and corresponding display
                name for the table header.
            data - The data to insert to the table formatted as a list of
                dictionaries.
            sort_by - A tuple (sort_key, sort_order) specifying which field
                to sort by and the sort order ('ASC', 'DESC').
            title - The title to display at the beginning of the document.
        """
        global ali
        self.fields = fields
        self.data = data
        self.title = title
        self.sort_by = sort_by
        print(len(fields))
        if (len(fields) < 11) :
           ali = 'LEFT'
           dim = (780.0,1000.0)
            ## esi (780.0,1000.0)
        if ( len(fields) >= 11) :
           ali = 'CENTER'
           dim = (900.0,1000.0)
              ## epf ((900.0,1000.0))
        
        
    def export(self, filename, data_align='LEFT', table_halign=ali):
        """
        Export the data to a PDF file.

        Arguments:
            filename - The filename for the generated PDF file.
            data_align - The alignment of the data inside the table (eg.
                'LEFT', 'CENTER', 'RIGHT')
            table_halign - Horizontal alignment of the table on the page
                (eg. 'LEFT', 'CENTER', 'RIGHT')
        """
        doc = SimpleDocTemplate(filename, pagesize=dim)

        styles = getSampleStyleSheet()
        styleH = styles['Heading1']

        story = []

        if self.title:
            story.append(Paragraph(self.title, styleH))
            story.append(Spacer(1, 0.25 * inch))

        if self.sort_by:
            reverse_order = False
            if (str(self.sort_by[1]).upper() == 'DESC'):
                reverse_order = True

            self.data = sorted(self.data,
                               key=itemgetter(self.sort_by[0]),
                               reverse=reverse_order)

        converted_data = self.__convert_data()
        table = Table(converted_data, hAlign=table_halign)
        table.setStyle(TableStyle([
            ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('ALIGN',(0, 0),(0,-1), data_align),
            ('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),
            ('BOX', (0,0), (-1,-1), 0.25, colors.black),
        ]))

        story.append(table)
        doc.build(story)

    def __convert_data(self):
        """
        Convert the list of dictionaries to a list of list to create
        the PDF table.
        """
        # Create 2 separate lists in the same order: one for the
        # list of keys and the other for the names to display in the
        # table header.
        keys, names = zip(*[[k, n] for k, n in self.fields])
        new_data = [names]

        for d in self.data:
            new_data.append([d[k] for k in keys])

        return new_data




client=mg()

app=Flask(__name__)
app.secret_key = "super secret key"
app.config['MONGO_DBNAME']='loginuser'
app.config['MONGO_URI']='mongodb://localhost:27017/loginuser'
mongo = PyMongo(app)
bcrypt =Bcrypt(app)
jwt =JWTManager(app)
CORS(app)


dic={}



@app.route('/users/login',methods=['POST'])
def login():
    users=mongo.db.users
    user_name=request.get_json()['user_name']
    password=hashlib.sha256(request.get_json()['password'].encode("UTF-8")).hexdigest()
   
    result =" "

    #response =users.find_one({'user_name':user_name})

    if (1==1):
        #if bcrypt.check_password_hash(response['password',password]):
        if (1==1):
             if(request.get_json()['password']=='admin'):
#            access_token = create_access_token(identity = {'user_name':response['user_name'],'device_name' : response['device_name'] })
               access_token = create_access_token(identity = {'user_name':request.get_json()['user_name'],'device_name' : 'device','Account': 2})
               print(create_access_token)

               result = jsonify({"token":access_token})
        if (1==1):
             if(request.get_json()['password']=='adminrollunroll'):
#            access_token = create_access_token(identity = {'user_name':response['user_name'],'device_name' : response['device_name'] })
               access_token = create_access_token(identity = {'user_name':request.get_json()['user_name'],'user_name' : request.get_json()['user_name'],'Account': 1})
               print(create_access_token)

               result = jsonify({"token":access_token})               
        else:
            result =jsonify({"error":"invalid info"})
    else:
        result = jsonify({"result":"no reesult found"})
    return result
    

@app.route('/all_employee_list',methods=['GET'])
def all_employee_list():
	all_employees=client.list_database_names()
	employee_list=[]
	employee_list.append({'customer_name':"all"})
	for i in all_employees:
		if(i!='admin' and i!='config' and i!='local' and i!='loginuser' and i!='esi_epf_shares' and i!='gopika_jewellers_plan' and i!='hand_dry_const'):
	          	
		  employee_list.append({'customer_name':i})

	return jsonify(employee_list)

months_list_post = ["january","february","march","april","may","june","july","august","september","october","november","december"]

department_list_post = ["main_cutting","edge_cutting","electrical_maintanence","mechanical_maintanence"]


#february  february_2021

@app.route('/all_employee_list',methods=['GET'])
def all_employee_list_new():
	all_employees=client.list_database_names()
	employee_list=[]
	employee_list.append({'customer_name':"all"})
	for i in all_employees:
		if(i!='admin' and i!='config' and i!='local' and i!='loginuser' and i!='esi_epf_shares' and i!='gopika_jewellers_plan' and i!='hand_dry_const'):
	          	
		  employee_list.append({'customer_name':i})

	return jsonify(employee_list)



@app.route('/get_overall_present_absent_overtime',methods=['PUT'])
def get_overall_present_absent_overtime():

    print("requesdted month    ",request.get_json()['month'] )
    y=int (request.get_json()['year'])

    if(request.get_json()['month'] =='feburary'):
  
         m=months_list_post.index('february') + 1
         fetch_month = "february"
    if(request.get_json()['month'] !='feburary'):
        m=months_list_post.index(request.get_json()['month']) + 1
        fetch_month =  request.get_json()['month']

    dc=calendar.SUNDAY
    matrix=calendar.monthcalendar(y,m)
    final_sunday = []
    present_day = []
    sundays = sum(1 for x in matrix if x[dc]!=0)
    sunday_list = list(x for x in matrix if x[dc]!=0)
    for s in sunday_list:
        for sun in s[-1:]:
            final_sunday.append(sun)
            
    print("final sunday      ",final_sunday)        
  
    #for qw in client[request.get_json()['employee_name']].attendence.find():
    all_doc =   client[request.get_json()['employee_name']].attendence.find({'month':fetch_month+"_"+str(request.get_json()['year'])})  
    print(all_doc)
    days_in_month=monthrange(int(request.get_json()['year']),m)[1]
    overtime = 0
    for k in all_doc:
        if (int(k['date'][0:2]) in final_sunday):
           print("sunday")
        if (int(k['date'][0:2]) not  in final_sunday):
            present_day.append(int(k['date'][0:2]))
        try:
          overtime = overtime + float(k['overtime'])
        except:
            print("e")
    for ss in final_sunday:
        present_day.append(int(ss))
    present_day.sort()
    print(present_day)
    all_days_month = []
    for dm in range(1,days_in_month+1):
        all_days_month.append(dm)
    print(all_days_month)    
    absent_list = []
    for ab in all_days_month :
        if ab not in present_day:
            absent_list.append(ab)
    print("ab    ",absent_list)   
    print("sundays     ",sundays,"    days  ",days_in_month)
    
    present_day = 0
    absent_day = 0
    
    
    print(present_day)
    present_days = client[request.get_json()['employee_name']].attendence.find({'month':fetch_month+"_"+str(request.get_json()['year'])})
    print(present_days)
    for i in present_days:
         if (int(i['date'][:2]) not in final_sunday):
             present_day = present_day + 1
         print(i['date'][:2])
    if (present_day) :
        present_day = present_day  + sundays
    if (present_day == 0 ):
        present_day = 0 
    print("present day     ",present_day)
    absent_day = days_in_month - present_day
    final_list = [{'present_day':present_day,'absent_day':str(absent_day)+"  -  "+str(absent_list),'overtime':overtime}]
    
    return jsonify(final_list)

@app.route('/get_selected_day_details',methods=['PUT'])
def get_selected_day_details():
    
    print(request.get_json())
    new_date = str(request.get_json()['date'][-2:]) + "/"+ str(request.get_json()['date'][5:7])+"/" + str(request.get_json()['date'][:4])
    
    print(new_date)
    details = client[request.get_json()['employee_name']].attendence.find({'date':new_date})

    department='None'
    in_time='00:00'
    out_time='00:00'
    advance='0'
    overtime='0'
    delay='00:00:00'
   
    for j in client[request.get_json()['employee_name']].details.find({}):
            department =j['FirstName'] + " " + j['LastName'].upper() + " : "+ j['department']+" "+j['position']
       
    for i in details:
        if 'in_time' in i:    
                in_time = i['in_time']
                out_time = i['out_time']
                advance = i['advance']
                delay = i['delay']
                overtime = i['overtime']
        else:
                
   
            
            in_time='00:00'
            out_time='00:00'
            advance='0'
            overtime='0'
            delay='00:00:00'
    
    final_list = [{'department':department,'in_time':in_time,'out_time':out_time,'advance':advance,'overtime':overtime,'delay':delay}]
    return jsonify(final_list)


@app.route('/add_mannual_attendence_new',methods=['PUT'])
def add_mannual_attendence_new():

    status = 'error'
    print(str(request.get_json()['employee_name']))

    if (str(request.get_json()['employee_name']) == 'all'):
        print("all_attendence")
        all_employees=client.list_database_names()
        print(all_employees)
        if (len(str(request.get_json()['in_time']))== 5 and len(str(request.get_json()['out_time']))==5 and len(str(request.get_json()['delay']))>= 1 and len(str(request.get_json()['advance']))>= 1 and len(str(request.get_json()['overtime']))>=1):
              new_date = str(request.get_json()['date'][-2:]) + "/"+ str(request.get_json()['date'][5:7])+"/" + str(request.get_json()['date'][:4])
              total_hours=abs(int(str(request.get_json()['out_time'])[0:2])-int(str(request.get_json()['in_time'])[0:2]))
              total_min=abs(int(str(request.get_json()['out_time'])[3:5])-int(str(request.get_json()['in_time'])[3:5]))
              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
              month = months_list_post[int(new_date[3:5])-1]+"_"+str(new_date[-4:])
              for i in all_employees:
                 client[i].attendence.delete_one({'_id':new_date}) 
                 att_format = {'_id':new_date,'status':'present','total_hours':str(total_hours_worked),'month':month,
                              'date':new_date,'employee_name':i,'in_time':str(request.get_json()['in_time']),
                              'out_time':str(request.get_json()['out_time']),'delay':str(request.get_json()['delay']),
                              'advance':str(request.get_json()['advance']),'overtime':str(request.get_json()['overtime'])}                  
            
                 client[i].attendence.insert_one(att_format)
        if (str(request.get_json()['in_time'])== "0" and str(request.get_json()['out_time'])== "0" and str(request.get_json()['delay']) == "0" and str(request.get_json()['advance'])== "0" and str(request.get_json()['overtime'])=="0"):
               for i in all_employees:
                   new_date = str(request.get_json()['date'][-2:]) + "/"+ str(request.get_json()['date'][5:7])+"/" + str(request.get_json()['date'][:4])
                   client[i].attendence.delete_one({'_id':new_date})
                   status = 'success'


    if (str(request.get_json()['employee_name']) != 'all'):
        print("att delete")
        if (str(request.get_json()['in_time'])== "0" and str(request.get_json()['out_time'])== "0" and str(request.get_json()['delay']) == "0" and str(request.get_json()['advance'])== "0" and str(request.get_json()['overtime'])=="0"):
               
                   new_date = str(request.get_json()['date'][-2:]) + "/"+ str(request.get_json()['date'][5:7])+"/" + str(request.get_json()['date'][:4])
                   client[str(request.get_json()['employee_name'])].attendence.delete_one({'_id':new_date})
                   status = 'deleted'

    
    prev_overtime = 0 
    if (request.get_json()['in_time'] is None):
            print("None")
    if (len(str(request.get_json()['in_time']))== 5 and len(str(request.get_json()['out_time']))==5 and len(str(request.get_json()['delay']))>= 1 and len(str(request.get_json()['advance']))>= 1 and len(str(request.get_json()['overtime']))>=1):
        status = 'success'
        if(1==1):
                new_date = str(request.get_json()['date'][-2:]) + "/"+ str(request.get_json()['date'][5:7])+"/" + str(request.get_json()['date'][:4])
                count = client[str(request.get_json()['employee_name'])].attendence.find({'date':new_date}).count()
                print('count     ',count)
                
                month = months_list_post[int(new_date[3:5])-1]+"_"+str(new_date[-4:])
                print(month)
                total_hours=abs(int(str(request.get_json()['out_time'])[0:2])-int(str(request.get_json()['in_time'])[0:2]))
                total_min=abs(int(str(request.get_json()['out_time'])[3:5])-int(str(request.get_json()['in_time'])[3:5]))
                print(total_hours,total_min)
                total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
                print(total_hours_worked)
                att_format = {'_id':new_date,'status':'present','total_hours':str(total_hours_worked),'month':month,
                              'date':new_date,'employee_name':str(request.get_json()['employee_name']),'in_time':str(request.get_json()['in_time']),
                              'out_time':str(request.get_json()['out_time']),'delay':str(request.get_json()['delay']),
                              'advance':str(request.get_json()['advance']),'overtime':str(request.get_json()['overtime'])}
                status = 'success'
                print(att_format)
                if (count ==1 ):
                        for ot in client[str(request.get_json()['employee_name'])].attendence.find({'_id':new_date}):
                                
                                prev_overtime = float(ot['overtime'])
                        att_format.update({'overtime':prev_overtime+float(request.get_json()['overtime'])})
                        print('new overtime', prev_overtime+float(request.get_json()['overtime']))
                        print(att_format)
                        client[str(request.get_json()['employee_name'])].attendence.delete_one({'_id':new_date})
                        client[str(request.get_json()['employee_name'])].attendence.insert_one(att_format)
                if (count == 0 ):        
                   client[str(request.get_json()['employee_name'])].attendence.insert_one(att_format)
                
        if(1==2) :
                status = 'error'
                
    if (len(str(request.get_json()['in_time'])) < 5 or len(str(request.get_json()['out_time']))<5 or len(str(request.get_json()['delay'])) < 1 or len(str(request.get_json()['advance']))< 1 or len(str(request.get_json()['overtime']))<1):
        status = 'error'    


    return status






@app.route('/attendence')
def attendence():
     all_employees=client.list_database_names()
     ab={}
     attendence_list=[]
     total_employee=[]
     present_employee=[]
     present_employee_id=[]
     total_employee_id=[]
     date="1/06/2020"

     for i in all_employees:
         if(i!='admin' and i!='config' and i!='loginuser' and i!='local' and i!='esi_epf_shares'):
             print(i)
             total_employee.append(i)
             for j in client[i].attendence.find({},{"_id":False}):
                 total_employee_id.append(j['employee_id'])
                 if(j['date']==date):
                      print(j)
                      present_employee.append(j['employee_name']+"_"+j['employee_id'])
                      present_employee_id.append(j['employee_id'])
                      print("")
     
     absent_employee_name= [x for x in present_employee + total_employee if x not in total_employee or x not in present_employee]
   
     for aabsentees in absent_employee_name:
         name_id=aabsentees.split("_")
         att_update=client[aabsentees].attendence
         leave={
             "date":date,
             "employee_name":name_id[0],
             "employee_id":name_id[1],
             "in_time":0,
             "out_time":0,
             "delay":0,
             "overtime":0,
             "totalhours":0,
             "status":"absent",             
         }
         att_update.insert_one(leave)


     for i in all_employees:
         if(i!='admin' and i!='config' and i!='loginuser' and i!='local' and i!='esi_epf_shares'):
             print(i)
             for j in client[i].attendence.find({},{"_id":False}):
                 if(j['date']==date):
                      print(j)
                      attendence_list.append(j)
                      ab.update({j['employee_id']:j})
                      print("")

     print("total_employee= ",total_employee)
     print("present employee= ",present_employee)
     print("absent_employee= ",absent_employee_name)

     return jsonify(attendence_list)

@app.route('/salary')
def salary():
	all_employees=client.list_database_names()
	
	month="01/2020"
	salary={}
       
	for i in all_employees:
         worked_hours=0
         over_time=0
         	 
         if(i!='admin' and i!='config' and i!='loginuser' and i!='local' and i!='esi_epf_shares'):
         
             for j in client[i].details.find({},{"_id":False}):
                 print(j['net_salary'])
                 employee_net_salary = int(j['net_salary'])
                 per_min_salary = employee_net_salary/27/8/60
         
             for k in client[i].attendence.find({},{"_id":False}):
         
             	 print(str(k['date'])[3:])
             	 if(str(k['date'])[3:]==month):
         
             	 	print(k['in_time'],k['out_time'])
             	 	worked_hours = worked_hours + (float(k['out_time'])-float(k['in_time']))
             	 	if(float(k['out_time'])-float(k['in_time'])>8):
             	 	    over_time= over_time+(float(k['out_time'])-float(k['in_time'])-8)
             	 	print(worked_hours)
             	 	
             	 salary.update({k['employee_id']:{k['employee_id']:worked_hours*60*per_min_salary,'worked_hours':worked_hours,'overtime':over_time}})
             	 
             print(worked_hours,employee_net_salary/27/8/60)  	 	
             print("employee-salary",worked_hours*60*per_min_salary)
             
	return jsonify(salary)

@app.route('/employee-details')
def  employee_details():
      ab={}
      bc=[]
      all_employees=client.list_database_names()
      
      employee_list=client.employee
       
      for j in all_employees: 
      
         for i in client[j].details.find({},{"_id":False}):
          #print(i)
          ab.update(i)
          bc.append(i)
          
     # print(bc[0])
      #print(bc[1])
      #print(bc)
      return jsonify(bc) 

@app.route('/employee-enroll',methods=['POST'])
def employee_enroll():

     print("email = ",request.get_json()['Email'])
 #   print("rollid = ",request.get_json()['RoleID'])
     print("gender = ",request.get_json()['Gender'])
     print("firstname = ",request.get_json()['FirstName'])
     print("middlename = ",request.get_json()['MiddleName'])
     print("lastname = ",request.get_json()['LastName'])
     print("contact num =",request.get_json()['ContactNo'])
     print("empcode = ",request.get_json()['EmployeeCode'])
     print("department = ",request.get_json()['DepartmentID'])
     print("dof join = ",request.get_json()['DateOfJoining'])
     print("dof terminate = ",request.get_json()['TerminateDate'])
     print("dposition = ",request.get_json()['PositionID'])
     
  
     
     att_update=client[request.get_json()['FirstName']+"_"+request.get_json()['EmployeeCode']].details
     leave={
             "FirstName":request.get_json()['FirstName'].lower(),
             "MiddleName":request.get_json()['MiddleName'].lower(),
             "LastName":request.get_json()['LastName'].lower(),
             "Email":request.get_json()['Email'].lower(),
             "EmployeeCode":request.get_json()['EmployeeCode'],
             "DOB":request.get_json()['DOB'],
             "ContactNo":request.get_json()['ContactNo'],
             "role":request.get_json()['EmployeeType'].lower(),
             "department":request.get_json()['DepartmentID'].lower(),
             "DateOfJoining":request.get_json()['DateOfJoining'],
             "position":request.get_json()['PositionID'].lower(),
             "TerminateDate":request.get_json()['TerminateDate'],
             "Bloodgroup":request.get_json()['BloodGroup'].lower(),
             "EmergencyContact":request.get_json()['EmergencyContact'],
             "ESINumber":request.get_json()['ESINumber'],
             "EPFNumber":request.get_json()['EPFNumber']
                
     }
     att_update.insert_one(leave)
  
     
 
     return "ab"
  
  
@app.route('/employee_details_update',methods=['POST'])
def employee_details_update():

    # print("email = ",request.get_json()['Email'])

     print("rollid = ",request.get_json()['RoleID'])
     print("gender = ",request.get_json()['Gender'])
     print("firstname = ",request.get_json()['FirstName'])
     print("middlename = ",request.get_json()['MiddleName'])
     print("lastname = ",request.get_json()['LastName'])
     print("contact num =",request.get_json()['ContactNo'])
     print("empcode = ",request.get_json()['EmployeeCode'])
     print("department = ",request.get_json()['DepartmentID'])
     print("dof join = ",request.get_json()['DateOfJoining'])
     print("dof terminate = ",request.get_json()['TerminateDate'])
     print("dposition = ",request.get_json()['PositionID'])
     
     
     client[request.get_json()['FirstName']+"_"+request.get_json()['EmployeeCode']].details.drop()
     
     att_update=client[request.get_json()['FirstName']+"_"+request.get_json()['EmployeeCode']].details
     leave={
             "FirstName":request.get_json()['FirstName'],
             "MiddleName":request.get_json()['MiddleName'],
             "LastName":request.get_json()['LastName'],
             "EmployeeCode":request.get_json()['EmployeeCode'],
             "DOB":request.get_json()['DOB'],
             "ContactNo":request.get_json()['ContactNo'],
             "role":request.get_json()['RoleID'],
             "department":request.get_json()['DepartmentID'],
             "DateOfJoining":request.get_json()['DateOfJoining'],
             "position":request.get_json()['PositionID'],
             "Bloodgroup":request.get_json()['BloodGroup'],
             "Email":request.get_json()['Email'],
             "EmergencyContact":request.get_json()['EmergencyContact'],
             "TerminateDate":request.get_json()['TerminateDate'],
             "ESINumber":request.get_json()['ESINumber'],
             "EPFNumber":request.get_json()['EPFNumber']
                
     }

     att_update.insert_one(leave)
  
     
 
     return "ab"
                  
@app.route('/employee_delete' , methods=['POST'])                  
def employee_delete():
    
    print("emp_id",request.get_json()['employee_id'])
    client=mg()
    print(request.get_json())
    client[request.get_json()['employee_id']].details.drop()
    client[request.get_json()['employee_id'].capitalize()].details.drop()
    
    
    return "ab"


@app.route('/employee_list',methods=['GET'])
def employee_list():
	all_employees=client.list_database_names()
	employee_list=[]
	for i in all_employees:
		if(i!='admin' and i!='config' and i!='local' and i!='loginuser' and i!='esi_epf_shares' and i!='contractors'):
		#  print(i)
		  employee_list.append({'employee_name':i})

	return jsonify(employee_list)	


@app.route('/employee_add_salary',methods=['POST'])
def employee_add_salary():

	print("emp_id",request.get_json()['Employee'])

	insert_salary=client[request.get_json()['Employee']].salary_details
	salary_details={

    "employee_name":request.get_json()['Employee'],
    "net_salary":request.get_json()['BasicSalary'],
    "bank_name":request.get_json()['BankName'],
    "account_no":request.get_json()['AccountNo'],
    "account_holder":request.get_json()['AccountHolderName'],
    "ifsc_code":request.get_json()['IFSCcode'],


	}

	insert_salary.insert_one(salary_details)

	return "ab"
    
                   
@app.route('/employee_salary_list')
def employee_salary_list():

      bc=[]
      all_employees=client.list_database_names()
      
      employee_list=client.employee
       
      for j in all_employees: 
      
         for i in client[j].salary_details.find({},{"_id":False}):
          #print(i)
          
          bc.append(i)
          
     # print(bc[0])
      #print(bc[1])
      #print(bc)
      return jsonify(bc) 


@app.route('/employee_salary_edit',methods=['PUT'])
def employee_salary_edit():

	print("employee",request.get_json()['Employee'])
	print("net_salary",request.get_json()['BasicSalary'])

	client[request.get_json()['Employee']].salary_details.drop()

	insert_salary=client[request.get_json()['Employee']].salary_details
	salary_details={

    "employee_name":request.get_json()['Employee'],
    "net_salary":request.get_json()['BasicSalary'],
    "bank_name":request.get_json()['BankName'],
    "account_no":request.get_json()['AccountNo'],
    "account_holder":request.get_json()['AccountHolderName'],
    "ifsc_code":request.get_json()['IFSCcode'],


	}

	insert_salary.insert_one(salary_details)


	return "emp salary edit"



@app.route('/attendence_edit',methods=['PUT'])
def attendence_edit():


	attendnece_edit={

    "in_time":request.get_json()['InTime'],
    "status":request.get_json()['Status'],
    "total_hours":request.get_json()['TotalHours'],
    "employee_id":request.get_json()['Employee_id'],
    "employee_name":request.get_json()['EmployeeName'],
    "date":request.get_json()['date'],
    
    "out_time":request.get_json()['OutTime'],
    "overtime":request.get_json()['OverTime'],
    "advance":request.get_json()['Advance'],
    "delay":request.get_json()['Delay'],
    "edited":"yes",



	}
        
        
	client[request.get_json()['EmployeeName']].attendence.update({"_id":request.get_json()['date']},attendnece_edit)
	print("overtime         ",request.get_json()['OverTime'])


	return "emp salary edit"


@app.route('/employee_salary_delete',methods=['PUT'])
def employee_salary_delete():
     
	print("employee_name",request.get_json()['employee_name']) 

	client[request.get_json()['employee_name']].salary_details.drop()
    
	return "deleted"



@app.route('/employee_monthly_salary_change',methods=['GET'])
def employee_monthly_salary():

	all_employees=client.list_database_names()
	
	employee_monthly_salary=[]
	
	month="01/2020"
	salary={}
	for shares in client.esi_epf_shares.esi_epf.find({},{"_id":False}):
	   db_basic_pay=float(shares['basic_pay'])
	   db_conveyence=float(shares['conveyence'])
	   db_epf_employeer_pension=float(shares['epf_employeer_pension'])
	   db_epf_employee_share=float(shares['epf_employee_share'])
	   db_esi_employeer_share=float(shares['esi_employeer_share'])
	   db_hra=float(shares['hra'])
	   db_esi_employee_share=float(shares['esi_employee_share'])
	   db_epf_employeer_epf=float(shares['epf_employeer_epf'])
	   db_wl_allowence=float(shares['wl_allowence'])
	
	for i in all_employees:
         worked_hours=0
         over_time=0
  
             
         if(i!='admin' and i!='config' and i!='loginuser' and i!='local' and i!='esi_epf_shares'):


         
             for j in client[i].salary_details.find({},{"_id":False}):

                 net_salary=int(j['net_salary'])
                 basic_salary=(db_basic_pay*net_salary)/100
                 wl_allowence=(db_wl_allowence*net_salary)/100
                 hra=(db_hra*net_salary)/100
                 conveyence=(db_conveyence*net_salary)/100
                 esi_employee_share=(db_esi_employee_share*basic_salary)/100
                 esi_employeer_share=(db_esi_employeer_share*basic_salary)/100
                 epf_employee_share=(db_epf_employee_share*basic_salary)/100
                 epf_pension_employeer_share=(db_epf_employeer_pension*basic_salary)/100
                 epf_employeer_epf_share=(db_epf_employeer_epf*basic_salary)/100
                 ot="attendence data error"
                 detection="attendence data error"

                 final_salary = net_salary-esi_employee_share-epf_employee_share
                 
                 print(net_salary,basic_salary,wl_allowence,hra,conveyence,esi_employee_share,epf_employee_share,final_salary)

                 print(j['net_salary'])

                 employee_net_salary = int(j['net_salary'])
                 per_min_salary = employee_net_salary/27/8/60
                 
                 employee_monthly_salary.append({'employee_name':i,'month':'data error','sq.ft':'0','net_salary':net_salary,'basic_salary':basic_salary,'wl_allowence':wl_allowence,'hra':hra,'conveyence':conveyence,'esi_employee_share':esi_employee_share,
                 'esi_employeer_share':esi_employeer_share,'epf_employee_share':epf_employee_share,'epf_pension_employeer_share':epf_pension_employeer_share,
                 'epf_employeer_epf_share':epf_employeer_epf_share,'overtime':ot,
                 'detection':detection,'final_salary':final_salary})
                 	
                 print(per_min_salary)


	return jsonify(employee_monthly_salary)      
	

@app.route('/edit_esi_epf_share')
def edit_esi_epf_share():

    return "esi_epf_share"
	       	

@app.route('/get_esi_epf_share',methods=['GET'])
def get_esi_epf_share():

    esi_epf={}
    for i in client.esi_epf_shares.esi_epf.find({},{"_id":False}):
      esi_epf.update(i)

    return jsonify([esi_epf])


@app.route('/get_contractors',methods=['GET'])
def get_contractoes():

    esi_epf={}
    for i in client.contractors.sqt_cost.find({},{"_id":False}):
      esi_epf.update(i)

    return jsonify([esi_epf])    


@app.route('/get_contractors_edit',methods=['PUT'])
def get_contractors_edit():

   client.contractors.sqt_cost.drop()
   
   esi_edit=client.contractors.sqt_cost
   esi_details={

    "bed_polish":request.get_json()['bedpolish'],
    "hand_polish":request.get_json()['handpolish'],
    "dry_cutting":request.get_json()['drycutting'],



	}

   esi_edit.insert_one(esi_details)

   return "edited"


@app.route('/esi_epf_share_edit',methods=['PUT'])
def esi_epf_share_edit():

   client.esi_epf_shares.esi_epf.drop()
   
   esi_edit=client.esi_epf_shares.esi_epf
   esi_details={

    "basic_pay":request.get_json()['basicpay'],
    "wl_allowence":request.get_json()['wlallowence'],
    "hra":request.get_json()['hra'],
    "conveyence":request.get_json()['conveyence'],
    "esi_employeer_share":request.get_json()['esiemployeershare'],
    "esi_employee_share":request.get_json()['esiemployeeshare'],
    "epf_employee_share":request.get_json()['epfemployeeshare'],
    "epf_employeer_pension":request.get_json()['epfemployeerpension'],
    "epf_employeer_epf":request.get_json()['epfemployeershare'],


	}

   esi_edit.insert_one(esi_details)

   return "edited"

@app.route('/attendence_list',methods=['PUT'])
def at_li():
    
    att_list = []
    
    print(request.get_json()['date'])
    
    all_employees=client.list_database_names()
    try:
       db_date =   request.get_json()['date'][-2:] +"/"+request.get_json()['date'][5:7] +"/" + request.get_json()['date'][:4]  
    except:
       db_date = "ab"

    print(db_date)   
    employee_list=client.employee
       
    for j in all_employees: 
       #if (j=='emp_102'):
         #   att_list = []
            
            k = client[j].attendence.find_one({"_id":db_date})
            if (k!=None):    
                att_list.append(k)
            
    #print(att_list)
    return jsonify(att_list)


@app.route('/salary_month',methods=['GET'])
def salary_month():
        
        
	employee_list = []
	for i in months_list_post:
	
		  employee_list.append({'month':i})

	return jsonify(employee_list)






@app.route('/salary_year',methods=['GET'])
def  salary_year():
        employee_list = []
        salary_year = [2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2037,2038,2039,2040,2041,2042,2043,2044,2045,2045,2046,2047,2048,2049,2050]
        for i in salary_year:
              employee_list.append({'year':i})
        return jsonify(employee_list)

@app.route('/employee_monthly_salary_month_years',methods=['PUT'])
def employee_monthly_salary_month_year():
     print("month   ",request.get_json()['month'])
     print("year   ",request.get_json()['year'])
     
     return "nothing"

def find_sunday (m,y) :
    dc=calendar.SUNDAY
    matrix=calendar.monthcalendar(int(m),int(y))
    final_sunday = []
    present_day = []
    sundays = sum(1 for x in matrix if x[dc]!=0)
    sunday_list = list(x for x in matrix if x[dc]!=0)
    for s in sunday_list:
        for sun in s[-1:]:
            final_sunday.append(sun)

    print(final_sunday)
    return final_sunday






@app.route('/employee_monthly_salary_month_year',methods=['PUT'])   ##original employee_monthly_salary_changed : its debug salary calculation
def salary_calculation_month_year():
    
    print("year    ",request.get_json()['year'])
    print("month    ",request.get_json()['month'])
    #try :
    months_list_post.index(request.get_json()['month'])
    month_date = months_list_post.index(request.get_json()['month']) + 1
       #month_date= month_date.replace("-","/")
       #print(month_date)
       #month = str(month_date[8:10]) + "/" + str(month_date[5:7]) +"/"+ str(month_date[0:4])
       
    #except:
       
       #month_date = 1    
    client.salary_log.monthly.drop()
    equate_db = request.get_json()['month']+"_"+str(request.get_json()['year'])
    cat = "NA"
    esi_st = "NA"
    epf_st = "NA"
    month = request.get_json()['month']
    month_year = request.get_json()['month'] + "_" + request.get_json()['year']
    bed_month = request.get_json()['month']
    all_employees=client.list_database_names()
    delay_minutes=0
    advance_minutes=0
    employee_monthly_salary=[]
    over_time=0
    inc=0
    total_detection=0

    year=datetime.today()
    
    days_in_month=monthrange(int(request.get_json()['year']),int(month_date))
    
    y=int (request.get_json()['year'])
    #y=int(month[6:])
    m=int(month_date) 
    #m=int(month[3:5])
    dc=calendar.SUNDAY
    final_sunday  = []
    matrix=calendar.monthcalendar(y,m)
    sundays = sum(1 for x in matrix if x[dc]!=0)
    sunday_list = list(x for x in matrix if x[dc]!=0)
    for s in sunday_list:
        for sun in s[-1:]:
            final_sunday.append(sun)

    

    days=[weekday(y,m,d+1) for d in range(*monthrange(y,m)) ]
    print(days)
    print("year   :",y,"     month:   ",m)
    #sundays=days.count(SUNDAY)
    
    print("number of sundays   ",sundays)
    print("no_of_days",days_in_month[1])
    num_of_days=days_in_month[1]
    #month="2020-08-01"
 
    admin_present_time="8:30"
    admin_out_time="17:35"
    admin_present_time=datetime.strptime(admin_present_time,"%H:%M").time()
    admin_out_time=datetime.strptime(admin_out_time,"%H:%M").time()
    #month=datetime.strptime(month,"%d/%m/%Y").date()
    employee_monthly_salary=[]
    salary={}
    
    for sqt_cost in client.contractors.sqt_cost.find({},{"_id":False}):
         bed_polish_per_sq_feet  = float(sqt_cost['bed_polish'])
         hand_polish_per_sq_feet = float(sqt_cost['hand_polish'])
         dry_cutting_per_sq_feet =  float (sqt_cost['dry_cutting'])
       
    for shares in client.esi_epf_shares.esi_epf.find({},{"_id":False}):
        
       db_basic_pay=float(shares['basic_pay'])
       db_conveyence=float(shares['conveyence'])
       db_epf_employeer_pension=float(shares['epf_employeer_pension'])
       db_epf_employee_share=float(shares['epf_employee_share'])
       db_esi_employeer_share=float(shares['esi_employeer_share'])
       db_hra=float(shares['hra'])
       db_esi_employee_share=float(shares['esi_employee_share'])
       db_epf_employeer_epf=float(shares['epf_employeer_epf'])
       db_wl_allowence=float(shares['wl_allowence'])
    
    for i in all_employees:
         worked_hours=0
         
  
             
         if(i!='admin' and i!='config' and i!='loginuser' and i!='local' and i!='esi_epf_shares' and i!='contractors' and i!='salary_log' ):
         #if(i=='emp_102' ):


             for department in client[i].details.find({},{"_id":False}):
             
                #if(department['department']=='admin' or department['department']=='edge_cutting' or  department['department']=='driver' or department['department']=='carving' or department['department']=='packing' or department['department']=='cleaning' ):

                    
                if(department['position'] != 'contractor' ): 
                    delay_minutes=0
                    worked_day=0
                    advance_minutes=0
                    inc=0
                    mins_worked = 0
                    over_time =0 


                    if(department['role'] == 'unroll' ):
                        
                           db_basic_pay=0
                           db_conveyence=0
                           db_epf_employeer_pension=0
                           db_epf_employee_share=0
                           db_esi_employeer_share=0
                           db_hra=0
                           db_esi_employee_share=0
                           db_epf_employeer_epf=0
                           db_wl_allowence=0
                           cat = "unroll"
                     

                    if(department['role'] == 'roll' ):
                           for shares in client.esi_epf_shares.esi_epf.find({},{"_id":False}):
                               
                                   db_basic_pay=float(shares['basic_pay'])
                                   db_conveyence=float(shares['conveyence'])
                                   db_epf_employeer_pension=float(shares['epf_employeer_pension'])
                                   db_epf_employee_share=float(shares['epf_employee_share'])
                                   db_esi_employeer_share=float(shares['esi_employeer_share'])
                                   db_hra=float(shares['hra'])
                                   db_esi_employee_share=float(shares['esi_employee_share'])
                                   db_epf_employeer_epf=float(shares['epf_employeer_epf'])
                                   db_wl_allowence=float(shares['wl_allowence'])
                                   cat= "roll"
                               
                    print(department)               
                    if(int(department['EPFNumber']) == 1  ):
    
                           db_epf_employeer_pension=0
                           db_epf_employee_share=0
                           epf_st = "no"   
                           db_epf_employeer_epf=0
                           
                    if(int(department['EPFNumber']) != 1  ):
                           epf_st = "yes"

                    if(int(department['ESINumber']) != 1  ):

                           esi_st = "yes"
                           
                    if(int(department['ESINumber']) == 1 ):
    
                           db_esi_employeer_share=0
                           db_esi_employee_share=0
                           esi_st = "no"
                                                      
                       

                    for date in client[i].attendence.find({},{"_id":False}):

                       # datetime.strptime(string,'%d/%m/%Y') = convert string to date
                        attendence_date=datetime.strptime(date['date'],'%d/%m/%Y').date()
                        total_detection=0
                        print(date)
                        print("compare string         =================",str(attendence_date)[5:7],"      ",m)
                        if(date['month'] == equate_db ):
                        #if(str(attendence_date)[5:7] == "09"):
                          print("inside salary             salary                   ")
                          try:
                             in_time=datetime.strptime(date['in_time'],"%H:%M")
                             out_time=datetime.strptime(date['out_time'],"%H:%M")
                          except:
                              in_time = datetime.strptime("00:00","%H:%M")
                              out_time=datetime.strptime("00:00","%H:%M")

                           
                          if (int(date['date'][:2]) in final_sunday ):
                              print("sunday")
                              print(final_sunday,"            ",date['date'][:2])

                          if (int(date['date'][:2]) not in final_sunday):  
                              worked_day=worked_day+1
                              

                          total_hours_worked = date['total_hours']
                          de = date['delay']
                          
                          print("delay",date['delay'],"advance", date['advance'])
                          print("emp_name","   ",i)
                          try:
                             advance_minutes = float(date['advance']) + advance_minutes
                          except:
                              advance_minutes = 0 + advance_minutes
                          try:
                           delay_minutes = float (de[0:2])*60 + float (de[3:5]) + delay_minutes
                          except:
                            delay_minutes =0
                          try:
                             print(date['overtime'],"    ",type(date['overtime']),"   ",date['date']) 
                             over_time =  float(date['overtime']) + over_time
                          except:
                              over_time = float (date['overtime'].split("-")[0]) + over_time
                    print(advance_minutes , "   ", delay_minutes)        
                    total_detection=int(delay_minutes)+int(advance_minutes)       
                    print("total_detection",total_detection)
                   
                    for j in client[i].salary_details.find({},{"_id":False}):
  #                      print("worked_day",worked_day)
                        
                        net_salary=int(j['net_salary'])
                    
                    print(client[i])

                    if ( i=='Kannan_200' or i=='Rajaram_801' or  department['department'] == 'admin' or  department['department'] =='mechanical_maintanence' or department['department'] == 'purchase_team' or  department['department'] == 'admin_prof'  ):
                        over_time =0 
                    if (department['department'] =='mechanical_maintanence' or i=='Balamurugan_1005' or i=='Ramkumar_1010' or i=='Ramasamy_900' or i=='Gopalakrishhnan_901'):
                        delay_minutes =0
                        advance_minutes=0
                        total_detection=0
                         
                    for k in client[i].details.find({},{"_id":False}):
                        try:
                           doj = k['DateOfJoining']
                           esi = k['ESINumber']
                           epf = k['EPFNumber']
                        except:
                           esi = '00000'
                           epf = '00000'
                           
                         
                    present_day = worked_day 
                        
                    absent_days=(num_of_days-sundays)-present_day
                     
                    per_day_salary = net_salary/(num_of_days)
                    increment=2
                    per_min_salary = net_salary/(num_of_days)/8/60

                    
                    if(absent_days-increment >=2 or absent_days-increment==1):
                             
                             inc =0
                             
                    if(absent_days-increment <=0):
                        
                             inc=2                    
                    

                    #per_day_salary = net_salary/num_of_days


                    if (absent_days <=2):    
                        new_salary_month= int(per_day_salary*(present_day+sundays))
                    if (absent_days >=3): 
                        new_salary_month = int(per_day_salary*(num_of_days)) - (absent_days-1)*per_day_salary
                        
                    new_salary_month = new_salary_month + (inc*per_min_salary*8*60)

                        
                        
                    print("net_salary_month",new_salary_month)
                    print("per_day_salary",per_day_salary) 
                       
                    basic_salary=(db_basic_pay*new_salary_month)/100
                    
                    wl_allowence=(db_wl_allowence*new_salary_month)/100

                    hra=(db_hra*new_salary_month)/100

                    conveyence=(db_conveyence*new_salary_month)/100

                    esi_employee_share=(db_esi_employee_share*new_salary_month)/100

                    esi_employeer_share=(db_esi_employeer_share*new_salary_month)/100

                    epf_employee_share=(db_epf_employee_share*basic_salary)/100

                    epf_pension_employeer_share=(db_epf_employeer_pension*basic_salary)/100

                    epf_employeer_epf_share=(db_epf_employeer_epf*basic_salary)/100
                    
                    print("present_day",present_day)
                    print("absent day ",absent_days)

                        
                    
                        
                    free_permission=120
                        

                                
                    print("net_salary",net_salary) 
                       
                    employee_net_salary = net_salary
                        
                    
                    
                    print(per_min_salary)   
                    
                    
                    delay_advance = total_detection- free_permission
                    
                    if (delay_advance > 0):
                    
                       detection = per_min_salary * (delay_advance)
                    
                    if (delay_advance <= 0):
                       
                       detection =0
                    
                    
                    
                    fin_salary = new_salary_month-esi_employee_share-epf_employee_share
                    
                    fin_salary = fin_salary - (per_min_salary*detection)
                    
                    #fin_salary = fin_salary + (inc*per_min_salary*8*60)
                    
                    fin_salary = fin_salary + (over_time*60*per_min_salary)
                    
                    t_detection = per_min_salary*detection
                        
                    #final_salary = net_salary-esi_employee_share-epf_employee_share-(per_min_salary*delay_minutes) 
                        
                    #detection= int(fin_salary - final_salary) 
                        #final_month_salary=worked_day*per_min_salary*60*8     
                        
                   # advance_detection=advance_minutes*per_min_salary                         
                   # t_detection = (total_detection-free_permission)*per_min_salary
                   
                   # final_month_salary=((present_day+inc)*per_min_salary*8*60)-(t_detection) + (over_time*per_min_salary)
   #                     print("final salary ",worked_day,delay_minutes,advance_minutes,total_detection,i)       
                             
                        #print(net_salary,basic_salary,wl_allowence,hra,conveyence,esi_employee_share,epf_employee_share,final_salary)

                        #print(j['net_salary'])
                        
                   # delay_minutes=int(delay_minutes/10)*60*per_min_salary


                    print("esi_employee ",esi_employee_share)
                    extra_amount = 0 
                    if(request.get_json()['month'] == 'december'):
                        extra_amount = (net_salary/30)*3 
                    if(request.get_json()['month'] != 'december'):
                        extra_amount = 0                        
                    if (new_salary_month > 0 ):
                    
                      salary_log = {'_id':i+"_"+str(month),'employee_name':i.upper(),'month':str(month),'sq_ft':0,'net_salary':round(new_salary_month,2),'basic_salary':round(basic_salary,2),'wl_allowence':wl_allowence,'hra':hra,'conveyence':conveyence,'esi_employee_share':int(esi_employee_share),
                            'esi_employeer_share':int(esi_employeer_share),'absent_days':absent_days,'epf_employee_share':int(epf_employee_share),'epf_pension_employeer_share':int(epf_pension_employeer_share),
                            'epf_employeer_epf_share':epf_employeer_epf_share,'overtime':round(over_time,2),'delay':round(detection/60,2),'worked_days':present_day+sundays,'doj':doj,'ESI-no':esi,'EPF-no':esi,
                            'detection':int(t_detection),'cat':cat,'esi_st':esi_st,'epf_st':epf_st,'final_salary':int(fin_salary)+extra_amount,'department':department['department'],'position':department['position'] }
                      print(salary_log)

                      already_present = client.salary_log.monthly.find({'_id':i+"_"+str(month)}).count()

                      if (already_present ==1 ):
                                  client.salary_log.monthly.delete_one({'_id':i+"_"+str(month)})
                                  client.salary_log.monthly.insert_one(salary_log)
                      if (already_present == 0 ):
                                  print("already_present    ",already_present)
                                  client.salary_log.monthly.insert_one(salary_log)
                    
                    employee_monthly_salary.append({'employee_name':i,'month':m,'sq.ft':'0','net_salary':int(new_salary_month),'basic_salary':int(basic_salary),'wl_allowence':wl_allowence,'hra':hra,'conveyence':conveyence,'esi_employee_share':esi_employee_share,
                        'esi_employeer_share':esi_employeer_share,'epf_employee_share':epf_employee_share,'epf_pension_employeer_share':epf_pension_employeer_share,
                        'epf_employeer_epf_share':epf_employeer_epf_share,'overtime':over_time,
                        'detection':int(t_detection),'final_salary':int(fin_salary)+extra_amount})
                    print("genetrated")
                        
                    print(employee_monthly_salary[0])    
                   #     print("eployee_per ",per_min_salary)
                    #    print("time delayed",delay_minutes)
                     #   print(fin_salary,final_salary)
                    
               #     print(i)
                
                
               # print(department['department'])
                #print(department['position'])   
          #  print('\n')

               
                if(department['position']=='contractor'):
                  
                 
                    
              
                            worked_day=0
                            advance_minutes=0
                            inc=0
                            delay_minutes=0
                            worked_day=0
                            sq_feet =0
                            monthly_sq_salary=0
  
                            new_salary_month=0
                            no_of_sq_feet=0
                            cat = "NA"
                            esi_st = "NA"
                            epf_st = "NA"
                            
                            for do in client[i].details.find({},{"_id":False}):
                                try:
                                  doj = do['DateOfJoining']
                                  esi = do ['ESINumber']
                                  epf = do ['EPFNumber']
                                except:
                                  doj = '00000'
                                  esi = '00000'
                                  epf = '00000'
                                
                            for date in client[i].attendence.find({},{"_id":False}):

                            # datetime.strptime(string,'%d/%m/%Y') = convert string to date
                                attendence_date=datetime.strptime(date['date'],'%d/%m/%Y').date()
                                #attendence_date=datetime.strptime(date['date'],'%d/%m/%Y').date()
                                if(str(attendence_date)[5:7] == str(m) ):
        #                         print(attendence_date)
                                    print("same")
                                    in_time=datetime.strptime(date['in_time'],"%H:%M")
                                    try:
                                      out_time=datetime.strptime(date['out_time'],"%H:%M")
                                    except:
                                        out_time = datetime.strptime("00:00","%H:%M")
                                    worked_day=worked_day+1
                            
                            print(client[i])

                            if(department['role'] == 'roll' ):
                                        for shares in client.esi_epf_shares.esi_epf.find({},{"_id":False}):
                               
                                                   db_basic_pay=float(shares['basic_pay'])
                                                   db_conveyence=float(shares['conveyence'])
                                                   db_epf_employeer_pension=float(shares['epf_employeer_pension'])
                                                   db_epf_employee_share=float(shares['epf_employee_share'])
                                                   db_esi_employeer_share=float(shares['esi_employeer_share'])
                                                   db_hra=float(shares['hra'])
                                                   db_esi_employee_share=float(shares['esi_employee_share'])
                                                   db_epf_employeer_epf=float(shares['epf_employeer_epf'])
                                                   db_wl_allowence=float(shares['wl_allowence'])
                                                   cat = "roll"
                                           


                            if(department['role'] == 'unroll' ):
                        
                                   db_basic_pay=0
                                   db_conveyence=0
                                   db_epf_employeer_pension=0
                                   db_epf_employee_share=0
                                   db_esi_employeer_share=0
                                   db_hra=0
                                   db_esi_employee_share=0
                                   db_epf_employeer_epf=0
                                   db_wl_allowence=0
                                   cat = "unroll"
                           




                            for no_esi_epf in client[i].details.find({},{"_id":False}):
                                if (int(department['EPFNumber']) == 1):
                                    db_epf_employeer_epf=0
                                    db_epf_employee_share=0
                                    epf_st = "no"  
                                    db_epf_employeer_pension=0
                                if(int(department['EPFNumber']) != 1  ):
                                    epf_st = "yes"
                                if(int(department['ESINumber']) != 1  ):
                                    esi_st = "yes"
                                if (int(department['ESINumber']) == 1 ):
                                    db_esi_employeer_share=0
                                    db_esi_employee_share=0
                                    esi_st="no"
                                                 
                            
                            for s_feet in client[i].monthly_sq_feet.find({},{"_id":False}):
                             # sqt_date=datetime.strptime(s_feet['date'],'%d/%m/%Y').date()
                              if(month_year == s_feet['month']):
                                print("sqt",s_feet['total_sq_feet'])
                                no_of_sq_feet = float(s_feet['total_sq_feet'])
                                print("no_of_sq_feet",no_of_sq_feet)
                                if(department['department']=='bed_polish'):
                                    
                                    monthly_sq_salary = no_of_sq_feet * bed_polish_per_sq_feet
                                    print(monthly_sq_salary)
                                if(department['department']=='hand_polish'):
                                    monthly_sq_salary = no_of_sq_feet * hand_polish_per_sq_feet
                                if (department['department']=='dry_cutting'):
                                    monthly_sq_salary = no_of_sq_feet * dry_cutting_per_sq_feet
                            
                            net_salary_month = monthly_sq_salary

                            present_day = worked_day + sundays
                            absent_days=num_of_days-present_day
                            
    #                     print("absent_day",absent_days)
    #                     print("present_day", present_day)                        
                            
                            per_day_salary = net_salary_month/num_of_days
                            
                            
        #                    print("net_salary_month",new_salary_month)
                            basic_salary=(db_basic_pay*net_salary_month)/100
                            wl_allowence=(db_wl_allowence*net_salary_month)/100
                            hra=(db_hra*net_salary_month)/100
                            conveyence=(db_conveyence*net_salary_month)/100
                            
                            esi_employee_share= int( (db_esi_employee_share*net_salary_month)/100)
                            
                            esi_employeer_share= int ((db_esi_employeer_share*net_salary_month)/100)
                            
                            epf_employee_share=int ( (db_epf_employee_share*basic_salary)/100 )
                            
                            epf_pension_employeer_share= int ((db_epf_employeer_pension*basic_salary)/100 )
                            
                            epf_employeer_epf_share= int ( (db_epf_employeer_epf*basic_salary)/100)
                        

                            
                            increment=2
                            
                            free_permission=120
                            
                            if(abs(absent_days-increment) ==2 or abs(absent_days-increment)==1 or absent_days-increment==1):
                            
                                print("no increment")
                                
                            if(absent_days-increment <=0):
                            
                                net_salary_month = net_salary_month + per_day_salary
                                    

                            
                            final_month_salary= net_salary_month-esi_employee_share-epf_employee_share

                 
                    
                                                
                            if (net_salary_month > 0 ):
                              salary_log = {'_id':i+"_"+str(month),'employee_name':i.upper(),'month':str(month),'sq_ft':no_of_sq_feet,'net_salary':round(net_salary_month,3),'basic_salary':round(basic_salary,3),'wl_allowence':wl_allowence,'hra':hra,'conveyence':conveyence,'esi_employee_share':esi_employee_share,
                            'esi_employeer_share':esi_employeer_share,'epf_employee_share':epf_employee_share,'epf_pension_employeer_share':epf_pension_employeer_share,
                            'epf_employeer_epf_share':epf_employeer_epf_share,'overtime':'0','absent_days':absent_days,'worked_days':present_day+sundays,'doj':doj,'ESI-no':epf,'EPF-no':esi,
                            'detection':0,'final_salary':int(final_month_salary),'cat':cat,'esi_st':esi_st,'epf_st':epf_st,'delay':0,'department':department['department'],'position':department['position'] }
                              print(salary_log)
                            


                              already_present = client.salary_log.monthly.find({'_id':i+"_"+str(month)}).count()

                              if (already_present ==1 ):
                                  client.salary_log.monthly.delete_one({'_id':i+"_"+str(month)})
                                  client.salary_log.monthly.insert_one(salary_log)
                              if (already_present == 0 ):
                                  client.salary_log.monthly.insert_one(salary_log)
                                                       
                            employee_monthly_salary.append({'employee_name':i,'month':m,'sq.ft':no_of_sq_feet,'net_salary':net_salary_month,'basic_salary':basic_salary,'wl_allowence':wl_allowence,'hra':hra,'conveyence':conveyence,'esi_employee_share':esi_employee_share,
                            'esi_employeer_share':esi_employeer_share,'epf_employee_share':epf_employee_share,'epf_pension_employeer_share':epf_pension_employeer_share,
                            'epf_employeer_epf_share':epf_employeer_epf_share,'overtime':'0',
                            'detection':0,'final_salary':int(final_month_salary)})
                            print("genetrated")
                                    
                    
             
    
    
    return jsonify(employee_monthly_salary) 








@app.route('/attendence_lists')
def attendence_list():
      
      # 8.30 to 5.30 =  > ec, dc, hp, carving, driver, packing, admin, maintanence[ele & mech]
           
      print("att list")
      
      admin_present_time="8:30"
      admin_out_time = "17:30"

      admin_shut_in = "6:00"
      admin_shut_out= "14:00"
      admin_shut_thres = "7:00"
      
      main_cuting_present= "8:30"
      main_cuting_out= "17:30"
      
      bed_polish_present = "8:30"
      bed_polish_out = "17:30"
      
      
      cleaning_present_time = "7:00"
      cleaning_out_time = "16:00"
      
      admin_prof_present_time = "9:00"
      admin_prof_out_time = "18:00"
      
      purchase_team_present_time = "10:30"
      purchase_team_out_time = "18:00"
      
      
      admin_present_time=datetime.strptime(admin_present_time,"%H:%M").time()
      admin_out_time_diff =  datetime.strptime(admin_out_time,"%H:%M")
      admin_out_time=datetime.strptime(admin_out_time,"%H:%M").time()

      admin_shut_in=datetime.strptime(admin_shut_in,"%H:%M").time()
      admin_shut_out=datetime.strptime(admin_shut_out,"%H:%M").time()
      admin_shut_thres=datetime.strptime(admin_shut_thres,"%H:%M").time()
      
      
      
      main_cuting_present=datetime.strptime(main_cuting_present,"%H:%M").time()
      main_cuting_out=datetime.strptime(main_cuting_out,"%H:%M").time()
      
      bed_polish_present=datetime.strptime(bed_polish_present,"%H:%M").time()
      bed_polish_out=datetime.strptime(bed_polish_out,"%H:%M").time()
      
      cleaning_present_time=datetime.strptime(cleaning_present_time,"%H:%M").time()
      cleaning_out_time_diff = datetime.strptime(cleaning_out_time,"%H:%M") 
      cleaning_out_time=datetime.strptime(cleaning_out_time,"%H:%M").time()
      
      admin_prof_present_time=datetime.strptime(admin_prof_present_time,"%H:%M").time()
      admin_prof_out_time_diff = datetime.strptime(admin_prof_out_time,"%H:%M") 
      admin_prof_out_time=datetime.strptime(admin_prof_out_time,"%H:%M").time()
      
      purchase_team_present_time=datetime.strptime(purchase_team_present_time,"%H:%M").time()
      purchase_team_out_time_diff = datetime.strptime(purchase_team_out_time,"%H:%M")
      purchase_team_out_time=datetime.strptime(purchase_team_out_time,"%H:%M").time()
      bc=[]
      all_employees=client.list_database_names()
      
      employee_list=client.employee
       
      for j in all_employees: 
       print(j)
       for department in client[j].details.find({},{"_id":False}):
       
          if(department['department']=='admin'  or  department['department']=='driver' or department['department']=='carving'  or department['department']=='electrical_maintanence' or department['department']=='mechanical_maintanence'  and department['position'] != 'contractor' ):   
      
             for i in client[j].attendence.find({},{"_id":False}):

                        
                       # attendence_date=datetime.strptime(i['date'],'%d/%m/%Y').date()
                        advance_minutes=0
                        attendence_date=datetime.strptime(i['date'],'%d/%m/%Y').date()
                        in_time=datetime.strptime(i['in_time'],"%H:%M")
                        try:
                           
                           out_time=datetime.strptime(i['out_time'],"%H:%M")
                           print(type(out_time))
                           
                           
                        except:
                           dem_time="0:00"
                           out_time=datetime.strptime(dem_time,"%H:%M")
                           print(out_time)

                        print(in_time.time())
                        
                        if(in_time.time() >= admin_shut_in  and in_time.time() < admin_shut_thres ):
                            
                        #if( 1==1 ):
                              print(j)
                              #print("late")
                             # print(str(admin_present_time)[0:2])
                              #print(str(admin_present_time)[3:5])
                              #print(str(in_time.time())[0:2])
                              #print(str(in_time.time())[3:5])    

                              delayed_hr=abs(int(str(in_time.time())[0:2]) - int(str(admin_shut_in)[0:2]))
                              delayed_min=abs(int(str(in_time.time())[3:5]) - int(str(admin_shut_in)[3:5]))
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                            
                              total_hours=abs(int(str(out_time.time())[0:2])-int(str(in_time.time())[0:2]))
                              total_min=abs(int(str(out_time.time())[3:5])-int(str(in_time.time())[3:5]))
                              print(total_hours,total_min)
                              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
                              
                              print("total Delay",total_delay)
                              print("hours worked",total_hours_worked)
                             #
                              print(type(i))
                              client[j].attendence.update({"_id":i['date']},{"$set":{'total_hours':str(total_hours_worked)}})
                              i.update({'totalhours':str(total_hours_worked)})
                              
                         
#####################################################################################################################################################                              
                              tw = out_time - in_time
                              
                              print("woooooo", tw.total_seconds()/60/60)
                              
                              total_hours_worked = str(total_hours_worked)
                              overtime = (tw.total_seconds()/60) - 480 
                              print("ot_min",overtime)
                              if(overtime >= 60):
                                 ot = overtime/60
                                 #ot = 0 
                              else:
                                ot=0   
                              print(type(i))
                              
                             
                              i.update({'overtime':str(str(ot)+"-"+"hrs")})                              
##########################################################################################################################################################

                              
                              temp = admin_out_time_diff - out_time
                              
                              print("difference ", temp.total_seconds()/60)
                              
                              try :
                                 print("yes")
                                 a=client[j].attendence.find_one({"_id":attendence['_id']})
                                 print(a)
                              except:
                                 print("no")
                              client[j].attendence.update({"_id":i['date']},{"$set":{'overtime':str(ot)}}) 
                              if(out_time.time() < admin_shut_out ):
                                           print("advance minutes shift one  if ",temp)
                                           client[j].attendence.update({"_id":i['date']},{"$set":{'advance':int(temp.total_seconds()/60)}})                            
                              
                              if(out_time.time() >= admin_shut_out ):
                                 print("advance minutes shift one else",advance_minutes)
                                 client[j].attendence.update({"_id":i['date']},{"$set":{'advance':0}})
                                  
                                                         
                              
                              if (in_time.time() > admin_shut_in ):
                                  i.update({'delay':str(total_delay)})
                                  client[j].attendence.update({"_id":i['date']},{"$set":{'delay':str(total_delay)}})
                              
                              if (in_time.time() <= admin_shut_in):
                                  i.update({'delay':"00:00:00"})
                                  client[j].attendence.update({"_id":i['date']},{"$set":{'delay':"00:00:00"}})

                              bc.append(i)
                                          
                        else :

                              print(j)
                              #print("late")
                             # print(str(admin_present_time)[0:2])
                              #print(str(admin_present_time)[3:5])
                              #print(str(in_time.time())[0:2])
                              #print(str(in_time.time())[3:5])    

                              delayed_hr=abs(int(str(in_time.time())[0:2]) - int(str(admin_present_time)[0:2]))
                              delayed_min=abs(int(str(in_time.time())[3:5]) - int(str(admin_present_time)[3:5]))
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                            
                              total_hours=abs(int(str(out_time.time())[0:2])-int(str(in_time.time())[0:2]))
                              total_min=abs(int(str(out_time.time())[3:5])-int(str(in_time.time())[3:5]))
                              print(total_hours,total_min)
                              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
                              
                              print("total Delay",total_delay)
                              print("hours worked",total_hours_worked)
                             #
                              print(type(i))
                              client[j].attendence.update({"_id":i['date']},{"$set":{'total_hours':str(total_hours_worked)}})
                              i.update({'totalhours':str(total_hours_worked)})
                              
                                                          
                            #  print(i)
                              
                              
                        
                              temp = admin_out_time_diff - out_time
                              
                              print("difference ", temp.total_seconds()/60)
                              
                              try :
                                 print("yes")
                                 a=client[j].attendence.find_one({"_id":attendence['_id']})
                                 print(a)
                              except:
                                 print("no")
                              
                              if(out_time.time() < admin_out_time ):
                                           print("advance minutes shift one  if ",temp)
                                           client[j].attendence.update({"_id":i['date']},{"$set":{'advance':int(temp.total_seconds()/60)}})                            
                              
                              if(out_time.time() >= admin_out_time ):
                                 print("advance minutes shift one else",advance_minutes)
                                 client[j].attendence.update({"_id":i['date']},{"$set":{'advance':0}})

#####################################################################################################################################################                              
                              tw = out_time - in_time
                              
                              print("woooooo", tw.total_seconds()/60/60)
                              
                              total_hours_worked = str(total_hours_worked)
                              overtime = (tw.total_seconds()/60) - 480 
                              print("ot_min",overtime)
                              if(overtime >= 60):
                                 ot = overtime/60
                                 #ot = 0 
                              else:
                                ot=0   
                              print(type(i))
                              
                             
                              i.update({'overtime':str(str(ot)+"-"+"hrs")})
                              client[j].attendence.update({"_id":i['date']},{"$set":{'overtime':str(ot)}}) 
##########################################################################################################################################################                                  
                                                         
                              
                              if (in_time.time() > admin_present_time ):
                                  i.update({'delay':str(total_delay)})
                                  client[j].attendence.update({"_id":i['date']},{"$set":{'delay':str(total_delay)}})
                              
                              if (in_time.time() <= admin_present_time):
                                  i.update({'delay':"00:00:00"})
                                  client[j].attendence.update({"_id":i['date']},{"$set":{'delay':"00:00:00"}})

                              bc.append(i)
                                          
                                                    
    
                          #######################################################################################################
                          # to be continue

          
          if(department['department']=='main_cutting'):   
             print("main_cutting")
             mc_shift_one = "7:00"
            
             mc_shift_one=datetime.strptime(mc_shift_one,"%H:%M").time()
             
             
             mc_shift_one_out = "15:00"
             mc_shift_one_out_diff = datetime.strptime(mc_shift_one_out,"%H:%M")
             mc_shift_one_out=datetime.strptime(mc_shift_one_out,"%H:%M").time()
             
             mc_shift_one_thres = "7:45"
             mc_shift_one_thres=datetime.strptime(mc_shift_one_thres,"%H:%M").time()
              
             mc_shift_two_in_thres = "14:15"
             mc_shift_two_in_thres=datetime.strptime(mc_shift_two_in_thres,"%H:%M").time()
              
              
             mc_shift_two = "15:00"
             mc_shift_two=datetime.strptime(mc_shift_two,"%H:%M").time()
             
             mc_shift_two_out = "22:00"
             mc_shift_two_out_diff = datetime.strptime(mc_shift_two_out,"%H:%M")
             mc_shift_two_out=datetime.strptime(mc_shift_two_out,"%H:%M").time()
                          
             
             mc_shift_two_thres = "15:45"
             
             mc_shift_two_thres=datetime.strptime(mc_shift_two_thres,"%H:%M").time()
             
             mc_shift_three = "22:00"
             mc_shift_three=datetime.strptime(mc_shift_three,"%H:%M").time()
             
             mc_shift_three_out = "7:00"
             mc_shift_three_out_diff = datetime.strptime(mc_shift_three_out,"%H:%M")
             mc_shift_three_out=datetime.strptime(mc_shift_three_out,"%H:%M").time()
             
             
             mc_shift_three_thres = "22:30"
             mc_shift_three_thres=datetime.strptime(mc_shift_three_thres,"%H:%M").time()
             
             
             for i in client[j].attendence.find({},{"_id":False}):

                        
                       # attendence_date=datetime.strptime(i['date'],'%d/%m/%Y').date()
                        advance_minutes = 0 
                        attendence_date=datetime.strptime(i['date'],'%d/%m/%Y').date()
                        
                        in_time=datetime.strptime(i['in_time'],"%H:%M")
                        print("inside main cutting")
                        try:
                           
                           out_time=datetime.strptime(i['out_time'],"%H:%M")
                           print(type(out_time))
                           
                           
                        except:
                        
                           dem_time="0:00"
                           out_time=datetime.strptime(dem_time,"%H:%M")
                           print(out_time)

                        print(in_time.time())  

                        if(in_time.time() >= mc_shift_one  or in_time.time() < mc_shift_one_thres ):
                              print(j)
        

                              delayed_hr=abs(int(str(in_time.time())[0:2]) - int(str(mc_shift_one)[0:2]))
                              delayed_min=abs(int(str(in_time.time())[3:5]) - int(str(mc_shift_one)[3:5]))
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                            
                              total_hours=abs(int(str(out_time.time())[0:2])-int(str(in_time.time())[0:2]))
                              total_min=abs(int(str(out_time.time())[3:5])-int(str(in_time.time())[3:5]))
                              
                              print(total_hours,total_min)
                              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
                             
                              tw = out_time - in_time
                              
                              print("woooooo", tw.total_seconds()/60/60)
                              
                              total_hours_worked = str(total_hours_worked)
                              overtime = (tw.total_seconds()/60) - 480 
                              print("ot_min",overtime)
                              if(overtime >= 60):
                                 ot=overtime/60
                              else:
                                ot=0   
                              print(type(i))
                             
                              try :
                                 print("yes")
                                 a=client[j].attendence.find_one({"_id":attendence['_id']})
                                 print(a)
                              except:
                                 print("no")
                                                            
                              
                              i.update({'totalhours':str(total_hours_worked)})
                              i.update({'overtime':str(str(ot)+"-"+"hrs")})
                              client[j].attendence.update({"_id":i['date']},{"$set":{'delay':str(total_delay)}})
                              client[j].attendence.update({"_id":i['date']},{"$set":{'overtime':str(ot)}})
                              client[j].attendence.update({"_id":i['date']},{"$set":{'total_hours':str(total_hours_worked)}})                               
                            #  print(i)
                              
                              #data_store[j].attendence.update({"_id":attendence_date},{"$set":{'out_time':total_delay}})  
                          #######################################################################################################
                          # to be continue
                              
                              temp = mc_shift_one_out_diff - out_time
                              
                              print("difference ", temp.total_seconds()/60)

                              if(in_time.time() > mc_shift_one ):
                                  
                                  i.update({'delay':str(total_delay)})
                                  
                              if(in_time.time() <= mc_shift_one ):
                                  i.update({'delay':"00:00:00"})
                                  
                              if(out_time.time() < mc_shift_one_out ):
                                           print("advance minutes shift one  if ",temp)
                                           client[j].attendence.update({"_id":i['date']},{"$set":{'advance':int(temp.total_seconds()/60)}})                            
                              if(out_time.time() >= mc_shift_one_out ):
                                 print("advance minutes shift one else",advance_minutes)
                                 client[j].attendence.update({"_id":i['date']},{"$set":{'advance':0}})
                              bc.append(i)   
                                                         

                              
                        if(in_time.time() >= mc_shift_two_in_thres  and in_time.time() <= mc_shift_two_thres ):
                              print(j)
        
                              total_delay = " "  
                              delayed_hr=abs(int(str(in_time.time())[0:2]) - int(str(mc_shift_two)[0:2]))
                              delayed_min=abs(int(str(in_time.time())[3:5]) - int(str(mc_shift_two)[3:5]))
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                            
                              total_hours=abs(int(str(out_time.time())[0:2])-int(str(in_time.time())[0:2]))
                              total_min=abs(int(str(out_time.time())[3:5])-int(str(in_time.time())[3:5]))
                            
                              print(total_hours,total_min)
                              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
          
                              tw = out_time - in_time
                              
                              print("woooooo", tw.total_seconds()/60/60)
 
                              total_hours_worked = str(total_hours_worked)
                              overtime = (tw.total_seconds()/60) - 480
                              print("ot_min",overtime)
                              if(overtime >= 60):
                                 ot=overtime/60
                              else:
                                ot=0   
                              print(type(i))

                              try :
                                 print("yes")
                                 a=client[j].attendence.find_one({"_id":attendence['_id']})
                                 print(a)
                              except:
                                 print("no")
                                                            
                             
                              i.update({'totalhours':str(total_hours_worked)})
                              i.update({'overtime':str(str(ot)+"-"+"hrs")})
                              client[j].attendence.update({"_id":i['date']},{"$set":{'delay':str(total_delay)}})
                              client[j].attendence.update({"_id":i['date']},{"$set":{'overtime':str(ot)}})
                              client[j].attendence.update({"_id":i['date']},{"$set":{'total_hours':str(total_hours_worked)}})                               
                            #  print(i)
                              
                          #######################################################################################################
                          # to be continue
                         
                              
                              temp = mc_shift_two_out_diff - out_time
                              print(out_time)
                              print("difference ", temp.total_seconds()/60)


                              if(in_time.time() > mc_shift_two ):
                                  
                                  i.update({'delay':str(total_delay)})
                                  
                              if(in_time.time() <= mc_shift_two ):
                                  i.update({'delay':"00:00:00"})
                                 
                              if(out_time.time() < mc_shift_two_out ):
                                           print("advance minutes shift one  if ",temp)
                                           client[j].attendence.update({"_id":i['date']},{"$set":{'advance':int(temp.total_seconds()/60)}})                            
                              if(out_time.time() >= mc_shift_two_out ):
                                 print("advance minutes shift one else",advance_minutes)
                                 client[j].attendence.update({"_id":i['date']},{"$set":{'advance':0}})
                                  
                              bc.append(i)                           

                                                                                     
                        if(in_time.time() >= mc_shift_three  and in_time.time() < mc_shift_three_thres ):
                              print(j)
             		      
             		      #const=datetime.strptime(const,"%H:%M").time()
                              total_delay = " "
                              const = "23:59"
                              const=datetime.strptime(const,"%H:%M")
                              day_start = "23:59"
                              day_start=datetime.strptime(day_start,"%H:%M")
                                                            
                              delayed_hr=abs(int(str(in_time.time())[0:2]) - int(str(mc_shift_three)[0:2]))
                              delayed_min=abs(int(str(in_time.time())[3:5]) - int(str(mc_shift_three)[3:5]))
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                            
                              total_hours=abs(int(str(out_time.time())[0:2])-int(str(in_time.time())[0:2]))
                              total_min=abs(int(str(out_time.time())[3:5])-int(str(in_time.time())[3:5]))
                            
                              print(total_hours,total_min)
                              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
                              client[j].attendence.update({"_id":i['date']},{"$set":{'total_hours':str(total_hours_worked)}})
                              print("total Delay",total_delay)
                              print("hours worked",total_hours_worked)
                             #
                              #total_hours_worked = str(total_hours_worked)
                              
                              tw = const - in_time
                              
                              print("night ",tw.total_seconds()/60/60)
                              
                             # total_hours_worked = (tw.total_seconds()/60) - 360
                              
                              total_hours_worked = int( int(str(out_time.time())[0:2])*60 + int(str(out_time.time())[3:5])  + int(tw.total_seconds()/60) ) 
                              
                              overtime = total_hours_worked - 480
                              
                          
                              
                              print("woooooo", tw.total_seconds()/60/60)
                              print("ot_min",overtime)
                              
                              if(overtime >= 60):
                                 ot=overtime/60
                                 
                              else:
                                ot=0   
                              print(type(i))


                              a=client[j].attendence.find({"_id":i['date']},"edited")
                              
                              for bv in a:
                                    print(bv)
                                    
                              print("db value ",a) 
                                                            
                              i.update({'delay':str(total_delay)})
                              
                              i.update({'totalhours':str(int(total_hours_worked/58))+"-"+"hrs"})
                              
                              i.update({'overtime':str(str(ot)+"-"+"hrs")})
                              
                              client[j].attendence.update({"_id":i['date']},{"$set":{'delay':str(total_delay)}})
                              client[j].attendence.update({"_id":i['date']},{"$set":{'overtime':str(ot)}})
                                                             
                            #  print(i)
                              bc.append(i)
                              
                        
                              
                              temp = mc_shift_three_out_diff - out_time
                              
                              print("difference ", temp.total_seconds()/60)

                              if(out_time.time() < mc_shift_three_out ):
                                           print("advance minutes shift one  if ",temp)
                                           client[j].attendence.update({"_id":i['date']},{"$set":{'advance':int(temp.total_seconds()/60)}})                            
                              if(out_time.time() >= mc_shift_three_out ):
                                 print("advance minutes shift one else",advance_minutes)
                                 client[j].attendence.update({"_id":i['date']},{"$set":{'advance':0}})
                                  
                                                         

                                                                                          
                              
                        if(in_time.time() >= mc_shift_one_thres  and in_time.time() < mc_shift_two ):
                              print(j)
        

                              delayed_hr=abs(int(str(in_time.time())[0:2]) - int(str(main_cuting_present)[0:2]))
                              delayed_min=abs(int(str(in_time.time())[3:5]) - int(str(main_cuting_present)[3:5]))
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                            
                              total_hours=abs(int(str(out_time.time())[0:2])-int(str(in_time.time())[0:2]))
                              total_min=abs(int(str(out_time.time())[3:5])-int(str(in_time.time())[3:5]))
                            
                              print(total_hours,total_min)
                              
                              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
                              
                              total_hours_worked = str(total_hours_worked)
                              
                              if(out_time < in_time):
                                 print("night")
                              
                              tw = out_time - in_time
                              
                              overtime = (tw.total_seconds()/60) - 480
                              
                              print("ot_min",overtime)
                              print("woooooo", tw.total_seconds()/60/60)                              
                              if(overtime > 60):
                                 ot=overtime/60
                              else:
                                ot=0   
                              print(type(i))
                              try :
                                 print("yes")
                                 a=client[j].attendence.find_one({"_id":attendence['_id']})
                                 print(a)
                              except:
                                 print("no")
                                                            
                              i.update({'delay':str(total_delay)})
                              i.update({'totalhours':str(total_hours_worked)})
                              i.update({'overtime':str(str(ot)+"-"+"hrs")})
                              client[j].attendence.update({"_id":i['date']},{"$set":{'delay':str(total_delay)}})
                              client[j].attendence.update({"_id":i['date']},{"$set":{'overtime':str(ot)}})
                              client[j].attendence.update({"_id":i['date']},{"$set":{'total_hours':str(total_hours_worked)}})                               
                            #  print(i)
                              bc.append(i) 

                              temp = admin_out_time_diff - out_time
                              
                              print("difference ", temp.total_seconds()/60)

                              if(out_time.time() < admin_out_time ):
                                           print("advance minutes shift one  if ",temp)
                                           client[j].attendence.update({"_id":i['date']},{"$set":{'advance':int(temp.total_seconds()/60)}})                            
                              if(out_time.time() >= admin_out_time ):
                                 print("advance minutes shift one else",advance_minutes)
                                 client[j].attendence.update({"_id":i['date']},{"$set":{'advance':0}})
                                  
                                                                                        
              

          if(department['department']=='bed_polish' or  department['department']=='edge_cutting' or department['department']=='drilling' or department['department']=='hand_polish' or department['department']=='dry_cutting' or department['department']=='packing'):   
            
             print("bed_polish")
             bp_shift_one = "6:00"
             bp_shift_one=datetime.strptime(bp_shift_one,"%H:%M").time()
             
             bp_shift_one_out = "14:00"
             bp_shift_one_out_diff = datetime.strptime(bp_shift_one_out,"%H:%M") 
             bp_shift_one_out=datetime.strptime(bp_shift_one_out,"%H:%M").time()
             
             bp_shift_one_thres = "7:15"
             bp_shift_one_thres=datetime.strptime(bp_shift_one_thres,"%H:%M").time()
             bp_shift_two = "14:00"
             bp_shift_two=datetime.strptime(bp_shift_two,"%H:%M").time()
             
             bp_shift_two_out = "22:00"
             bp_shift_two_out_diff = datetime.strptime(bp_shift_two_out,"%H:%M")
             bp_shift_two_out=datetime.strptime(bp_shift_two_out,"%H:%M").time()
             
             bp_shift_two_thres = "14:45"
             bp_shift_two_thres=datetime.strptime(bp_shift_two_thres,"%H:%M").time()
        
             
             
             for i in client[j].attendence.find({},{"_id":False}):

                        
                       # attendence_date=datetime.strptime(i['date'],'%d/%m/%Y').date()
                        advance_minutes=0
                        
                        attendence_date=datetime.strptime(i['date'],'%d/%m/%Y').date()
                        print("employee","   ",j)
                        in_time=datetime.strptime(i['in_time'],"%H:%M")
                        
                        try:
                           
                           out_time=datetime.strptime(i['out_time'],"%H:%M")
                           print(type(out_time))
                           print("out time",i['out_time'])
                           print("ad time",admin_out_time)
                           
                           
                        except:
                        
                           dem_time="0:00"
                           out_time=datetime.strptime(dem_time,"%H:%M")
                           print(out_time)

                        print(in_time.time())  

                        if(in_time.time() >= bp_shift_one  and in_time.time() < bp_shift_one_thres or in_time.time() <= bp_shift_one  ):
                              print(j)
                              
                              print("shift_one")
                              delayed_hr=abs(int(str(in_time.time())[0:2]) - int(str(bp_shift_one)[0:2]))
                              delayed_min=abs(int(str(in_time.time())[3:5]) - int(str(bp_shift_one)[3:5]))
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                            
                              total_hours=abs(int(str(out_time.time())[0:2])-int(str(in_time.time())[0:2]))
                              total_min=abs(int(str(out_time.time())[3:5])-int(str(in_time.time())[3:5]))
                            
                              print(total_hours,total_min)
                              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
                             
                              tw = out_time - in_time
                              
                              print("woooooo", tw.total_seconds()/60/60)
                              
                              total_hours_worked = str(total_hours_worked)
                              overtime = (tw.total_seconds()/60) - 480 
                              
                              print("ot_min",overtime)
                              
                              if(overtime >= 60):
                                 ot=overtime/60
                              else:
                                ot=0   
                              print(type(i))
                              try :
                                 print("yes")
                                 a=client[j].attendence.find_one({"_id":attendence['_id']})
                                 print(a)
                              except:
                                 print("no")
                                                            
                              
                              i.update({'totalhours':str(total_hours_worked)})
                              i.update({'overtime':str(str(ot)+"-"+"hrs")})
                              client[j].attendence.update({"_id":i['date']},{"$set":{'overtime':str(ot)}}) 
                              client[j].attendence.update({"_id":i['date']},{"$set":{'total_hours':str(total_hours_worked)}})                               
                            #  print(i)
                              

                               
                              temp = bp_shift_one_out_diff - out_time
                              
                              print("difference ", temp.total_seconds()/60)

                              if (in_time.time() > bp_shift_one  ) :
                                  i.update({'delay':str(total_delay)})
                                  client[j].attendence.update({"_id":i['date']},{"$set":{'delay':str(total_delay)}})
                              if (in_time.time() <= bp_shift_one ):
                                  i.update({'delay':"00:00:00"})
                                  client[j].attendence.update({"_id":i['date']},{"$set":{'delay':"00:00:00"}})
                                  
                              if(out_time.time() < bp_shift_one_out ):
                                           print("advance minutes shift one  if ",temp)
                                           client[j].attendence.update({"_id":i['date']},{"$set":{'advance':str(temp.total_seconds()/60)}})                            
                              if(out_time.time() >= bp_shift_one_out ):
                                 
                                 client[j].attendence.update({"_id":i['date']},{"$set":{'advance':0}})
                              bc.append(i)                                                                                                                        

                        if(in_time.time() >= bp_shift_two  and in_time.time() < bp_shift_two_thres ):
                              print(j)
                           
                              print("shift_two")
                              delayed_hr=abs(int(str(in_time.time())[0:2]) - int(str(bp_shift_one)[0:2]))
                              delayed_min=abs(int(str(in_time.time())[3:5]) - int(str(bp_shift_one)[3:5]))
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                            
                              total_hours=abs(int(str(out_time.time())[0:2])-int(str(in_time.time())[0:2]))
                              total_min=abs(int(str(out_time.time())[3:5])-int(str(in_time.time())[3:5]))
                            
                              print(total_hours,total_min)
                              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
                             
                              tw = out_time - in_time
                              
                              print("woooooo", tw.total_seconds()/60/60)
                              
                              total_hours_worked = str(total_hours_worked)
                              overtime = (tw.total_seconds()/60) - 480 
                              print("ot_min",overtime)
                              if(overtime >= 60):
                                 ot=overtime/60
                              else:
                                ot=0   
                              print(type(i))
                              try :
                                 print("yes")
                                 a=client[j].attendence.find_one({"_id":attendence['_id']})
                                 print(a)
                              except:
                                 print("no")
                                                            
                              
                              i.update({'totalhours':str(total_hours_worked)})
                              i.update({'overtime':str(str(ot)+"-"+"hrs")})
                              client[j].attendence.update({"_id":i['date']},{"$set":{'overtime':str(ot)}})
                              client[j].attendence.update({"_id":i['date']},{"$set":{'total_hours':str(total_hours_worked)}})                               
                            #  print(i)
                             
                              
                              
                                      
                              temp = bp_shift_two_out_diff - out_time
                              
                              print("difference ", temp.total_seconds()/60)

                              if(in_time.time() > bp_shift_two ):
                                        client[j].attendence.update({"_id":i['date']},{"$set":{'delay':str(total_delay)}})
                                        i.update({'delay':str(total_delay)})

                              if(in_time.time() <= bp_shift_two ):
                                         client[j].attendence.update({"_id":i['date']},{"$set":{'delay':"00:00:00"}})
                                         i.update({'delay':"00:00:00"})
                                  
                              if(out_time.time() < bp_shift_two_out ):
                                           print("advance minutes shift one  if ",temp)
                                           client[j].attendence.update({"_id":i['date']},{"$set":{'advance':str(temp.total_seconds()/60)}})                            
                              if(out_time.time() >= bp_shift_two_out ):
                                 
                                 client[j].attendence.update({"_id":i['date']},{"$set":{'advance':0}})                                
                              bc.append(i)

                        if(in_time.time() >= bp_shift_one_thres  and in_time.time() < bp_shift_two ):
                              print(j)
        
                              print("day_shift")
                              delayed_hr=abs(int(str(in_time.time())[0:2]) - int(str(bed_polish_present)[0:2]))
                              delayed_min=abs(int(str(in_time.time())[3:5]) - int(str(bed_polish_present)[3:5]))
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                            
                              total_hours=abs(int(str(out_time.time())[0:2])-int(str(in_time.time())[0:2]))
                              total_min=abs(int(str(out_time.time())[3:5])-int(str(in_time.time())[3:5]))
                            
                              print(total_hours,total_min)
                              
                              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
                              
                              total_hours_worked = str(total_hours_worked)
                              
                              if(out_time < in_time):
                                 print("night")
                              
                              tw = out_time - in_time
                              
                              overtime = (tw.total_seconds()/60) - 480
                              
                              print("ot_min",overtime)
                              print("woooooo", tw.total_seconds()/60/60)                              
                              if(overtime >= 60):
                                 ot=overtime/60
                              else:
                                ot=0   
                              print(type(i))
                              try :
                                 print("yes")
                                 a=client[j].attendence.find_one({"_id":attendence['_id']})
                                 print(a)
                              except:
                                 print("no")
                                                            
                              client[j].attendence.update({"_id":i['date']},{"$set":{'overtime':str(ot)}})
                              i.update({'totalhours':str(total_hours_worked)})
                              i.update({'overtime':str(str(ot)+"-"+"hrs")})
                              
                              client[j].attendence.update({"_id":i['date']},{"$set":{'total_hours':str(total_hours_worked)}})                               
                            #  print(i)
                              bc.append(i)
                              
                              
                              temp = admin_out_time_diff - out_time
                              
                              print("difference ", temp.total_seconds()/60)

                              if(in_time.time() > admin_present_time ):
                                  i.update({'delay':str(total_delay)})
                                  client[j].attendence.update({"_id":i['date']},{"$set":{'delay':str(total_delay)}})

                              if(in_time.time() <= admin_present_time ):
                                   i.update({'delay':"00:00:00"})
                                   client[j].attendence.update({"_id":i['date']},{"$set":{'delay':"00:00:00"}})
                                  
                              if(out_time.time() < admin_out_time ):
                                           print("advance minutes shift one  if ",temp)
                                           client[j].attendence.update({"_id":i['date']},{"$set":{'advance':str(temp.total_seconds()/60)}})                            
                              if(out_time.time() >= admin_out_time ):
                                 
                                 client[j].attendence.update({"_id":i['date']},{"$set":{'advance':0}})
                              
                                                          
                               

          if(department['department']=='cleaning'):   
      
        
             
             
             for i in client[j].attendence.find({},{"_id":False}):

                        
                       # attendence_date=datetime.strptime(i['date'],'%d/%m/%Y').date()
                        print(i['date'])
                        advance_minutes=0
                        attendence_date=datetime.strptime(i['date'],'%d/%m/%Y').date()
                        
                        in_time=datetime.strptime(i['in_time'],"%H:%M")
                        
                        try:
                           
                           out_time=datetime.strptime(i['out_time'],"%H:%M")
                           print(type(out_time))
                           
                           
                        except:
                        
                           dem_time="0:00"
                           out_time=datetime.strptime(dem_time,"%H:%M")
                           print(out_time)

                        print(in_time.time())  

                        if( 1==1 ):
                              print(j)
        

                              delayed_hr=abs(int(str(in_time.time())[0:2]) - int(str(cleaning_present_time)[0:2]))
                              delayed_min=abs(int(str(in_time.time())[3:5]) - int(str(cleaning_present_time)[3:5]))
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                            
                              total_hours=abs(int(str(out_time.time())[0:2])-int(str(in_time.time())[0:2]))
                              total_min=abs(int(str(out_time.time())[3:5])-int(str(in_time.time())[3:5]))
                              
                              print(total_hours,total_min)
                              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
                             
                              tw = out_time - in_time
                              
                              print("woooooo", tw.total_seconds()/60/60)
                              
                              total_hours_worked = str(total_hours_worked)
                              overtime = (tw.total_seconds()/60) - 480 
                              print("ot_min",overtime)
                              if(overtime >= 60):
                                 ot=overtime/60
                                 #ot = 0 
                              else:
                                ot=0   
                              print(type(i))
                              
                              i.update({'totalhours':str(total_hours_worked)})
                              i.update({'overtime':str(str(ot)+"-"+"hrs")})
                              client[j].attendence.update({"_id":i['date']},{"$set":{'overtime':str(ot)}})
                              client[j].attendence.update({"_id":i['date']},{"$set":{'total_hours':str(total_hours_worked)}})
                              bc.append(i) 
                              print(str(total_delay))
                         
                              
                              temp = cleaning_out_time_diff - out_time
                              
                              print("difference ", temp.total_seconds()/60)

                              if(out_time.time() < cleaning_out_time ):
                                           print("advance minutes shift one  if ",temp)
                                           client[j].attendence.update({"_id":i['date']},{"$set":{'advance':str(temp.total_seconds()/60)}})                            
                              if(out_time.time() >= cleaning_out_time ):
                                 
                                 client[j].attendence.update({"_id":i['date']},{"$set":{'advance':0}})
                         
                              if (in_time.time() > cleaning_present_time ):
                                  i.update({'delay':str(total_delay)})
                                  client[j].attendence.update({"_id":i['date']},{"$set":{'delay':str(total_delay)}})
                              if (in_time.time() <= cleaning_present_time):
                                  i.update({'delay':"00:00:00"})
                                  client[j].attendence.update({"_id":i['date']},{"$set":{'delay':"00:00:00"}})

          if(department['department']=='office_boy'):   
      
        
             
             
             for i in client[j].attendence.find({},{"_id":False}):

                        
                       # attendence_date=datetime.strptime(i['date'],'%d/%m/%Y').date()
                        print(i['date'])
                        advance_minutes=0
                        attendence_date=datetime.strptime(i['date'],'%d/%m/%Y').date()
                        
                        in_time=datetime.strptime(i['in_time'],"%H:%M")
                        
                        try:
                           
                           out_time=datetime.strptime(i['out_time'],"%H:%M")
                           print(type(out_time))
                           
                           
                        except:
                        
                           dem_time="0:00"
                           out_time=datetime.strptime(dem_time,"%H:%M")
                           print(out_time)

                        print(in_time.time())  

                        if( 1==1 ):
                              print(j)
        

                              delayed_hr=abs(int(str(in_time.time())[0:2]) - int(str(cleaning_present_time)[0:2]))
                              delayed_min=abs(int(str(in_time.time())[3:5]) - int(str(cleaning_present_time)[3:5]))
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                            
                              total_hours=abs(int(str(out_time.time())[0:2])-int(str(in_time.time())[0:2]))
                              total_min=abs(int(str(out_time.time())[3:5])-int(str(in_time.time())[3:5]))
                            
                              print(total_hours,total_min)
                              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
                             
                              tw = out_time - in_time
                              
                              print("woooooo", tw.total_seconds()/60/60)
                              
                              total_hours_worked = str(total_hours_worked)
                              overtime = (tw.total_seconds()/60) - 480 
                              print("ot_min",overtime)
                              if(overtime >= 60):
                                 ot=overtime/60
                                 ot = 0 
                              else:
                                ot=0   
                              print(type(i))
                              
                              i.update({'totalhours':str(total_hours_worked)})
                              i.update({'overtime':str(str(ot)+"-"+"hrs")})
                              client[j].attendence.update({"_id":i['date']},{"$set":{'overtime':str(ot)}})
                              client[j].attendence.update({"_id":i['date']},{"$set":{'total_hours':str(total_hours_worked)}})
                              bc.append(i) 
                              print(str(total_delay))
                         
                              
                              temp = cleaning_out_time_diff - out_time
                              
                              print("difference ", temp.total_seconds()/60)

                              if(out_time.time() < cleaning_out_time ):
                                           print("advance minutes shift one  if ",temp)
                                           client[j].attendence.update({"_id":i['date']},{"$set":{'advance':str(temp.total_seconds()/60)}})                            
                              if(out_time.time() >= cleaning_out_time ):
                                 
                                 client[j].attendence.update({"_id":i['date']},{"$set":{'advance':0}})
                         
                              if (in_time.time() > cleaning_present_time ):
                                  i.update({'delay':str(total_delay)})
                                  client[j].attendence.update({"_id":i['date']},{"$set":{'delay':str(total_delay)}})
                              if (in_time.time() <= cleaning_present_time):
                                  i.update({'delay':"00:00:00"})
                                  client[j].attendence.update({"_id":i['date']},{"$set":{'delay':"00:00:00"}})


                                                                                                                                                          
        
        
          if(department['department']=='admin_prof'):   
      
        
             
             
             for i in client[j].attendence.find({},{"_id":False}):

                        
                       # attendence_date=datetime.strptime(i['date'],'%d/%m/%Y').date()
                        attendence_date=datetime.strptime(i['date'],'%d/%m/%Y').date()
                        
                        in_time=datetime.strptime(i['in_time'],"%H:%M")
                        
                        try:
                           
                           out_time=datetime.strptime(i['out_time'],"%H:%M")
                           print(type(out_time))
                           
                           
                        except:
                        
                           dem_time="0:00"
                           out_time=datetime.strptime(dem_time,"%H:%M")
                           print(out_time)

                        print(in_time.time())  

                        if(1==1 ):
                              print(j)
        

                              delayed_hr=abs(int(str(in_time.time())[0:2]) - int(str(admin_prof_present_time)[0:2]))
                              delayed_min=abs(int(str(in_time.time())[3:5]) - int(str(admin_prof_present_time)[3:5]))
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                            
                              total_hours=abs(int(str(out_time.time())[0:2])-int(str(in_time.time())[0:2]))
                              total_min=abs(int(str(out_time.time())[3:5])-int(str(in_time.time())[3:5]))
                            
                              print(total_hours,total_min)
                              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
                             
                              tw = out_time - in_time
                              
                              print("woooooo", tw.total_seconds()/60/60)
                              
                              total_hours_worked = str(total_hours_worked)
                              overtime = (tw.total_seconds()/60) - 480 
                              print("ot_min",overtime)
                              if(overtime >= 60):
                                 ot=overtime/60
                                 #ot = 0 
                              else:
                                ot=0   
                              print(type(i))
                              
                              i.update({'totalhours':str(total_hours_worked)})
                              i.update({'overtime':str(str(ot)+"-"+"hrs")})
                              client[j].attendence.update({"_id":i['date']},{"$set":{'delay':str(total_delay)}})
                              client[j].attendence.update({"_id":i['date']},{"$set":{'total_hours':str(total_hours_worked)}})                              
                            #  print(i)
                              
                        
                         
                              temp = admin_prof_out_time_diff - out_time
                              
                              print("difference ", temp.total_seconds()/60)

                              if(out_time.time() < admin_prof_out_time ):
                                           print("advance minutes shift one  if ",temp)
                                           client[j].attendence.update({"_id":i['date']},{"$set":{'advance':str(temp.total_seconds()/60)}})                            
                              if(out_time.time() >= admin_prof_out_time ):
                                 
                                 client[j].attendence.update({"_id":i['date']},{"$set":{'advance':0}})
                                                       
                              
                              if (in_time.time() > admin_prof_present_time ):
                                  i.update({'delay':str(total_delay)})
                                  client[j].attendence.update({"_id":i['date']},{"$set":{'delay':str(total_delay)}})
                              if (in_time.time() <= admin_prof_present_time):
                                  i.update({'delay':"00:00:00"})
                                  client[j].attendence.update({"_id":i['date']},{"$set":{'delay':"00:00:00"}})
                              bc.append(i)
                                                                                                                                                          
        
                              
          if(department['department']=='purchase_team'):   
      
        
             
             
             for i in client[j].attendence.find({},{"_id":False}):

                        
                       # attendence_date=datetime.strptime(i['date'],'%d/%m/%Y').date()
                        attendence_date=datetime.strptime(i['date'],'%d/%m/%Y').date()

                        try:
                           in_time=datetime.strptime(i['in_time'],"%H:%M")
                        except:
                            in_time=datetime.strptime("10:30","%H:%M")
                        try:
                           
                           out_time=datetime.strptime(i['out_time'],"%H:%M")
                           print(type(out_time))
                           
                           
                        except:
                        
                           dem_time="0:00"
                           out_time=datetime.strptime(dem_time,"%H:%M")
                           print(out_time)

                        print(in_time.time())  

                        if(1==1 ):
                              print(j)
        

                              delayed_hr=abs(int(str(in_time.time())[0:2]) - int(str(purchase_team_present_time)[0:2]))
                              delayed_min=abs(int(str(in_time.time())[3:5]) - int(str(purchase_team_present_time)[3:5]))
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                            
                              total_hours=abs(int(str(out_time.time())[0:2])-int(str(in_time.time())[0:2]))
                              total_min=abs(int(str(out_time.time())[3:5])-int(str(in_time.time())[3:5]))
                            
                              print(total_hours,total_min)
                              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
                             
                              tw = out_time - in_time
                              
                              print("woooooo", tw.total_seconds()/60/60)
                              
                              total_hours_worked = str(total_hours_worked)
                              overtime = (tw.total_seconds()/60) - 480 
                              print("ot_min",overtime)
                              if(overtime >= 60):
                                 ot=overtime/60
                                 #ot = 0 
                              else:
                                ot=0   
                              print(type(i))
                              
                              i.update({'totalhours':str(total_hours_worked)})
                              i.update({'overtime':str(str(ot)+"-"+"hrs")})
                              #client[j].attendence.update({"_id":i['date']},{"$set":{'delay':str(total_delay)}})
                              client[j].attendence.update({"_id":i['date']},{"$set":{'total_hours':str(total_hours_worked)}})                               
                            #  print(i)
                              

                        
                    
                              
                              temp = purchase_team_out_time_diff - out_time
                              
                              print("difference ", temp.total_seconds()/60)

                              if(out_time.time() < purchase_team_out_time ):

                                           
                                             client[j].attendence.update({"_id":i['date']},{"$set":{'advance':str(temp.total_seconds()/60)}})                            

                              if(out_time.time() >= admin_prof_out_time ):
                                 
                                 client[j].attendence.update({"_id":i['date']},{"$set":{'advance':0}})
                                                                                     
                              
                              if (in_time.time() > purchase_team_present_time ):
                                  i.update({'delay':str(total_delay)})
                                  client[j].attendence.update({"_id":i['date']},{"$set":{'delay':str(total_delay)}})
                                  
                              if (in_time.time() <= purchase_team_present_time):
                                  i.update({'delay':"00:00:00"})
                                  client[j].attendence.update({"_id":i['date']},{"$set":{'delay':"00:00:00"}})

                              bc.append(i)
                                  
                                                                                                                              
          
          
                       # bc.append(i)
      print(bc)
      return jsonify(bc) 


############################################################################################################################
#debug salary calculation

@app.route('/employee_monthly_salary',methods=['PUT'])   ##original employee_monthly_salary_changed : its debug salary calculation
def salary_calculation():
    
    try :
       
       month_date = request.get_json()['month']
       month_date= month_date.replace("-","/")
       print(month_date)
       month = str(month_date[8:10]) + "/" + str(month_date[5:7]) +"/"+ str(month_date[0:4])
       
    except:
       month="01/08/2020"    
    
    
    print(month)
    all_employees=client.list_database_names()
    delay_minutes=0
    advance_minutes=0
    employee_monthly_salary=[]
    over_time=0
    inc=0
    total_detection=0
    
    year=datetime.today()
    days_in_month=monthrange(int(month[6:]),int(month[3:5]))
    
    y=int(month[6:])
    m=int(month[3:5])
    days=[weekday(y,m,d+1) for d in range(*monthrange(y,m)) ]
    
    sundays=days.count(SUNDAY)
    
    print(sundays)
    print("no_of_days",days_in_month[1])
    num_of_days=days_in_month[1]
    #month="2020-08-01"
 
    admin_present_time="8:30"
    admin_out_time="17:35"
    admin_present_time=datetime.strptime(admin_present_time,"%H:%M").time()
    admin_out_time=datetime.strptime(admin_out_time,"%H:%M").time()
    month=datetime.strptime(month,"%d/%m/%Y").date()
    employee_monthly_salary=[]
    salary={}
    
    for sqt_cost in client.contractors.sqt_cost.find({},{"_id":False}):
         bed_polish_per_sq_feet  = float(sqt_cost['bed_polish'])
         hand_polish_per_sq_feet = float(sqt_cost['hand_polish'])
         dry_cutting_per_sq_feet =  float (sqt_cost['dry_cutting'])
       
    for shares in client.esi_epf_shares.esi_epf.find({},{"_id":False}):
       db_basic_pay=float(shares['basic_pay'])
       db_conveyence=float(shares['conveyence'])
       db_epf_employeer_pension=float(shares['epf_employeer_pension'])
       db_epf_employee_share=float(shares['epf_employee_share'])
       db_esi_employeer_share=float(shares['esi_employeer_share'])
       db_hra=float(shares['hra'])
       db_esi_employee_share=float(shares['esi_employee_share'])
       db_epf_employeer_epf=float(shares['epf_employeer_epf'])
       db_wl_allowence=float(shares['wl_allowence'])
    
    for i in all_employees:
         worked_hours=0
         
  
             
         if(i!='admin' and i!='config' and i!='loginuser' and i!='local' and i!='esi_epf_shares' and i!='contractors' and i!='salary_log' ):


             for department in client[i].details.find({},{"_id":False}):
             
                #if(department['department']=='admin' or department['department']=='edge_cutting' or  department['department']=='driver' or department['department']=='carving' or department['department']=='packing' or department['department']=='cleaning' ):

                    
                if(department['position'] != 'contractor' ): 
                    delay_minutes=0
                    worked_day=0
                    advance_minutes=0
                    inc=0
                    mins_worked = 0
                    over_time =0 
                	#over_time=0
                
                    
                    for date in client[i].attendence.find({},{"_id":False}):

                       # datetime.strptime(string,'%d/%m/%Y') = convert string to date
                        attendence_date=datetime.strptime(date['date'],'%d/%m/%Y').date()
                   
                    
                        if(str(attendence_date)[5:7] == str(month)[5:7]):
 #                         print(attendence_date)
                          try:
                            in_time=datetime.strptime(date['in_time'],"%H:%M")
                          except:
                             in_time=datetime.strptime("00:00","%H:%M") 
                          try:
                            out_time=datetime.strptime(date['out_time'],"%H:%M")
                          except:
                            out_time=datetime.strptime("0:00","%H:%M")  
                          worked_day=worked_day+1
                          total_hours_worked = date['total_hours']
                          de = date['delay']
                          
                          print("delay",date['delay'],"advance", date['advance'])
                          print("emp_name","   ",i)
                          advance_minutes = float(date['advance']) + advance_minutes
                          try:
                           delay_minutes = float (de[0:2])*60 + float (de[3:5]) + delay_minutes
                          except:
                            delay_minutes =0
                          over_time = float (date['overtime']) + over_time
                          
                    print(advance_minutes , "   ", delay_minutes)        
                    total_detection=int(delay_minutes)+int(advance_minutes)       
                    print("total_detection",total_detection)
                   
                    for j in client[i].salary_details.find({},{"_id":False}):
  #                      print("worked_day",worked_day)
                        
                        net_salary=int(j['net_salary'])
                    
                    print(client[i])    
                    for k in client[i].details.find({},{"_id":False}):
                        try:
                           doj = k['DateOfJoining']
                           esi = k['ESINumber']
                           epf = k['EPFNumber']
                        except:
                           esi = '00000'
                           epf = '00000'
                           
                         
                    present_day = worked_day 
                        
                    absent_days=(num_of_days-sundays)-present_day
                     
                    per_day_salary = net_salary/(num_of_days-sundays)
                        
                    new_salary_month= int(per_day_salary*(present_day))
                        
                    print("net_salary_month",new_salary_month)
                    print("per_day_salary",per_day_salary) 
                       
                    basic_salary=(db_basic_pay*new_salary_month)/100
                    wl_allowence=(db_wl_allowence*new_salary_month)/100
                    hra=(db_hra*new_salary_month)/100
                    conveyence=(db_conveyence*new_salary_month)/100
                    esi_employee_share=(db_esi_employee_share*new_salary_month)/100
                    esi_employeer_share=(db_esi_employeer_share*new_salary_month)/100
                    epf_employee_share=(db_epf_employee_share*new_salary_month)/100
                    epf_pension_employeer_share=(db_epf_employeer_pension*basic_salary)/100
                    epf_employeer_epf_share=(db_epf_employeer_epf*basic_salary)/100
                    print("present_day",present_day)
                    print("absent day ",absent_days)

                        
                    increment=2 
                        
                    free_permission=120
                        
                    if(absent_days-increment ==2 or absent_days-increment>2 or absent_days-increment==1):
                             print("no increment")
                             inc =0
                             
                    if(absent_days-increment <=0):
                             inc=1
                                  
                    print("net_salary",net_salary) 
                       
                    employee_net_salary = net_salary
                        
                    per_min_salary = net_salary/(num_of_days-sundays)/8/60
                    
                    print(per_min_salary)   
                    
                    
                    delay_advance = total_detection- free_permission
                    
                    if (delay_advance > 0):
                    
                       detection = per_min_salary * (delay_advance)
                    
                    if (delay_advance <= 0):
                       
                       detection =0
                    
                    
                    
                    fin_salary = new_salary_month-esi_employee_share-epf_employee_share
                    
                    fin_salary = fin_salary - (per_min_salary*detection)
                    
                    fin_salary = fin_salary + (inc*per_min_salary*8*60)
                    
                    fin_salary = fin_salary + (over_time*per_min_salary)
                    
                    t_detection = per_min_salary*detection
                        
                    #final_salary = net_salary-esi_employee_share-epf_employee_share-(per_min_salary*delay_minutes) 
                        
                    #detection= int(fin_salary - final_salary) 
                        #final_month_salary=worked_day*per_min_salary*60*8     
                        
                   # advance_detection=advance_minutes*per_min_salary                         
                   # t_detection = (total_detection-free_permission)*per_min_salary
                   
                   # final_month_salary=((present_day+inc)*per_min_salary*8*60)-(t_detection) + (over_time*per_min_salary)
   #                     print("final salary ",worked_day,delay_minutes,advance_minutes,total_detection,i)       
                             
                        #print(net_salary,basic_salary,wl_allowence,hra,conveyence,esi_employee_share,epf_employee_share,final_salary)

                        #print(j['net_salary'])
                        
                   # delay_minutes=int(delay_minutes/10)*60*per_min_salary


                    print("esi_employee ",esi_employee_share)
                    #sal.salary_log.monthly.drop()
                    if (new_salary_month > 0 ):
                    
                      salary_log = {'_id':i+"_"+str(month),'employee_name':i,'month':str(month),'sq_ft':0,'net_salary':new_salary_month,
                                    'basic_salary':basic_salary,'wl_allowence':wl_allowence,'hra':hra,'conveyence':conveyence,
                                    'esi_employee_share':int(esi_employee_share),
                            'esi_employeer_share':int(esi_employeer_share),'epf_employee_share':int(epf_employee_share),
                                    'epf_pension_employeer_share':int(epf_pension_employeer_share),
                            'epf_employeer_epf_share':int(epf_employeer_epf_share),'overtime':int(over_time),'new_t':over_time,'worked_days':present_day+sundays,
                                    'doj':doj,'ESI-no':esi,'EPF-no':esi,
                            'detection':int(t_detection),'final_salary':int(fin_salary),'department':department['department'],
                                    'position':department['position'],'new':'new' }
                      print(salary_log)
                      #client.salary_log.monthly.update({'_id':i+"_"+str(month)[5:7]},salary_log)
                      already_present = client.salary_log.monthly.find({'_id':i+"_"+str(month)}).count()

                      if (already_present ==1 ):
                          client.salary_log.monthly.delete_one({'_id':i+"_"+str(month)})
                          client.salary_log.monthly.insert_one(salary_log)
                      if (already_present == 0 ):
                          client.salary_log.monthly.insert_one(salary_log)

                    
                    employee_monthly_salary.append({'employee_name':i,'month':month,'sq.ft':'0','net_salary':new_salary_month,'basic_salary':basic_salary,'wl_allowence':wl_allowence,'hra':hra,'conveyence':conveyence,'esi_employee_share':esi_employee_share,
                        'esi_employeer_share':esi_employeer_share,'epf_employee_share':epf_employee_share,'epf_pension_employeer_share':epf_pension_employeer_share,
                        'epf_employeer_epf_share':epf_employeer_epf_share,'overtime':over_time,
                        'detection':int(t_detection),'final_salary':int(fin_salary)})
                    print("genetrated")
                        
                    print(employee_monthly_salary[0])    
                   #     print("eployee_per ",per_min_salary)
                    #    print("time delayed",delay_minutes)
                     #   print(fin_salary,final_salary)
                    
               #     print(i)
                
                
               # print(department['department'])
                #print(department['position'])   
          #  print('\n')

               
                if(department['position']=='contractor'):
                  
                 
                    
              
                            worked_day=0
                            advance_minutes=0
                            inc=0
                            delay_minutes=0
                            worked_day=0
                            sq_feet =0
                            monthly_sq_salary=0
  
                            new_salary_month=0
                            no_of_sq_feet=0
                            
                            for do in client[i].details.find({},{"_id":False}):
                                try:
                                  doj = do['DateOfJoining']
                                  esi = do ['ESINumber']
                                  epf = do ['EPFNumber']
                                except:
                                  doj = '00000'
                                  esi = '00000'
                                  epf = '00000'
                                
                            for date in client[i].attendence.find({},{"_id":False}):

                            # datetime.strptime(string,'%d/%m/%Y') = convert string to date
                                attendence_date=datetime.strptime(date['date'],'%d/%m/%Y').date()
                                #attendence_date=datetime.strptime(date['date'],'%d/%m/%Y').date()
                                if(str(attendence_date)[5:7] == str(month)[5:7]):
        #                         print(attendence_date)
                                    print("same")
                                    in_time=datetime.strptime(date['in_time'],"%H:%M")
                                    try:
                                      out_time=datetime.strptime(date['out_time'],"%H:%M")
                                    except:
                                        out_time = datetime.strptime("00:00","%H:%M")
                                    worked_day=worked_day+1
                            
                            print(client[i])
                            
                            for s_feet in client[i].monthly_sq_feet.find({},{"_id":False}):
                              sqt_date=datetime.strptime(s_feet['date'],'%d/%m/%Y').date()
                              if(str(sqt_date)[5:7] == str(month)[5:7]):
                                print("sqt",s_feet['total_sq_feet'])
                                no_of_sq_feet = int(s_feet['total_sq_feet'])
                                print("no_of_sq_feet",no_of_sq_feet)
                                if(department['department']=='bed_polish'):
                                    
                                    monthly_sq_salary = no_of_sq_feet * bed_polish_per_sq_feet
                                    print(monthly_sq_salary)
                                if(department['department']=='hand_polish'):
                                    monthly_sq_salary = no_of_sq_feet * hand_polish_per_sq_feet
                                if (department['department']=='dry_cutting'):
                                    monthly_sq_salary = no_of_sq_feet * dry_cutting_per_sq_feet
                            
                            net_salary_month = monthly_sq_salary

                            present_day = worked_day + sundays
                            absent_days=num_of_days-present_day
                            
    #                     print("absent_day",absent_days)
    #                     print("present_day", present_day)                        
                            
                            per_day_salary = net_salary_month/num_of_days
                            
                            
        #                    print("net_salary_month",new_salary_month)
                            basic_salary=(db_basic_pay*net_salary_month)/100
                            wl_allowence=(db_wl_allowence*net_salary_month)/100
                            hra=(db_hra*net_salary_month)/100
                            conveyence=(db_conveyence*net_salary_month)/100
                            
                            esi_employee_share= int( (db_esi_employee_share*net_salary_month)/100)
                            
                            esi_employeer_share= int ((db_esi_employeer_share*net_salary_month)/100)
                            
                            epf_employee_share=int ( (db_epf_employee_share*net_salary_month)/100 )
                            
                            epf_pension_employeer_share= int ((db_epf_employeer_pension*basic_salary)/100 )
                            
                            epf_employeer_epf_share= int ( (db_epf_employeer_epf*basic_salary)/100)
                        

                            
                            increment=2
                            
                            free_permission=120
                            
                            if(abs(absent_days-increment) ==2 or abs(absent_days-increment)==1 or absent_days-increment==1):
                            
                                print("no increment")
                                
                            if(absent_days-increment <=0):
                            
                                net_salary_month = net_salary_month + per_day_salary
                                    

                            
                            final_month_salary= net_salary_month-esi_employee_share-epf_employee_share

                 
                    
                                                
                            if (net_salary_month > 0 ):
                              salary_log = {'_id':i+"_"+str(month)[5:7],'employee_name':i,'month':str(month),'sq_ft':no_of_sq_feet,'net_salary':net_salary_month,'basic_salary':basic_salary,'wl_allowence':wl_allowence,'hra':hra,'conveyence':conveyence,'esi_employee_share':esi_employee_share,
                            'esi_employeer_share':esi_employeer_share,'epf_employee_share':epf_employee_share,'epf_pension_employeer_share':epf_pension_employeer_share,
                            'epf_employeer_epf_share':epf_employeer_epf_share,'overtime':over_time,'worked_days':present_day+sundays,'doj':doj,'ESI-no':epf,'EPF-no':esi,
                            'detection':0,'final_salary':int(final_month_salary),'department':department['department'],'position':department['position'] }
                              print(salary_log)
                            
                              if(client.salary_log.monthly.find_one({'_id':i+"_"+str(month)[5:7]})):
                                  client.salary_log.monthly.update({'_id':i+"_"+str(month)[5:7]},salary_log)
                                  print("already")
                              else:               
                                 client.salary_log.monthly.insert_one(salary_log)
                                                       
                            employee_monthly_salary.append({'employee_name':i,'month':month,'sq.ft':no_of_sq_feet,'net_salary':net_salary_month,'basic_salary':basic_salary,'wl_allowence':wl_allowence,'hra':hra,'conveyence':conveyence,'esi_employee_share':esi_employee_share,
                            'esi_employeer_share':esi_employeer_share,'epf_employee_share':epf_employee_share,'epf_pension_employeer_share':epf_pension_employeer_share,
                            'epf_employeer_epf_share':epf_employeer_epf_share,'overtime':'0',
                            'detection':0,'final_salary':int(final_month_salary)})
                            print("genetrated")
                                    
                    
             
    

    return jsonify(employee_monthly_salary) 

#debug salary calculation
#############################################################################################################################################

##########################################################        roll only starts ##########################################################

@app.route('/monthly_salary_download',methods=["PUT"])
def doenload():
 
   main_list = [] 
   
   fields = (
    ('employee_name', 'Employee Name'),
    ('department', 'Department'),
    ('net_salary', 'Gross Salary'),
    ('basic_salary', 'Basic Salary'),
     ('sq_ft', 'Sq.feet'),
    ('detection', 'Detection'),
    ('overtime','overtime'),
    ('final_salary', 'Salary'),
    ('delay','Delay')
    
 
)
   
   if (len(str(request.get_json()['date'])) == 1):
       print("0"+str(request.get_json()['date']))
   else:
       print(str(request.get_json()['date'])[5:7])   
   final_amount = 0 
   for i in client.salary_log.monthly.find({},{"_id":False}):
      print(i)
      final_amount = final_amount + int(i['final_salary'])
      main_list.append(i)

   
   doc = DataToPdf(fields, main_list,
                title='MARP SALARY REPORT'+"  "+":"+"  "+str(main_list[0]['month'])+" : "+str(final_amount))
   try :
     os.remove('MARP_REPORT.pdf')
   except:
     pass
                    
   doc.export('MARP_REPORT.pdf')
   webbrowser.open_new_tab('/monthly_salary_downloads')
   return send_file('MARP_REPORT.pdf', as_attachment=True,cache_timeout=60)


@app.route('/monthly_salary_downloads')
def doenloads():

   
   return send_file('MARP_REPORT.pdf', as_attachment=True,cache_timeout=60)





@app.route('/monthly_esi_download',methods=["PUT"])
def doenload_esi():

   main_list = [] 
   print("esi")
   fields_esi = (
    ('employee_name', 'Employee Name'),
   
     ('ESI-no','ESI-no'),
     
    ('month', 'Month'),

   ('doj', 'Date of Joining'),
   
   ('absent_days', 'NCP'),
   
   ('net_salary', 'Gross Salary'),
   

   
   
    ('esi_employee_share', 'ESI Eployee'),
    
    ('esi_employeer_share', 'ESI Employeer'),

)
   
   if (len(str(request.get_json()['date'])) == 1):
       print("0"+str(request.get_json()['date']))
   else:
       print(str(request.get_json()['date'])[5:7])   
   
   for i in client.salary_log.monthly.find({},{"_id":False}):
      if (i['cat'] == 'roll' and i['esi_st'] == 'yes' ):
         main_list.append(i)


   
   
   doc = DataToPdf(fields_esi, main_list,
                title='MARP ESI REPORT'+"  "+"-"+"  "+str(main_list[0]['month']))
   
   try :
     os.remove('MARP_ESI_REPORT.pdf')
   except:
     pass  
   
   doc.export('MARP_ESI_REPORT.pdf')
   
   webbrowser.open_new_tab('/monthly_esi_downloads_main')
   
   return send_file('MARP_ESI_REPORT.pdf', as_attachment=True,cache_timeout=60)


@app.route('/monthly_esi_downloads_main')
def doenloads_esi_main():

  return send_file('MARP_ESI_REPORT.pdf', as_attachment=True,cache_timeout=60)
 



@app.route('/monthly_epf_download',methods=["PUT"])
def doenload_epf():

   main_list = [] 
   print("esi")
   fields_esi = (
    ('employee_name', 'Employee Name'),
   
     ('EPF-no','EPF-no'),
     
    ('month', 'Month'),

    ('final_salary', 'Salary'),
   
   ('doj', 'Date of Joining'),
   
   ('absent_days', 'NCP'),
   
   
   ('basic_salary', 'Basic Salary'),
   
   ('epf_employee_share','EPF Employee'),
   
    ('epf_pension_employeer_share', 'EPF Employeer'),
    
    ('epf_employeer_epf_share', 'EPF Employeer Pension'),

)
   
   if (len(str(request.get_json()['date'])) == 1):
       print("0"+str(request.get_json()['date']))
   else:
       print(str(request.get_json()['date'])[5:7])   
   
   for i in client.salary_log.monthly.find({},{"_id":False}):
     if (i['cat'] == 'roll' and i['epf_st'] == 'yes' ):
        main_list.append(i)

   
   
   doc = DataToPdf(fields_esi, main_list,
                title='MARP EPF REPORT'+"  "+"-"+"  "+str(main_list[0]['month']))
   
   try :
     os.remove('MARP_EPF_REPORT.pdf')
   except:
     pass  
   
   doc.export('MARP_EPF_REPORT.pdf')
   
   webbrowser.open_new_tab('/monthly_epf_downloads_main')
   
   return send_file('MARP_EPF_REPORT.pdf', as_attachment=True,cache_timeout=60)


@app.route('/monthly_epf_downloads_main')
def doenloads_epf_main():

  return send_file('MARP_EPF_REPORT.pdf', as_attachment=True,cache_timeout=60)

@app.route('/employee-details/roll')
def  employee_details_roll():
      ab={}
      bc=[]
      all_employees=client.list_database_names()
      
      employee_list=client.employee
       
      for j in all_employees: 
      
         for i in client[j].details.find({},{"_id":False}):
          if(i['role']=='roll'):	
            print(i['role'])
          #print(i)
            ab.update(i)
            bc.append(i)
          
     # print(bc[0])
      #print(bc[1])
      #print(bc)
      return jsonify(bc)
       

@app.route('/employee_salary_list/roll')
def employee_salary_list_role():

      bc=[]
      all_employees=client.list_database_names()
      
      employee_list=client.employee
       
      for j in all_employees: 
         for k in client[j].details.find({},{"_id":False}):
           if(k['role']=='roll'):
                for i in client[j].salary_details.find({},{"_id":False}):
          #print(i)
          
                  bc.append(i)
          
     # print(bc[0])
      #print(bc[1])
      #print(bc)
      return jsonify(bc) 



@app.route('/employee_monthly_salary/roll',methods=['GET'])   ##original employee_monthly_salary_changed : its debug salary calculation
def salary_calculation_roll():
 
    all_employees=client.list_database_names()
    delay_minutes=0
    
    employee_monthly_salary=[]
    over_time=0
    month="01/06/2020"
    admin_present_time="8:30"
    admin_present_time=datetime.strptime(admin_present_time,"%H:%M").time()
    month=datetime.strptime(month,"%d/%m/%Y").date()

    salary={}
    for shares in client.esi_epf_shares.esi_epf.find({},{"_id":False}):
       db_basic_pay=float(shares['basic_pay'])
       db_conveyence=float(shares['conveyence'])
       db_epf_employeer_pension=float(shares['epf_employeer_pension'])
       db_epf_employee_share=float(shares['epf_employee_share'])
       db_esi_employeer_share=float(shares['esi_employeer_share'])
       db_hra=float(shares['hra'])
       db_esi_employee_share=float(shares['esi_employee_share'])
       db_epf_employeer_epf=float(shares['epf_employeer_epf'])
       db_wl_allowence=float(shares['wl_allowence'])
    
    for i in all_employees:
         worked_hours=0
         
  
             
         if(i!='admin' and i!='config' and i!='loginuser' and i!='local' and i!='esi_epf_shares'):
            
            

             for department in client[i].details.find({},{"_id":False}):
               if department['role']=='roll':          
                         
                if(department['department']=='Administration'):
                    delay_minutes=0
                	#over_time=0
                    for date in client[i].attendence.find({},{"_id":False}):

                       # datetime.strptime(string,'%d/%m/%Y') = convert string to date

                        attendence_date=datetime.strptime(date['date'],'%d/%m/%Y').date()
                        if(str(attendence_date)[5:7] == str(month)[5:7]):
                          print(attendence_date)
                          in_time=datetime.strptime(date['in_time'],"%H:%M")
                          
                          if(in_time.time() > admin_present_time ):
                              #print("late")
                             # print(str(admin_present_time)[0:2])
                              #print(str(admin_present_time)[3:5])
                              #print(str(in_time.time())[0:2])
                              #print(str(in_time.time())[3:5])    

                              delayed_hr=int(str(in_time.time())[0:2]) - int(str(admin_present_time)[0:2])
                              delayed_min=int(str(in_time.time())[3:5]) - int(str(admin_present_time)[3:5])
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                              
                             # print("total Delay",total_delay)
                              delay_minutes=int(str(total_delay)[0:2])*60 + int(str(total_delay)[3:5]) + delay_minutes
                              print("delay_minutes",delay_minutes)
                              #print(in_time.time())
                              #over_time=0
                          #######################################################################################################
                          # to be continue
                          else:
                               print(" ")
                               #print(date['in_time'])
                          #print(str(month)[5:7])
                    for j in client[i].salary_details.find({},{"_id":False}):

                        net_salary=int(j['net_salary'])
                        basic_salary=(db_basic_pay*net_salary)/100
                        wl_allowence=(db_wl_allowence*net_salary)/100
                        hra=(db_hra*net_salary)/100
                        conveyence=(db_conveyence*net_salary)/100
                        esi_employee_share=(db_esi_employee_share*basic_salary)/100
                        esi_employeer_share=(db_esi_employeer_share*basic_salary)/100
                        epf_employee_share=(db_epf_employee_share*basic_salary)/100
                        epf_pension_employeer_share=(db_epf_employeer_pension*basic_salary)/100
                        epf_employeer_epf_share=(db_epf_employeer_epf*basic_salary)/100
                    

                        employee_net_salary = int(j['net_salary'])
                        per_min_salary = employee_net_salary/27/8/60
                        
                        fin_salary = net_salary-esi_employee_share-epf_employee_share
                        final_salary = net_salary-esi_employee_share-epf_employee_share-(per_min_salary*delay_minutes)
                        
                        detection= int(fin_salary - final_salary)             
                        #print(net_salary,basic_salary,wl_allowence,hra,conveyence,esi_employee_share,epf_employee_share,final_salary)

                        #print(j['net_salary'])

                        
                        
                        employee_monthly_salary.append({'employee_name':i,'month':'month','sq.ft':'0','net_salary':net_salary,'basic_salary':basic_salary,'wl_allowence':wl_allowence,'hra':hra,'conveyence':conveyence,'esi_employee_share':esi_employee_share,
                        'esi_employeer_share':esi_employeer_share,'epf_employee_share':epf_employee_share,'epf_pension_employeer_share':epf_pension_employeer_share,
                        'epf_employeer_epf_share':epf_employeer_epf_share,'overtime':over_time,
                        'detection':delay_minutes,'final_salary':int(final_salary)})
      
             
               
             
             if(department['department']=='operator'):
                     print("operator")

    return jsonify(employee_monthly_salary) 
    
@app.route('/attendence_list/roll')
def attendence_list_roll():
           

      admin_present_time="8:30"
      admin_present_time=datetime.strptime(admin_present_time,"%H:%M").time()
      bc=[]
      all_employees=client.list_database_names()
      
      employee_list=client.employee
       
      for j in all_employees: 
       for department in client[j].details.find({},{"_id":False}):
        if department['role']=='roll': 
          if(department['department']=='Administration'):   
      
             for i in client[j].attendence.find({},{"_id":False}):


                        attendence_date=datetime.strptime(i['date'],'%d/%m/%Y').date()
      
                        in_time=datetime.strptime(i['in_time'],"%H:%M")
                        print(in_time.time())  

                        if(in_time.time() > admin_present_time ):
                              print("late")
                             # print(str(admin_present_time)[0:2])
                              #print(str(admin_present_time)[3:5])
                              #print(str(in_time.time())[0:2])
                              #print(str(in_time.time())[3:5])    

                              delayed_hr=int(str(in_time.time())[0:2]) - int(str(admin_present_time)[0:2])
                              delayed_min=int(str(in_time.time())[3:5]) - int(str(admin_present_time)[3:5])
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                              
                              print("total Delay",total_delay)
                              print(type(i))
                              i.update({'delay':str(total_delay)})
                              print(i)
                              bc.append(i)
                          #######################################################################################################
                          # to be continue
                        else:
                              i.update({'delay':"00:00:00"})
                              print("ab")
                              bc.append(i)
          
          
                       # bc.append(i)
  
      return jsonify(bc)    
      

@app.route('/md_ot_list')
def md_ot_list():
           
      admin_late_comers=[]
      supervisor_late_comers=[]
      operator_late_comers=[]
      helpers_late_comers=[]
      incharge_late_comers=[]
      
      incharge_overtime=[]
      operators_overtime=[]
      helpers_overtime=[]
      
      admin_present_time="8:30"
      employee_out_time ="6:30"
      
      admin_present_time=datetime.strptime(admin_present_time,"%H:%M").time()
      employee_out_time=datetime.strptime(employee_out_time,"%H:%M").time()
      
      bc=[]
      all_employees=client.list_database_names()
      
      employee_list=client.employee
       
      for j in all_employees: 
       for department in client[j].details.find({},{"_id":False}):
          if(department['department']=='Administration'):   
      
             for i in client[j].attendence.find({},{"_id":False}):


                        attendence_date=datetime.strptime(i['date'],'%d/%m/%Y').date()
      
                        in_time=datetime.strptime(i['in_time'],"%H:%M")
                  
                        print(in_time.time())  

                        if(in_time.time() > admin_present_time ):
                              print("late")
                             # print(str(admin_present_time)[0:2])
                              #print(str(admin_present_time)[3:5])
                              #print(str(in_time.time())[0:2])
                              #print(str(in_time.time())[3:5])    

                              delayed_hr=int(str(in_time.time())[0:2]) - int(str(admin_present_time)[0:2])
                              delayed_min=int(str(in_time.time())[3:5]) - int(str(admin_present_time)[3:5])
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                              if(delayed_min>=15 or delayed_hr>=1):
                                  admin_late_comers.append(j+"     "+i['in_time']+"     "+str(total_delay))
                                  
                              print("total Delay",total_delay)
                              print(type(i))
                              i.update({'delay':str(total_delay)})
                              print(i)
                              bc.append(i)
                          #######################################################################################################
                          # to be continue
                       
                        else:
                              i.update({'delay':"00:00:00"})
                              print("ab")
                              bc.append(i)

       for department in client[j].details.find({},{"_id":False}):
          if(department['department']=='supervisor'):   
      
             for i in client[j].attendence.find({},{"_id":False}):


                        attendence_date=datetime.strptime(i['date'],'%d/%m/%Y').date()
      
                        in_time=datetime.strptime(i['in_time'],"%H:%M")
                        print(in_time.time())  

                        if(in_time.time() > admin_present_time ):
                              print("late")
                             # print(str(admin_present_time)[0:2])
                              #print(str(admin_present_time)[3:5])
                              #print(str(in_time.time())[0:2])
                              #print(str(in_time.time())[3:5])    

                              delayed_hr=int(str(in_time.time())[0:2]) - int(str(admin_present_time)[0:2])
                              delayed_min=int(str(in_time.time())[3:5]) - int(str(admin_present_time)[3:5])
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                              if(delayed_min>=15 or delayed_hr>=1):
                                  supervisor_late_comers.append(j+"    "+i['in_time']+"     "+str(total_delay))
                                  
                              print("total Delay",total_delay)
                              print(type(i))
                              i.update({'delay':str(total_delay)})
                              print(i)
                              bc.append(i)
                          #######################################################################################################
                          # to be continue
                        else:
                              i.update({'delay':"00:00:00"})
                              print("ab")
                              bc.append(i)          
       for department in client[j].details.find({},{"_id":False}):
          if(department['department']=='incharge'):   
      
             for i in client[j].attendence.find({},{"_id":False}):


                        attendence_date=datetime.strptime(i['date'],'%d/%m/%Y').date()
      
                        in_time=datetime.strptime(i['in_time'],"%H:%M")
                        out_time=datetime.strptime(i['out_time'],"%H:%M")
                        print(in_time.time())  

                        if(in_time.time() > admin_present_time ):
                              print("late")
                             # print(str(admin_present_time)[0:2])
                              #print(str(admin_present_time)[3:5])
                              #print(str(in_time.time())[0:2])
                              #print(str(in_time.time())[3:5])    

                              delayed_hr=int(str(in_time.time())[0:2]) - int(str(admin_present_time)[0:2])
                              delayed_min=int(str(in_time.time())[3:5]) - int(str(admin_present_time)[3:5])
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                              if(delayed_min>=15 or delayed_hr>=1):
                                  incharge_late_comers.append(j+"     "+i['in_time']+"     "+str(total_delay))
                                  
                              print("total Delay",total_delay)
                              print(type(i))
                              i.update({'delay':str(total_delay)})
                              print(i)
                              bc.append(i)
                              
                        if(out_time.time() > employee_out_time ):
                              print("overtime")
                             # print(str(admin_present_time)[0:2])
                              #print(str(admin_present_time)[3:5])
                              #print(str(in_time.time())[0:2])
                              #print(str(in_time.time())[3:5])    

                              delayed_hr=int(str(out_time.time())[0:2]) - int(str(employee_out_time)[0:2])
                              delayed_min=int(str(out_time.time())[3:5]) - int(str(employee_out_time)[3:5])
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                              incharge_overtime.append(j+"     "+i['out_time']+"     "+str(total_delay))                                 
                          #######################################################################################################
                          # to be continue
                        else:
                              i.update({'delay':"00:00:00"})
                              print("ab")
                              bc.append(i)          
       for department in client[j].details.find({},{"_id":False}):
          if(department['department']=='operators'):   
      
             for i in client[j].attendence.find({},{"_id":False}):


                        attendence_date=datetime.strptime(i['date'],'%d/%m/%Y').date()
      
                        in_time=datetime.strptime(i['in_time'],"%H:%M")
                        print(in_time.time())  

                        if(in_time.time() > admin_present_time ):
                              print("late")
                             # print(str(admin_present_time)[0:2])
                              #print(str(admin_present_time)[3:5])
                              #print(str(in_time.time())[0:2])
                              #print(str(in_time.time())[3:5])    

                              delayed_hr=int(str(in_time.time())[0:2]) - int(str(admin_present_time)[0:2])
                              delayed_min=int(str(in_time.time())[3:5]) - int(str(admin_present_time)[3:5])
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                              if(delayed_min>=15 or delayed_hr>=1):
                                  operator_late_comers.append(j+"     "+i['in_time']+"     "+str(total_delay))
                                  
                              print("total Delay",total_delay)
                              print(type(i))
                              i.update({'delay':str(total_delay)})
                              print(i)
                              bc.append(i)
                        if(out_time.time() > employee_out_time ):
                              print("overtime")
                             # print(str(admin_present_time)[0:2])
                              #print(str(admin_present_time)[3:5])
                              #print(str(in_time.time())[0:2])
                              #print(str(in_time.time())[3:5])    

                              delayed_hr=int(str(out_time.time())[0:2]) - int(str(employee_out_time)[0:2])
                              delayed_min=int(str(out_time.time())[3:5]) - int(str(employee_out_time)[3:5])
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                              operators_overtime.append(j+"     "+i['out_time']+"     "+str(total_delay))                                    
                          #######################################################################################################
                          # to be continue
                        else:
                              i.update({'delay':"00:00:00"})
                              print("ab")
                              bc.append(i)          
                              
       for department in client[j].details.find({},{"_id":False}):
          if(department['department']=='helpers'):   
      
             for i in client[j].attendence.find({},{"_id":False}):


                        attendence_date=datetime.strptime(i['date'],'%d/%m/%Y').date()
      
                        in_time=datetime.strptime(i['in_time'],"%H:%M")
                        print(in_time.time())  

                        if(in_time.time() > admin_present_time ):
                              print("late")
                             # print(str(admin_present_time)[0:2])
                              #print(str(admin_present_time)[3:5])
                              #print(str(in_time.time())[0:2])
                              #print(str(in_time.time())[3:5])    

                              delayed_hr=int(str(in_time.time())[0:2]) - int(str(admin_present_time)[0:2])
                              delayed_min=int(str(in_time.time())[3:5]) - int(str(admin_present_time)[3:5])
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                              if(delayed_min>=15 or delayed_hr>=1):
                                  helpers_late_comers.append(j+"     "+i['in_time']+"     "+str(total_delay))
                                  
                              print("total Delay",total_delay)
                              print(type(i))
                              i.update({'delay':str(total_delay)})
                              print(i)
                              bc.append(i)
                        if(out_time.time() > employee_out_time ):
                              print("overtime")
                             # print(str(admin_present_time)[0:2])
                              #print(str(admin_present_time)[3:5])
                              #print(str(in_time.time())[0:2])
                              #print(str(in_time.time())[3:5])    

                              delayed_hr=int(str(out_time.time())[0:2]) - int(str(employee_out_time)[0:2])
                              delayed_min=int(str(out_time.time())[3:5]) - int(str(employee_out_time)[3:5])
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                              helpers_overtime.append(j+"     "+i['out_time']+"     "+str(total_delay))                                    
                          # to be continue
                          #######################################################################################################
                        else:
                              i.update({'delay':"00:00:00"})
                              print("ab")
                              bc.append(i)          
          
          
          
          

                      
      print(admin_late_comers)
      print(operator_late_comers)
      print(incharge_late_comers)
      print(helpers_late_comers)
      print(supervisor_late_comers)
      print(incharge_overtime)
      return jsonify(bc) 


@app.route('/get_selected_employee_details',methods=['PUT'])
def get_selected_employee_details():
    
    
   # details = client[request.get_json()['employee_name']].attendence.find({'date':new_date})

    department = ''
    employee_name = ''
    sqt_value = '0'
    print(request.get_json())
   
    for j in client[request.get_json()['employee_name']].details.find({}):
            department =   j['department']+" "+j['position']
            employee_name =  j['FirstName'] + " " + j['LastName'].upper()
    if ( client[request.get_json()['employee_name']].monthly_sq_feet.find_one({"month":request.get_json()['month']+"_"+request.get_json()['year']})):
        print ("present")
        sqt_value =  client[request.get_json()['employee_name']].monthly_sq_feet.find_one({"month":request.get_json()['month']+"_"+request.get_json()['year']})['total_sq_feet'] 
 
   
    final_list = [{'department':department,'employee_name':employee_name+"  |  "+ sqt_value}]
  #  
    print(department, employee_name)
    print(request.get_json()['employee_name'])
    return jsonify(final_list)


@app.route('/save_square_feet_db',methods=['PUT'])
def save_square_feet_db():
    print (request.get_json())
    cli = mg ()
    if ( cli[request.get_json()['employee_name']].monthly_sq_feet.find_one({"month":request.get_json()['month']+"_"+request.get_json()['year']})):
        cli[request.get_json()['employee_name']].monthly_sq_feet.update({"month":request.get_json()['month']+"_"+request.get_json()['year']},{"$set":{'total_sq_feet':request.get_json()['sqtft']}})
        return "updated"
    else:
        sqtft =  {"_id": request.get_json()['month']+"_"+request.get_json()['year'],
           "month":request.get_json()['month']+"_"+request.get_json()['year'],
           "employee_name": request.get_json()['employee_name'],
            "total_sq_feet": request.get_json()['sqtft']
           }
        abcd = cli[sqtft['employee_name']].monthly_sq_feet
        print(sqtft)
        abcd.insert_one(sqtft)
        return "added" 


@app.route('/salary_list_download',methods=['PUT'])
def attendence_upload_location():
    print("download function called ")
    return "downloaded"    


@app.route('/department_post',methods=['GET'])
def department_post():
    global department_list_post
    department_list = []
    for i in department_list_post:
        department_list.append({'department':i})
    return jsonify(department_list)

@app.route('/update_ot_zero',methods=['PUT'])
def update_ot_zero():

    cli = mg ()

    all_name = cli.list_database_names()
    month = request.get_json()['month']+"_" + request.get_json()['year']

    for i in all_name:
        try:
            if (cli[i].details.find_one({'department':request.get_json()['department']})['department'] == request.get_json()['department']):
                cli[i].attendence.update_many({"month":month},{"$set" : {"overtime":0}})
                print(i)
        except:
            pass

    print(request.get_json())
    return "updated"



if __name__=="__main__":
  app.run(debug=True,host='0.0.0.0')

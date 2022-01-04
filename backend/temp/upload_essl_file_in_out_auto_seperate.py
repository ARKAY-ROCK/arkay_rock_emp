from pymongo import MongoClient
from bson.objectid import ObjectId
import csv
from datetime import datetime
import calendar

data_store = MongoClient()

all_employees=data_store.list_database_names()

months_list_post = ["january","february","march","april","may","june","july","august","september","october","november","december"]


def attendence_put(attendence):
    

      admin_present_time="8:30"
      admin_present_time_thres="7:45"
      admin_out_time = "17:30"

      admin_shut_in = "6:00"
      admin_shut_in_thres = "5:30"
      admin_shut_out= "14:00"
      admin_shut_thres = "7:00"
      
      main_cuting_present= "8:30"
      main_cuting_out= "17:30"
      
      bed_polish_present = "8:30"
      bed_polish_out = "17:30"


      mc_shift_basic = "10:00"
                        
      mc_shift_basic=datetime.strptime(mc_shift_basic,"%H:%M").time()      
      
      cleaning_present_time = "7:00"
      cleaning_out_time = "16:00"
      
      admin_prof_present_time = "9:30"
      admin_prof_out_time = "18:00"
      
      purchase_team_present_time = "10:30"
      purchase_team_out_time = "18:00"
      
      
      admin_present_time=datetime.strptime(admin_present_time,"%H:%M").time()
      admin_present_time_thres=datetime.strptime(admin_present_time_thres,"%H:%M").time()
      admin_out_time_diff =  datetime.strptime(admin_out_time,"%H:%M")
      admin_out_time_diff_shut =  datetime.strptime(admin_shut_out,"%H:%M")
      admin_out_time=datetime.strptime(admin_out_time,"%H:%M").time()

      admin_shut_in=datetime.strptime(admin_shut_in,"%H:%M").time()
      admin_shut_out=datetime.strptime(admin_shut_out,"%H:%M").time()
      admin_shut_thres=datetime.strptime(admin_shut_thres,"%H:%M").time()
      admin_shut_in_thres=datetime.strptime(admin_shut_in_thres,"%H:%M").time()
      
      
      
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

      mc_shift_one = "7:00"
                        
      mc_shift_one=datetime.strptime(mc_shift_one,"%H:%M").time()

                         
                         
      mc_shift_one_out = "15:00"
      mc_shift_one_out_diff = datetime.strptime(mc_shift_one_out,"%H:%M")
      mc_shift_one_out=datetime.strptime(mc_shift_one_out,"%H:%M").time()
                         
      mc_shift_one_thres = "7:45"
      mc_shift_one_thres=datetime.strptime(mc_shift_one_thres,"%H:%M").time()
                          
      mc_shift_two_in_thres = "14:15"
      mc_shift_two_in_thres=datetime.strptime(mc_shift_two_in_thres,"%H:%M").time()


      mc_shift_one_in_thres = "6:30"
      mc_shift_one_in_thres=datetime.strptime(mc_shift_one_in_thres,"%H:%M").time()                          
                          
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


      bp_shift_one = "6:00"
      bp_shift_one=datetime.strptime(bp_shift_one,"%H:%M").time()

      bp_shift_one_in_thres = "5:30"
      bp_shift_one_in_thres=datetime.strptime(bp_shift_one_in_thres,"%H:%M").time()
                         
      bp_shift_one_out = "14:00"
      bp_shift_one_out_diff = datetime.strptime(bp_shift_one_out,"%H:%M") 
      bp_shift_one_out=datetime.strptime(bp_shift_one_out,"%H:%M").time()
                         
      bp_shift_one_thres = "7:15"
      bp_shift_one_thres=datetime.strptime(bp_shift_one_thres,"%H:%M").time()
      bp_shift_two = "14:00"
      bp_shift_two=datetime.strptime(bp_shift_two,"%H:%M").time()

      bp_shift_two_in_thres = "13:00"
      bp_shift_two_in_thres=datetime.strptime(bp_shift_two_in_thres,"%H:%M").time()
                         
      bp_shift_two_out = "22:00"
      bp_shift_two_out_diff = datetime.strptime(bp_shift_two_out,"%H:%M")
      bp_shift_two_out=datetime.strptime(bp_shift_two_out,"%H:%M").time()
                         
      bp_shift_two_thres = "14:45"
      bp_shift_two_thres=datetime.strptime(bp_shift_two_thres,"%H:%M").time()      
      
     
      for department in data_store[attendence['employee_name']].details.find({},{"_id":False}):
       
          if(department['department']=='admin'  or  department['department']=='driver' or department['department']=='carving'  or department['department']=='electrical_maintanence' or department['department']=='mechanical_maintanence'  and department['position'] != 'contractor' ):   
                      
                        advance_minutes=0
                        
                        attendence_date=datetime.strptime(attendence['date'],'%d/%m/%Y').date()

                        #if ('in_time' in attendence):
                            
                        in_time=datetime.strptime(attendence['in_time'],"%H:%M")
                           
                        #if ('in_time' not in attendence):
                        #   attendence.update({'in_time':"08:30"}) 
                        #   in_time=datetime.strptime("08:30","%H:%M")

                        #if ('out_time' in attendence):
                            
                        out_time=datetime.strptime(attendence['out_time'],"%H:%M")
                           
                        #if ('out_time' not in attendence):
                        #   attendence.update({"out_time":"17:30"}) 
                        #   out_time=datetime.strptime("17:30","%H:%M")



                        if(in_time.time() >= bp_shift_two_in_thres  and in_time.time() < bp_shift_two_thres ):
                        
                              delayed_hr=abs(int(str(in_time.time())[0:2]) - int(str(bp_shift_two)[0:2]))
                              delayed_min=abs(int(str(in_time.time())[3:5]) - int(str(bp_shift_two)[3:5]))
                              if (delayed_hr == 1 and delayed_min <=30):
                                    delayed_hr = '00'
                                    #delayed_min = int(delayed_min) + 30

                              if (delayed_hr != 1 and delayed_min >30):
                                    print("not ddd")                              
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                            
                              total_hours=abs(int(str(out_time.time())[0:2])-int(str(in_time.time())[0:2]))
                              total_min=abs(int(str(out_time.time())[3:5])-int(str(in_time.time())[3:5]))
                            
                              print(total_hours,total_min)
                              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
                             
                              tw = out_time - in_time
                       
                              
                              total_hours_worked = str(total_hours_worked)
                              overtime = (tw.total_seconds()/60) - 480 
                          
                              if(overtime >= 60):
                                 ot=overtime/60
                              else:
                                ot=0   
                      
                   
                              
                              attendence.update({'total_hours':str(total_hours_worked)})
                              attendence.update({'overtime':ot})
                                                           
                              
                              
                                      
                              temp = bp_shift_two_out_diff - out_time
                              
                          

                              if(in_time.time() > bp_shift_two ):
                                    
                                        attendence.update({'delay':str(total_delay)})

                              if(in_time.time() <= bp_shift_two ):
                                        
                                         attendence.update({'delay':"00:00:00"})
                                  
                              if(out_time.time() < bp_shift_two_out ):
                                           
                                           attendence.update({'advance':str(temp.total_seconds()/60)})                            
                              if(out_time.time() >= bp_shift_two_out ):
                                          attendence.update({'advance':0})  
                                                                

               
                        
                        if(in_time.time() >= admin_shut_in_thres  and in_time.time() < admin_shut_thres ):
                             

                              delayed_hr=abs(int(str(in_time.time())[0:2]) - int(str(admin_shut_in)[0:2]))
                              delayed_min=abs(int(str(in_time.time())[3:5]) - int(str(admin_shut_in)[3:5]))
                              if (delayed_hr == 1 and delayed_min <=30):
                                    delayed_hr = '00'
                                    #delayed_min = int(delayed_min) + 30

                              if (delayed_hr != 1 and delayed_min >30):
                                    print("not ddd")
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                            
                              total_hours=abs(int(str(out_time.time())[0:2])-int(str(in_time.time())[0:2]))
                              total_min=abs(int(str(out_time.time())[3:5])-int(str(in_time.time())[3:5]))
                       
                              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
           

                              attendence.update({'total_hours':str(total_hours_worked)})
                              
                         
#####################################################################################################################################################                              
                              tw = out_time - in_time
                              
                      
                              
                              total_hours_worked = str(total_hours_worked)
                              overtime = (tw.total_seconds()/60) - 480 

                 
                              if(overtime >= 60):
                                 print("over time detected") 
                                 ot = overtime/60
                                 #ot = 0 
                              else:
                                ot=0   

                              
                             
                              attendence.update({'overtime':ot})
                              
##########################################################################################################################################################

                              
                              temp = admin_out_time_diff_shut - out_time
                              

       
                              if(out_time.time() < admin_shut_out ):
                                         
                                           attendence.update({'advance':int(temp.total_seconds()/60)})
                              
                              if(out_time.time() >= admin_shut_out ):

                                 attendence.update({'advance':0}) 
                                                         
                              
                              if (in_time.time() > admin_shut_in ):

                                  attendence.update({'delay':str(total_delay)})
                              
                              if (in_time.time() <= admin_shut_in):
                                  
                                  attendence.update({'delay':"00:00:00"})
                                  

       
                                          
                        if (in_time.time() >= admin_present_time_thres  and in_time.time() < mc_shift_basic):
                              
                              overtime = 0
                              delayed_hr=abs(int(str(in_time.time())[0:2]) - int(str(admin_present_time)[0:2]))
                              delayed_min=abs(int(str(in_time.time())[3:5]) - int(str(admin_present_time)[3:5]))

                              if (delayed_hr == 1 and delayed_min <=30):
                                    delayed_hr = '00'
                                    total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
   

                              if (delayed_hr == 1 and int(delayed_min) >30):
                                    delayed_hr = '00'
                                    total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min+30),"%H:%M").time()
                              
                                    
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                            
                              total_hours=abs(int(str(out_time.time())[0:2])-int(str(in_time.time())[0:2]))
                              total_min=abs(int(str(out_time.time())[3:5])-int(str(in_time.time())[3:5]))
              
                              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
                              

                              attendence.update({'total_hours':str(total_hours_worked)})
  
                              temp = admin_out_time_diff - out_time
                              

                              
                              if(out_time.time() < admin_out_time ):
                                     
                                           attendence.update({'advance':int(temp.total_seconds()/60)})
                              
                              if(out_time.time() >= admin_out_time ):

                                 attendence.update({'advance':0})

#####################################################################################################################################################                              
                              tw = out_time - in_time
                              
                    
                              
                              total_hours_worked = str(total_hours_worked)
                              overtime = (tw.total_seconds()/60) - 540 
                         
                              if(overtime >= 60):
                                 print("over time problem") 
                                 ot = overtime/60
                                 #ot = 0 
                              else:
                                ot=0   
                             
                              
                             
                              attendence.update({'overtime':ot})
                          
##########################################################################################################################################################                                  
                                                         
                              
                              if (in_time.time() > admin_present_time ):
                                  attendence.update({'delay':str(total_delay)})
                                 
                              
                              if (in_time.time() <= admin_present_time):
                                  attendence.update({'delay':"00:00:00"})



                                  
                                  
          if(department['department']=='main_cutting'):   
      

                         
             
         

                        
                       # attendence_date=datetime.strptime(i['date'],'%d/%m/%Y').date()
                        advance_minutes = 0 
                        attendence_date=datetime.strptime(attendence['date'],'%d/%m/%Y').date()
                        
                        in_time=datetime.strptime(attendence['in_time'],"%H:%M")
                    

                        #if ('out_time' in attendence):
                           
                        out_time=datetime.strptime(attendence['out_time'],"%H:%M")
            
                        #if ('out_time' not  in attendence):
                        
                        #   dem_time="0:00"
                        #   out_time=datetime.strptime(dem_time,"%H:%M")


                        if(in_time.time() >= bp_shift_two_in_thres  and in_time.time() < bp_shift_two_thres ):
                        
                              delayed_hr=abs(int(str(in_time.time())[0:2]) - int(str(bp_shift_two)[0:2]))
                              delayed_min=abs(int(str(in_time.time())[3:5]) - int(str(bp_shift_two)[3:5]))
                              if (delayed_hr == 1 and delayed_min <=30):
                                    delayed_hr = '00'
                                    #delayed_min = int(delayed_min) + 30

                              if (delayed_hr != 1 and delayed_min >30):
                                    print("not ddd")
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                            
                              total_hours=abs(int(str(out_time.time())[0:2])-int(str(in_time.time())[0:2]))
                              total_min=abs(int(str(out_time.time())[3:5])-int(str(in_time.time())[3:5]))
                            
                              print(total_hours,total_min)
                              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
                             
                              tw = out_time - in_time
                       
                              
                              total_hours_worked = str(total_hours_worked)
                              overtime = (tw.total_seconds()/60) - 480 
                          
                              if(overtime >= 60):
                                 ot=overtime/60
                              else:
                                ot=0   
                      
                   
                              
                              attendence.update({'total_hours':str(total_hours_worked)})
                              attendence.update({'overtime':ot})
                                                           
                              
                              
                                      
                              temp = bp_shift_two_out_diff - out_time
                              
                          

                              if(in_time.time() > bp_shift_two ):
                                    
                                        attendence.update({'delay':str(total_delay)})

                              if(in_time.time() <= bp_shift_two ):
                                        
                                         attendence.update({'delay':"00:00:00"})
                                  
                              if(out_time.time() < bp_shift_two_out ):
                                           
                                           attendence.update({'advance':str(temp.total_seconds()/60)})                            
                              if(out_time.time() >= bp_shift_two_out ):
                                          attendence.update({'advance':0})  
                                                                

          
                        if(in_time.time() >= mc_shift_one_in_thres  and in_time.time() < mc_shift_one_thres ):
                             
        
                              print("shift_one   ",attendence['employee_name'])   
                              delayed_hr=abs(int(str(in_time.time())[0:2]) - int(str(mc_shift_one)[0:2]))
                              delayed_min=abs(int(str(in_time.time())[3:5]) - int(str(mc_shift_one)[3:5]))
                              if (delayed_hr == 1 and delayed_min <=30):
                                    delayed_hr = '00'
                                    #delayed_min = int(delayed_min) + 30

                              if (delayed_hr != 1 and delayed_min >30):
                                    print("not ddd")
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                            
                              total_hours=abs(int(str(out_time.time())[0:2])-int(str(in_time.time())[0:2]))
                              total_min=abs(int(str(out_time.time())[3:5])-int(str(in_time.time())[3:5]))
                              
           
                              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
                             
                              tw = out_time - in_time
                              
                            
                              
                              total_hours_worked = str(total_hours_worked)
                              overtime = (tw.total_seconds()/60) - 480 
   
                              if(overtime >= 60):
                                 ot=overtime/60
                              else:
                                ot=0   
                    
                     
                              
                              attendence.update({'total_hours':str(total_hours_worked)})
                              attendence.update({'overtime':ot})
                         

                              
                              temp = mc_shift_one_out_diff - out_time
                              


                              if(in_time.time() > mc_shift_one ):
                                  print("delay adding")
                                  attendence.update({'delay':str(total_delay)})
                                  
                              if(in_time.time() <= mc_shift_one ):
                                  
                                  attendence.update({'delay':"00:00:00"})
                                  
                              if(out_time.time() < mc_shift_one_out ):

                                           attendence.update({'advance':int(temp.total_seconds()/60)})
                                           
                              if(out_time.time() >= mc_shift_one_out ):
                       
                                 attendence.update({'advance':0})

              
                                                         

                              
                        if(in_time.time() > mc_shift_two_in_thres  and in_time.time() < mc_shift_two_thres ):
                              
                              print("shift_two   ",attendence['employee_name']) 
                              total_delay = " "  
                              delayed_hr=abs(int(str(in_time.time())[0:2]) - int(str(mc_shift_two)[0:2]))
                              delayed_min=abs(int(str(in_time.time())[3:5]) - int(str(mc_shift_two)[3:5]))
                              if (delayed_hr == 1 and delayed_min <=30):
                                    delayed_hr = '00'
                                    #delayed_min = int(delayed_min) + 30

                              if (delayed_hr != 1 and delayed_min >30):
                                    print("not ddd")
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                            
                              total_hours=abs(int(str(out_time.time())[0:2])-int(str(in_time.time())[0:2]))
                              total_min=abs(int(str(out_time.time())[3:5])-int(str(in_time.time())[3:5]))
                            
             
                              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
          
                              tw = out_time - in_time
                              
           
 
                              total_hours_worked = str(total_hours_worked)
                              overtime = (tw.total_seconds()/60) - 480
                   
                              if(overtime >= 60):
                                 ot=overtime/60
                              else:
                                ot=0   
                       
            
                             
                              attendence.update({'total_hours':str(total_hours_worked)})
                              attendence.update({'overtime':ot})

                              
                              temp = mc_shift_two_out_diff - out_time
  


                              if(in_time.time() > mc_shift_two ):
                                  print("delay adding shift 2")
                                  attendence.update({'delay':str(total_delay)})
                                 
                              if(in_time.time() <= mc_shift_two ):
                                  print("delay problem")
                                  attendence.update({'delay':"00:00:00"})
                                 
                              if(out_time.time() < mc_shift_two_out ):
            
                                           attendence.update({'advance':int(temp.total_seconds()/60)})
                                           
                              if(out_time.time() >= mc_shift_two_out ):
                                 print(" no advance ") 
                                 attendence.update({'advance':0})
                                  
                    

                                                                                     
                        if(in_time.time() >= mc_shift_three  and in_time.time() < mc_shift_three_thres ):

                              print("shift_three   ",attendence['employee_name'])  
                              total_delay = " "
                              const = "23:59"
                              const=datetime.strptime(const,"%H:%M")
                              day_start = "23:59"
                              day_start=datetime.strptime(day_start,"%H:%M")
                                                            
                              delayed_hr=abs(int(str(in_time.time())[0:2]) - int(str(mc_shift_three)[0:2]))
                              delayed_min=abs(int(str(in_time.time())[3:5]) - int(str(mc_shift_three)[3:5]))
                              if (delayed_hr == 1 and delayed_min <=30):
                                    delayed_hr = '00'
                                    #delayed_min = int(delayed_min) + 30

                              if (delayed_hr != 1 and delayed_min >30):
                                    print("not ddd")
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                            
                              total_hours=abs(int(str(out_time.time())[0:2])-int(str(in_time.time())[0:2]))
                              total_min=abs(int(str(out_time.time())[3:5])-int(str(in_time.time())[3:5]))
                            
                           
                              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
                              attendence.update({'total_hours':str(total_hours_worked)})

                              
                              tw = const - in_time
 
                              
                              total_hours_worked = int( int(str(out_time.time())[0:2])*60 + int(str(out_time.time())[3:5])  + int(tw.total_seconds()/60) ) 
                              
                              overtime = total_hours_worked - 480
                              

                              
                              if(overtime >= 60):
                                 ot=overtime/60
                                 
                              else:
                                ot=0   

                                                            
                          
                              
                              
                              
                              attendence.update({'overtime':ot})

                              
                              temp = mc_shift_three_out_diff - out_time
                              

                              if(in_time.time() > mc_shift_three ):
                                  print("delay problem three")
                                  attendence.update({'delay':str(total_delay)})
                                 
                              if(in_time.time() <= mc_shift_three ):
                                  attendence.update({'delay':"00:00:00"})                              

                              if(out_time.time() < mc_shift_three_out ):
                                
                                           attendence.update({'advance':int(temp.total_seconds()/60)})
                              if(out_time.time() >= mc_shift_three_out ):
                                 
                                 attendence.update({'advance':0})
                                  

                        if(in_time.time() >= admin_present_time_thres  and in_time.time() < mc_shift_basic ):

                              print("shift_three   ",attendence['employee_name'])  
                              total_delay = " "
                              const = "23:59"
                              const=datetime.strptime(const,"%H:%M")
                              day_start = "23:59"
                              day_start=datetime.strptime(day_start,"%H:%M")
                                                            
                              delayed_hr=abs(int(str(in_time.time())[0:2]) - int(str(admin_present_time)[0:2]))
                              delayed_min=abs(int(str(in_time.time())[3:5]) - int(str(admin_present_time)[3:5]))
                              if (delayed_hr == 1 and delayed_min <=30):
                                    delayed_hr = '00'
                                    #delayed_min = int(delayed_min) + 30

                              if (delayed_hr != 1 and delayed_min >30):
                                    print("not ddd")
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                            
                              total_hours=abs(int(str(out_time.time())[0:2])-int(str(in_time.time())[0:2]))
                              total_min=abs(int(str(out_time.time())[3:5])-int(str(in_time.time())[3:5]))
                            
                           
                              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
                              

                              
                              tw = out_time - in_time
 
                              
                              
                              total_hours_worked = str(total_hours_worked)
                              
                              overtime = (tw.total_seconds()/60) - 480 
                              

                              
                              if(overtime >= 60):
                                 ot=overtime/60
                                 
                              else:
                                ot=0   

                                                            
                          
                              
                              
                              attendence.update({'total_hours':str(total_hours_worked)})
                              attendence.update({'overtime':ot})

                              
                              temp = admin_out_time_diff - out_time
                              #temp_delay = 
                              

                              if(in_time.time() > admin_present_time ):
                                  print("delay problem three")
                                  attendence.update({'delay':str(total_delay)})
                                 
                              if(in_time.time() <= admin_present_time ):
                                  attendence.update({'delay':"00:00:00"})                              

                              if(out_time.time() < admin_out_time ):
                                
                                           attendence.update({'advance':int(temp.total_seconds()/60)})
                              if(out_time.time() >= admin_out_time ):
                                 
                                 attendence.update({'advance':0})
                                  
                                                                                                                  
          if(department['department']=='bed_polish' or  department['department']=='edge_cutting' or department['department']=='drilling' or department['department']=='hand_polish' or department['department']=='dry_cutting' or department['department']=='packing'):   
            
                           
                        advance_minutes=0
                        
                        attendence_date=datetime.strptime(attendence['date'],'%d/%m/%Y').date()
                
                       
                        
                        #if ('in_time' in attendence):
                            
                        in_time=datetime.strptime(attendence['in_time'],"%H:%M")
                           
                        #if ('in_time' not in attendence):
                        #attendence.update({'in_time':"08:30"}) 
                        #   in_time=datetime.strptime("08:30","%H:%M")

                        #if ('out_time' in attendence):
                            
                        out_time=datetime.strptime(attendence['out_time'],"%H:%M")
                           
                        #if ('out_time' not in attendence):
                        #   attendence.update({"out_time":"17:30"}) 
                         #  out_time=datetime.strptime("17:30","%H:%M")

                           

                      

                        if(in_time.time() >= bp_shift_one  and in_time.time() < bp_shift_one_thres or in_time.time() <= bp_shift_one  ):

                              print("bed polish 6:00 to 14:00 shift",attendence['employee_name'])  
                              delayed_hr=abs(int(str(in_time.time())[0:2]) - int(str(bp_shift_one)[0:2]))
                              delayed_min=abs(int(str(in_time.time())[3:5]) - int(str(bp_shift_one)[3:5]))
                              
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                            
                              total_hours=abs(int(str(out_time.time())[0:2])-int(str(in_time.time())[0:2]))
                              total_min=abs(int(str(out_time.time())[3:5])-int(str(in_time.time())[3:5]))
                            
                              
                              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
                             
                              tw = out_time - in_time
                              
                       
                              
                              total_hours_worked = str(total_hours_worked)
                              overtime = (tw.total_seconds()/60) - 480 
                              
                  
                              
                              if(overtime >= 60):
                                 ot=overtime/60
                              else:
                                ot=0   
              
          
                                                            
                              
                              attendence.update({'total_hours':str(total_hours_worked)})
                              attendence.update({'overtime':ot})
             
                               
                              temp = bp_shift_one_out_diff - out_time
                              
                              

                              if (in_time.time() > bp_shift_one  ) :
                                  attendence.update({'delay':str(total_delay)})
                                 
                              if (in_time.time() <= bp_shift_one ):
                                  attendence.update({'delay':"00:00:00"})
                                 
                                  
                              if(out_time.time() < bp_shift_one_out ):
                                          
                                           attendence.update({'advance':str(temp.total_seconds()/60)})                            
                              if(out_time.time() >= bp_shift_one_out ):
                                 attendence.update({'advance':0})
                                                                                                                                         

                        if(in_time.time() >= bp_shift_two_in_thres  and in_time.time() < bp_shift_two_thres ):
                        
                              delayed_hr=abs(int(str(in_time.time())[0:2]) - int(str(bp_shift_two)[0:2]))
                              delayed_min=abs(int(str(in_time.time())[3:5]) - int(str(bp_shift_two)[3:5]))
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                            
                              total_hours=abs(int(str(out_time.time())[0:2])-int(str(in_time.time())[0:2]))
                              total_min=abs(int(str(out_time.time())[3:5])-int(str(in_time.time())[3:5]))
                            
                              print(total_hours,total_min)
                              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
                             
                              tw = out_time - in_time
                       
                              
                              total_hours_worked = str(total_hours_worked)
                              overtime = (tw.total_seconds()/60) - 480 
                          
                              if(overtime >= 60):
                                 ot=overtime/60
                              else:
                                ot=0   
                      
                   
                              
                              attendence.update({'total_hours':str(total_hours_worked)})
                              attendence.update({'overtime':ot})
                                                           
                              
                              
                                      
                              temp = bp_shift_two_out_diff - out_time
                              
                          

                              if(in_time.time() > bp_shift_two ):
                                    
                                        attendence.update({'delay':str(total_delay)})

                              if(in_time.time() <= bp_shift_two ):
                                        
                                         attendence.update({'delay':"00:00:00"})
                                  
                              if(out_time.time() < bp_shift_two_out ):
                                           
                                           attendence.update({'advance':str(temp.total_seconds()/60)})                            
                              if(out_time.time() >= bp_shift_two_out ):
                                          attendence.update({'advance':0})  
                                                                
                             

                        if(in_time.time() >= admin_present_time_thres  and in_time.time() < mc_shift_basic ):

                              print("bed polish normal   ",attendence['employee_name'])  
                              total_delay = " "
                              const = "23:59"
                              const=datetime.strptime(const,"%H:%M")
                              day_start = "23:59"
                              day_start=datetime.strptime(day_start,"%H:%M")
                                                            
                              delayed_hr=abs(int(str(in_time.time())[0:2]) - int(str(admin_present_time)[0:2]))
                              delayed_min=abs(int(str(in_time.time())[3:5]) - int(str(admin_present_time)[3:5]))
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                            
                              total_hours=abs(int(str(out_time.time())[0:2])-int(str(in_time.time())[0:2]))
                              total_min=abs(int(str(out_time.time())[3:5])-int(str(in_time.time())[3:5]))
                            
                           
                              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
                              
                              

                              
                              tw = out_time - in_time
 
                              
                              
                              total_hours_worked = str(total_hours_worked)
                              overtime = (tw.total_seconds()/60) - 540 
                              

                              
                              if(overtime >= 60):
                                 ot=overtime/60
                                 
                              else:
                                ot=0   

                                                            
                          
                              
                              
                              attendence.update({'total_hours':str(total_hours_worked)})
                              attendence.update({'overtime':ot})

                              
                              temp = admin_out_time_diff - out_time
                              

                              if(in_time.time() > admin_present_time ):
                                  print("delay problem three")
                                  attendence.update({'delay':str(total_delay)})
                                 
                              if(in_time.time() <= admin_present_time ):
                                  attendence.update({'delay':"00:00:00"})                              

                              if(out_time.time() < admin_out_time ):
                                
                                           attendence.update({'advance':int(temp.total_seconds()/60)})
                              if(out_time.time() >= admin_out_time ):
                                 
                                 attendence.update({'advance':0})



          if(department['department']=='cleaning'):
                
                              print("cleaning fi")      
                              advance_minutes=0
                              
                              attendence_date=datetime.strptime(attendence['date'],'%d/%m/%Y').date()
                      
                       
                        
                              if ('in_time' in attendence):
                                  
                                 in_time=datetime.strptime(attendence['in_time'],"%H:%M")
                                 
                              if ('in_time' not in attendence):
                                 attendence.update({'in_time':"08:30"}) 
                                 in_time=datetime.strptime("08:30","%H:%M")

                              if ('out_time' in attendence):
                                  
                                 out_time=datetime.strptime(attendence['out_time'],"%H:%M")
                                 
                              if ('out_time' not in attendence):
                                 attendence.update({"out_time":"17:30"}) 
                                 out_time=datetime.strptime("17:30","%H:%M")
        

                              delayed_hr=abs(int(str(in_time.time())[0:2]) - int(str(cleaning_present_time)[0:2]))
                              delayed_min=abs(int(str(in_time.time())[3:5]) - int(str(cleaning_present_time)[3:5]))
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                            
                              total_hours=abs(int(str(out_time.time())[0:2])-int(str(in_time.time())[0:2]))
                              total_min=abs(int(str(out_time.time())[3:5])-int(str(in_time.time())[3:5]))
                              
                              print(total_hours,total_min)
                              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
                             
                              tw = out_time - in_time
                              
                            
                              
                              total_hours_worked = str(total_hours_worked)
                              overtime = (tw.total_seconds()/60) - 480 
                           
                              if(overtime >= 60):
                                 ot=overtime/60
                                 
                              else:
                                ot=0   
                                
                              attendence.update({'total_hours':str(total_hours_worked)})
                              attendence.update({'overtime':ot})

                         
                              
                              temp = cleaning_out_time_diff - out_time
                              
                             

                              if(out_time.time() < cleaning_out_time ):
                                          
                                           attendence.update({'advance':str(temp.total_seconds()/60)})                            
                              if(out_time.time() >= cleaning_out_time ):
                                 
                                           attendence.update({'advance':0})
                         
                              if (in_time.time() > cleaning_present_time ):
                                  attendence.update({'delay':str(total_delay)})
                                  
                              if (in_time.time() <= cleaning_present_time):
                                  attendence.update({'delay':"00:00:00"})
                                                                
                                                                                          

          if(department['department']=='office_boy'):
                
                              print("office boy ")      
                              advance_minutes=0
                              
                              attendence_date=datetime.strptime(attendence['date'],'%d/%m/%Y').date()
                      
                       
                        
                              if ('in_time' in attendence):
                                  
                                 in_time=datetime.strptime(attendence['in_time'],"%H:%M")
                                 
                              if ('in_time' not in attendence):
                                 attendence.update({'in_time':"08:30"}) 
                                 in_time=datetime.strptime("08:30","%H:%M")

                              if ('out_time' in attendence):
                                  
                                 out_time=datetime.strptime(attendence['out_time'],"%H:%M")
                                 
                              if ('out_time' not in attendence):
                                 attendence.update({"out_time":"17:30"}) 
                                 out_time=datetime.strptime("17:30","%H:%M")
        

                              delayed_hr=abs(int(str(in_time.time())[0:2]) - int(str(cleaning_present_time)[0:2]))
                              delayed_min=abs(int(str(in_time.time())[3:5]) - int(str(cleaning_present_time)[3:5]))
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                            
                              total_hours=abs(int(str(out_time.time())[0:2])-int(str(in_time.time())[0:2]))
                              total_min=abs(int(str(out_time.time())[3:5])-int(str(in_time.time())[3:5]))
                              
                              print(total_hours,total_min)
                              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
                             
                              tw = out_time - in_time
                              
                            
                              
                              total_hours_worked = str(total_hours_worked)
                              overtime = (tw.total_seconds()/60) - 480 
                           
                              if(overtime >= 60):
                                 ot=overtime/60
                                 
                              else:
                                ot=0   
                              attendence.update({'total_hours':str(total_hours_worked)})
                             
                              
                              attendence.update({'overtime':ot})

                         
                              
                              temp = cleaning_out_time_diff - out_time
                              
                             

                              if(out_time.time() < cleaning_out_time ):
                                          
                                           attendence.update({'advance':str(temp.total_seconds()/60)})                            
                              if(out_time.time() >= cleaning_out_time ):
                                 
                                           attendence.update({'advance':0})
                         
                              if (in_time.time() > cleaning_present_time ):
                                   #attendence.update({'delay':"00:00:00"}) 
                                  attendence.update({'delay':str(total_delay)})
                                  
                              if (in_time.time() <= cleaning_present_time):
                                  attendence.update({'delay':"00:00:00"})
                                                                
                                                                               
          if(department['department']=='admin_prof'):
                
                              print("admin_prof")      
                              advance_minutes=0
                              
                              attendence_date=datetime.strptime(attendence['date'],'%d/%m/%Y').date()
                      
                       
                        
                              if ('in_time' in attendence):
                                  
                                 in_time=datetime.strptime(attendence['in_time'],"%H:%M")
                                 
                              if ('in_time' not in attendence):
                                 attendence.update({'in_time':"08:30"}) 
                                 in_time=datetime.strptime("08:30","%H:%M")

                              if ('out_time' in attendence):
                                  
                                 out_time=datetime.strptime(attendence['out_time'],"%H:%M")
                                 
                              if ('out_time' not in attendence):
                                 attendence.update({"out_time":"17:30"}) 
                                 out_time=datetime.strptime("17:30","%H:%M")
        

                              delayed_hr=abs(int(str(in_time.time())[0:2]) - int(str(admin_prof_present_time)[0:2]))
                              delayed_min=abs(int(str(in_time.time())[3:5]) - int(str(admin_prof_present_time)[3:5]))
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                            
                              total_hours=abs(int(str(out_time.time())[0:2])-int(str(in_time.time())[0:2]))
                              total_min=abs(int(str(out_time.time())[3:5])-int(str(in_time.time())[3:5]))
                              
                              print(total_hours,total_min)
                              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
                             
                              tw = out_time - in_time
                              
                            
                              
                              total_hours_worked = str(total_hours_worked)
                              overtime = (tw.total_seconds()/60) - 480 
                           
                              if(overtime >= 60):
                                 ot=overtime/60
                                 
                              else:
                                ot=0   
                              attendence.update({'total_hours':str(total_hours_worked)})
                              attendence.update({'overtime':ot})

                         
                              
                              temp = admin_prof_out_time_diff - out_time
                              
                             

                              if(out_time.time() < admin_prof_out_time ):
                                          
                                           attendence.update({'advance':str(temp.total_seconds()/60)})                            
                              if(out_time.time() >= admin_prof_out_time ):
                                 
                                           attendence.update({'advance':0})
                         
                              if (in_time.time() > admin_prof_present_time ):
                                  attendence.update({'delay':str(total_delay)})
                                  
                              if (in_time.time() <= admin_prof_present_time):
                                  attendence.update({'delay':"00:00:00"})
                                                                

          if(department['department']=='purchase_team'):
                
                              print("purchase team")      
                              advance_minutes=0
                              
                              attendence_date=datetime.strptime(attendence['date'],'%d/%m/%Y').date()
                      
                       
                        
                              if ('in_time' in attendence):
                                  
                                 in_time=datetime.strptime(attendence['in_time'],"%H:%M")
                                 
                              if ('in_time' not in attendence):
                                 attendence.update({'in_time':"08:30"}) 

                                 in_time=datetime.strptime("08:30","%H:%M")

                              if ('out_time' in attendence):
                                  
                                 out_time=datetime.strptime(attendence['out_time'],"%H:%M")
                                 
                              if ('out_time' not in attendence):
                                 attendence.update({"out_time":"17:30"})
                                 
                                 out_time=datetime.strptime("17:30","%H:%M")
        

                              delayed_hr=abs(int(str(in_time.time())[0:2]) - int(str(purchase_team_present_time)[0:2]))
                              delayed_min=abs(int(str(in_time.time())[3:5]) - int(str(purchase_team_present_time)[3:5]))
                              total_delay=datetime.strptime(str(delayed_hr)+":"+str(delayed_min),"%H:%M").time()
                            
                              total_hours=abs(int(str(out_time.time())[0:2])-int(str(in_time.time())[0:2]))
                              total_min=abs(int(str(out_time.time())[3:5])-int(str(in_time.time())[3:5]))
                              
                              print(total_hours,total_min)
                              
                              total_hours_worked=datetime.strptime(str(total_hours)+":"+str(total_min),"%H:%M").time()
                             
                              tw = out_time - in_time
                              
                            
                              
                              total_hours_worked = str(total_hours_worked)
                              overtime = (tw.total_seconds()/60) - 480 
                           
                              if(overtime >= 60):
                                 ot=overtime/60
                                 
                              else:
                                ot=0   
                              attendence.update({'total_hours':str(total_hours_worked)})
                              attendence.update({'overtime':ot})

                         
                              
                              temp = purchase_team_out_time_diff - out_time
                              
                              
                              print(attendence['employee_name'])
                              if(out_time.time() < purchase_team_out_time ):
                                           if (attendence['employee_name'] =='Kamaraj_1001'):
                                                 attendence.update({'advance':0})
                                           if (attendence['employee_name'] !='Kamaraj_1001'):
                                                 
                                                attendence.update({'advance':str(temp.total_seconds()/60)})                            
                              if(out_time.time() >= purchase_team_out_time ):
                                 
                                           attendence.update({'advance':0})
                         
                              if (in_time.time() > purchase_team_present_time ):
                                         if (attendence['employee_name'] =='Kamaraj_1001'):
                                               attendence.update({'delay':"00:00:00"})
                                         if (attendence['employee_name'] !='Kamaraj_1001'):
                                               attendence.update({'delay':str(total_delay)})
                                  
                              if (in_time.time() <= purchase_team_present_time):
                              
                                  attendence.update({'delay':"00:00:00"})                                                                               
                              
                              


                              
      #for department in data_store[attendence['employee_name']].details.find({},{"_id":False}): 
      #   if(department['department']=='admin' or department['department']=='admin_prof' or department['department']=='bed_polish' or  department['department']=='edge_cutting' or department['department']=='drilling' or department['department']=='hand_polish' or department['department']=='dry_cutting' or department['department']=='packing' or department['department']=='main_cutting' or department['department']=='driver' or department['department']=='carving'  or department['department']=='electrical_maintanence' or department['department']=='mechanical_maintanence'  and department['position'] != 'contractor' ):
      #data_store[attendence['employee_name']].attendence.find_one_and_delete({"_id":"27/09/2020"})
     # data_store[attendence['employee_name']].attendence.insert_one(attendence)
     
      #no_intime(attendence)
      db_store(attendence)

         
def no_intime(attendence):
      if ('in_time'  in attendence and 'out_time'  in attendence):
                  month = months_list_post[int(attendence['date'][3:5])-1] +"_"+ str(attendence['date'][-4:])
                  attendence.update({'month':month})
                  print(month)
           #if (attendence['total_hours'] == '0' ):
           #      print(attendence)
                  print(attendence)
           
def db_store(attendence):
     data_store[attendence['employee_name']].attendence.find_one_and_delete({"_id":attendence['date']}) 
     if ('in_time'  in attendence and 'out_time'  in attendence):
            month = months_list_post[int(attendence['date'][3:5])-1] +"_"+ str(attendence['date'][-4:])
            attendence.update({'month':month})      
            print("")
            if(1==1):
           # if(attendence['employee_name'] =='gowtham_74' or attendence['employee_name'] =='palraj_75' ):      
               print(attendence['total_hours'],"    ",attendence['date'][:2],"  ",attendence['date'][3:5])
               sun = find_sunday(attendence['date'][-4:],attendence['date'][3:5])
               if (int(attendence['date'][:2]) in sun ):
                     total_hours=abs(int(attendence['out_time'][0:2])-int(attendence['in_time'][0:2]))
                     total_min=abs(int(attendence['out_time'][3:5])-int(attendence['in_time'][3:5]))
                     attendence.update({'overtime':str(total_hours)+"."+str(total_min)})
                     print(attendence)
                     data_store[attendence['employee_name']].attendence.insert_one(attendence)

               if (int(attendence['date'][:2]) not  in sun ): 
                   print("deleted")     
                   data_store[attendence['employee_name']].attendence.insert_one(attendence)
            if(1==2):
                  print("")


def db_store_gp(attendence):
   
     if ('in_time'  in attendence and 'out_time'  in attendence):
            month = months_list_post[int(attendence['date'][3:5])-1] +"_"+ str(attendence['date'][-4:])
            attendence.update({'month':month})      
            print("")
            #if(1==1):
            if(attendence['employee_name'] =='palraj_75'):      
               print(attendence['total_hours'],"    ",attendence['date'][:2],"  ",attendence['date'][3:5])
               print("only                       ggpp                                                                  :     attendence added ", attendence['employee_name'])
               sun = find_sunday(attendence['date'][-4:],attendence['date'][3:5])
               if (int(attendence['date'][:2]) in sun ):
                     total_hours=abs(int(attendence['out_time'][0:2])-int(attendence['in_time'][0:2]))
                     total_min=abs(int(attendence['out_time'][3:5])-int(attendence['in_time'][3:5]))
                     attendence.update({'overtime':str(total_hours)+"."+str(total_min)})
                     print(attendence)
                     data_store[attendence['employee_name']].attendence.insert_one(attendence)

               if (int(attendence['date'][:2]) not  in sun ):      
                   data_store[attendence['employee_name']].attendence.insert_one(attendence)
                   print( attendence )
            if(1==2):
                  print("")



data_store = MongoClient()

def night_attendences(attendence):
      
     # print(attendence)
     try :
      if (data_store[attendence['employee_name']].details.find_one({'EmployeeCode':attendence['employee_id']})['position'] != 'contractor'):
       if ('in_time' in  attendence):
            print("   in time  :  ",attendence['in_time'] ,"  ",attendence['date'], "   ", attendence['employee_id'] )
            try:
               emp_dep = data_store[attendence['employee_name']].details.find_one({'EmployeeCode':attendence['employee_id']})['department']
               print(emp_dep)
            except:
                  pass 
       if ('out_time' in  attendence):
            print("   out time  :  ",attendence['out_time'],"   ",attendence['date'] , attendence['employee_id'] )
            try:
               emp_dep = data_store[attendence['employee_name']].details.find_one({'EmployeeCode':attendence['employee_id']})['department']
               print(emp_dep)
            except:
                  pass
     except :
           print(['employee_name'])



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


def night_attendence(attendence):
      # print(attendence['employee_name'],"    ",attendence['employee_id'])
       emp_dep = data_store[attendence['employee_name']].details.find_one({'EmployeeCode':int(attendence['employee_id'])})

       if (emp_dep is  None ):
             emp_dep = data_store[attendence['employee_name']].details.find_one({'EmployeeCode':attendence['employee_id']})
       
       if (emp_dep['position'] != 'contractor'):
             
             if ('in_time' in attendence):
                    print(attendence['employee_name'], "   ", emp_dep['department'], "   ", attendence['in_time'])
             if ('out_time' in attendence):
                     print(attendence['employee_name'], "   ", emp_dep['department'], "   ",attendence['out_time'])
             
data_store = MongoClient()

employee_attendence_data=[]

emp_week = [i.strip().split() for i in open("june_2021.dat").readlines()]

emp_data=[]

################################################################################## DATE SELECTION ##################################################

################################################################################## DATE SELECTION ##################################################

def attendence_process(emp_data):
 #  print("function " , emp_data)
   all_employees = data_store.list_database_names()

   in_time=[]
   out_time =[]
   for i in all_employees:
      
      if(i!='admin' and i!='config' and i!='local' and i!='loginuser' and i!='esi_epf_shares'):
         
         emp_name=i
         com_pos=i.find("_")
         i=i[com_pos+1:]

         employee_attendence_data.clear()
         
         for employee in emp_data:
               
               if (i == employee[0]):
                  employee_attendence_data.append(employee)

         if(employee_attendence_data):
            
            date_format=employee_attendence_data[0][1][8:]+"/"+employee_attendence_data[0][1][5:7]+"/"+employee_attendence_data[0][1][0:4]
            attendence = {}
            attendence= {'_id':date_format,'employee_id':employee_attendence_data[0][0],'date':date_format}

            for day_data in employee_attendence_data:
            
               if(day_data[4]==str(0)):

                  tw_form=datetime.strptime(day_data[2][:5],"%H:%M")

                  tw_form=tw_form.strftime("%I:%M &p")

                  if('in_time' in attendence):
                        attendence.update({'out_time':day_data[2][:5]})
                           

                  if('in_time' not in attendence):
                        in_time.append(emp_name)
                        
                        attendence.update({'in_time':day_data[2][:5]})

                     
               if(day_data[4]==str(1)):

                  tw_form=datetime.strptime(day_data[2][:5],"%H:%M")
                  tw_form=tw_form.strftime("%I:%M &p")

                  if ('out_time' in attendence):
                     if ('in_time' in attendence):
                        attendence.update({'out_time':day_data[2][:5]})
                     if ('in_time' not in attendence):
                           attendence.update({'in_time':attendence['out_time']})
                           attendence.update({'out_time':day_data[2][:5]})
                  if ('out_time' not in attendence):
                     attendence.update({'out_time':day_data[2][:5]})
               
                  
                  

               if(day_data[4]==str(4)):

                  tw_form=datetime.strptime(day_data[2][:5],"%H:%M")
                  tw_form=tw_form.strftime("%I:%M &p")

                  # print(emp_name,"     ","overin_time","     ",tw_form[:5])
                  attendence.update({'overin_time':day_data[2][:5]})

               if(day_data[4]==str(5)):

                  tw_form=datetime.strptime(day_data[2][:5],"%H:%M")
                  tw_form=tw_form.strftime("%I:%M &p")
      
                  # print(emp_name,"     ","overoutin_time","     ",tw_form[:5])
                  attendence.update({'overout_time':day_data[2][:5]})

            if(data_store[emp_name].attendence.find_one({"_id":attendence['_id']})):

               attendence.update({'employee_name':emp_name})
               attendence.update({'status':'present'})

            

               
            
            attendence.update({'delay':'0'})
            attendence.update({'advance':'0'})
            attendence.update({'overtime':'0'})
            attendence.update({'total_hours':'0'})
            attendence.update({'employee_name':emp_name})
            attendence.update({'status':'present'})
               
               #data_store[emp_name].attendence.insert_one(attendence)

            # attendence_put(attendence)
            # no_intime(attendence)
            if ('in_time' not in attendence and 'out_time' in attendence ):
                  attendence.update({'in_time':'08:30'})
                  attendence.update({'out_time':'17:30'})
            #       print(attendence)
            if ('out_time' not in attendence and 'in_time' in attendence):
                  attendence.update({'out_time':'17:30'})
                  attendence.update({'in_time':'08:30'})
            #       print(attendence)
                  
            if ('in_time' in attendence  and 'out_time' in attendence):
               
               att_in_time = attendence['in_time']
               temp_in  = attendence['in_time']
               temp_out = attendence['out_time']
               att_in_time=datetime.strptime(att_in_time,"%H:%M").time()
         
               att_out_time=datetime.strptime(attendence['out_time'],"%H:%M")
      
               if  (att_in_time > att_out_time.time() ):
                     attendence.update({'in_time':temp_out})
                     attendence.update({'out_time':temp_in})
                  




   
               attendence_put(attendence)
              # print(attendence)
               
               #no_intime(attendence)

            if ('in_time' in attendence  and 'out_time' not  in attendence):

                        night_attendence(attendence)


            if ('in_time' not in attendence  and 'out_time' in attendence):

                        night_attendence(attendence)

def main_method (file_loco):
   global emp_week
#   location = "C:/Users/marp/Desktop/Attendance_files/" + file_name
#   print(location)
   emp_week = [i.strip().split() for i in open(file_loco).readlines()]
   for i in emp_week:
   # print(i)
      emp_data = [] 
      for j in range(1,32,1):
         emp_data = [] 
         if (len(str(j))==1):
            j = '0'+str(j)  
         date_man = '2021-'+'06-'+str(j)
   #  print(date_man)
         if(i[1]== date_man):
            emp_data.append(i)
         if (emp_data):
      #  print(emp_data)
            attendence_process(emp_data)


#main_method('june_2021.dat')




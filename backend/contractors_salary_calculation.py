from pymongo import MongoClient as mg

db_cli = mg()


class ContractorSalaryCal:
    def __init__(self, emp_name=None, department=None, month_year=None):
        self.emp_name = emp_name
        self.department = department
        self.month_year = month_year

    def contractor_salary(self):
        print(self.emp_name)
        emp_sq = int(db_cli[self.emp_name].monthly_sq_feet.find_one(
            {'month': self.month_year})['total_sq_feet'])
        sqt_variable_cost = db_cli.contractors.sqt_cost.find_one({})
        department_var_cost = sqt_variable_cost[self.department]

        var_sq = department_var_cost.split("-")[0].split(",")

        if len(var_sq) <=1 :
            
            salary = emp_sq * float (department_var_cost)
            return salary 


        var_cost = department_var_cost.split("-")[1].split(",")


        salary = 0
        remaining = 0

        print(var_sq, "  ", var_cost)
       
        differ_in_sq =[int(var_sq[0])]

        for i in range(0,len(var_sq)-1):
            
            differ_in_sq.append(int(var_sq[i+1]) - int(var_sq[i]))
        
        print(differ_in_sq)
        if (emp_sq <= differ_in_sq[0]):
            salary = emp_sq * float(var_cost[0])
            return  salary
        
        if (emp_sq >= differ_in_sq[0]):
            remaining = emp_sq - differ_in_sq[0]
            salary = differ_in_sq[0] * float(var_cost[0])

            for i in range (0,len(differ_in_sq)-1):
                if (remaining >= differ_in_sq[i+1]):
                    salary = salary + ( differ_in_sq[i+1] * float(var_cost[i+1]))
                    remaining = remaining - differ_in_sq[i+1]
                if (remaining <= differ_in_sq[i+1]):
                    salary = salary + (remaining * float (var_cost[i+1]))
    
            return salary


        return salary


get_co = ContractorSalaryCal(
    emp_name='firstone_001', month_year='december_2021', department='bed_polish').contractor_salary()

print(get_co)

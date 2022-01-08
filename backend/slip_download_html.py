

class SlipDownloadHtml:
    def __init__(self, rep=None):
        self.rep = rep

    def replace_html(self):
        with open('salary_slip.html', 'r') as file:
            filedata = file.read()

    
        rep_all = {
            'emp_id': self.rep['employee_id'],
            'emp_name': self.rep['employee_name'],
            'emp_bank': self.rep['employee_bank'],
            'emp_act': self.rep['employee_account'],
            'emp_pf_num': self.rep['employee_pf_no'],
            'emp_tot': int(self.rep['present_days']) + int(self.rep['absent_days']),
            'emp_work': self.rep['present_days'],
            'emp_depar': self.rep['employee_dep'],
            'emp_design': self.rep['employee_design'],
            'emp_basic': self.rep['emp_basic'],
            'emp_pf': self.rep['emp_pf'],
            'emp_hra': self.rep['emp_hr'],
            'emp_wl': self.rep['emp_wl'],
            'emp_esi':self.rep['emp_esi'],
            'emp_con': self.rep['conveyance'],
            'emp_net' : self.rep['emp_net'],
            'emp_det': self.rep['emp_det'],
            'emp_fin' : self.rep['emp_fin'],
            'emp_month':self.rep['emp_month'],
            'emp_year' : self.rep['emp_year']
        }

        for i in rep_all:
            filedata = filedata.replace(i,str(rep_all[i]))

        with open('salary_slip_temp.html', 'w') as file:
            file.write(filedata)

        #print(filedata)    

        return filedata


# SlipDownloadHtml().replace_html()

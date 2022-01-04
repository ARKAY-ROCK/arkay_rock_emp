from flask.helpers import total_seconds
from pymongo import MongoClient as mg

db_con = mg()

table = db_con['esi_epf_shares']['esi_epf']
# documents = table['month_year'


field = {
    'FirstName': 'gowthaman s',
    'MiddleName': 'id_name',
    'month': 'month',
    'basic slary': '1000',
    'gross salary': '500'
}

att = {
    "_id": "02/12/2021",
    "status": "present",
    "total_hours": "04:03:00",
    "month": "december_2021",
    "employee_name": "firstone_001",
    "in_time": "06:00",
    "out_time": "02:05",
    "delay": "0",
    "advance": "0",
    "overtime": "0"
}

esi_details = {

    "bed_polish": "12.5",
    "hand_polish": "12.5",
    "dry_cutting": "12.5",

}


esi_details = {

    "basic_pay":  'basicpay',
    "wl_allowence":  'wlallowence',
    "hra":  'hra',
    "conveyence":  'conveyence',
    "esi_employeer_share":  'esiemployeershare',
    "esi_employee_share":  'esiemployeeshare',
    "epf_employee_share":  'epfemployeeshare',
    "epf_employeer_pension":  'epfemployeerpension',
    "epf_employeer_epf":  'epfemployeershare',


}

salary_slip = {

    "basic_pay":  'basicpay',
    "wl_allowence":  'wlallowence',
    "hra":  'hra',
    "conveyence":  'conveyence',
    "esi_employeer_share":  'esiemployeershare',
    "esi_employee_share":  'esiemployeeshare',
    "epf_employee_share":  'epfemployeeshare',
    "epf_employeer_pension":  'epfemployeerpension',
    "epf_employeer_epf":  'epfemployeershare',


}

salary_history = {
    
}

# documents.delete_many({'employee_name':'id_name'})

table.insert_one(esi_details)

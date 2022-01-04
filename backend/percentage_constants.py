from re import escape
from pymongo import MongoClient as mg

db_cli = mg()


class PercentageConstant:
    def __init__(self, req=None):
        self.req = req

    def get_esi_epf_percent(self):
        esi_epf = {}
        db_path = db_cli.esi_epf_shares.esi_epf.find({}, {"_id": False})
        for i in db_path:
            esi_epf.update(i)

        return esi_epf

    def get_contractor_percent(self):
        cont_per = {}
        db_path = db_cli.contractors.sqt_cost.find({}, {"_id": False})
        for i in db_path:
            cont_per.update(i)
        return cont_per

    def edit_esi_epf_per(self):
        print(self.req)

        db_cli.esi_epf_shares.esi_epf.drop()
        db_path = db_cli.esi_epf_shares.esi_epf
        esi_details = {

            "basic_pay":  self.req['basicpay'],
            "wl_allowence":  self.req['wlallowence'],
            "hra":  self.req['hra'],
            "conveyence":  self.req['conveyence'],
            "esi_employeer_share":  self.req['esiemployeershare'],
            "esi_employee_share":  self.req['esiemployeeshare'],
            "epf_employee_share":  self.req['epfemployeeshare'],
            "epf_employeer_pension":  self.req['epfemployeerpension'],
            "epf_employeer_epf":  self.req['epfemployeershare'],
        }
        db_path.insert_one(esi_details)
        return "updated"

    def edit_sqt_per(self):
        db_cli.contractors.sqt_cost.drop()
        db_path = db_cli.contractors.sqt_cost
        sql_cost_update = {

            "bed_polish":  self.req['bedpolish'],
            "hand_polish":  self.req['handpolish'],
            "dry_cutting":  self.req['drycutting'],
        }

        db_path.insert_one(sql_cost_update)

        return "updated"

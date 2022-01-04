class convert_mon_list:
    def __init__ (self,mongo_obj):
        self.mongo_obj = mongo_obj
        self.mongo_list = []
    def convert_to_list(self):
        for i in self.mongo_obj:
            self.mongo_list.append(i)
        return self.mongo_list
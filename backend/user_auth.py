from pymongo import MongoClient as mg
from flask_jwt_extended import  create_access_token ,JWTManager
from flask import jsonify, Flask

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)
db_con = mg()
user_auth = db_con['users']['users']

class user_authentication:
    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password
    
    def user_login(self):
        with app.app_context():
            Account = ""
            result = ""
            user_role = ""
            user_info = user_auth.find_one({"user_name":self.user_name})
            print(user_info)
            if (user_info['user_name']):
                if(self.password == user_info['password']):
                    user_role = user_info['user_role']
                    if (user_info['role'] == 'admin'):
                        Account = 1
                    if (user_info['role'] == 'user'):
                        Account = 2
                
                    access_token = create_access_token(identity={'role':user_info['role'].upper(),'show_role':user_info['show_role'].upper(),'user_name':user_info['user_name'].upper(),'Account':Account,'role':user_role})
                   
                    result = jsonify({"token": access_token})
                else:
                    result = jsonify({"result": "Invalid Email/Password"})
            else:
                result = jsonify({"result": "Invalid Email/Password"})

            print(result)
            return result   

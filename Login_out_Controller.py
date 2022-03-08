from xml.dom.pulldom import parseString

from Login_GUI import LogInGUI
from SignUp_GUI import SignupGUI
from Dashboard_Controller import DashboardController
from Pop_up_gui import PopUpGUI
from user import User
from Learnset import Learnset
import sys
 
class LoginOutController():
    def __init__(self, GGA_DB):
        self.database_manager = GGA_DB
        #self.login_gui = LoginGUI()
        #self.signup = SignupGUI()
        #self.popup = PopUpGUI()
        pass
    
    #Functions SignUp
    def create_sign_up_gui(self): 
        self.signup = SignupGUI()
        self.signup.createMainFrame()
        
    def write_new_user_to_database(self):
        pass   
    
    def check_username_taken(self):
        pass
    

    #Functions login 
       
    def create_login_gui(self):
        self.login_gui = LogInGUI(self)

    def handle_login_request(self, username, password):
        print(username, password)
        userid = self.validate_username_password(username, password)
        if userid>0:  #existing user
            #self.login_gui.handle_close_window()
            self.get_user_data_from_database(username, password)
            self.create_user_object()
        else: 
            favorites_learnset = Learnset()
            User(userid, username, password, )
        self.create_dashboard_controller()
            
    def validate_username_password(self, username, password):
        userid_out = self.database_manager.return_user_id(username, password)
        if userid_out == []:
            return -1
        else: return userid_out[0][0]
        

    
    #Dashboard
    def create_dashboard_controller(self):
        pass
    
    #Logout
    def logout_push_changes_to_database(self): 
        pass 
    
    #delete Account
    def delete_account(self):
        pass
    
    def close_app(self):
        print("Close App.")
        #close DB

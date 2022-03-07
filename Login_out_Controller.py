from xml.dom.pulldom import parseString

from Login_GUI import LogInGUI
from SignUp_GUI import SignupGUI
from Dashboard_Controller import DashboardController
from Pop_up_gui import PopUpGUI
from user import User
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
        if self.validate_username_password(username, password):
            self.login_gui.handle_close_window()
            self.get_user_data_from_database(username, password)
            self.create_user_object()
            self.create_dashboard_controller()
            
    def validate_username_password(self):
        pass
    
    def get_user_data_from_database(self):
        pass
    
        def create_user_object(self):
            pass
    
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

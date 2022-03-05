from xml.dom.pulldom import parseString
from Database_Manager import Database_Manager
from Login_GUI import LoginGUI
from SignUp_GUI import SignupGUI
from Dashboard_Controller import DashboardController
from Pop_up_gui import PopUpGUI

class LoginOutController():
    def __init__(self):
        self.database_manager = Database_Manager()
        self.login_gui = LoginGUI()
        self.signup = SignupGUI()
        self.popup = PopUpGUI()
        
    #Functions SignUp
    def create_sign_up_gui(self): 
        self.signup.createMainFrame()
        
    def write_new_user_to_database(self):
        pass   
    
    def check_username_taken(self):
        pass
    

    #Functions login        
    def create_login_gui(self):
        self.login_gui.createMainFrame()

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
    def logout_push_changes_to_database(): 
        pass
    
    #delete Account
    def delete_account():
        pass
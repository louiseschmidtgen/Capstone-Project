from Login_GUI import LogInGUI
from SignUp_GUI import SignupGUI
from Dashboard_Controller import DashboardController
from Pop_up_gui import PopUpGUI
from user import User
from Learnset import Learnset
from Word import Word

import sys
 
class LoginOutController():
    def __init__(self, GGA_DB):
        self.database_manager = GGA_DB
        self.login_gui = None
        self.signup = None
        self.popup = PopUpGUI()
    
    #Functions SignUp
    def create_sign_up_gui(self): 
        if self.signup == None:
            self.signup = SignupGUI(self)
            self.signup.createMainFrame()
            self.signup.show()
        
    def write_new_user_to_database(self, username, password, repeatpassword):
        if password == repeatpassword:
            userid_out = self.database_manager.return_user_id(username, password)
            if userid_out == []:
                #check if already taken
                self.database_manager.insert_user(username, password)
                self.signup.hide()
            else:
                self.popup.createPopUp("Please choose different username.")         
        else:
            self.popup.createPopUp("Password does not match")
    

    #Functions login 
       
    def create_login_gui(self):
        if self.login_gui == None:
            self.login_gui = LogInGUI(self)
            self.login_gui.createMainFrame()
        self.login_gui.show()

    def get_user_id(self, username, password):
        userid_out = self.database_manager.return_user_id(username, password)
        if userid_out == []:
            return -1
        else: 
            return userid_out[0][0]
        
    def handle_login_request(self, username, password):
        print(username, password)
        userid = self.get_user_id(username, password)
        print("userid", userid)
        if userid>0:  #existing user
            #self.login_gui.handle_close_window()
            self.user = self.create_user_from_database(userid, username, password)
        else: #create new user
            favorites_learnset = Learnset(learnsetID=-1, learnset_name="Favorites")
            self.user = User(userid, username, password, favorites_learnset)
        self.create_dashboard_controller()
            
    def create_user_from_database(self, userid, username, password):
        users_learnsets = []
        favorites_learnset = None
        learnsets = self.database_manager.get_learnsets(userid)
        #returns format: [(4, 'animals', 2), (5, 'food', 2)]first is learnset id, learnset name, userid
        for learnset_data in learnsets:
            learnsetid = learnset_data[0]
            learnsetname = learnset_data[1]
            #get words in learnset
            users_words = []
            words = self.database_manager.get_words(learnsetid)
            #words format: [(1, 1, 'Cat', 'Katze', '/images/cat.png'), (2, 1, 'Dog', 'Hund', '/images/dog.png')] 
            # wordid, learnsetid, wordEngl, wordGer, wordimg
            for word_data in words:
                wordid = word_data[0]
                wordEngl = word_data[2]
                wordGer = word_data[3]
                wordimg = word_data[4]
                new_word = Word(wordid, wordEngl, wordGer, wordimg)
                users_words.append(new_word)
                print(new_word)
            new_learnset = Learnset(learnsetid, learnsetname, users_words)
            users_learnsets.append(new_learnset)
            if learnsetname == "Favorites":
                favorites_learnset = new_learnset
        if favorites_learnset == None:
            favorites_learnset = Learnset(learnsetID=-1, learnset_name="Favorites")
        my_user = User(userid, username, password, favorites_learnset, users_learnsets)
        print(users_learnsets, users_words)
        return my_user
    
    #Dashboard
    def create_dashboard_controller(self):
        self.dashboard_controller = DashboardController(self.user, self)
        self.login_gui.hide()
        self.dashboard_controller.create_dashboard_gui()
        
    
    #Logout
    def logout_push_changes_to_database(self): 
        pass 
    
    #delete Account
    def delete_account(self):
        self.database_manager.delete_user(self.user.userID)
        self.login_gui.show()
        #To_do: Check if all linked to user is deleted
    
    def close_app(self):
        print("Close App.")
        #close DB

from Login_GUI import LogInGUI
from SignUp_GUI import SignupGUI
from Dashboard_Controller import DashboardController
from Pop_up_gui import PopUpGUI
from user import User
from Learnset import Learnset
from Word import Word
from PyQt5.QtCore import QCoreApplication, Qt


import sys
 
class LoginOutController():
    def __init__(self, GGA_DB):
        self.database_manager = GGA_DB
        self.login_gui = None
        self.signup = None
        self.popup = PopUpGUI()
    
    #Functions SignUp
    def create_sign_up_gui(self): 
        """This function creates the Sign up GUI."""
        self.signup = SignupGUI(self)
        self.signup.createMainFrame()
        self.signup.show()
        
    def write_new_user_to_database(self, username, password, repeatpassword):
        """This function first checks that the info fits in the databse allocated space.
        Then it checks if the passwords match. If they do it checks wether the user already exists in db.
        If it does not it creates a new user and pushes the new user to the database. 
        The function creates pop ups if the passwords don't match ot the sign in info is not unique.

        Args:
            username (str): name of the user
            password (str): password of the user
            repeatpassword (str): password of the user
        """
        if len(username) > 40 or len(password) > 15 or len(repeatpassword)>15:
            self.popup.createPopUp("username or password is too long.")
        if password == repeatpassword:
            userid_out = self.database_manager.return_user_id(username, password)
            #user doesnt exist
            if userid_out == []:
                #check if already taken
                favorites_learnset = Learnset(learnsetID=-1, learnset_name="Favorites")
                my_user = User(-1, username, password, favorites_learnset)
                my_user.learnset_list.append(favorites_learnset)
                self.user = self.push_changes_to_database(my_user)
                
                self.signup.hide()
            else:
                self.popup.createPopUp("Please choose different username.")         
        else:
            self.popup.createPopUp("Password does not match")
    
        
    #Functions login 
       
    def create_login_gui(self):
        """This function creates the Login GUI."""
        self.login_gui = LogInGUI(self)
        self.login_gui.createMainFrame()
        self.login_gui.show()

    def get_user_id(self, username, password):
        """Given the input this function asks the database manager to return the userid. 
        If there is none it returns -1.

        Args:
            username (str): name of the user
            password (str): password of the user

        Returns:
            int: userid
        """
        userid_out = self.database_manager.return_user_id(username, password)
        if userid_out == []:
            return -1
        else: 
            return userid_out[0][0]
        
    def handle_login_request(self, username, password):
        """This function checks the login info and decides what to do with it.
        If it is incorrect it creates a popup. 
        If user exists in database it calls a function
        that creates a user object based on the database.
        Args:
            username (str): name of the user
            password (str): password of the user
        """
        print(username, password)
        if username =="" or password =="":
            self.popup.createPopUp("Username and Password must be specified.")
            return
        userid = self.get_user_id(username, password)
        print(userid)
        print("userid", userid)
        if userid>0:  #existing user
            #self.login_gui.handle_close_window()
            self.user = self.create_user_from_database(userid, username, password)
        # else: #create new user
        #     #favorites_learnset = Learnset(learnsetID=-1, learnset_name="Favorites")
        #     self.user = User(userid, username, password, favorites_learnset)
            self.create_dashboard_controller()
        else:
            self.popup.createPopUp("Login Information Incorrect.")
            
    def create_user_from_database(self, userid, username, password):
        """This function builds a user object after the data held on the user in the database.

        Args:
            userid (int): unique identifier of user
            username (str): name of the user
            password (str): password of the user

        Returns:
            user object
        """
        users_learnsets = []
        favorites_learnset = None
        learnsets = self.database_manager.get_learnsets(userid) #only one favorites ls
        #print(learnsets)
        #[(63, 'Favorites', 13), (64, 'Food', 13), (65, 'Animals', 13), (66, 'Numbers', 13), (67, 'Colors', 13)]
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
        #print(users_learnsets) #only 1 Favorite ls
        if favorites_learnset == None:
            
            favorites_learnset = Learnset(learnsetID=-1, learnset_name="Favorites")
        my_user = User(userid, username, password, favorites_learnset, users_learnsets)
        my_user.print_learnsets()
        
        return my_user
    
    #Dashboard
    def create_dashboard_controller(self):
        """This function creates the Dashboard Controller and opens its GUI"""
        self.dashboard_controller = DashboardController(self.user, self)
        self.login_gui.hide()
        self.dashboard_controller.create_dashboard_gui()
        
    
    #Logout
    def push_changes_to_database(self, new_user):
        """This function takes a user object and compares the changes
        in the object to the user data it finds in the database. 
        Based on what is in the database it makes changes by adding or removing words, learnsets or the user.
        A negative index stands for an object being new and needs to be added in the database. 
        Now the object is assigned a positive ID which is generated by the database.
        If a object is in the database but not in the user object it gets deleted in the database.

        Args:
            new_user (user object): holds users learsets and words

        Returns:
            new_user (user object): holds users learsets and words
        """
        #Table 1: User
        #if user new, insert them 
        if new_user.userID <0:
            #insert user
            self.database_manager.insert_user(new_user.username, new_user.password)               
            #get userid
            user_id = self.database_manager.return_user_id(new_user.username, new_user.password)[0][0]   
            new_user.userID = user_id
        
        #Table 2: Learnset
        for new_ls in new_user.learnset_list:
            #is a new learnset, add to db
            if new_ls.learnsetID <0:
                print(new_ls.learnset_name, new_user.userID)
                self.database_manager.insert_learnset(new_ls.learnset_name, new_user.userID)
                ls_id_new = self.database_manager.get_ls_id(new_ls.learnset_name, new_user.userID)[0][0]
                print(ls_id_new)
                new_ls.learnsetID = ls_id_new 
            #there is no delete option for learnsets
            
        print("Words")   
        #Table 3: Words
        for ls in new_user.learnset_list:
            #get wordids in DB related to this learnset            
            db_words_out = self.database_manager.get_words(ls.learnsetID)
            print("Get words of db:")
            print(db_words_out)
            #words format: [(1, 1, 'Cat', 'Katze', '/images/cat.png'), (2, 1, 'Dog', 'Hund', '/images/dog.png')] 
            # wordid, learnsetid, wordEngl, wordGer, wordimg
            db_words_wordids = []
            for word_data in db_words_out:
                wordid = word_data[0]
                db_words_wordids.append(wordid)
            print("Wordids")
            print(db_words_wordids)
            for word in ls.wordlist:
                print(word)
                #word is new- create the word in the db
                if word.wordID <0:
                    self.database_manager.insert_word(learnsetId= ls.learnsetID, wordEngl= word.wordEngl, wordGer = word.wordGer, wordImg= word.image)
                #word in db, remove the word from the list, 
                # so that we can remove all words in the next step 
                # that the user deleted in the current session
                elif word.wordID in db_words_wordids:
                    db_words_wordids.remove(word.wordID)
            
            #delete words that are no longer in current user but still in db
            for wordid in db_words_wordids:
                self.database_manager.delete_word(wordid)
        self.create_login_gui()
        return new_user
    
    #delete Account
    def delete_account(self, user):
        """This function deletes a user and its data in the database. It first deletes words then learnset and lastly the user, to avoid dependency problems.

        Args:
            user (user object): holds users learsets and words
        """
        #first delete words then learnset and last user, to avoid dependency problems
        print(user.userID)
        for ls in user.learnset_list:
            print(ls.learnsetID)
            for word in ls.wordlist:
                if word.wordID >0:
                    self.database_manager.delete_word(word.wordID)
            if ls.learnsetID >0:
                self.database_manager.delete_learnset(ls.learnsetID)
                
        self.database_manager.delete_user(user.userID)
        self.create_login_gui()
        #To_do: Check if all linked to user is deleted
    
    def close_app(self):
        """This function closes the Application"""
        print("Close App.")
        QCoreApplication.instance().quit
        #close DB

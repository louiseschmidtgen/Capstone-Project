from Database_Manager import DB
from Login_GUI import LogInGUI
from SignUp_GUI import SignupGUI
from Dashboard_Controller import DashboardController
from Pop_up_gui import PopUpGUI
from user import User
from Learnset import Learnset
from Word import Word
from Learnset_Controller import LearnsetController
import os
import sys
import os
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QAction
from Login_GUI import LogInGUI
from Database_Manager import DB

def create_user_from_database(mydb, userid, username, password):
    users_learnsets = []
    favorites_learnset = None
    learnsets = mydb.get_learnsets(userid)
    #returns format: [(4, 'animals', 2), (5, 'food', 2)]first is learnset id, learnset name, userid
    for learnset_data in learnsets:
        learnsetid = learnset_data[0]
        learnsetname = learnset_data[1]
        #get words in learnset
        users_words = []
        words = mydb.get_words(learnsetid)
        #words format: [(1, 1, 'Cat', 'Katze', '/images/cat.png'), (2, 1, 'Dog', 'Hund', '/images/dog.png')] 
        # wordid, learnsetid, wordEngl, wordGer, wordimg
        for word_data in words:
            wordid = word_data[0]
            wordEngl = word_data[2]
            wordGer = word_data[3]
            wordimg = word_data[4]
            print(wordimg)
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

def create_default_user():
    favorites_learnset = Learnset(learnsetID=-1, learnset_name="Favorites")
    my_user = User(-1, 'lu', 'password', favorites_learnset)
    return my_user

def main():
    #set environ
    os.environ['SQLUser']='root'
    os.environ['SQLPassword']= 'Veritas!10'
    os.environ['SQLHost'] = "localhost"
    os.environ['DB_NAME'] ='GeniusGermanDatabase'
    #SECTION 1 Create DB
    #my_db = DB()
    username = "lou"
    password = "123"
    userid = 1
    
    user = create_default_user()
    ls_controller = LearnsetController(user, None)
    app = QApplication(sys.argv) 
    ls_controller.create_learnset_menu_gui()
    sys.exit(app.exec_())
    
main()
    
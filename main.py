import sys
import os
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QAction
import PyQt5
from Login_GUI import LogInGUI
from Login_out_Controller import LoginOutController
from Database_Manager import DB

def set_env_variables():
    #export variables to environment for google api
    os.environ["X_RapidAPI_Host"]= "google-translate1.p.rapidapi.com"
    os.environ["X_RapidAPI_Key"]= '9928c7260amshad0766390e03e89p1f4683jsn18824f37a5dc'
    # os.environ["GENIUS_GERMAN_DB_NAME"]= "GeniusGermanDB"
    os.environ['SQLUser']='root'
    os.environ['SQLPassword']= 'Veritas!10'
    os.environ['SQLHost'] = "localhost"
    os.environ['DB_NAME'] ='GeniusGermanDatabase2'

def main():
    #1. set environment variables. 
    set_env_variables()
    
    #2. create/connect to DB
    GGA_DB = DB()
    GGA_DB.connect_to_db()  
    
    #3. creates login out controller
    login_out_controller = LoginOutController(GGA_DB)
    
    #4. create PYQT Application, first window is login GUI
    app = PyQt5.QtWidgets.QApplication(sys.argv)   
    login_out_controller.create_login_gui()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 
    #todo fix favorites word needs to be created with -1id
    #add animals to favorites broken?
    #runs put word in db twice for favorites ls
    #sign in ls are duplicateds
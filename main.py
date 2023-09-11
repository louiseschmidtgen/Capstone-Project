import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QAction
import PyQt5
from dotenv import load_dotenv
from Login_GUI import LogInGUI
from Login_out_Controller import LoginOutController
from Database_Manager import DB


def set_env_variables():
    # Load environment variables from .env file
    load_dotenv()


def main():
    # 1. set environment variables.
    set_env_variables()

    # 2. create/connect to DB
    GGA_DB = DB()
    GGA_DB.connect_to_db()

    # 3. creates login out controller
    login_out_controller = LoginOutController(GGA_DB)

    # 4. create PYQT Application, first window is login GUI
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    login_out_controller.create_login_gui()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    # todo fix favorites word needs to be created with -1id
    # add animals to favorites broken?
    # runs put word in db twice for favorites ls
    # sign in ls are duplicateds

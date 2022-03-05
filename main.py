import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QAction
from Login_GUI import LogInGUI
from Login_out_Controller import LoginOutController

def main():
    app = QApplication(sys.argv)
    login_out_controller = LoginOutController()
    ex = LogInGUI(login_out_controller)
    ex.createMainFrame()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 
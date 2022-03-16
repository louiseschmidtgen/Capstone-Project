from PyQt5.QtWidgets import QMainWindow, QLineEdit, QFormLayout, QWidget, QPushButton, QApplication, QAction, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

class LogInGUI(QWidget): 
    
    def __init__(self, login_out_controller):
        super().__init__()
        # self.createMainFrame()
        self.login_out_controller = login_out_controller
        
    def createMainFrame(self):
        self.setWindowTitle('GGA: Login Window ')
        self.setGeometry(100, 100, 280, 80)
        self.move(60, 15)
        layout = QFormLayout()
        # Logo:
        self.logo_label = QLabel(self)      
        self.logo_pixmap = QPixmap('images\dog.JPG')
        self.logo_label.setPixmap(self.logo_pixmap)
        #Buttons:
        self.login_button = QPushButton("Log In")
        self.login_button.setObjectName("login") 
        self.login_button.clicked.connect(self.handle_login_event)
        
        self.signup_button = QPushButton("Sign Up")
        self.signup_button.setObjectName("signup")
        self.signup_button.clicked.connect(self.handle_sign_up_event)
        
        self.exit_button = QPushButton("Exit")
        self.exit_button.setObjectName("Exit")  
        self.exit_button.clicked.connect(self.handle_close_window)       
        #Entry fields:
        self.username = QLineEdit()
        self.password = QLineEdit()
        
        #self.setStyleSheet(open('geniusgermanapp\mystylesheet.css').read())
        
        #add items to layout
        layout.addRow(self.logo_label, )
        layout.addRow('Username:', self.username)
        layout.addRow('Password:', self.password)
        layout.addRow(self.login_button)
        layout.addRow(self.signup_button)
        layout.addRow(self.exit_button)

        #set layout
        self.setLayout(layout)
     
    
    def handle_close_window(self):
        print("Exit button pressed.")
        self.login_out_controller.close_app()
        self.close()
    
    def handle_login_event(self):
        print("login button pressed.")
        print(self.username.text())
        self.login_out_controller.handle_login_request(self.username.text(), self.password.text())
        
    def handle_sign_up_event(self):
        print("Sign Up button pressed.")
        self.login_out_controller.create_sign_up_gui()

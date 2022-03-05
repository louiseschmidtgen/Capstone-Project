from PyQt5.QtWidgets import QLineEdit, QFormLayout, QWidget, QPushButton, QApplication, QAction, QLabel

class LogInGUI(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('GGA: Login Window ')
        self.setGeometry(100, 100, 280, 80)
        # self.setStyle()
        self.move(60, 15)
        layout = QFormLayout()

        self.login_button = QPushButton("LogIn")
        self.login_button.setObjectName("signup") 
        self.setStyleSheet(open('geniusgermanapp\mystylesheet.css').read())
        
        layout.addRow('Username:', QLineEdit())
        layout.addRow('Password:', QLineEdit())
        layout.addRow(self.login_button)
        layout.addRow(QPushButton("Sign Up"))
        layout.addRow(QPushButton("Exit" ))

        self.setLayout(layout)
        
        
        # helloMsg = QLabel('<h1>Hello World!</h1>', parent=self)
        # helloMsg.move(60, 15)



class LoginGUI():
    
    
    def __init__(self, master):
        self.master = master
        
    def createMainFrame(self):
        pass
    
    def close_window(self):
        pass
    
    def handle_login_event(self):
        pass
    
    def handle_sign_up_event(self):
        pass
    

from PyQt5.QtWidgets import QMainWindow, QLineEdit, QFormLayout, QWidget, QPushButton, QApplication, QAction, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt


class SignupGUI(QWidget):
    def __init__(self, login_out_controller):
        super().__init__()
        # self.createMainFrame()
        self.login_out_controller = login_out_controller

    def createMainFrame(self):
        """This function builds the GUI using Form Layout."""
        self.setWindowTitle('GGA: Sign Up Window ')
        self.setGeometry(100, 100, 280, 80)
        self.move(60, 15)
        layout = QFormLayout()
        # Logo:
        self.logo_label = QLabel(self)
        self.logo_pixmap = QPixmap('images/GGA_logo.png')
        self.logo_label.setPixmap(self.logo_pixmap)
        # Buttons:
        self.signup_button = QPushButton("Sign Up")
        self.signup_button.setObjectName("signup")
        self.signup_button.clicked.connect(self.handle_sign_up_event)

        self.exit_button = QPushButton("Exit")
        self.exit_button.setObjectName("Exit")
        self.exit_button.clicked.connect(self.handle_close_window)
        # Entry fields:
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.repeat_password = QLineEdit()

        # self.setStyleSheet(open('geniusgermanapp\mystylesheet.css').read())

        # add items to layout
        layout.addRow(self.logo_label, )
        layout.addRow('Username:', self.username)
        layout.addRow('Password:', self.password)
        layout.addRow('Repeat Password:', self.repeat_password)
        layout.addRow(self.signup_button)
        layout.addRow(self.exit_button)

        # set layout
        self.setLayout(layout)

    def handle_close_window(self):
        """This function invokes close function in login logout controller."""
        print("Exit button pressed.")
        self.login_out_controller.close_app()
        self.close()

    def handle_sign_up_event(self):
        """This function invokes write_new_user_to_database function in login logout controller."""
        print("Sign Up button pressed.")
        username = self.username.text()
        password = self.password.text()
        repeat_password = self.repeat_password.text()
        self.login_out_controller.write_new_user_to_database(
            username, password, repeat_password)

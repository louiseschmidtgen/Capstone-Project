from PyQt5.QtWidgets import QMainWindow, QLineEdit, QFormLayout, QWidget, QPushButton, QApplication, QAction, QLabel
from PyQt5.QtGui import QIcon, QPixmap

class TranslatorGUI(QWidget):
    def __init__(self, dashboard_controller):
        super().__init__()
        self.dashboard_controller = dashboard_controller
        self.e2g_in = ""
        self.e2g_out = ""
        self.g2e_in = ""
        self.g2e_out = ""  
              
    def create_main_frame(self):
        self.setWindowTitle('GGA: Translator Window ')
        self.setGeometry(100, 100, 280, 80)
        self.move(60, 15)
        
    def handle_e2g_translation(self):
        pass
    
    def handle_g2e_translation(self):
        pass   
     
    def close_gui(self):
        self.hide()
        self.dashboard_controller.create_dashboard_gui()    
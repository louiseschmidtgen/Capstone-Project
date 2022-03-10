from PyQt5.QtWidgets import QMainWindow, QLineEdit, QFormLayout, QWidget, QPushButton, QApplication, QAction, QLabel
from PyQt5.QtGui import QIcon, QPixmap

class GermanHolidaysGUI(QWidget):
    def __init__(self,  dashboard_controller):
        super().__init__()
        self.dashboard_controller = dashboard_controller
        
    def create_main_frame(self):
        self.setWindowTitle('GGA: German Holidays')
        self.setGeometry(100, 100, 280, 80)
        self.move(60, 15)
    
    def handle_info_request(self, holiday):
        pass 
    
    def close_gui(self):
        self.hide()
        self.dashboard_controller.create_dashboard_gui()
    

        
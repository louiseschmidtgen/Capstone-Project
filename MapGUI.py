from PyQt5.QtWidgets import QGridLayout, QMainWindow, QLineEdit, QFormLayout, QWidget, QPushButton, QApplication, QAction, QLabel
from PyQt5.QtGui import QIcon, QPixmap

class MapGUI(QWidget):
    def __init__(self, dashboard_controller):
        super().__init__()
        self.dashboard_controller = dashboard_controller
        
    def create_main_frame(self):
        self.setWindowTitle('GGA: Map of Germany')
        self.setGeometry(100, 100, 280, 80)
        self.move(60, 15)
        layout = QGridLayout()
        # Logo:
        self.logo_label = QLabel(self)      
        self.logo_pixmap = QPixmap('geniusgermanapp\MapGer.png')
        self.logo_label.setPixmap(self.logo_pixmap)        
        # Map Image:
        self.map_label = QLabel(self)      
        self.map_pixmap = QPixmap('geniusgermanapp\GGA_logo.png')
        self.map_label.setPixmap(self.logo_pixmap) 
        #button
        self.exit_button = QPushButton("Exit")
        self.exit_button.setObjectName("Exit")  
        self.exit_button.clicked.connect(self.handle_close_window)
        
        layout.addWidget(self.logo_label, 0, 0)
        layout.addWidget(QLabel("Map"), 0,2)
        layout.addWidget(self.map_label, 1, 1)        
        layout.addWidget(self.exit_button, 0,2)
                
    def handle_close_window(self):
        self.hide()
        self.dashboard_controller.create_dashboard_gui()
from PyQt5.QtWidgets import QGridLayout, QMainWindow, QLineEdit, QFormLayout, QWidget, QPushButton, QApplication, QAction, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

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
        self.logo_pixmap = QPixmap('images\GGA_logo.png')
        smaller_pixmap = self.logo_pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.logo_label.setPixmap(smaller_pixmap)        
        # Map Image:
        self.map_label = QLabel(self)      
        self.map_pixmap = QPixmap('images\MapGer.png')
        map_smaller_pixmap = self.map_pixmap.scaled(600, 600, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.map_label.setPixmap(map_smaller_pixmap) 
        #button
        self.exit_button = QPushButton("Exit")
        self.exit_button.setObjectName("Exit")  
        self.exit_button.clicked.connect(self.handle_close_window)
        
        layout.addWidget(self.logo_label, 0, 0)
        layout.addWidget(QLabel("Map"), 0,1)
        layout.addWidget(self.map_label, 1, 1)        
        layout.addWidget(self.exit_button, 2,2)
        
        #set layout
        self.setLayout(layout)         
    def handle_close_window(self):
        self.hide()
        self.dashboard_controller.create_dashboard_gui()
from PyQt5.QtWidgets import QGridLayout, QMainWindow, QLineEdit, QFormLayout, QWidget, QPushButton, QApplication, QAction, QLabel
from PyQt5.QtGui import QIcon, QPixmap

class AddWordGUI(QWidget):
    def __init__(self,  learnset):
        super().__init__()
        self.learnset = learnset

        
    def create_main_frame(self):
        self.setWindowTitle('GGA: Add Learnset ')
        self.setGeometry(100, 100, 280, 80)
        self.move(60, 15)
        
        layout = QGridLayout()
        
        # Logo:
        self.logo_label = QLabel(self)      
        self.logo_pixmap = QPixmap('images\GGA_logo.png')
        self.logo_label.setPixmap(self.logo_pixmap)
        #Label
        self.engl_label = QLabel("Word in English: ")
        self.ger_label = QLabel("Word in German: ")
        
        #Entry field
        self.in_ls_name = QLineEdit()

        #Buttons 
        self.close_button = QPushButton("Close")
        self.close_button.setObjectName("Red")  
        self.close_button.clicked.connect(self.handle_close_window)
        
        self.add_button = QPushButton("Add")
        self.add_button.setObjectName("Green")  
        self.add_button.clicked.connect(self.handle_add_learnset_event)
        
        #Layout
        layout.addWidget(self.logo_label, 0, 0)
        layout.addWidget(self.prompt_label, 1, 1)   
        layout.addWidget(self.in_ls_name, 2, 1)   
        layout.addWidget(self.add_button, 3, 1)   
        layout.addWidget(self.close_button, 4, 1)           
        
        #set layout
        self.setLayout(layout)     
        
    def handle_add_learnset_event(self):
        name = ""
        self.learnset_controller.add_learnset(name)
        
    def handle_close_window(self):
        self.hide()
        self.learnset_controller.create_learnset_menu_gui()
        
    
        
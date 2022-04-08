from PyQt5.QtWidgets import QComboBox, QMainWindow,QGridLayout, QLineEdit, QFormLayout, QWidget, QPushButton, QApplication, QAction, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

class LSMenuGUI(QWidget):
    def __init__(self, learnset_controller, user_obj):
        super().__init__()
        self.learnset_controller = learnset_controller
        self.user_obj = user_obj
        
    def create_main_frame(self):
        self.setWindowTitle('GGA: German Holidays')
        self.setGeometry(100, 100, 280, 80)
        self.move(60, 15)
        layout = QGridLayout()
        
        # Logo:
        self.logo_label = QLabel(self)      
        self.logo_pixmap = QPixmap('images\GGA_logo.png')
        smaller_pixmap = self.logo_pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.logo_label.setPixmap(smaller_pixmap)
        
        #Label
        self.learnsets_label = QLabel("Learnsets")
        #Buttons 
        self.exit_button = QPushButton("Close")
        self.exit_button.setObjectName("Red")  
        self.exit_button.clicked.connect(self.handle_close_window)       

        self.add_ls_button = QPushButton("+Learnset")
        self.add_ls_button.setObjectName("Green")  
        self.add_ls_button.clicked.connect(self.handle_add_learnset_event) 
    
        self.submit_button = QPushButton("Submit")
        self.submit_button.setObjectName("Green")  
        self.submit_button.clicked.connect(self.handle_submit_event) 

        #ComboBox
        self.learnset_menu = QComboBox()
        self.learnset_obj_list = self.user_obj.learnset_list
        self.learnset_list = [x.learnset_name for x in self.learnset_obj_list]
        print(self.learnset_list)
        self.learnset_menu.addItems(self.learnset_list)
        
        #ComboBox
        self.mode_menu = QComboBox()
        self.mode_menu.addItems(["Study Mode","Quiz Mode" ])  
        
        #layout
        layout.addWidget(self.logo_label, 0, 0)
        layout.addWidget(self.learnsets_label, 0, 1)
        layout.addWidget(self.add_ls_button, 0, 2)    
        layout.addWidget(self.learnset_menu, 1, 1)   
        layout.addWidget(self.mode_menu, 1, 2) 
        layout.addWidget(self.submit_button, 2, 1, 1, 2)  
        layout.addWidget(self.exit_button, 4, 2)
         
        self.setLayout(layout) 
        
    def handle_submit_event(self):
        learnset_name = self.learnset_menu.currentText()
        print(learnset_name)
        learnset_obj = self.learnset_obj_list[self.learnset_menu.currentIndex()]
        mode = self.mode_menu.currentText()
        print(mode)
        if mode =="Study Mode":
            self.learnset_controller.open_learnset_study_mode_gui(learnset_obj) 
        else:
            self.learnset_controller.open_learnset_quiz_mode_gui(learnset_obj) 
   
    def handle_add_learnset_event(self):
        self.hide()
        self.learnset_controller.open_add_learnset_gui()
    
    def handle_close_window(self):
        self.hide()
        self.learnset_controller.open_dashboard()

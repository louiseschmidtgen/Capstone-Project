from PyQt5.QtWidgets import QFileDialog, QGridLayout, QMainWindow, QLineEdit, QFormLayout, QWidget, QPushButton, QApplication, QAction, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

class AddWordGUI(QWidget):
    def __init__(self,  learnset_controller, learnset):
        super().__init__()
        self.learnset_controller = learnset_controller
        self.learnset = learnset
        
    def create_main_frame(self):
        self.setWindowTitle('GGA: Add Word ')
        self.setGeometry(100, 100, 280, 80)
        self.move(60, 15)
        
        layout = QGridLayout()
        
        # Logo:
        self.logo_label = QLabel(self)      
        self.logo_pixmap = QPixmap('images\GGA_logo.png')
        smaller_pixmap = self.logo_pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.logo_label.setPixmap(smaller_pixmap)
        #Label
        self.engl_label = QLabel("Word in English: ")
        self.ger_label = QLabel("Word in German: ")
        self.img_label = QLabel("Image: ")
        
        #Entry field
        self.in_engl = QLineEdit()
        self.in_ger = QLineEdit()
        
        self.imagePath = 'images\imagenotfound.png'

        #Buttons 
        self.select_img_button = QPushButton("Open Image Location")
        self.select_img_button.setObjectName("OpenImg")
        self.select_img_button.clicked.connect(self.get_image)
        
        self.close_button = QPushButton("Close")
        self.close_button.setObjectName("Red")  
        self.close_button.clicked.connect(self.handle_close_window)
        
        self.add_button = QPushButton("Add")
        self.add_button.setObjectName("Green")  
        self.add_button.clicked.connect(self.handle_add_word_event)
        
        #Layout
        layout.addWidget(self.logo_label, 0, 0)
        layout.addWidget(self.engl_label, 1, 1)   
        layout.addWidget(self.in_engl, 1, 2)   
        layout.addWidget(self.ger_label, 2, 1)   
        layout.addWidget(self.in_ger, 2, 2) 
        layout.addWidget(self.img_label, 3,1)  
        layout.addWidget(self.select_img_button, 3,2)
        layout.addWidget(self.add_button, 4, 1, 1,2)   
        layout.addWidget(self.close_button, 5, 2)           
        
        #set layout
        self.setLayout(layout)    
         
    def get_image(self):
        self.image = QFileDialog.getOpenFileName(None,'OpenFile','',"Image file(*.png)")
        self.imagePath = self.image[0] 
        
    def handle_add_word_event(self):
        wordEngl = self.in_engl.text()
        wordGer = wordGer = self.in_ger.text()
        self.in_engl.setText("")
        self.in_ger.setText("")
        self.learnset_controller.create_word(wordEngl, wordGer, self.imagePath, self.learnset)
        
        
    def handle_close_window(self):
        self.hide()
        #self.learnset_controller.create_learnset_menu_gui()
        
    
        
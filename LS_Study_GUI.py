from PyQt5.QtWidgets import QComboBox, QMainWindow,QGridLayout, QLineEdit, QFormLayout, QWidget, QPushButton, QApplication, QAction, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
import random
from Pop_up_gui import PopUpGUI
from Word import Word

class LSStudyGUI(QWidget):   
    def __init__(self, learnset_controller, learnset_obj):
        super().__init__()
        self.learnset_controller = learnset_controller
        self.learnset_obj = learnset_obj
        self.word_index = 0
        self.popup = None
        random.shuffle(self.learnset_obj.wordlist) #shuffle words
        print(self.learnset_obj.wordlist)
        if len(self.learnset_obj.wordlist) >0:
            self.current_word = self.learnset_obj.wordlist[self.word_index]
        else:
            self.current_word = Word(-1, wordEngl="", wordGer="", word_image= 'images\imagenotfound.png')
            
    def create_main_frame(self):
        self.setWindowTitle("GGA: Study "+ self.learnset_obj.learnset_name)
        self.setGeometry(100, 100, 280, 80)
        self.move(60, 15)
        layout = QGridLayout()
        print(self.current_word)
        # Logo:
        self.logo_label = QLabel(self)      
        self.logo_pixmap = QPixmap('images\GGA_logo.png')
        smaller_pixmap = self.logo_pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.logo_label.setPixmap(smaller_pixmap)
        
        #Main Image
        self.img_label = QLabel(self)    
        img_location =  self.current_word.image 
        self.img_pixmap = QPixmap(img_location)
        img_scaled_pixmap = self.img_pixmap.scaled(250, 250, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.img_label.setPixmap(img_scaled_pixmap)        
        
        #Label
        self.learnsets_label = QLabel(self.learnset_obj.learnset_name)
        self.wordEngl = self.current_word.wordEngl
        self.wordGer = self.current_word.wordGer
        self.engl_label = QLabel(self.wordEngl)
        self.ger_label = QLabel(self.wordGer)
        #Buttons 
        self.exit_button = QPushButton("Close")
        self.exit_button.setObjectName("Red")  
        self.exit_button.clicked.connect(self.handle_close_window)       
        
        self.delete_word_button = QPushButton("Delete Word")
        self.delete_word_button.setObjectName("Red")  
        self.delete_word_button.clicked.connect(self.handle_close_window)       

        self.add_word_button = QPushButton("+Word")
        self.add_word_button.setObjectName("Green")  
        self.add_word_button.clicked.connect(self.handle_add_word_event)
        
        self.favorite_button = QPushButton("Favorite")
        self.favorite_button.setObjectName("YellowButton")  
        self.favorite_button.clicked.connect(self.handle_add_word_to_favorites)
        
        self.next_button = QPushButton("Next")
        self.next_button.setObjectName("Green")
        self.favorite_button.clicked.connect(self.handle_next_event)

        self.previous_button = QPushButton("Previous")
        self.previous_button.setObjectName("Previous")
        self.previous_button.clicked.connect(self.handle_previous_event)      
        
        layout.addWidget(self.logo_label, 0, 0)
        layout.addWidget(self.learnsets_label, 0,1)
        layout.addWidget(self.add_word_button, 0,2)
        layout.addWidget(self.img_label, 1, 1, 1, 2)
        layout.addWidget(self.favorite_button, 1,3)
        layout.addWidget(self.engl_label, 3,1)
        layout.addWidget(self.ger_label, 3,2)
        layout.addWidget(self.previous_button, 4, 1)
        layout.addWidget(self.next_button, 4,2)
        layout.addWidget(self.delete_word_button, 5,0)
        layout.addWidget(self.exit_button, 5,3)
                
        self.setLayout(layout)   
        
    def handle_add_word_to_favorites(self):
        self.learnset_controller.add_word_to_favorites(self.word)

    def handle_add_word_event(self):
        self.learnset_controller.open_add_word_gui(self.learnset_obj)
        
    def handle_delete_word(self):
        self.learnset_controller.remove_word_from_learnset(self.current_word, self.learnset_obj)
        
        if len() ==0:
            self.current_word = Word(wordEngl="", wordGer="", word_image="", word_imag= 'images\GGA_logo.png')
    
    def handle_previous_event(self):
        #no words
        if len(self.learnset_obj.wordlist)== 0:
            self.create_popup("There are no words in the learnset.")
            return
        #only 1 word
        elif len(self.learnset_obj.wordlist)== 1:
            self.create_popup("There is only one word in the learnset.")
            return
        #word with previous word   
        elif (self.word_index -1) >0:
            self.word_index -=1
            self.current_word = self.learnset_obj.wordlist[self.word_index]
        #first word in list
        else:
            self.word_index = len(self.learnset_obj.wordlist) -1
            self.current_word = self.learnset_obj.wordlist[self.word_index]
        self.update()
        
    def update(self):
        self.engl_label.setText(self.current_word.wordEngl)
        self.ger_label.setText(self.current_word.wordGer)
        self.img_pixmap = QPixmap(self.current_word.image)
        img_scaled_pixmap = self.img_pixmap.scaled(250, 250, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.img_label.setPixmap(self.img_pixmap)  
        self.learnsets_label.setText(self.learnset_obj.learnset_name)
        
    def handle_next_event(self):
        if len(self.learnset_obj.wordlist)== 0:
            self.create_popup("There are no words in the learnset.")
        elif len(self.learnset_obj.wordlist)== 1:
            self.create_popup("There is only one word in the learnset.")
                
        elif (self.word_index +1) < len(self.learnset_obj.wordlist):
            self.word_index +=1
            self.current_word = self.learnset_obj.wordlist[self.word_index]
        else:
            self.word_index =0
            self.current_word = self.learnset_obj.wordlist[self.word_index]
        self.update()
        
    def create_popup(self, msg):
        if self.popup == None:
            self.popup = PopUpGUI()
        self.popup.createPopUp(msg)
        
    def handle_close_window(self):
        self.destroy()
        self.learnset_controller.create_learnset_menu_gui()

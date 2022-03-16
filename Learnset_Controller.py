from Learnset import Learnset
from Word import Word
from Pop_up_gui import PopUpGUI
from LS_Menu_GUI import LSMenuGUI
from LS_Quiz_GUI import LSQuizGUI
from LS_Study_GUI import LSStudyGUI
from Add_Word import AddWordGUI
from Add_LS import AddLearnsetGUI

class LearnsetController(): 
    def __init__(self, user_object, dashboard_object):
        self.user_object = user_object
        self.ls_menu_gui = None
        self.ls_quiz_gui = None
        self.ls_study_gui = None
        self.add_word_gui = None
        self.add_learnset_gui = None
        self.popup = PopUpGUI()
        self.dashboard_object = dashboard_object
        

    def create_word(self, wordEngl, wordGer, word_image, learnset, wordID=-1):
        """Creates a word if given info is correct and adds it to learnset
        creates a popup gui to inform about success/no success.

        Args:
            wordEngl (str): word in english
            wordGer (str): word in german
            word_image (_type_): image associated with word
            learnset (learnset object): learnset object that holds all info on learnset
            wordID (int, optional): unique identifier of word. Defaults to -1.
        """
        if wordEngl.isalpha() and wordGer.isalpha():
            #TO-DO: check image
            new_word = Word(wordID, wordEngl, wordGer, word_image)
            self.add_word_to_learnset(new_word, learnset)
            self.popup.createPopUp("New Word added.")
        else:
            self.popup.createPopUp("Please check your input. Word could not be added.")
            
    def add_word_to_learnset(self, new_word, learnset):
        """_summary_

        Args:
            new_word (word object): holds all info on a word
            learnset (learnset object): holds all info on learnset
        """
        learnset.add_word_to_learnset(new_word)
         
    def add_word_to_favorites(self, word):
        """adds a word to favorites

        Args:
            word (word object): holds all info on a word
        """
        word.isfavorite = True
        self.favorites_learnset.add_word_to_learnset(word)
   
    def remove_word_from_favorites(self, word):
        """removes a word from favorites

        Args:
            word (word object): holds all info on a word
        """
        if word.isfavorite == True:
            self.favorites_learnset.remove_word_from_learnset(word)        
            word.isfavorite = False
  
    def remove_word_from_learnset(self, word, learnset):
        """removes a word from learnset

        Args:
            word (word object): holds all info on word
            learnset (learnset object): holds all info on learnset

        Returns:
            Boolean: success/unsuccessful in removing word.
        """
        #remove word from learnset
        if learnset.remove_word_from_learnset(word):
            #remove word from favorites if possible
            self.favorites_learnset.remove_word_from_learnset(word)
            del word

    def add_learnset(self, name):
        """adds a learnset under a new name if name is not already used.

        Args:
            name (str): name of new learnset
        """
        if self.user_object.check_learnset_is_unique(name) and name !="":
           new_learnset = Learnset(learnsetID=-1, learnset_name=name, wordlist= [])
           self.user_object.add_learnset(new_learnset) 
           self.popup.createPopUp(f"New Learnset created: {name}")
           #TO-DO: Destroy Add Learnset GUI
        else:
            self.popup.createPopUp(f"Learnset could not be created: {name}")
    
    def add_learnset(self, learnset):
        self.user_object.add_learnset(learnset)

    def delete_learnset(self, learnset):               
        self.user_object.delete_learnset(learnset)
        
    def open_learnset_study_mode_gui(self, learnset_obj):
        self.ls_study_gui = LSStudyGUI(self, learnset_obj)
        self.ls_study_gui.create_main_frame()
        self.ls_menu_gui.hide()
        self.ls_study_gui.show()
    
    def open_learnset_quiz_mode_gui(self, learnset_obj):
        self.ls_quiz_gui = LSQuizGUI(self, learnset_obj)
        self.ls_quiz_gui.create_main_frame()
        self.ls_menu_gui.hide()
        self.ls_quiz_gui.show()
    
    def open_add_word_gui(self, learnset_obj):
        if self.add_word_gui == None:
            self.add_word_gui = AddWordGUI(self, learnset_obj)
            self.add_word_gui.create_main_frame()
        self.add_word_gui.show()
    
    def open_add_learnset_gui(self):
        if self.add_learnset_gui == None:
            self.add_learnset_gui = AddLearnsetGUI(self)
            self.add_learnset_gui.create_main_frame()
        self.add_learnset_gui.show()
    
    def create_learnset_menu_gui(self):
        if self.ls_menu_gui == None:
            self.ls_menu_gui = LSMenuGUI(self, self.user_object)
            self.ls_menu_gui.create_main_frame()
        self.ls_menu_gui.show()
    
    def open_dashboard(self):
        self.dashboard_object.create_dashboard_gui()
    
    
    
    
    
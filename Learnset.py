
import random 
from Pop_up_gui import PopUpGUI

class Learnset():
    """The Learnset Object holds all information on a given learnset."""
    def __init__(self, learnsetID, learnset_name, wordlist= []):
        """initialize Learnset Object

        Args:
            learnsetID (int): unique identifier of learnset
            learnset_name (str): name of learnset
            wordlist (list, optional): collection of words in learnset. Defaults to [].
        """
        self.learnsetID = learnsetID
        self.learnset_name = learnset_name
        self.wordlist = wordlist
        self.popup = PopUpGUI()
        
    def __str__(self):
        """Function for debugging"""
        engl_words= [x.wordEngl for x in self.wordlist]
        return f"id: {self.learnsetID}, name: {self.learnset_name}, words: {engl_words}"
    
    def return_shuffled_words_in_learnset(self):
        """
        Returns:
            wordlist: list of word objects in this learnset
        """
        return random.shuffle(self.wordlist)
    
    def add_word_to_learnset(self, word):
        """Adds a word to the learnset

        Args:
            word (Word Object)
        """
        self.wordlist.append(word)
        
    def remove_word_from_learnset(self, word):
        """Function tries to remove a word from learnset.

        Args:
            word (word object)

        Returns:
            Boolean: wether removal was successful or not
        """
        try:
            self.wordlist.remove(word)
            
            self.popup.createPopUp(f"Succesfully removed {word.wordEngl} from {self.learnset_name}")
            return True
        except:
            print(f"Could not remove {word.wordEngl} from {self.learnset_name}.")
            self.popup.createPopUp(f"Could not remove {word.wordEngl} from {self.learnset_name}")
            return False
        
    
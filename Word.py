import logging

class Word():
    """The Word class holds a words translations, id and image
    """
    def __init__(self, wordID, wordEngl, wordGer, word_image):
        self.wordID = wordID
        self.wordEngl = wordEngl
        self.wordGer = wordGer
        self.image = word_image
        self.isfavorite = False
        
    def __str__(self):
        """Funtion for debugging"""
        return f"wordid: {self.wordID}, engl: {self.wordEngl}, \
              ger: {self.wordGer}"
        
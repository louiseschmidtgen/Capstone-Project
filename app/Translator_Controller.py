from Translator_GUI import TranslatorGUI
from Google_API import GoogleAPI
class Translator_Controller():
    def __init__(self, dashboard_controller):
        self.dashboard_controller = dashboard_controller
        self.translator_gui = None
        self.google_api = None
        
    def get_e2g_tranlation(self, engl_word):
        """This function translates an English word to German

        Args:
            engl_word (str): Users input that needs to be translated.

        Returns:
            str: The German translation of the Word.
        """
        if self.google_api == None:
            self.google_api  = GoogleAPI()
        translation = self.google_api.get_e2g_translation(engl_word)
        return translation
    
    def get_g2e_tranlation(self, ger_word):
        """This function translates an German word to English

        Args:
            ger_word (str): Users input that needs to be translated.

        Returns:
            str: The English translation of the Word."""
        if self.google_api == None:
            self.google_api  = GoogleAPI()
        translation = self.google_api.get_g2e_translation(ger_word)
        return translation
    
    def create_translator_gui(self):
        """This function creates the translator GUI"""
        if self.translator_gui == None:
            self.translator_gui = TranslatorGUI(self)
            self.translator_gui.create_main_frame()
        self.translator_gui.show()       
    
    def close_translator(self):
        """This function unvokes create dashboard gui in the dashboard controller."""
        self.dashboard_controller.create_dashboard_gui()
        
            
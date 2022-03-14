from Translator_GUI import TranslatorGUI
from Google_API import GoogleAPI
class Translator_Controller():
    def __init__(self, dashboard_controller):
        self.dashboard_controller = dashboard_controller
        self.translator_gui = None
        self.google_api = None
        
    def get_e2g_tranlation(self, engl_word):
        if self.google_api == None:
            self.google_api  = GoogleAPI(self)
        translation = self.google_api.get_e2g_translation(engl_word)
        return translation
    
    def get_g2e_tranlation(self, ger_word):
        if self.google_api == None:
            self.google_api  = GoogleAPI(self)
        translation = self.google_api.get_g2e_translation(ger_word)
        return translation
    
    def create_translator_gui(self):
        if self.translator_gui == None:
            self.translator_gui = TranslatorGUI(self)
            self.translator_gui.create_main_frame()
        self.translator_gui.show()       
    
    def close_translator(self):
        self.dashboard_controller.create_dashboard_gui()
        
            
from Pop_up_gui import PopUpGUI

class GoogleAPI():
    def __init__(self):
        self.popup = PopUpGUI()
        
    def create_pop_up_with_error(self, message):
        self.popup.createPopUp(message)
        
    def get_e2g_translation(self, engl_word):
        pass
    
    def get_g2e_translation(self, ger_word):
        pass    
        
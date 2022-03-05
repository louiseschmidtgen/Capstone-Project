
class AddWordGUI():
    def __init__(self, master, learnset_controller, learnset):
        self.learnset_controller = learnset_controller
        self.master = master
        self.learnset = learnset
        
    def handle_add_word_event(self,wordEngl, wordGer, word_image, learnset):
        self.learnset_controller.create_word(self, wordEngl, wordGer, word_image, learnset, wordID=-1)
        
    def handle_close_event(self):
        pass
        
    
        
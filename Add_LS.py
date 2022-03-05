
class AddLearnsetGUI():
    def __init__(self, master, learnset_controller):
        self.learnset_controller = learnset_controller
        self.master = master
        
    def handle_add_learnset_event(self, name):
        self.learnset_controller.add_learnset(name)
        
    def handle_close_event(self):
        pass
        
    
        
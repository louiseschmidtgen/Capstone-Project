from Pop_up_gui import PopUpGUI
from MapGUI import MapGUI
from Learnset_Controller import LearnsetController
class DashboardController():
    def __init__(self, user_object, login_out_controller):
        self.user_object = user_object
        self.login_out_controller = login_out_controller
        self.popup = PopUpGUI()
        self.mapgui = MapGUI()
        self.learnset_controller = LearnsetController(user_object)
        
    def logout_processing(self):
        pass
    
    def popup_account_deletion(self):
        self.popup.create_yes_no_pop_up("Are you sure that you want to delete this account?")
        
    def delete_account_processing(self):
        pass
    
    def open_map(self):
        self.mapgui.create_main_frame()
    
    def open_translator(self):
        pass
    
    def open_learnsets(self):
        self.learnset_controller.create_learnset_menu_gui()
    
    def open_german_holidays():
        pass
    
    def open_login():
        pass
    
    def create_dashboard_gui():
        pass
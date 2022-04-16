from Pop_up_gui import PopUpGUI
from MapGUI import MapGUI
from Learnset_Controller import LearnsetController
from Translator_Controller import Translator_Controller
from Dashboard_GUI import DashboardGUI
from Holidays_Controller import GermanHolidaysController

class DashboardController():
    def __init__(self, user_object, login_out_controller):
        self.user_object = user_object
        self.login_out_controller = login_out_controller
        self.popup = PopUpGUI()
        self.mapgui = None
        self.holiday_controller = None
        self.translator_controller = None
        self.dashboard_gui = None
        self.learnset_controller = LearnsetController(user_object, self)
        
    def logout_processing(self):
        self.login_out_controller.push_changes_to_database(self.user_object)
        
    def popup_account_deletion(self):
        self.popup.create_yes_no_pop_up( "Are you sure that you want to delete this account?", self)
        
    def delete_account_processing(self):
        self.dashboard_gui.hide()
        self.login_out_controller.delete_account(self.user_object)
    
    def open_map(self):
        if self.mapgui == None:
            self.mapgui = MapGUI(self)
            self.mapgui.create_main_frame()
        self.mapgui.show()
        self.dashboard_gui.hide()
    
    def open_translator(self):
        if self.translator_controller == None:
            self.translator_controller = Translator_Controller(self)
            self.translator_controller.create_translator_gui()
        
        self.dashboard_gui.hide()
    
    def open_learnsets(self):
        self.learnset_controller.create_learnset_menu_gui()
        self.dashboard_gui.hide()
        
    def open_german_holidays(self):
        if self.holiday_controller == None:
            self.holiday_controller = GermanHolidaysController(self)
            self.holiday_controller.create_holidays_gui()
        self.dashboard_gui.hide()
    
    def open_login(self):
        self.login_out_controller.create_login_gui()
        self.dashboard_gui.hide()
        
    def create_dashboard_gui(self):
        if self.dashboard_gui == None:
            self.dashboard_gui = DashboardGUI(self)
            self.dashboard_gui.createMainFrame()
        self.dashboard_gui.show()
        
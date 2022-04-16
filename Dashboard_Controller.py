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
        """This function invokes push_changes_to_database function in login logout controller."""
        self.login_out_controller.push_changes_to_database(self.user_object)
        
    def popup_account_deletion(self):
        """This function creates popup GUI with prompt asking about confirming account deletion."""
        self.popup.create_yes_no_pop_up( "Are you sure that you want to delete this account?", self)
        
    def delete_account_processing(self):
        """This function invokes delete_account function in login logout controller."""
        self.dashboard_gui.hide()
        self.login_out_controller.delete_account(self.user_object)
    
    def open_map(self):
        """This function opens Map GUI."""
        if self.mapgui == None:
            self.mapgui = MapGUI(self)
            self.mapgui.create_main_frame()
        self.mapgui.show()
        self.dashboard_gui.hide()
    
    def open_translator(self):
        """This function opens Translator GUI"""
        if self.translator_controller == None:
            self.translator_controller = Translator_Controller(self)
            self.translator_controller.create_translator_gui()
        
        self.dashboard_gui.hide()
    
    def open_learnsets(self):
        """This function calls learnset controller to create learnset Menu GUI."""
        self.learnset_controller.create_learnset_menu_gui()
        self.dashboard_gui.hide()
        
    def open_german_holidays(self):
        """This function calls holiday controller to open Holiday GUI."""
        if self.holiday_controller == None:
            self.holiday_controller = GermanHolidaysController(self)
            self.holiday_controller.create_holidays_gui()
        self.dashboard_gui.hide()
    
    def open_login(self):
        """This function calls Login Logout Controller to create the Login GUI."""
        self.login_out_controller.create_login_gui()
        self.dashboard_gui.hide()
        
    def create_dashboard_gui(self):
        """This function creates the dasboard GUI."""
        if self.dashboard_gui == None:
            self.dashboard_gui = DashboardGUI(self)
            self.dashboard_gui.createMainFrame()
        self.dashboard_gui.show()
        
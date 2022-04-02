from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
# this class controls the graphical user interface of the Pop up window and what it displays.
#  The attibute message is what will be displayed. Its methods are createPopUp()
class PopUpGUI():
    def __init__(self):
        pass

    def createPopUp(self, message, title="Pop Up"):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        x = msg.exec_() 
    
    def create_yes_no_pop_up(self, message, dashboard_obj, title="Pop Up", ):
        def popup_clicked( i):
            print(i.text())
            if i.text() == "&Yes":
                dashboard_obj.delete_account_processing()
            else:
                pass
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No ) 
        msg.buttonClicked.connect(popup_clicked)
        msg.setText(message)
        x = msg.exec_() 
        

                


        

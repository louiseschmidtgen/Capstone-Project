from PyQt5.QtWidgets import QMessageBox

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
    
    def create_yes_no_pop_up(self, message, title="Pop Up"):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No ) 
        msg.buttonClicked.connect(self.popup_clicked)
        msg.setText(message)
        x = msg.exec_() 
        
    def popup_clicked(self, i):
        if i.text() == "Yes":
            pass
        else:
            self.hide()
                
    def create_pop_up_with_picture(self, message, image="images/sth.png"):
        pass

        

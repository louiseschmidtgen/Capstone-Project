from PyQt5 import QtCore, QtGui, QtWidgets

import bookPopout
import mainmenu


class BookPopoutWindow(QtWidgets.QMainWindow, bookPopout.BookPopout):
    def __init__(self, parent=None):
        super(BookPopoutWindow, self).__init__(parent)
        self.setupUi(self)


class MainMenu(QtWidgets.QMainWindow, mainmenu.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainMenu, self).__init__(parent)
        self.setupUi(self)
        self.createNewBookButton.clicked.connect(self.openNewBook)
        self.popups = []

    @QtCore.pyqtSlot()
    def openNewBook(self):
        popWin = BookPopoutWindow()
        popWin.show()
        self.popups.append(popWin)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainMenu()
    w.show()
    sys.exit(app.exec_())
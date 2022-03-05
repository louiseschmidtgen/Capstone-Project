import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QAction
from Login_GUI import LogInGUI

def main():
    app = QApplication(sys.argv)
    ex = LogInGUI()
    ex.setWindowTitle('GGA: Login Window ')
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
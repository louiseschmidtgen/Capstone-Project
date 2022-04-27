import sys

from PyQt5.QtWidgets import QWidget, QApplication, QDialog, QGridLayout, QLabel, QLineEdit
from PyQt5.Qt import QHBoxLayout, QWindow, QMainWindow, QVBoxLayout


class Example(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)            
        self.initUI()

    def initUI(self):
        vlayout = QVBoxLayout()
        hlayout1 = QHBoxLayout()
        hlayout2 = QHBoxLayout()
        widget = QWidget()
        widget.setLayout(vlayout)

        a1 = QLabel('label1')
        a2 = QLabel('label2')
        hlayout1.addWidget(a1)
        hlayout1.addWidget(a2)
        hlayout1.addStretch(2)
        vlayout.addLayout(hlayout1)
        vlayout.addStretch(1)
        a3 = QLabel('label3')
        a4 = QLabel('label3')
        hlayout2.addWidget(a3)
        hlayout2.addWidget(a4)
        hlayout2.addStretch(1)
        vlayout.addLayout(hlayout2)
        vlayout.addStretch(1)

        self.setCentralWidget(widget)

        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Lines')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
#     ex.show()
    sys.exit(app.exec_())
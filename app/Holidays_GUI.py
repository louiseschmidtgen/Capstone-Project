from PyQt5.QtWidgets import QMainWindow, QGridLayout, QLineEdit, QFormLayout, QWidget, QPushButton, QApplication, QAction, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt


class GermanHolidaysGUI(QWidget):
    def __init__(self,  holiday_controller):
        super().__init__()
        self.holiday_controller = holiday_controller

    def create_main_frame(self):
        """ This function builds the GUI using Grid Layout."""
        self.setWindowTitle('GGA: German Holidays')
        self.setGeometry(100, 100, 280, 80)
        self.move(60, 15)
        layout = QGridLayout()

        # Logo:
        self.logo_label = QLabel(self)
        self.logo_pixmap = QPixmap('images/GGA_logo.png')
        smaller_pixmap = self.logo_pixmap.scaled(
            100, 100, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.logo_label.setPixmap(smaller_pixmap)
        # Buttons
        self.exit_button = QPushButton("Exit")
        self.exit_button.setObjectName("Exit")
        self.exit_button.clicked.connect(self.handle_close_window)

        self.carnival_button = QPushButton("i")
        self.carnival_button.setObjectName("i")
        self.carnival_button.clicked.connect(
            lambda: self.handle_info_request("Carnival"))

        self.christmas_button = QPushButton("i")
        self.christmas_button.setObjectName("i")
        self.christmas_button.clicked.connect(
            lambda: self.handle_info_request("Christmas"))

        self.oktoberfest_button = QPushButton("i")
        self.oktoberfest_button.setObjectName("i")
        self.oktoberfest_button.clicked.connect(
            lambda: self.handle_info_request("Oktoberfest"))

        self.gud_button = QPushButton("i")
        self.gud_button.setObjectName("i")
        self.gud_button.clicked.connect(
            lambda: self.handle_info_request("German Unity Day"))

        self.holocaust_mem_button = QPushButton("i")
        self.holocaust_mem_button.setObjectName("i")
        self.holocaust_mem_button.clicked.connect(
            lambda: self.handle_info_request("Holocaust Memorial"))

        layout.addWidget(self.logo_label, 0, 0)
        layout.addWidget(QLabel("German Holidays"), 0, 1)
        layout.addWidget(self.carnival_button, 1, 2)
        layout.addWidget(QLabel("Carnival"), 1, 1)
        layout.addWidget(QLabel("Christmas"), 2, 1)
        layout.addWidget(self.christmas_button, 2, 2)
        layout.addWidget(QLabel("Oktoberfest"), 3, 1)
        layout.addWidget(self.oktoberfest_button, 3, 2)
        layout.addWidget(QLabel("German Unity Day"), 4, 1)
        layout.addWidget(self.gud_button, 4, 2)
        layout.addWidget(QLabel("Holocaust Memorial Day"), 5, 1)
        layout.addWidget(self.holocaust_mem_button, 5, 2)
        layout.addWidget(self.exit_button, 6, 2)

        self.setLayout(layout)
        self.show()

    def handle_info_request(self, holiday):
        """This function invokes display_pop_up_with_info_on_holiday function in the holiday controller

        Args:
            holiday (str): name of holiday
        """
        print(holiday)
        self.holiday_controller.display_pop_up_with_info_on_holiday(holiday)

    def handle_close_window(self):
        """This function invokes create_dashboard_gui function in holiday controller."""
        self.hide()
        self.holiday_controller.create_dashboard_gui()

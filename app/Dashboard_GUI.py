from PyQt5.QtWidgets import QMainWindow, QGridLayout, QLineEdit, QFormLayout, QWidget, QPushButton, QApplication, QAction, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt


class DashboardGUI(QWidget):
    def __init__(self, dashboard_controller):
        super().__init__()
        self.dashboard_controller = dashboard_controller

    def createMainFrame(self):
        """This function builds the GUI using Grid Layout."""
        self.setWindowTitle('GGA: Dashboard Window ')
        self.setGeometry(100, 100, 280, 80)
        self.move(60, 15)
        layout = QGridLayout()

        # Logo:
        self.logo_label = QLabel(self)
        self.logo_pixmap = QPixmap('images/GGA_logo.png')
        smaller_pixmap = self.logo_pixmap.scaled(
            100, 100, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.logo_label.setPixmap(smaller_pixmap)
        # Buttons:
        self.learnset_button = QPushButton("Learnsets")
        self.learnset_button.setObjectName("learnsets")
        self.learnset_button.clicked.connect(self.handle_learnsets)

        self.translator_button = QPushButton("Translator")
        self.translator_button.setObjectName("translator")
        self.translator_button.clicked.connect(self.handle_translator)

        self.holiday_button = QPushButton("German Holidays")
        self.holiday_button.setObjectName("holidays")
        self.holiday_button.clicked.connect(self.handle_german_holidays)

        self.map_button = QPushButton("Map")
        self.map_button.setObjectName("map")
        self.map_button.clicked.connect(self.handle_map)

        self.exit_button = QPushButton("Exit")
        self.exit_button.setObjectName("Exit")
        self.exit_button.clicked.connect(self.log_out_event)

        self.delete_button = QPushButton("Delete Account")
        self.delete_button.setObjectName("Delete")
        self.delete_button.clicked.connect(self.delete_account_event)

        layout.addWidget(self.logo_label, 0, 0)
        layout.addWidget(self.learnset_button, 1, 1)
        layout.addWidget(self.translator_button, 2, 1)
        layout.addWidget(self.holiday_button, 3, 1)
        layout.addWidget(self.map_button, 4, 1)
        layout.addWidget(self.exit_button, 5, 2)
        layout.addWidget(self.delete_button, 5, 0)
        self.setLayout(layout)
        self.show()

    def log_out_event(self):
        """This function invokes logout_processing function in dashboard controller."""
        self.hide()
        self.dashboard_controller.logout_processing()

    def delete_account_event(self):
        """This function invokes popup_account_deletion function in dashboard controller."""
        self.dashboard_controller.popup_account_deletion()

    def handle_map(self):
        """This function invokes open_map function in dashboard controller."""
        self.hide()
        self.dashboard_controller.open_map()

    def handle_translator(self):
        """This function invokes open_translator function in dashboard controller."""
        self.hide()
        self.dashboard_controller.open_translator()

    def handle_learnsets(self):
        """This function invokes open_learnsets function in dashboard controller."""
        self.hide()
        self.dashboard_controller.open_learnsets()

    def handle_german_holidays(self):
        """This function invokes open_german_holidays function in dashboard controller."""
        self.hide()
        self.dashboard_controller.open_german_holidays()

from PyQt5.QtWidgets import QGridLayout, QMainWindow, QLineEdit, QFormLayout, QWidget, QPushButton, QApplication, QAction, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt


class TranslatorGUI(QWidget):
    def __init__(self, translator_controller):
        super().__init__()
        self.translator_controller = translator_controller

    def create_main_frame(self):
        """This function builds the GUI using Grid Layout."""
        self.setWindowTitle('GGA: Translator Window ')
        self.setGeometry(100, 100, 280, 80)
        self.move(60, 15)

        layout = QGridLayout()

        # Logo:
        self.logo_label = QLabel(self)
        self.logo_pixmap = QPixmap('images/GGA_logo.png')
        smaller_pixmap = self.logo_pixmap.scaled(
            100, 100, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.logo_label.setPixmap(smaller_pixmap)

        info = "For ß use ss\nFor ä use ae \nFor ü use ue \nFor ö use oe"
        self.info_label = QLabel(info)

        self.german_label = QLabel("German: ")
        self.german_label.setObjectName("LangLabel")
        self.engl_label = QLabel("English: ")
        self.engl_label.setObjectName("LangLabel")
        self.german_label2 = QLabel("German: ")
        self.german_label2.setObjectName("LangLabel")
        self.engl_label2 = QLabel("English: ")
        self.engl_label2.setObjectName("LangLabel")

        # Buttons
        self.exit_button = QPushButton("Exit")
        self.exit_button.setObjectName("Exit")
        self.exit_button.clicked.connect(self.handle_close_window)

        self.translate_e2g = QPushButton("Translate to German")
        self.translate_e2g.setObjectName("Translator")
        self.translate_e2g.clicked.connect(self.handle_e2g_translation)

        self.translate_g2e = QPushButton("Translate to English")
        self.translate_g2e.setObjectName("Translator")
        self.translate_g2e.clicked.connect(self.handle_g2e_translation)

        # Entry fields:
        self.in_engl = QLineEdit()
        self.in_ger = QLineEdit()
        # Output fields labels need to change
        self.out_ger = QLabel("")
        self.out_engl = QLabel("")

        # Layout
        layout.addWidget(self.logo_label, 0, 0)
        layout.addWidget(QLabel("Translator"), 0, 1)
        layout.addWidget(self.translate_e2g, 1, 1)
        layout.addWidget(self.engl_label, 2, 0)
        layout.addWidget(self.german_label, 2, 1)
        layout.addWidget(self.in_engl, 3, 0)
        layout.addWidget(self.out_ger, 3, 1)
        layout.addWidget(self.translate_g2e, 4, 1)
        layout.addWidget(self.german_label2, 5, 0)
        layout.addWidget(self.engl_label2, 5, 1)
        layout.addWidget(self.in_ger, 6, 0)
        layout.addWidget(self.out_engl, 6, 1)
        layout.addWidget(self.info_label, 7, 0)
        layout.addWidget(self.exit_button, 7, 1)

        # set layout
        self.setLayout(layout)

    def handle_e2g_translation(self, ):
        """gets word, calls translator controller to translate it and displays the translation."""
        engl_word = self.in_engl.text()
        translation = self.translator_controller.get_e2g_tranlation(engl_word)
        self.out_ger.setText(translation)

    def handle_g2e_translation(self):
        """gets word, calls translator controller to translate it and displays the translation."""
        ger_word = self.in_ger.text()
        translation = self.translator_controller.get_g2e_tranlation(ger_word)
        self.out_engl.setText(translation)

    def handle_close_window(self):
        """This function invokes close_translator function in translator controller."""
        self.hide()
        self.translator_controller.close_translator()

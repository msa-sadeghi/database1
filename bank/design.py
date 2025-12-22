from PyQt5.QtWidgets import (
    QWidget,
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
)
from ui.login import Ui_Dialog


class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 300, 200)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def login(self):
        if 1 == 1:
            self.accept()

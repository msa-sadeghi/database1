from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox

from ui_login import Ui_Dialog


class LoginForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
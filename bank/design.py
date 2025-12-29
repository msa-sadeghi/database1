from PyQt5.QtWidgets import (
    QWidget,
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMainWindow
)
from ui.login import Ui_Dialog
from ui.main_windows import Ui_MainWindow
from auth_manager import AuthManager


class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 300, 200)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.login)

    def login(self):
        a = AuthManager()
        if a.login(self.ui.lineEdit_2.text(), self.ui.lineEdit.text()):
            self.accept()
        else:
            self.reject()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
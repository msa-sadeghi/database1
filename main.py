import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from login_form import LoginForm
from db import Database
from main_form import MainWindow

app  = QApplication(sys.argv)
login = LoginForm()

if login.exec_() == LoginForm.Accepted:
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
else:
    print("not valid")



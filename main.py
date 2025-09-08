import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from login_form import LoginForm
from db import Database


app  = QApplication(sys.argv)
login = LoginForm()

if login.exec_() == LoginForm.Accepted:
    print("login success")
else:
    print("not valid")

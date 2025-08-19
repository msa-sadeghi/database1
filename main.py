import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from login_form import LoginForm
from db import Database


app  = QApplication(sys.argv)
login = LoginForm()
login.show()
sys.exit(app.exec_())
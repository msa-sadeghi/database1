from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from student_form import Ui_Dialog

from db import Database

class StudentForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


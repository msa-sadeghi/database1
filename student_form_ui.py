from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from student_form import Ui_Dialog
from db import Database
class StudentForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.db = Database()
        self.load_students()

    def load_students(self):
        rows = self.db.fetchall('SELECT * FROM students')
        self.ui.table_students.setColumnCount(len(dict(rows[0]).keys()))
        self.ui.table_students.setHorizontalHeaderLabels(dict(rows[0]).keys())
        for row_num, row in enumerate(rows):
            self.ui.table_students.insertRow(row_num)
            col_index = 0
            for col_num, data in dict(row).items():
                self.ui.table_students.setItem(row_num, col_index, QTableWidgetItem(str(data)))
                col_index += 1



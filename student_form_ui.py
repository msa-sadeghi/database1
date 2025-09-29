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
        self.ui.add_button.clicked.connect(self.add_student)
        self.ui.delete_button.clicked.connect(self.delete_student)
        self.ui.update_button.clicked.connect(self.update_student)

    def load_students(self):
        rows = self.db.fetchall('SELECT * FROM students')
        self.ui.table_students.setColumnCount(len(dict(rows[0]).keys()))
        self.ui.table_students.setHorizontalHeaderLabels(dict(rows[0]).keys())
        self.ui.table_students.setRowCount(0)
        for row_num, row in enumerate(rows):
            self.ui.table_students.insertRow(row_num)
            col_index = 0
            for col_num, data in dict(row).items():
                self.ui.table_students.setItem(row_num, col_index, QTableWidgetItem(str(data)))
                col_index += 1


    def add_student(self):
        firstname = self.ui.first_name_input.text()
        lastname = self.ui.last_name_input.text()
        classid = self.ui.class_id_input.text()

        self.db.execute('INSERT INTO students (first_name, last_name, class_id) VALUES (%s, %s, %s)',
                        (firstname, lastname, classid)
                        )
        
        self.load_students()


    def delete_student(self):
        row_number = self.ui.table_students.currentRow()

        studet_id = self.ui.table_students.item(row_number,  0).text()
        self.db.execute('DELETE FROM students WHERE id=%s ', (studet_id,))
        self.load_students()

    def update_student(self):
        row_number = self.ui.table_students.currentRow()
        studet_id = self.ui.table_students.item(row_number,  0).text()
        firstname = self.ui.first_name_input.text()
        lastname = self.ui.last_name_input.text()
        classid = self.ui.class_id_input.text()

        self.db.execute('UPDATE students SET first_name=%s, last_name=%s, class_id=%s WHERE id=%s',
                        (firstname, lastname,classid, studet_id))
        self.load_students()

        



from PyQt5.QtWidgets import QMainWindow, QMessageBox
from main_window import Ui_MainWindow
from student_form_ui import StudentForm
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionExit.triggered.connect(self.close_app)
        self.ui.actionManage_Students.triggered.connect(self.open_students)
        self.ui.actionManage_Classes.triggered.connect(self.open_classes)
        self.ui.actionManage_Subjects.triggered.connect(self.open_subjects)
        self.ui.actionEnroll_Student.triggered.connect(self.open_enrollments)

    def close_app(self):
        self.close()
    
    def open_students(self):
        dialog = StudentForm()
        dialog.exec_()
    def open_classes(self):
        pass
    def open_subjects(self):
        pass
    def open_enrollments(self):
        pass
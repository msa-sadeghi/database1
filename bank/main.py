from PyQt5.QtWidgets import QApplication
from design import LoginWindow, MainWindow

app = QApplication([])
window = LoginWindow()
if window.exec_():
    main = MainWindow()
    main.show()
app.exec_()

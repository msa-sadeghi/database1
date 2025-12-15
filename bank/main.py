from PyQt5.QtWidgets import QApplication
from design import LoginWindow

app = QApplication([])
window = LoginWindow()
window.show()
app.exec_()
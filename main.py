import sys

from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets

from main_win import Ui_MainWindow

class Mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.configure()

    def configure(self):
        self.ok_button.clicked.connect(self.change_label_after_click)

    def change_label_after_click(self):
        self.label_1.setText('1')
        self.label_2.setText('2')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    win = Mywindow()
    win.show()

    app.exec_()
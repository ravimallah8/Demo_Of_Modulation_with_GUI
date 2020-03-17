import sys
from PyQt5 import QtCore,QtGui
from PyQt5.QtWidgets import *

from modulations import *
from main_window import Ui_MainWindow
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.exitButton.clicked.connect(qApp.exit)
        self.amButton.clicked.connect(amAnimation)
        self.fmButton.clicked.connect(fmAnimation)
        self.pmButton.clicked.connect(pmAnimation)
        self.pamButton.clicked.connect(pamAnimation)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
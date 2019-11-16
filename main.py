# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UI import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Hide Window Title
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.exit = QShortcut(QKeySequence("Ctrl+D"), self)
        self.exit.activated.connect(self.exitEvent)

    def exitEvent(self):
        sys.exit()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
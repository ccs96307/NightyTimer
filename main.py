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
        self.setWindowOpacity(0.9)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setCursor(Qt.CrossCursor)

        # LCD
        self.ui.lcdNumber.display('00:00')

        # Button
        self.start = True
        self.sec = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.LCDEvent)
        self.ui.pushButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.ui.pushButton.clicked.connect(self.timeGo)

        # Shortcut
        self.exit = QShortcut(QKeySequence("Ctrl+D"), self)
        self.exit.activated.connect(self.exitEvent)

    def timeGo(self):
        if self.start:
            self.ui.pushButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
            self.timer.start(1000)
            self.start = False
        else:
            self.ui.pushButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
            self.timer.stop()
            self.start = True

    def LCDEvent(self):
        self.sec += 1

        hour = self.sec//60
        sec = self.sec%60
        self.ui.lcdNumber.display('%02d:%02d' % (hour, sec))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moveFlag = True
            self.movePosition = event.globalPos() - self.pos()
            self.setCursor(QCursor(Qt.OpenHandCursor))
            event.accept()

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.moveFlag:
            self.move(event.globalPos() - self.movePosition)
            event.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.moveFlag = False
        self.setCursor(Qt.CrossCursor)

    def exitEvent(self):
        sys.exit()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


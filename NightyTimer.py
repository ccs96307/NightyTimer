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
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowOpacity(0.9)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setCursor(Qt.CrossCursor)
        self.screenWidth = QDesktopWidget().screenGeometry().width()
        self.screenHeight = QDesktopWidget().screenGeometry().height()

        # LCD
        self.ui.lcdNumber.setDigitCount(8)
        self.ui.lcdNumber.display('00:00:00')

        # Button
        self.start = True
        self.sec = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.LCDEvent)
        self.ui.pushButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.ui.pushButton.clicked.connect(self.timeGo)
        self.ui.pushButton_2.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.ui.pushButton_2.clicked.connect(self.initTime)
        self.ui.pushButton_3.setIcon(self.style().standardIcon(QStyle.SP_DialogCancelButton))
        self.ui.pushButton_3.clicked.connect(self.exitEvent)

        # Shortcut
        self.startShortcut = QShortcut(QKeySequence("Ctrl+s"), self)
        self.startShortcut.activated.connect(self.timeGo)

        self.leftMove = QShortcut(QKeySequence("Ctrl+left"), self)
        self.rightMove = QShortcut(QKeySequence("Ctrl+right"), self)
        self.upMove = QShortcut(QKeySequence("Ctrl+up"), self)
        self.downMove = QShortcut(QKeySequence("Ctrl+down"), self)

        self.leftMove.activated.connect(lambda: self.shortcutMoveEvent('left'))
        self.rightMove.activated.connect(lambda: self.shortcutMoveEvent('right'))
        self.upMove.activated.connect(lambda: self.shortcutMoveEvent('up'))
        self.downMove.activated.connect(lambda: self.shortcutMoveEvent('down'))

        self.exit = QShortcut(QKeySequence("Ctrl+D"), self)
        self.exit.activated.connect(self.exitEvent)

    def initTime(self):
        self.ui.lcdNumber.display('00:00:00')
        self.sec = 0
        self.start = True
        self.ui.pushButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.timer.stop()

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

        hour = self.sec//3600
        min = self.sec%3600//60
        sec = self.sec%60
        print(hour, min, sec)

        self.ui.lcdNumber.display('%02d:%02d:%02d' % (hour, min, sec))

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

    def shortcutMoveEvent(self, direction):
        if direction == 'left':
            self.move(QPoint(0, self.pos().y()))
        elif direction == 'right':
            self.move(QPoint(self.screenWidth-self.width(), self.pos().y()))
        elif direction == 'up':
            self.move(QPoint(self.pos().x(), 0))
        elif direction == 'down':
            self.move(QPoint(self.pos().x(), self.screenHeight-self.height()))

    def exitEvent(self):
        sys.exit()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


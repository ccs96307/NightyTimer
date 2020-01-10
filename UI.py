# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(411, 151)
        MainWindow.setStyleSheet("    background:gray;\n"
"    border-top:1px solid white;\n"
"    border-bottom:1px solid white;\n"
"    border-left:1px solid white;\n"
"    border-right:1px solid white;\n"
"    border-top-left-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"    border-top-right-radius:10px;\n"
"    border-bottom-right-radius:10px;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 411, 111))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(155, 110, 100, 39))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(150, 150, 150);\n"
"border-style:none;\n"
"border:1px solid #3f3f3f; \n"
"\n"
"padding:5px;\n"
"min-height:20px;\n"
"border-radius:35px;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(0, 0, 411, 111))
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(55, 110, 100, 39))
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(150, 150, 150);\n"
"border-style:none;\n"
"border:1px solid #3f3f3f; \n"
"\n"
"padding:5px;\n"
"min-height:20px;\n"
"border-radius:35px;")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(255, 110, 100, 39))
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(150, 150, 150);\n"
"border-style:none;\n"
"border:1px solid #3f3f3f; \n"
"\n"
"padding:5px;\n"
"min-height:20px;\n"
"border-radius:35px;")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.raise_()
        self.pushButton_2.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.lcdNumber.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

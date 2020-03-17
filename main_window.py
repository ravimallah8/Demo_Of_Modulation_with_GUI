# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 550)
        MainWindow.setMinimumSize(QtCore.QSize(320, 550))
        MainWindow.setMaximumSize(QtCore.QSize(320, 550))
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color: #ffffff;\n"
"\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.amButton = QtWidgets.QPushButton(self.centralwidget)
        self.amButton.setGeometry(QtCore.QRect(10, 160, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.amButton.setFont(font)
        self.amButton.setStyleSheet("QPushButton{\n"
"    background-color: #FB5E6F;\n"
"    border-width: 20px;\n"
"    border-radius: 25px;\n"
"}\n"
"QPushButton:pressed{\n"
"    font-size: 14px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 255, 86, 255), stop:0.840909 rgba(255, 255, 0, 255));\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 255, 86, 255), stop:0.840909 rgba(255, 255, 0, 255));\n"
"}")
        self.amButton.setObjectName("amButton")
        self.fmButton = QtWidgets.QPushButton(self.centralwidget)
        self.fmButton.setGeometry(QtCore.QRect(10, 220, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fmButton.setFont(font)
        self.fmButton.setStyleSheet("QPushButton{\n"
"    background-color: #FB5E6F;\n"
"    border-width: 20px;\n"
"    border-radius: 25px;\n"
"}\n"
"QPushButton:pressed{\n"
"    font-size: 14px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 255, 86, 255), stop:0.840909 rgba(255, 255, 0, 255));\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 255, 86, 255), stop:0.840909 rgba(255, 255, 0, 255));\n"
"}")
        self.fmButton.setObjectName("fmButton")
        self.pmButton = QtWidgets.QPushButton(self.centralwidget)
        self.pmButton.setGeometry(QtCore.QRect(10, 280, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pmButton.setFont(font)
        self.pmButton.setStyleSheet("QPushButton{\n"
"    background-color: #FB5E6F;\n"
"    border-width: 20px;\n"
"    border-radius: 25px;\n"
"}\n"
"QPushButton:pressed{\n"
"    font-size: 14px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 255, 86, 255), stop:0.840909 rgba(255, 255, 0, 255));\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 255, 86, 255), stop:0.840909 rgba(255, 255, 0, 255));\n"
"}")
        self.pmButton.setObjectName("pmButton")
        self.pamButton = QtWidgets.QPushButton(self.centralwidget)
        self.pamButton.setGeometry(QtCore.QRect(10, 340, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pamButton.setFont(font)
        self.pamButton.setStyleSheet("QPushButton{\n"
"    background-color: #FB5E6F;\n"
"    border-width: 20px;\n"
"    border-radius: 25px;\n"
"}\n"
"QPushButton:pressed{\n"
"    font-size: 14px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 255, 86, 255), stop:0.840909 rgba(255, 255, 0, 255));\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 255, 86, 255), stop:0.840909 rgba(255, 255, 0, 255));\n"
"}")
        self.pamButton.setObjectName("pamButton")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(70, 480, 181, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet("QPushButton{\n"
"    background-color: #fcba03;\n"
"    border-width: 25px;\n"
"    border-radius: 25px;\n"
"}\n"
"QPushButton:pressed{\n"
"    font-size : 25px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 91, 255, 255), stop:1 rgba(41, 255, 255, 255));\n"
"    color: #ffffff;\n"
"}\n"
"QPushButton:hover{\n"
"        background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 91, 255, 255), stop:1 rgba(41, 255, 255, 255));\n"
"}")
        self.exitButton.setObjectName("exitButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 30, 101, 101))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo.svg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Demo of Modulation"))
        self.amButton.setText(_translate("MainWindow", "AMPLITUDE MODULATION"))
        self.fmButton.setText(_translate("MainWindow", "FREQUENCY MODULATION"))
        self.pmButton.setText(_translate("MainWindow", "PHASE MODUALTION"))
        self.pamButton.setText(_translate("MainWindow", "PULSE AMPLITUDE MODULATION"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))


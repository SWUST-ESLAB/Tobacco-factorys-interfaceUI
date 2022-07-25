# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log_in.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1270, 709)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1271, 711))
        self.label.setStyleSheet("background-image: url(:/bg/log720.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(724, 350, 200, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(724, 419, 200, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(660, 500, 121, 41))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("\n"
"\n"
"QPushButton {border-radius: 10px;  \n"
"    border: 2px groove gray;background-color:rgba(255, 255, 255,255);\n"
" } QPushButton:hover { background-color: rgb(67, 126, 207); }")
        self.pushButton.setObjectName("pushButton")
        "self.pushButton.clicked.connect(self.demo_ui)"
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(810, 500, 121, 41))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("\n"
"\n"
"QPushButton {border-radius: 10px;  \n"
"    border: 2px groove gray;background-color:rgba(255, 255, 255,255);\n"
" } QPushButton:hover { background-color: rgb(67, 126, 207); }")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "红丝数据可视化软件V1.0"))
        self.pushButton.setText(_translate("Form", "登陆"))
        self.pushButton_2.setText(_translate("Form", "退出"))


import demo

from cmath import log
import logging
import sys
from PyQt5 import QtWidgets, QtCore
from log_in import Ui_Form
from main_interface import login


app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
wi=QtWidgets.QWidget()
widget.resize(1920, 1080)
widget.setWindowTitle("hello, pyqt5")



ui = Ui_Form()
ui.setupUi(widget)
widget.show()

A = login()
A.setupUi(wi)
ui.pushButton.clicked.connect(lambda:{widget.close(),wi.show()})
sys.exit(app.exec_())
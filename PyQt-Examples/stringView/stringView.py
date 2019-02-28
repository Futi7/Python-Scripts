# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stringView.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *

class Ui_MainWindow(object):
    global counter
    counter = 0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 262)
        MainWindow.setStyleSheet(".QPushButton\n"
"{\n"
"color: #fff;\n"
"  background-color: #8a6d3b;\n"
"  border-color: #8a6d3b;\n"
"}\n"
".QLabel\n"
"{\n"
"    text-align:center;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(240, 180, 89, 25))
        self.next.setStyleSheet("")
        self.next.setObjectName("next")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(130, 180, 89, 25))
        self.back.setObjectName("back")
        self.tag = QtWidgets.QLabel(self.centralwidget)
        self.tag.setGeometry(QtCore.QRect(200, 90, 67, 17))
        self.tag.setAlignment(QtCore.Qt.AlignCenter)
        self.tag.setObjectName("tag")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        string = ["Emin","Yusuf","Fuat"]
        self.next.clicked.connect(lambda : self.ilerle(string))
        self.back.clicked.connect(lambda : self.geri(string))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.next.setText(_translate("MainWindow", "Next"))
        self.back.setText(_translate("MainWindow", "Back"))
        self.tag.setText(_translate("MainWindow", "Veri"))

    def ilerle(self,string):
        global counter
        counter += 1
        self.tag.setText(string[counter])
        print(counter)

    def geri(self,string):
        global counter
        counter -= 1
        self.tag.setText(string[counter])
        print(counter)
    
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

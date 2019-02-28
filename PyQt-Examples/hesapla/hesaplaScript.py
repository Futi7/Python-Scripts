# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hesapla.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 402)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 190, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.cevap = QtWidgets.QLabel(self.centralwidget)
        self.cevap.setGeometry(QtCore.QRect(180, 160, 67, 17))
        self.cevap.setObjectName("cevap")
        self.ilk = QtWidgets.QTextEdit(self.centralwidget)
        self.ilk.setGeometry(QtCore.QRect(150, 120, 51, 31))
        self.ilk.setObjectName("ilk")
        self.iki = QtWidgets.QTextEdit(self.centralwidget)
        self.iki.setGeometry(QtCore.QRect(210, 120, 51, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iki.sizePolicy().hasHeightForWidth())
        self.iki.setSizePolicy(sizePolicy)
        self.iki.setObjectName("iki")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 130, 16, 17))
        self.label_2.setObjectName("label_2")
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

        
        self.pushButton.clicked.connect(self.hesaplaFonksiyon)
        



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Hesapla"))
        self.cevap.setText(_translate("MainWindow", "Cevap"))
        self.label_2.setText(_translate("MainWindow", "+"))


    
    def hesaplaFonksiyon(self):
     cevap1 = int(self.ilk.toPlainText())+int(self.iki.toPlainText())
     self.cevap.setText(str(cevap1))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

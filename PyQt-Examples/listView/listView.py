# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listView2.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QDialog

class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(502, 250)
        self.list = QtWidgets.QListWidget(Dialog)
        self.list.setGeometry(QtCore.QRect(40, 10, 256, 192))
        self.list.setObjectName("list")
        self.Add = QtWidgets.QPushButton(Dialog)
        self.Add.setGeometry(QtCore.QRect(400, 10, 89, 25))
        self.Add.setObjectName("Add")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 50, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.Add.clicked.connect(self.AddData)


    def AddData(self):
        row = self.list.currentRow()
        text, ok = QInputDialog.getText(self, "Employee Dialog", "Enter EMployee")
        if ok and text is not None:
            self.list.insertItem(row, text)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Add.setText(_translate("Dialog", "Add"))
        self.pushButton_2.setText(_translate("Dialog", "Delete"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):  


    global pizzaCounter
    pizzaCounter = 0
    global kolaCounter
    kolaCounter = 0
    global fiyat
    fiyat = 0



    def guncelle(self):
        global fiyat

        self.Fiyat.setText(str(fiyat)+" tl")


    def pizzaEkle(self):
        global fiyat
        global pizzaCounter
        pizzaCounter += 1
        fiyat = fiyat + 15
        self.listWidget.addItem("Pizza")
        self.guncelle()

    def kolaEkle(self):
        global fiyat
        global kolaCounter
        kolaCounter += 1
        fiyat = fiyat + 5
        self.listWidget.addItem("Kola")
        self.guncelle()

    def musteriEkle(self):
        global pizzaCounter
        global kolaCounter
        global fiyat
        musteriIsim = str(self.Musteri.text())
        client_items = self.listWidget.findItems(
            "Pizza",
            QtCore.Qt.MatchExactly
        )
        for item in reversed(client_items):
            row = self.listWidget.row(item)
            it = self.listWidget.takeItem(row)
            del it
        kola_items = self.listWidget.findItems(
            "Kola",
            QtCore.Qt.MatchExactly
        )
        for item in reversed(kola_items):
            row = self.listWidget.row(item)
            it = self.listWidget.takeItem(row)
            del it


        self.listWidget.addItem(musteriIsim + " " * 12 + str(pizzaCounter) + "xPizza" + " " * 12 + str(
            kolaCounter) + "xKola" + " " * 12 + str(fiyat) + "tl")
        fiyat = 0
        pizzaCounter = 0
        kolaCounter = 0
        self.Musteri.setText("")
        self.guncelle()

    def urunSil(self):
        global fiyat
        row = self.listWidget.currentItem().text()
        if row == 'Pizza':
            fiyat -= 15
        else:
            fiyat -=5

        row = self.listWidget.currentRow()
        self.listWidget.takeItem(row)
        self.guncelle()




    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 615)
        MainWindow.setStyleSheet(".QPushButton {\n"
"  color: #fff;\n"
"  background-color: #337ab7;\n"
"  border-color: #2e6da4;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"  color: #fff;\n"
"  background-color: #286090;\n"
"  border-color: #204d74;\n"
"}\n"
"#Ekle {\n"
"  color: #fff;\n"
"  background-color: #f0ad4e;\n"
"  border-color: #eea236;\n"
"}\n"
"#Ekle:hover {\n"
"  color: #fff;\n"
"  background-color: #ec971f;\n"
"  border-color: #d58512;\n"
"}\n"
"#Sil {\n"
"  color: #fff;\n"
"  background-color: #d9534f;\n"
"  border-color: #d43f3a;\n"
"}\n"
"#Sil:hover {\n"
"  color: #fff;\n"
"  background-color: #c9302c;\n"
"  border-color: #ac2925;\n"
"}\n"
".QLineEdit {\n"
"  display: block;\n"
"  width: 100%;\n"
"  height: 34px;\n"
"  padding: 6px 12px;\n"
"  font-size: 14px;\n"
"  line-height: 1.42857143;\n"
"  color: #555;\n"
"  background-color: #fff;\n"
"  background-image: none;\n"
"  border: 1px solid #ccc;\n"
"  border-radius: 4px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Pizza = QtWidgets.QPushButton(self.centralwidget)
        self.Pizza.setGeometry(QtCore.QRect(30, 20, 101, 51))
        self.Pizza.setObjectName("Pizza")
        self.Kola = QtWidgets.QPushButton(self.centralwidget)
        self.Kola.setGeometry(QtCore.QRect(30, 90, 101, 51))
        self.Kola.setObjectName("Kola")
        self.Sil = QtWidgets.QPushButton(self.centralwidget)
        self.Sil.setGeometry(QtCore.QRect(30, 400, 101, 25))
        self.Sil.setStyleSheet("")
        self.Sil.setObjectName("Sil")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(160, 10, 651, 541))
        self.listWidget.setObjectName("listWidget")
        self.Ekle = QtWidgets.QPushButton(self.centralwidget)
        self.Ekle.setGeometry(QtCore.QRect(30, 440, 101, 25))
        self.Ekle.setObjectName("Ekle")
        self.Fiyat = QtWidgets.QLabel(self.centralwidget)
        self.Fiyat.setGeometry(QtCore.QRect(30, 490, 101, 20))
        self.Fiyat.setAlignment(QtCore.Qt.AlignCenter)
        self.Fiyat.setObjectName("Fiyat")
        self.Musteri = QtWidgets.QLineEdit(self.centralwidget)
        self.Musteri.setGeometry(QtCore.QRect(30, 180, 101, 31))
        self.Musteri.setObjectName("Musteri")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 838, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    

        self.Pizza.clicked.connect(self.pizzaEkle)
        self.Kola.clicked.connect(self.kolaEkle)
        self.Ekle.clicked.connect(self.musteriEkle)
        self.Sil.clicked.connect(self.urunSil)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Pizza.setText(_translate("MainWindow", "Pizza"))
        self.Kola.setText(_translate("MainWindow", "Kola"))
        self.Sil.setText(_translate("MainWindow", "Sil"))
        self.Ekle.setText(_translate("MainWindow", "Ekle"))
        self.Fiyat.setText(_translate("MainWindow", ""))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

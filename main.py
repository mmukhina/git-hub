import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QComboBox
import sqlite3
from PyQt5.QtWidgets import QInputDialog
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 450)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 2, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 8, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 4, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 4, 2, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setReadOnly(False)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_2.addWidget(self.lineEdit_5, 5, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 7, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 6, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_2.addWidget(self.plainTextEdit, 7, 2, 2, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 3, 2, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_2, 6, 2, 1, 1)
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "Степень обжарки:"))
        self.label.setText(_translate("Form", "Объем упаковки:"))
        self.label_2.setText(_translate("Form", "Цена:"))
        self.label_3.setText(_translate("Form", "Описание:"))
        self.label_4.setText(_translate("Form", "Молотый/В зернах"))
        self.label_6.setText(_translate("Form", "Название сорта:"))
        self.comboBox.setItemText(0, _translate("Form", "Слабообжаренный"))
        self.comboBox.setItemText(1, _translate("Form", "Среднеобжаренный"))
        self.comboBox.setItemText(2, _translate("Form", "Сильнообжаренный"))
        self.comboBox_2.setItemText(0, _translate("Form", "Молотый"))
        self.comboBox_2.setItemText(1, _translate("Form", "В зернах"))
        self.pushButton.setText(_translate("Form", "Изменить"))
        self.pushButton_2.setText(_translate("Form", "Новый"))
        self.pushButton_3.setText(_translate("Form", "Сохранить"))

class New_Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Make changes")
        
        self.get_names()

        self.pushButton_2.clicked.connect(self.new)
        self.pushButton.clicked.connect(self.change)
        self.pushButton_3.clicked.connect(self.save)

    def get_names(self):
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM coffee""").fetchall()
        con.close()
        self.names = []
        self.create_new = 1

        for i in result:
            self.names.append(i[1].lower())

    def save(self):
        if self.create_new == 1:
            if self.lineEdit_2.text() == [] or self.lineEdit_2.text().lower() in self.names:
                self.pushButton_3.setStyleSheet("background-color: red")
            else:
                try:
                    con = sqlite3.connect("coffee.db")
                    cur = con.cursor()
                    cur.execute("""INSERT INTO coffee (id, name, roast, type, description, price, volume)
                    VALUES (?,?,?,?,?,?,?)""", (len(self.names) + 1,str(self.lineEdit_2.text()),self.comboBox.currentText(),
                                               self.comboBox_2.currentText(),str(self.plainTextEdit.toPlainText()),
                                               int(self.lineEdit.text()),int(self.lineEdit_5.text())))
                    con.commit()
                    con.close()
                    self.pushButton_3.setStyleSheet("background-color: None")
                    self.close()
                except Exception:
                    self.pushButton_3.setStyleSheet("background-color: red")
        else:
            try:
                con = sqlite3.connect("coffee.db")
                cur = con.cursor()
                ind = cur.execute("""SELECT * FROM coffee WHERE name like ?""", (self.item.capitalize(),)).fetchall()[0][0]
                cur.execute("""UPDATE coffee
                              SET name = ?, roast = ?, type = ?,
                              description = ?, price = ?, volume = ?
                              WHERE id = ?""", (self.lineEdit_2.text(),self.comboBox.currentText(),
                                                   self.comboBox_2.currentText(),self.plainTextEdit.toPlainText(),
                                                   float(self.lineEdit.text().split()[0]),self.lineEdit_5.text().split()[0], ind))
                con.commit()
                con.close()
                self.pushButton_3.setStyleSheet("background-color: None")
                self.close()

            except Exception as e:
                print(e)
                self.pushButton_3.setStyleSheet("background-color: red")            

    def change(self):
        try:
            self.get_names
            self.item, ok_pressed = QInputDialog.getItem( self,
                                                     "Выберите кофе", "Выберите кофе:", self.names, 1, False)

            if ok_pressed:
                con = sqlite3.connect("coffee.db")
                cur = con.cursor()
                result = cur.execute("""SELECT * FROM coffee WHERE name like ?""", (self.item.capitalize(),)).fetchall()[0]
                self.lineEdit_2.setText(result[1])
                self.comboBox.setCurrentText(result[2])
                self.lineEdit.setText(str(result[5]) + " руб")
                self.lineEdit_5.setText(str(result[6]) + " кг")
                self.comboBox_2.setCurrentText(result[3])
                self.plainTextEdit.clear()
                self.plainTextEdit.setPlainText(str(result[4]))
                con.close()
                self.create_new = 0
                self.pushButton_3.setStyleSheet("background-color: None")
        except Exception as e:
            print(e)

    def new(self):
        self.lineEdit_2.clear()
        self.lineEdit.clear()
        self.lineEdit_5.clear()
        self.plainTextEdit.clear()
        self.create_new = 1
        self.pushButton_3.setStyleSheet("background-color: None")
        


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 8, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 5, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 6, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 7, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 2, 1, 1, 3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 3, 1, 1, 3)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 4, 1, 1, 3)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_2.addWidget(self.lineEdit_5, 5, 1, 1, 3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 6, 1, 1, 3)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 7, 1, 2, 3)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Арабика"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Либерика"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Робуста"))
        self.label_2.setText(_translate("MainWindow", "Цена:"))
        self.label_5.setText(_translate("MainWindow", "Степень обжарки:"))
        self.label.setText(_translate("MainWindow", "Объем упаковки:"))
        self.pushButton.setText(_translate("MainWindow", "Показать"))
        self.label_4.setText(_translate("MainWindow", "Молотый/В зернах"))
        self.label_3.setText(_translate("MainWindow", "Описание:"))
        self.pushButton_2.setText(_translate("MainWindow", "Изменить"))
        self.label_6.setText(_translate("MainWindow", "Название сорта:"))
        self.pushButton_3.setText(_translate("MainWindow", "Обновить"))

class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Coffee")
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.new)
        self.pushButton_3.clicked.connect(self.load)

    def load(self):
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM coffee""").fetchall()
        con.close()
        self.names = []

        for i in result:
            self.names.append(str(i[1]))

        self.comboBox.clear()
        self.comboBox.addItems(self.names)
    

    def new(self):
        self.w = New_Window()
        self.w.show()
       

    def run(self):
        name = self.comboBox.currentText()
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM coffee WHERE name like ?""", (name,)).fetchall()[0]
        self.lineEdit_2.setText(str(result[1]))
        self.lineEdit_3.setText(result[2])
        self.lineEdit.setText(str(result[5]) + " руб")
        self.lineEdit_5.setText(str(result[6]) + " кг")
        self.lineEdit_4.setText(result[3])
        self.textEdit.clear()
        self.textEdit.insertPlainText(str(result[4]))
        con.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

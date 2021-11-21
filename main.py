import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QComboBox
import sqlite3
from PyQt5.QtWidgets import QInputDialog

class New_Window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
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
        


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
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

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QComboBox
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle("Coffee")
        self.pushButton.clicked.connect(self.run)

    def run(self):
        name = self.comboBox.currentText()
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM coffee WHERE name like ?""", (name,)).fetchall()[0]
        self.lineEdit_2.setText(result[1])
        self.lineEdit_3.setText(result[2])
        self.lineEdit.setText(str(result[5]) + " руб")
        self.lineEdit_5.setText(str(result[6]) + " кг")
        self.lineEdit_4.setText(result[3])
        self.textEdit.clear()
        self.textEdit.insertPlainText(result[4])
        con.close()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

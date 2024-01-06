from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout
import sqlite3
import sys
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.load_data()

    def load_data(self):
        conn = sqlite3.connect('coffee.sqlite')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM coffee')
        row_data = [tuple(row) for row in cursor.fetchall()]

        self.tableWidget.setRowCount(len(row_data))
        self.tableWidget.setColumnCount(len(row_data[0]))

        headers = [description[0] for description in cursor.description]
        self.tableWidget.setHorizontalHeaderLabels(headers)

        for row, row_data in enumerate(row_data):
            for col, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableWidget.setItem(row, col, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
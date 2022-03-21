import sys
import random

from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QAbstractItemView, QPushButton, QApplication, QWidget, QHBoxLayout

from ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # 设置总的行数，列数已经在designer中做好了
        self.tableWidget.setRowCount(5)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        for i in range(5):
            # 设置第一列
            item_id = QTableWidgetItem(str(i + 1))
            self.tableWidget.setItem(i, 0, item_id)

            # 设置第二列
            item_num = QTableWidgetItem(str(random.randint(10, 100)))
            self.tableWidget.setItem(i, 1, item_num)

            # 设置第三列，也就是添加一个清零按钮
            self.tableWidget.setCellWidget(i, 2, self.add_button(i, 1))

    def add_button(self, row, column):
        self.button_add = QPushButton('清零')
        self.button_add.setStyleSheet(''' text-align : center;
                                            background-color : Red;
                                            height : 30px;
                                            font : 12px; ''')
        self.button_add.clicked.connect(lambda: self.clear_number(row, column))

        widget = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(self.button_add)
        widget.setLayout(layout)
        return widget

    def clear_number(self, row, column):
        item = QTableWidgetItem('0')
        self.tableWidget.setItem(row, column, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec_())

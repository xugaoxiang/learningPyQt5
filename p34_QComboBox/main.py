import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # 增加单个选项
        self.comboBox.addItem("Python")
        self.comboBox.addItem("Java")

        # 增加多个选项
        self.comboBox.addItems(["C", "C++", "Javascript"])

        # 绑定信号和槽
        # 当下拉选项的index发生变化，才发射这个信号，比如连续选中同一个选项，这个信号就不会发射
        self.comboBox.currentIndexChanged.connect(self.on_item_selected)

        # 和currentIndexChanged不同的是，即使前后选择的是同一个选项，信号也会被发射
        self.comboBox.activated.connect(self.on_activated)

        # 当焦点在下拉选项上时，信号被发射，此时的index是已经被选中的选项的index，默认是0
        self.comboBox.highlighted.connect(self.on_highlighted)

    def on_item_selected(self):
        print("{}: {}, index={}, total count={}".format(self.label.text(), self.comboBox.currentText(), self.comboBox.currentIndex(), self.comboBox.count()))

    def on_activated(self):
        print('on_activated.')

    def on_highlighted(self):
        print('on_highlighted, index={}'.format(self.comboBox.currentIndex()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec_())

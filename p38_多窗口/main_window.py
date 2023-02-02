import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_mainwindow import Ui_MainWindow
from second_window import SecondWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.showSecondWindow)

    def showSecondWindow(self):
        self.secWin = SecondWindow("Hello SecondWindow.")
        self.secWin.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec_())

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton

from ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.pushButton_min.clicked.connect(self.do_min)
        self.pushButton_max.clicked.connect(self.do_max)
        self.pushButton_normal.clicked.connect(self.do_normal)
        self.pushButton_fullscreen.clicked.connect(self.do_fullscreen)

    def do_min(self):
        self.showMinimized()

    def do_max(self):
        self.showMaximized()

    def do_normal(self):
        self.showNormal()

    def do_fullscreen(self):
        self.showFullScreen()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec_())

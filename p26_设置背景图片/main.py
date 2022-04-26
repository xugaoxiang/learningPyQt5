import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':

    stylesheet = """
        MainWindow {
            background-image: url("bg.jpg"); 
            background-repeat: no-repeat; 
            background-position: center;
        }
    """

    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec_())

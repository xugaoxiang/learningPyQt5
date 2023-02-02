from PyQt5.QtWidgets import QMainWindow
from ui_secondwindow import Ui_MainWindow


class SecondWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, param, parent=None):
        super(SecondWindow, self).__init__(parent)
        self.setupUi(self)

        print("从主窗口传递过来的字符是：{}".format(param))
        self.label.setText(param)
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QShortcut
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence

from ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.onClick)
        # 给按钮操作设置一个快捷键
        self.pushButton.setShortcut(QKeySequence(Qt.Key_A))

        # 或者这样
        # self.shortcut_button = QShortcut(QKeySequence('Ctrl+S'), self)
        # self.shortcut_button.activated.connect(self.onClick)

    def onClick(self):
        print('onClick.')

    def keyPressEvent(self, event):
        # 判断按下的是什么键
        if event.key() == Qt.Key_D:
            print('keyPressEvent, Key_D')

            # ctrl 修饰键
            if event.modifiers() & Qt.ControlModifier:
                print('Ctrl+D')
            # alt 修饰键
            elif event.modifiers() & Qt.AltModifier:
                print('Alt+D')
            # shift 修饰键
            elif event.modifiers() & Qt.ShiftModifier:
                print('Shift+D')

    def keyReleaseEvent(self, event):
        print('keyReleaseEvent')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec_())

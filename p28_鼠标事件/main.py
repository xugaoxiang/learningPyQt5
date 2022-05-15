import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtCore import Qt

from ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

    def mousePressEvent(self, event):
        print('mousePressEvent')

        if event.button() == Qt.LeftButton:
            print('left')
        elif event.button() == Qt.RightButton:
            print('right')
        elif event.button() == Qt.MiddleButton:
            print('middle')

        # 相对于窗口的位置
        x = event.x()
        y = event.y()
        # xy类型是QPoint，QPoint的x()和y()方法就是x和y的值
        xy = event.pos()
        print('x={}, y={}, xy={}, x={}, y={}'.format(x, y, xy, xy.x(), xy.y()))

        # 相对于屏幕的位置
        x_global = event.globalX()
        y_global = event.globalY()
        # xy_global类型是QPoint
        xy_global = event.globalPos()
        print('x_global={}, y_global={}, xy_global={}'.format(x_global, y_global, xy_global))

    def mouseReleaseEvent(self, event):
        print('mouseReleaseEvent')

    def mouseMoveEvent(self, event):
        print('mouseMoveEvent')

    def enterEvent(self, event):
        print('enterEvent')

    def leaveEvent(self, event):
        print('leaveEvent')

    def mouseDoubleClickEvent(self, event):
        print('mouseDoubleClickEvent')

    def wheelEvent(self, event):
        print('wheelEvent')

    def closeEvent(self, event):
        """
        重写 closeEvent 方法，实现在窗口关闭时去执行一些功能
        """
        reply = QMessageBox.question(self,
                                     '这是标题',
                                     "这是消息体",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            # 关闭窗口
            event.accept()
        else:
            # 取消
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec_())

import sys
import cv2
from PyQt5 import QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)

        self.ui_init()

        self.show_cv_image()

    def ui_init(self):
        '''
        画界面，非常简单，就一个label，用来承载图片
        :return:
        '''

        self.main_layout = QtWidgets.QHBoxLayout()
        self.label_image = QtWidgets.QLabel()
        self.main_layout.addWidget(self.label_image)
        self.setLayout(self.main_layout)

    def show_cv_image(self):
        '''
        使用cv2读取图片并显示
        :return:
        '''

        image = cv2.imread('logo.png')
        image = cv2.resize(image, (1200, 300))
        result = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # 构建QImage对象
        show_image = QtGui.QImage(result.data, result.shape[1], result.shape[0], QtGui.QImage.Format_RGB888)
        self.label_image.setPixmap(QtGui.QPixmap.fromImage(show_image))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())

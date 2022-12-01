import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene
from PyQt5.QtGui import QPixmap
from ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        scene = QGraphicsScene()
        img = QPixmap('Lenna.jpg')
        img = img.scaled(self.window().width(), self.window().height())
        scene.addPixmap(img)
        self.graphicsView.setScene(scene)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec_())
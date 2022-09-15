import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QSlider

from ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(100)
        self.label_horizontal.setText('50')
        self.horizontalSlider.setSingleStep(2)
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider.valueChanged.connect(self.update_horizontal)

        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(1000)
        self.label_vertical.setText('500')
        self.verticalSlider.setSingleStep(10)
        self.verticalSlider.setTickPosition(QSlider.TicksRight)
        self.verticalSlider.valueChanged.connect(self.update_vertical)

    def update_horizontal(self):
        self.label_horizontal.setText(str(self.horizontalSlider.value()))

    def update_vertical(self):
        self.label_vertical.setText(str(self.verticalSlider.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec_())

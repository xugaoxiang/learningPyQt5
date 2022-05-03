import sys
import matplotlib

matplotlib.use('Qt5Agg')

from PyQt5 import QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


# 在PyQt5中显示matplotlib，它的原理就是使用FigureCanvasQTAgg作为后端(backend)，将plot渲染成简单的bitmap图片
class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        # figsize尺寸，dpi指定绘图分辨率
        fig = Figure(figsize=(width, height), dpi=dpi)

        # add_subplot的参数是ijn的形式，代表3个数，其中ij是行列数，n是第n个图，比如（111）则是一个有1个图，该图位于第1个
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('matplotlib with pyqt5')

        sc = MplCanvas(self, width=5, height=4, dpi=200)
        # x轴、y轴的数据
        sc.axes.plot([0, 1, 2, 3, 4, 5, 6], [1, 10, 20, 4, 50, 16, 20])

        # 创建toolbar,2个参数分别是canvas对象和当前窗口对象
        toolbar = NavigationToolbar(sc, self)

        # 放到垂直布局里
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        # 设置整个窗口布局并显示
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec_())

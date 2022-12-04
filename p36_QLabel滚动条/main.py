import sys

from PyQt5.QtWidgets import QWidget, QLabel, QScrollArea, QApplication, QVBoxLayout, QMainWindow
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 实例化滚动区域
        self.scrollarea = QScrollArea()

        self.widget = QWidget()

        # 垂直布局
        self.vboxlayout = QVBoxLayout()

        for i in range(0, 10):
            # label显示的文本
            label = QLabel("This is a label.")

            # label加入到垂直布局中
            self.vboxlayout.addWidget(label)

            # 第四个label中显示xml文件的内容
            if i == 3:
                # 读取test.xml文件的内容并显示在label上
                with open('test.xml', encoding='UTF-8') as f:
                    text_label = f.read()

                label.setText(text_label)

        self.widget.setLayout(self.vboxlayout)

        # 设置滚动条的属性
        self.scrollarea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollarea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollarea.setWidgetResizable(True)
        self.scrollarea.setWidget(self.widget)

        # 居中
        self.setCentralWidget(self.scrollarea)

        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('PyQt5 Label滚动条示例')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())

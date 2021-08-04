import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('网页示例')
        self.setGeometry(10, 20, 1080, 720)

        self.browser = QWebEngineView()
        self.browser.load(QUrl('https://xugaoxiang.com'))

        # 打开本地html文件
        # self.browser = QWebEngineView()
        # self.browser.load(QUrl('file:///test.html'))

        # 使用setHtml方法显示
        # self.browser = QWebEngineView()
        # self.browser.setHtml('''
        #     <!DOCTYPE html>
        #     <html lang="en">
        #     <head>
        #         <meta charset="UTF-8">
        #         <title>本地网页文件示例</title>
        #     </head>
        #     <body>
        #         <p>PyQt5打开本地HTML文件示例，采用setHtml方法</p>
        #     </body>
        #     </html>
        # ''')

        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()
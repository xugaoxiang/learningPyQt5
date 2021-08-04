# -*- coding: utf-8 -*-


"""
@author: Xu Gaoxiang
@license: Apache V2
@email: xugx.ai@gmail.com
@site: https://www.xugaoxiang.com
@software: PyCharm
@file: main.py
@time: 3/21/2019 11:13 AM
"""

import sys

from PyQt5.QtWidgets import QApplication , QMainWindow

from designer import *

if __name__ == '__main__':
    '''
    主函数
    '''

    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
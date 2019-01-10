# -*- coding: utf-8 -*-


"""
@author: Xu Gaoxiang
@license: Apache V2
@email: djstava@gmail.com
@site: https://www.xugaoxiang.com
@software: PyCharm
@file: main.py
@time: 2019/1/10 10:50
"""

import sys

from PyQt5.QtWidgets import QApplication

from gui.mainwindow import MainWindow

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
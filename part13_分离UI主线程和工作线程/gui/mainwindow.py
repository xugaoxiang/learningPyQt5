# -*- coding: utf-8 -*-


"""
@author: Xu Gaoxiang
@license: Apache V2
@email: djstava@gmail.com
@site: https://www.xugaoxiang.com
@software: PyCharm
@file: mainwindow.py
@time: 2019/1/10 10:49
"""


from PyQt5.QtWidgets import QMainWindow

from gui.ui_mainwindow import *
from .threads import WorkThread

class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.button_ok.clicked.connect(self.button_start)

    def button_start(self):

        print('button_start clicked.')
        
        self.button_ok.setChecked(True)
        self.button_ok.setDisabled(True)
        
        self.th = WorkThread(ip='192.168.1.1', port=4000)
        self.th.finishSignal.connect(self.button_finish)
        self.th.start()
        
    def button_finish(self, msg):
        
        print('msg: {}'.format(msg))

        self.button_ok.setChecked(False)
        self.button_ok.setDisabled(False)
# -*- coding: utf-8 -*-


"""
@author: Xu Gaoxiang
@license: Apache V2
@email: xugx.ai@gmail.com
@site: https://www.xugaoxiang.com
@software: PyCharm
@file: mainwindow.py.py
@time: 3/24/2019 10:48 PM
"""

from PyQt5.QtWidgets import QMainWindow
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.actionExit.triggered.connect(self.onExitTriggered)

        self.actionCopy.triggered.connect(self.onCopyTriggered)
        self.actionPaste.triggered.connect(self.onPasteTriggered)
        self.actionCut.triggered.connect(self.onCutTriggered)
        
    def onExitTriggered(self):
        print('Exit triggered.')
        
    def onCopyTriggered(self):
        print('Copy triggered.')
        
    def onCutTriggered(self):
        print('Cut triggered.')
        
    def onPasteTriggered(self):
        print('Paste triggered.')
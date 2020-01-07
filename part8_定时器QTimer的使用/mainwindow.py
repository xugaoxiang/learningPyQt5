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
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QMainWindow, QLineEdit
from ui_mainwindow import Ui_MainWindow

from PyQt5.QtGui import QIcon, QPixmap


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        icon = QIcon()
        icon.addPixmap(QPixmap("qt.png"))
        self.setWindowIcon(icon)

        self.actionExit.triggered.connect(self.onExitTriggered)

        self.actionCopy.triggered.connect(self.onCopyTriggered)
        self.actionPaste.triggered.connect(self.onPasteTriggered)
        self.actionCut.triggered.connect(self.onCutTriggered)

        # QLabel
        self.label.setToolTip("这是一个气泡提示！")
        self.label.setAlignment(Qt.AlignLeft)
        # self.label.setText('修改后的文本')

        # QLineedit
        self.lineEdit.setAlignment(Qt.AlignRight)
        self.lineEdit.setEchoMode(QLineEdit.Normal)
        self.lineEdit.setText("这是一个QLineedit！")
        print(self.lineEdit.text())

        self.lineEdit.textChanged.connect(self.onQLineeditTextChanged)
        self.lineEdit.editingFinished.connect(self.onQLineeditFinished)
        self.lineEdit.selectionChanged.connect(self.onQLineeditSelectionChanged)

        # QTextEdit
        strs = "MQTT(Message Queuing Telemetry Transport),是一个物联网传输协议，它被设计用于轻量级的发布/订阅式消息传输，旨在为低带宽和不稳定的网络环境中的物联网设备提供可靠的网络服务。MQTT是专门针对物联网开发的轻量级传输协议。MQTT协议针对低带宽网络，低计算能力的设备，做了特殊的优化，使得其能适应各种物联网应用场景。本文旨在研究其在消息发布/订阅/接收场景下的应用."
        self.textEdit.setPlainText(strs)
        print(self.textEdit.toHtml())

        # Qpushbutton
        self.pushButton.setCheckable(True)
        self.pushButton.setEnabled(False)
        self.pushButton.clicked.connect(self.onClicked)

        self.timer = QTimer(self)
        self.count = 0
        self.timer.timeout.connect(self.showNum)
        # self.timer.timeout.connect(self.showNum2)
        # self.startCount()

    def onClicked(self):
        print('The pushbutton is clicked.')

    def onQLineeditTextChanged(self):
        print("onQLineeditTextChanged")

    def onQLineeditFinished(self):
        print("onQLineeditFinished")

    def onQLineeditSelectionChanged(self):
        print("onQLineeditSelectionChanged")

    def startCount(self):
        self.timer.start(1000)

    def showNum(self):
        self.count = self.count + 1
        print(self.count)

    def showNum2(self):
        print("showNum2, {}".format(self.count))

    def onExitTriggered(self):
        print("Exit triggered.")

    def onCopyTriggered(self):
        print("Copy triggered.")

    def onCutTriggered(self):
        print("Cut triggered.")

    def onPasteTriggered(self):
        print("Paste triggered.")

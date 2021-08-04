import time

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal
from .ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.thread = Worker()
        self.thread.sig.connect(self.updateLabel)
        
        self.pushButton.clicked.connect(self.buttonClicked)
    
    def buttonClicked(self):
        self.thread.start()
    
    def updateLabel(self, text):
        self.label.setText(text)


class Worker(QThread):
    sig = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        self.count = 0
    
    def run(self):
        
        while True:
            time.sleep(1)
            self.count += 1
            if (self.count % 5 == 0):
                self.sig.emit(f"已执行{self.count}秒")

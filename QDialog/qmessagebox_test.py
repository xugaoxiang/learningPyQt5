import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DialogDemo(QMainWindow):
    
    def __init__(self, parent=None):
        super(DialogDemo, self).__init__(parent)
        self.setWindowTitle("QMessageBox demo")
        self.resize(600, 400)
        
        self.button = QPushButton(self)
        self.button.setText("点击弹出QMessageBox")
        self.button.move(50, 50)
        self.button.clicked.connect(self.showDialog)
    
    def showDialog(self):
        # warning、critical、question
        reply = QMessageBox.information(self, "标题", "消息正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        print(reply)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DialogDemo()
    demo.show()
    sys.exit(app.exec_())
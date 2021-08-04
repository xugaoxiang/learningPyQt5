import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DialogDemo(QMainWindow):
    
    def __init__(self, parent=None):
        super(DialogDemo, self).__init__(parent)
        self.setWindowTitle("Dialog demo")
        self.resize(600, 400)
        
        self.button = QPushButton(self)
        self.button.setText("点击弹出字体对话框")
        self.button.move(50, 50)
        self.button.clicked.connect(self.showDialog)
    
    def showDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            print(f'font: {font.pointSize()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DialogDemo()
    demo.show()
    sys.exit(app.exec_())
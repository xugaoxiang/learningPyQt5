import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QPushButton


class QMessageBoxDemo(QMainWindow):

    def __init__(self, parent=None):
        super(QMessageBoxDemo, self).__init__(parent)
        self.setWindowTitle("QMessageBox demo")
        self.resize(600, 400)

        self.button = QPushButton(self)
        self.button.setText("点击弹出QMessageBox")
        self.button.resize(180, 140)
        self.button.move(200, 100)
        self.button.clicked.connect(self.showDialog)

    def showDialog(self):
        msgBox = QMessageBox(QMessageBox.Warning, "标题", "消息正文")
        yes = msgBox.addButton("自定义Yes按钮", QMessageBox.YesRole)
        no = msgBox.addButton("自定义No按钮", QMessageBox.NoRole)
        msgBox.exec_()
        if msgBox.clickedButton() == yes:
            print('yes')
        else:
            print('no')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = QMessageBoxDemo()
    demo.show()
    sys.exit(app.exec_())

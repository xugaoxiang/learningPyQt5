import sys
from qt_material import apply_stylesheet, list_themes

from PyQt5.QtWidgets import QMainWindow, QApplication

from ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.pushButton_login.setProperty('class', 'danger')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 查看所有的主题
    print(list_themes())

    extra = {

        # 按钮颜色
        'danger': '#dc3545',
        'warning': '#ffc107',
        'success': '#17a2b8',

        # 字体
        'font_family': 'Roboto',
    }

    apply_stylesheet(app, theme='default_dark.xml', extra=extra)

    windows = MainWindow()
    windows.show()
    sys.exit(app.exec_())

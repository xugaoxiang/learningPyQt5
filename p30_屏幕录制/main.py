import sys
import numpy as np
import cv2
from PIL import ImageGrab
from threading import Thread

from PyQt5.QtWidgets import QMainWindow, QApplication

from ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # 标志位
        self.record_flag = False

        self.pushButton_start.clicked.connect(self.start)
        self.pushButton_stop.clicked.connect(self.stop)

    def start(self):
        self.pushButton_start.setEnabled(False)
        self.pushButton_stop.setEnabled(True)

        # 开启线程
        self.th = Thread(target=self.start_recording)
        self.th.start()

    def start_recording(self):
        img = ImageGrab.grab()
        print('type: {}'.format(type(img)))
        width, height = img.size
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        fps = 30
        out = cv2.VideoWriter('record.avi', fourcc, fps, (width, height))

        while True:
            img = ImageGrab.grab()
            img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
            out.write(img_cv)

            if self.record_flag:
                out.release()
                break

    def stop(self):
        self.record_flag = True
        self.pushButton_start.setEnabled(True)
        self.pushButton_stop.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec_())

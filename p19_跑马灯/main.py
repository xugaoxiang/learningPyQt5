import sys
from PyQt5.QtCore import QTimeLine
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout


class Marquee(QWidget):
    def __init__(self):
        super(Marquee, self).__init__()
        self.setWindowTitle("PyQt5跑马灯示例")
        self.resize(600, 600)

        self.label = QLabel(
            '你好，我是一个跑马灯！欢迎访问我的网站：https://xugaoxiang.com ', self)

        # label开始的位置，label在纵坐标为280的水平线上滚动
        self.label.move(-100, 280)

        # 10000是持续时间，单位是毫秒
        self.timeline = QTimeLine(10000, self)

        # 设置帧范围，越大，变化的越快
        self.timeline.setFrameRange(0, 500)

        # 绑定frameChanged信号到槽函数slot_frame_changed
        self.timeline.frameChanged.connect(self.slot_frame_changed)

        # 设置循环次数，0表示无限次
        self.timeline.setLoopCount(0)

        # 开始timeline，QTimeLine有3种状态，NotRunning、Running和Paused，其状态切换涉及到的方法有start、stop、resume、setPaused，状态变化后，会发出信号stateChanged
        self.timeline.start()

        # 创建2个按钮，分别用来控制从左到右和从右向左
        self.forward_btn = QPushButton('从左到右', self)
        self.backward_btn = QPushButton('从右到左', self)

        # 设置2个按钮的位置
        self.forward_btn.move(150, 100)
        self.backward_btn.move(350, 100)

        # 处理2个按钮的点击
        self.forward_btn.clicked.connect(
            lambda: self.slot_direction_changed(self.forward_btn))
        self.backward_btn.clicked.connect(
            lambda: self.slot_direction_changed(self.backward_btn))

    def slot_frame_changed(self, frame):
        # 这里的frame就是setFrameRange设定的范围
        self.label.move(-100 + frame, 280)

    def slot_direction_changed(self, btn):
        if btn == self.forward_btn:
            # 设置时间轴动画，从左到右，这是默认的
            self.timeline.setDirection(QTimeLine.Forward)
        else:
            # 设置时间轴动画，从右到左
            self.timeline.setDirection(QTimeLine.Backward)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Marquee = Marquee()
    Marquee.show()
    sys.exit(app.exec_())

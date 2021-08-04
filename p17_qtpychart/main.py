import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5饼图")

        # 显示位置
        self.setGeometry(100, 100, 800, 600)
        self.create_piechart()
        self.show()

    def create_piechart(self):
        # 创建QPieSeries对象，它用来存放饼图的数据
        series = QPieSeries()
        
        # append方法中的数字，代表的是权重，完成可以改成其它，如80,70,60等等
        series.append("Python", 8)
        series.append("Java", 7)
        series.append("C", 6)
        series.append("C++", 5)
        series.append("PHP", 4)
        series.append("Swift", 3)

        # 单独处理某个扇区
        slice = QPieSlice()

        # 这里要处理的是python项，是依据前面append的顺序，如果是处理C++项的话，那索引就是3
        slice = series.slices()[0]

        # 突出显示，设置颜色
        slice.setExploded(True)
        slice.setLabelVisible(True)
        slice.setPen(QPen(Qt.red, 2))
        slice.setBrush(Qt.red)

        # 创建QChart实例，它是PyQt5中的类
        chart = QChart()
        # QLegend类是显示图表的图例，先隐藏掉
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()

        # 设置动画效果
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # 设置标题
        chart.setTitle("饼图示例")

        chart.legend().setVisible(True)

        # 对齐方式
        chart.legend().setAlignment(Qt.AlignBottom)

        # 创建ChartView，它是显示图表的控件
        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chartview)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis
import sys
import random

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 600, 400)
        self.setWindowTitle("柱状图示例")

        set = QBarSet("Points")

        for i in range(7):
            # 随机7个样本数据
            set.append(random.randint(0, 100))

        # 若显示各部分所占百分比，用QPercentBarSeries
        series = QBarSeries()
        series.append(set)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("一周数据展示")
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTheme(QChart.ChartThemeDark)

        # 横轴数据
        categories = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

        axis = QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        # 实例化chartview
        chartview = QChartView(chart)

        vbox = QVBoxLayout()
        vbox.addWidget(chartview)

        self.setLayout(vbox)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
import sys
import random

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis

from ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.pushButton_1.clicked.connect(self.show_1)
        self.pushButton_2.clicked.connect(self.show_2)

    def show_1(self):
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
        categories = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]

        axis = QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        # 实例化chartview
        chartview = QChartView(chart)
        for i in range(self.verticalLayout.count()):
            self.verticalLayout.itemAt(i).widget().deleteLater()
        self.verticalLayout.addWidget(chartview)

    def show_2(self):
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
        categories = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]

        axis = QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        # 实例化chartview
        chartview = QChartView(chart)
        for i in range(self.verticalLayout.count()):
            self.verticalLayout.itemAt(i).widget().deleteLater()
        self.verticalLayout.addWidget(chartview)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec_())

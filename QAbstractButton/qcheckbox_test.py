import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        layout = QHBoxLayout()
        
        self.checkbox1 = QCheckBox("CheckBox1")
        self.checkbox1.stateChanged.connect(lambda: self.checkboxChecked(self.checkbox1))
        layout.addWidget(self.checkbox1)
        
        self.checkbox2 = QCheckBox("CheckBox2")
        self.checkbox2.stateChanged.connect(lambda: self.checkboxChecked(self.checkbox2))
        layout.addWidget(self.checkbox2)
        
        self.setLayout(layout)
        self.setWindowTitle("CheckBox")
    
    def checkboxChecked(self, cb):
        if cb.text() == "CheckBox1":
            if cb.isChecked():
                print(f"{cb.text()} is checked.")
            else:
                print(f"{cb.text()} is unchecked.")
        
        if cb.text() == "CheckBox2":
            if cb.isChecked():
                print(f"{cb.text()} is checked.")
            else:
                print(f"{cb.text()} is unchecked.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

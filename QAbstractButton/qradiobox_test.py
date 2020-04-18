import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Example(QWidget):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)
        layout = QHBoxLayout()
        self.button1 = QRadioButton("Button1")
        self.button1.setChecked(True)
        self.button1.toggled.connect(lambda: self.buttonToggled(self.button1))
        layout.addWidget(self.button1)
        
        self.button2 = QRadioButton("Button2")
        self.button2.toggled.connect(lambda: self.buttonToggled(self.button2))
        layout.addWidget(self.button2)
        
        self.setLayout(layout)
        self.setWindowTitle("RadioButton")
    
    def buttonToggled(self, button):
        if button.text() == "Button1":
            if button.isChecked() == True:
                print(f"{button.text()} is selected.")
            else:
                print(f"{button.text()} is deselected.")
        
        if button.text() == "Button2":
            if button.isChecked() == True:
                print(f"{button.text()} is selected.")
            else:
                print(f"{button.text()} is deselected.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Example()
    example.show()
    sys.exit(app.exec_())

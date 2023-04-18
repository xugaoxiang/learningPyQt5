import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtTextToSpeech import QTextToSpeech
from PyQt5.QtWidgets import QMainWindow, QApplication

from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.play)

        self.engine = None
        engineNames = QTextToSpeech.availableEngines()
        print('engine names: {}'.format(engineNames))

        if len(engineNames) > 0:
            engineName = engineNames[0]
            self.engine = QTextToSpeech(engineName)
            self.engine.stateChanged.connect(self.stateChanged)

            self.voices = []

            for voice in self.engine.availableVoices():
                print('voice: {}'.format(voice))
                self.voices.append(voice)
                self.comboBox.addItem(voice.name())

        else:
            self.pushButton.setEnabled(False)

    def play(self):
        self.pushButton.setEnabled(False)
        self.engine.setVoice(self.voices[self.comboBox.currentIndex()])
        # self.engine.setVolume(float(self.horizontalSlider.value() / 100))
        self.engine.say(self.lineEdit.text())

    def stateChanged(self, state):
        if (state == QTextToSpeech.State.Ready):
            self.pushButton.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec_())

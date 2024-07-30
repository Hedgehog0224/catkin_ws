#!/usr/bin/python3 
from PyQt5.QtWidgets import (
    QApplication, 
    QMainWindow)
from App import Ui_Form
import sys

class ExampleApp(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.buttonOn.clicked.connect(self.StartBut)
        self.buttonStop.clicked.connect(self.StopBut)
        self.buttonRun.clicked.connect(self.RunBut)
        self.buttonJoy.clicked.connect(self.JoyBut)

        self.buttonOn.setCheckable(True)
        self.buttonStop.setCheckable(True)
        self.buttonRun.setCheckable(True)
        self.buttonJoy.setCheckable(True)

        self.buttonStop.setEnabled(False)
        self.buttonJoy.setEnabled(False)
        self.buttonRun.setEnabled(False)

    def StartBut(self):
        if not self.buttonOn.isChecked():
            self.buttonStop.setEnabled(False)
            self.buttonJoy.setEnabled(False)
            self.buttonRun.setEnabled(False)
        else:
            self.buttonStop.setEnabled(True)
            self.buttonJoy.setEnabled(True)
            self.buttonRun.setEnabled(True)

    def StopBut(self):
        if self.buttonStop.isChecked():
            self.buttonJoy.setEnabled(False)
            self.buttonRun.setEnabled(False)
        else:
            self.buttonStop.setEnabled(True)
            self.buttonJoy.setEnabled(True)
            self.buttonRun.setEnabled(True)

    def RunBut(self):
        if not self.buttonRun.isChecked():
            self.buttonJoy.setEnabled(True)
            print('Run')
        else:
            self.buttonJoy.setEnabled(False)

    def JoyBut(self):
        if not self.buttonJoy.isChecked():
            self.buttonRun.setEnabled(True)
            print('Joy')
        else:
            self.buttonRun.setEnabled(False)

def main():
    app = QApplication(sys.argv)  
    window = ExampleApp() 
    window.show() 
    app.exec_() 

if __name__ == '__main__':
    main() 

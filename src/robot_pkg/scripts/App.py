from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(462, 324)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 431, 281))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonOn = QtWidgets.QPushButton(self.widget)
        self.buttonOn.setMaximumSize(QtCore.QSize(161, 91))
        self.buttonOn.setObjectName("buttonOn")
        self.gridLayout.addWidget(self.buttonOn, 1, 0, 1, 1)
        self.buttonStop = QtWidgets.QPushButton(self.widget)
        self.buttonStop.setMaximumSize(QtCore.QSize(161, 91))
        self.buttonStop.setObjectName("buttonStop")
        self.gridLayout.addWidget(self.buttonStop, 1, 1, 1, 1)
        self.buttonJoy = QtWidgets.QPushButton(self.widget)
        self.buttonJoy.setMaximumSize(QtCore.QSize(161, 91))
        self.buttonJoy.setObjectName("buttonJoy")
        self.gridLayout.addWidget(self.buttonJoy, 2, 1, 1, 1)
        self.buttonRun = QtWidgets.QPushButton(self.widget)
        self.buttonRun.setMaximumSize(QtCore.QSize(161, 91))
        self.buttonRun.setObjectName("buttonRun")
        self.gridLayout.addWidget(self.buttonRun, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.buttonOn.setText(_translate("Form", "ON"))
        self.buttonStop.setText(_translate("Form", "STOP"))
        self.buttonJoy.setText(_translate("Form", "JOY"))
        self.buttonRun.setText(_translate("Form", "SELF RUN"))

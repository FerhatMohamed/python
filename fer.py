# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(40, 250, 281, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalSlider = QtWidgets.QSlider(Form)
        self.verticalSlider.setGeometry(QtCore.QRect(370, 10, 22, 191))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.dial = QtWidgets.QDial(Form)
        self.dial.setGeometry(QtCore.QRect(340, 230, 50, 64))
        self.dial.setObjectName("dial")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 70, 151, 111))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        self.horizontalSlider.valueChanged['int'].connect(self.label.setNum)
        self.dial.valueChanged['int'].connect(self.label.setNum)
        self.horizontalSlider.valueChanged['int'].connect(self.dial.setValue)
        self.dial.valueChanged['int'].connect(self.horizontalSlider.setValue)
        self.verticalSlider.valueChanged['int'].connect(self.label.setNum)
        self.dial.valueChanged['int'].connect(self.verticalSlider.setValue)
        self.verticalSlider.valueChanged['int'].connect(self.horizontalSlider.setValue)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


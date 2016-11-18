# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fer1.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 667)
        self.spinBox = QSpinBox(Form)
        self.spinBox.setGeometry(QRect(50, 70, 41, 21))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QSpinBox(Form)
        self.spinBox_2.setGeometry(QRect(130, 70, 41, 21))
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QSpinBox(Form)
        self.spinBox_3.setGeometry(QRect(200, 70, 41, 21))
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QSpinBox(Form)
        self.spinBox_4.setGeometry(QRect(280, 70, 41, 21))
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_5 = QSpinBox(Form)
        self.spinBox_5.setGeometry(QRect(50, 130, 41, 21))
        self.spinBox_5.setObjectName("spinBox_5")
        self.spinBox_6 = QSpinBox(Form)
        self.spinBox_6.setGeometry(QRect(130, 130, 41, 21))
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_7 = QSpinBox(Form)
        self.spinBox_7.setGeometry(QRect(200, 130, 41, 21))
        self.spinBox_7.setObjectName("spinBox_7")
        self.spinBox_8 = QSpinBox(Form)
        self.spinBox_8.setGeometry(QRect(280, 130, 41, 21))
        self.spinBox_8.setObjectName("spinBox_8")
        self.spinBox_9 = QSpinBox(Form)
        self.spinBox_9.setGeometry(QRect(50, 190, 41, 21))
        self.spinBox_9.setObjectName("spinBox_9")
        self.dateEdit = QDateEdit(Form)
        self.dateEdit.setGeometry(QRect(0, 0, 110, 22))
        self.dateEdit.setObjectName("dateEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    
    app = QApplication([])
    palette = QPalette()

    palette.setBrush(QPalette.Background, QBrush(QPixmap('H:\image\large (5).jpg')))
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
  
    Form.setBackgroundRole(QPalette.Base)
    Form.setPalette(palette)
    
    Form.show()
    sys.exit(app.exec_())


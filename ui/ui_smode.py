# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'smode.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_smode(object):
    def setupUi(self, smode):
        smode.setObjectName("smode")
        smode.resize(540, 750)
        smode.setMaximumSize(QtCore.QSize(540, 750))
        smode.setStyleSheet("QWidget {\n"
"    border-radius : \"10px\";\n"
"}")
        self.bgLbl = QtWidgets.QLabel(smode)
        self.bgLbl.setGeometry(QtCore.QRect(0, 0, 540, 750))
        self.bgLbl.setMaximumSize(QtCore.QSize(540, 750))
        self.bgLbl.setStyleSheet("background-color: rgb(47, 47, 47);")
        self.bgLbl.setText("")
        self.bgLbl.setObjectName("bgLbl")
        self.logoLbl = QtWidgets.QLabel(smode)
        self.logoLbl.setGeometry(QtCore.QRect(100, 0, 355, 122))
        self.logoLbl.setStyleSheet("QLabel {\n"
"    image: url(:/5 1.png);\n"
"}")
        self.logoLbl.setText("")
        self.logoLbl.setObjectName("logoLbl")
        self.fullScreenBtn = QtWidgets.QPushButton(smode)
        self.fullScreenBtn.setGeometry(QtCore.QRect(450, 20, 30, 30))
        self.fullScreenBtn.setStyleSheet("QPushButton {\n"
"    border-image: url(:/image 27.png);\n"
"    background-color : transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(0,0,0,0.2);\n"
"}")
        self.fullScreenBtn.setText("")
        self.fullScreenBtn.setObjectName("fullScreenBtn")
        self.filterBtn = QtWidgets.QPushButton(smode)
        self.filterBtn.setGeometry(QtCore.QRect(490, 20, 30, 30))
        self.filterBtn.setStyleSheet("QPushButton {\n"
"    \n"
"    image: url(:/image 5.png);\n"
"    background-color : transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(0,0,0,0.2);\n"
"}")
        self.filterBtn.setText("")
        self.filterBtn.setObjectName("filterBtn")
        self.closeBtn = QtWidgets.QPushButton(smode)
        self.closeBtn.setGeometry(QtCore.QRect(30, 30, 25, 25))
        self.closeBtn.setStyleSheet("QPushButton {\n"
"    \n"
"    border-image: url(:/X.png);\n"
"    background-color : transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(0,0,0,0.2);\n"
"}")
        self.closeBtn.setText("")
        self.closeBtn.setObjectName("closeBtn")
        self.noteLbl = QtWidgets.QLabel(smode)
        self.noteLbl.setGeometry(QtCore.QRect(70, 660, 130, 72))
        self.noteLbl.setStyleSheet("QLabel {\n"
"    background-color : \"#666666\";\n"
"    border-radius : \"22px\";\n"
"}")
        self.noteLbl.setText("")
        self.noteLbl.setObjectName("noteLbl")
        self.captureBtn = QtWidgets.QLabel(smode)
        self.captureBtn.setGeometry(QtCore.QRect(370, 660, 130, 72))
        self.captureBtn.setStyleSheet("QLabel {\n"
"    background-color : \"#666666\";\n"
"    border-radius : \"22px\";\n"
"}")
        self.captureBtn.setText("")
        self.captureBtn.setObjectName("captureBtn")
        self.smodeLbl = QtWidgets.QLabel(smode)
        self.smodeLbl.setGeometry(QtCore.QRect(215, 660, 141, 72))
        self.smodeLbl.setStyleSheet("QLabel {\n"
"    background-color : \"#666666\";\n"
"    border-radius : \"22px\";\n"
"}")
        self.smodeLbl.setText("")
        self.smodeLbl.setObjectName("smodeLbl")
        self.noteBtn = QtWidgets.QPushButton(smode)
        self.noteBtn.setGeometry(QtCore.QRect(90, 684, 89, 25))
        self.noteBtn.setStyleSheet("QPushButton {\n"
"    color : \"#FFFFFF\";\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image 6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.noteBtn.setIcon(icon)
        self.noteBtn.setObjectName("noteBtn")
        self.smodeBtn = QtWidgets.QPushButton(smode)
        self.smodeBtn.setGeometry(QtCore.QRect(221, 683, 131, 25))
        self.smodeBtn.setStyleSheet("QPushButton {\n"
"    color : \"#FFFFFF\";\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/keyboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.smodeBtn.setIcon(icon1)
        self.smodeBtn.setObjectName("smodeBtn")
        self.captureBtn_2 = QtWidgets.QPushButton(smode)
        self.captureBtn_2.setGeometry(QtCore.QRect(381, 683, 111, 25))
        self.captureBtn_2.setStyleSheet("QPushButton {\n"
"    color : \"#FFFFFF\";\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/image 8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.captureBtn_2.setIcon(icon2)
        self.captureBtn_2.setObjectName("captureBtn_2")
        self.label = QtWidgets.QLabel(smode)
        self.label.setGeometry(QtCore.QRect(70, 100, 420, 420))
        self.label.setStyleSheet("QLabel {\n"
"    image: url(:/image 18.png);\n"
"}\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.recordBtn = QtWidgets.QPushButton(smode)
        self.recordBtn.setGeometry(QtCore.QRect(160, 510, 100, 100))
        self.recordBtn.setStyleSheet("QPushButton {\n"
"    background-color : \"#666666\";    \n"
"    image: url(:/image 3.png);\n"
"    border-radius : \"50px\";\n"
"}")
        self.recordBtn.setText("")
        self.recordBtn.setObjectName("recordBtn")
        self.stopBtn = QtWidgets.QPushButton(smode)
        self.stopBtn.setGeometry(QtCore.QRect(313, 510, 100, 100))
        self.stopBtn.setStyleSheet("QPushButton {\n"
"    background-color : \"#666666\";    \n"
"    \n"
"    image: url(:/Rectangle 24.png);\n"
"    border-radius : \"50px\";\n"
"}")
        self.stopBtn.setText("")
        self.stopBtn.setObjectName("stopBtn")

        self.retranslateUi(smode)
        QtCore.QMetaObject.connectSlotsByName(smode)

    def retranslateUi(self, smode):
        _translate = QtCore.QCoreApplication.translate
        smode.setWindowTitle(_translate("smode", "Form"))
        self.noteBtn.setText(_translate("smode", "Note"))
        self.smodeBtn.setText(_translate("smode", "Keyboard Mode"))
        self.captureBtn_2.setText(_translate("smode", "Screenshot"))
import resource.resource_rc

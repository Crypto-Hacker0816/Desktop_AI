# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(540, 750)
        main.setMaximumSize(QtCore.QSize(540, 750))
        main.setStyleSheet("QWidget {\n"
"    border-radius : \"10px\";\n"
"}")
        self.bgLbl = QtWidgets.QLabel(main)
        self.bgLbl.setGeometry(QtCore.QRect(0, 0, 540, 750))
        self.bgLbl.setMaximumSize(QtCore.QSize(540, 750))
        self.bgLbl.setStyleSheet("background-color: rgb(47, 47, 47);")
        self.bgLbl.setText("")
        self.bgLbl.setObjectName("bgLbl")
        self.logoLbl = QtWidgets.QLabel(main)
        self.logoLbl.setGeometry(QtCore.QRect(100, 0, 355, 122))
        self.logoLbl.setStyleSheet("QLabel {\n"
"    image: url(:/5 1.png);\n"
"}")
        self.logoLbl.setText("")
        self.logoLbl.setObjectName("logoLbl")
        self.fullScreenBtn = QtWidgets.QPushButton(main)
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
        self.filterBtn = QtWidgets.QPushButton(main)
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
        self.closeBtn = QtWidgets.QPushButton(main)
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
        self.recordBtn = QtWidgets.QPushButton(main)
        self.recordBtn.setGeometry(QtCore.QRect(30, 599, 35, 35))
        self.recordBtn.setStyleSheet("QPushButton {\n"
"    \n"
"    border-image: url(:/image 3.png);\n"
"}")
        self.recordBtn.setText("")
        self.recordBtn.setObjectName("recordBtn")
        self.label = QtWidgets.QLabel(main)
        self.label.setGeometry(QtCore.QRect(70, 590, 427, 53))
        self.label.setStyleSheet("QLabel {\n"
"    background-color : \"#666666\";\n"
"    border-radius : \"18px\";\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.messagInput = QtWidgets.QLineEdit(main)
        self.messagInput.setGeometry(QtCore.QRect(86, 591, 341, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.messagInput.setFont(font)
        self.messagInput.setStyleSheet("QLineEdit {\n"
"    background-color : \"#666666\";\n"
"    color : \"#CBCBCB\";\n"
"}")
        self.messagInput.setObjectName("messagInput")
        self.sendMsgBtn = QtWidgets.QPushButton(main)
        self.sendMsgBtn.setGeometry(QtCore.QRect(441, 596, 40, 40))
        self.sendMsgBtn.setStyleSheet("QPushButton {\n"
"    background-color : \"#FFFFFF\";\n"
"    border-image: url(:/image 4.png);\n"
"}")
        self.sendMsgBtn.setText("")
        self.sendMsgBtn.setObjectName("sendMsgBtn")
        self.noteLbl = QtWidgets.QLabel(main)
        self.noteLbl.setGeometry(QtCore.QRect(70, 670, 130, 62))
        self.noteLbl.setStyleSheet("QLabel {\n"
"    background-color : \"#666666\";\n"
"    border-radius : \"22px\";\n"
"}")
        self.noteLbl.setText("")
        self.noteLbl.setObjectName("noteLbl")
        self.captureBtn = QtWidgets.QLabel(main)
        self.captureBtn.setGeometry(QtCore.QRect(370, 670, 130, 62))
        self.captureBtn.setStyleSheet("QLabel {\n"
"    background-color : \"#666666\";\n"
"    border-radius : \"22px\";\n"
"}")
        self.captureBtn.setText("")
        self.captureBtn.setObjectName("captureBtn")
        self.smodeLbl = QtWidgets.QLabel(main)
        self.smodeLbl.setGeometry(QtCore.QRect(220, 670, 130, 62))
        self.smodeLbl.setStyleSheet("QLabel {\n"
"    background-color : \"#666666\";\n"
"    border-radius : \"22px\";\n"
"}")
        self.smodeLbl.setText("")
        self.smodeLbl.setObjectName("smodeLbl")
        self.noteBtn = QtWidgets.QPushButton(main)
        self.noteBtn.setGeometry(QtCore.QRect(77, 678, 114, 45))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.noteBtn.setFont(font)
        self.noteBtn.setStyleSheet("QPushButton {\n"
"    color : \"#FFFFFF\";\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image 6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.noteBtn.setIcon(icon)
        self.noteBtn.setObjectName("noteBtn")
        self.smodeBtn = QtWidgets.QPushButton(main)
        self.smodeBtn.setGeometry(QtCore.QRect(227, 678, 115, 44))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.smodeBtn.setFont(font)
        self.smodeBtn.setStyleSheet("QPushButton {\n"
"    color : \"#FFFFFF\";\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/image 7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.smodeBtn.setIcon(icon1)
        self.smodeBtn.setObjectName("smodeBtn")
        self.smodeBtn_2 = QtWidgets.QPushButton(main)
        self.smodeBtn_2.setGeometry(QtCore.QRect(378, 677, 113, 48))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.smodeBtn_2.setFont(font)
        self.smodeBtn_2.setStyleSheet("QPushButton {\n"
"    color : \"#FFFFFF\";\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/image 8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.smodeBtn_2.setIcon(icon2)
        self.smodeBtn_2.setObjectName("smodeBtn_2")
        self.scrollArea = QtWidgets.QScrollArea(main)
        self.scrollArea.setGeometry(QtCore.QRect(40, 130, 481, 451))
        self.scrollArea.setStyleSheet("background-color:rgb(47,47,47);")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 481, 451))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Form"))
        self.messagInput.setPlaceholderText(_translate("main", "Enter message"))
        self.noteBtn.setText(_translate("main", "Note"))
        self.smodeBtn.setText(_translate("main", "Speech Mode"))
        self.smodeBtn_2.setText(_translate("main", "Screenshot"))
import resource.resource_rc

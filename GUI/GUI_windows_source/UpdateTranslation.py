# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UpdateTranslation.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from GUI.pictures import resources

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 380)
        Dialog.setMinimumSize(QtCore.QSize(650, 380))
        Dialog.setMaximumSize(QtCore.QSize(650, 380))
        Dialog.setStyleSheet("background-color: transparent;\n"
"")
        self.BackgroundFrame = QtWidgets.QFrame(Dialog)
        self.BackgroundFrame.setGeometry(QtCore.QRect(0, -10, 687, 387))
        self.BackgroundFrame.setMinimumSize(QtCore.QSize(687, 387))
        self.BackgroundFrame.setMaximumSize(QtCore.QSize(687, 387))
        self.BackgroundFrame.setStyleSheet("background-image: url(:/backgrounds/backgrounds/UpdateTranslation.png);")
        self.BackgroundFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BackgroundFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BackgroundFrame.setObjectName("BackgroundFrame")
        self.ExitButton = QtWidgets.QPushButton(Dialog)
        self.ExitButton.setGeometry(QtCore.QRect(620, 0, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.ExitButton.setFont(font)
        self.ExitButton.setStyleSheet("QPushButton{\n"
"    background-color: rgba(31, 37, 51, 10);\n"
"    color: #ffffff;\n"
"    }\n"
"QPushButton:hover{\n"
"    background-color: rgba(56, 57, 61, 50);\n"
"    color: rgb(199, 199, 199);\n"
"    }\n"
"QPushButton:pressed{\n"
"    background-color: rgba(194, 194, 194, 50);\n"
"    color: rgb(255, 60, 63)\n"
"    }")
        self.ExitButton.setText("X")
        self.ExitButton.setObjectName("ExitButton")
        self.ReferenceButton = QtWidgets.QPushButton(Dialog)
        self.ReferenceButton.setGeometry(QtCore.QRect(10, 0, 21, 21))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ReferenceButton.setFont(font)
        self.ReferenceButton.setStyleSheet("QPushButton{\n"
"    background-color: rgba(31, 37, 51, 0);\n"
"    color: #ffffff;\n"
"    }\n"
"QPushButton:hover{\n"
"    background-color: rgba(56, 57, 61, 50);\n"
"    color: rgb(199, 199, 199);\n"
"    }\n"
"QPushButton:pressed{\n"
"    background-color: rgba(194, 194, 194, 50);\n"
"    color: #5abe41\n"
"    }")
        self.ReferenceButton.setText("?")
        self.ReferenceButton.setObjectName("ReferenceButton")
        self.UpdateTranslationLabel = QtWidgets.QLabel(Dialog)
        self.UpdateTranslationLabel.setGeometry(QtCore.QRect(20, 40, 281, 41))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.UpdateTranslationLabel.setFont(font)
        self.UpdateTranslationLabel.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.UpdateTranslationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.UpdateTranslationLabel.setObjectName("UpdateTranslationLabel")
        self.BottomShadowFrame = QtWidgets.QFrame(Dialog)
        self.BottomShadowFrame.setGeometry(QtCore.QRect(-20, 300, 687, 100))
        self.BottomShadowFrame.setMinimumSize(QtCore.QSize(687, 100))
        self.BottomShadowFrame.setMaximumSize(QtCore.QSize(687, 100))
        self.BottomShadowFrame.setMouseTracking(False)
        self.BottomShadowFrame.setAcceptDrops(False)
        self.BottomShadowFrame.setStyleSheet("background-image: url(:/effects/effects/bottom_shadow.png);")
        self.BottomShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BottomShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BottomShadowFrame.setObjectName("BottomShadowFrame")
        self.WindowMoveButton = QtWidgets.QPushButton(Dialog)
        self.WindowMoveButton.setGeometry(QtCore.QRect(0, 0, 651, 21))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.WindowMoveButton.setFont(font)
        self.WindowMoveButton.setStyleSheet("QPushButton{\n"
"    color: transparent;\n"
"}")
        self.WindowMoveButton.setText("")
        self.WindowMoveButton.setObjectName("WindowMoveButton")
        self.OldTrTitleLabel = QtWidgets.QLabel(Dialog)
        self.OldTrTitleLabel.setGeometry(QtCore.QRect(10, 101, 281, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.OldTrTitleLabel.setFont(font)
        self.OldTrTitleLabel.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.OldTrTitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.OldTrTitleLabel.setObjectName("OldTrTitleLabel")
        self.NewVerTitleLabel = QtWidgets.QLabel(Dialog)
        self.NewVerTitleLabel.setGeometry(QtCore.QRect(360, 100, 271, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.NewVerTitleLabel.setFont(font)
        self.NewVerTitleLabel.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.NewVerTitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.NewVerTitleLabel.setObjectName("NewVerTitleLabel")
        self.ChooseNewVerFileButton = QtWidgets.QPushButton(Dialog)
        self.ChooseNewVerFileButton.setGeometry(QtCore.QRect(430, 156, 141, 27))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ChooseNewVerFileButton.setFont(font)
        self.ChooseNewVerFileButton.setStyleSheet("QPushButton{\n"
"    background-color: rgba(50, 50, 50, 50);\n"
"    border: #c2c2c2;\n"
"    border-radius: 13px;\n"
"    min-height: 27px;\n"
"    color: #ffffff;\n"
"    }\n"
"QPushButton:hover{\n"
"    background-color: #31858f;\n"
"    border: #31858f;\n"
"    color: #ffffff;\n"
"    }\n"
"QPushButton:pressed{\n"
"    background-color: #05B8CC;\n"
"    border: 2px solid #05B8CC;\n"
"    }")
        self.ChooseNewVerFileButton.setObjectName("ChooseNewVerFileButton")
        self.ChooseOldTrFileButton = QtWidgets.QPushButton(Dialog)
        self.ChooseOldTrFileButton.setGeometry(QtCore.QRect(80, 154, 141, 27))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ChooseOldTrFileButton.setFont(font)
        self.ChooseOldTrFileButton.setStyleSheet("QPushButton{\n"
"    background-color: rgba(50, 50, 50, 50);\n"
"    border: #c2c2c2;\n"
"    border-radius: 13px;\n"
"    min-height: 27px;\n"
"    color: #ffffff;\n"
"    }\n"
"QPushButton:hover{\n"
"    background-color: #438e30;\n"
"    border: #31858f;\n"
"    color: #ffffff;\n"
"    }\n"
"QPushButton:pressed{\n"
"    background-color: #c2c2c2;\n"
"    border: 2px solid #c2c2c2;\n"
"    }")
        self.ChooseOldTrFileButton.setObjectName("ChooseOldTrFileButton")
        self.OldTrStatusLabel = QtWidgets.QLabel(Dialog)
        self.OldTrStatusLabel.setGeometry(QtCore.QRect(130, 236, 41, 41))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.OldTrStatusLabel.setFont(font)
        self.OldTrStatusLabel.setStyleSheet("QLabel{\n"
"    background-color: #c93c3c;\n"
"    border: #c2c2c2;\n"
"    border-radius: 20px;\n"
"    min-height: 27px;\n"
"    color: #ffffff;\n"
"    }\n"
"QLabel:hover{\n"
"    background-color: #b33434;\n"
"    border: #31858f;\n"
"    color: #ffffff;\n"
"    }")
        self.OldTrStatusLabel.setText("—")
        self.OldTrStatusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.OldTrStatusLabel.setObjectName("OldTrStatusLabel")
        self.NewVerStatusLabel = QtWidgets.QLabel(Dialog)
        self.NewVerStatusLabel.setGeometry(QtCore.QRect(480, 236, 41, 41))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.NewVerStatusLabel.setFont(font)
        self.NewVerStatusLabel.setStyleSheet("QLabel{\n"
"    background-color: #c93c3c;\n"
"    border: #c2c2c2;\n"
"    border-radius: 20px;\n"
"    min-height: 27px;\n"
"    color: #ffffff;\n"
"    }\n"
"QLabel:hover{\n"
"    background-color: #b33434;\n"
"    border: #31858f;\n"
"    color: #ffffff;\n"
"    }")
        self.NewVerStatusLabel.setText("—")
        self.NewVerStatusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.NewVerStatusLabel.setObjectName("NewVerStatusLabel")
        self.AcceptButton = QtWidgets.QPushButton(Dialog)
        self.AcceptButton.setGeometry(QtCore.QRect(220, 320, 211, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.AcceptButton.setFont(font)
        self.AcceptButton.setStyleSheet("QPushButton{\n"
"    background-color: rgba(31, 37, 51, 50);\n"
"    border: 2px solid #ffffff;\n"
"    border-radius: 15px;\n"
"    color: #ffffff;\n"
"    }\n"
"QPushButton:hover{\n"
"    background-color: rgba(100, 100, 100, 50);\n"
"    }\n"
"QPushButton:pressed{\n"
"    background-color: rgba(194, 194, 194, 50);\n"
"    border: #c2c2c2;\n"
"    }")
        self.AcceptButton.setObjectName("AcceptButton")
        self.update_logo = QtWidgets.QLabel(Dialog)
        self.update_logo.setGeometry(QtCore.QRect(550, 30, 61, 51))
        self.update_logo.setStyleSheet("background-color: none;\n"
"image: url(:/icons/icons/update.png);")
        self.update_logo.setText("")
        self.update_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.update_logo.setObjectName("update_logo")
        self.BackgroundFrame.raise_()
        self.UpdateTranslationLabel.raise_()
        self.BottomShadowFrame.raise_()
        self.WindowMoveButton.raise_()
        self.ReferenceButton.raise_()
        self.ExitButton.raise_()
        self.OldTrTitleLabel.raise_()
        self.NewVerTitleLabel.raise_()
        self.ChooseNewVerFileButton.raise_()
        self.ChooseOldTrFileButton.raise_()
        self.OldTrStatusLabel.raise_()
        self.NewVerStatusLabel.raise_()
        self.AcceptButton.raise_()
        self.update_logo.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Обновление перевода"))
        self.UpdateTranslationLabel.setText(_translate("Dialog", "Обновить перевод"))
        self.OldTrTitleLabel.setText(_translate("Dialog", "Устаревший перевод"))
        self.NewVerTitleLabel.setText(_translate("Dialog", "Новая версия оригинала"))
        self.ChooseNewVerFileButton.setText(_translate("Dialog", "Выбрать"))
        self.ChooseOldTrFileButton.setText(_translate("Dialog", "Выбрать"))
        self.AcceptButton.setText(_translate("Dialog", "Подтвердить"))

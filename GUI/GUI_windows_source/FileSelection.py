# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FileSelection.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
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
        self.BackgroundFrame.setStyleSheet("background-image: url(:/backgrounds/backgrounds/FileSelection.png);")
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
        self.UpdateTranslationLabel.setGeometry(QtCore.QRect(20, 80, 611, 51))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.UpdateTranslationLabel.setFont(font)
        self.UpdateTranslationLabel.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.UpdateTranslationLabel.setText("")
        self.UpdateTranslationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.UpdateTranslationLabel.setWordWrap(True)
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
        self.LandingArea = QtWidgets.QScrollArea(Dialog)
        self.LandingArea.setGeometry(QtCore.QRect(10, 140, 631, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LandingArea.sizePolicy().hasHeightForWidth())
        self.LandingArea.setSizePolicy(sizePolicy)
        self.LandingArea.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LandingArea.setStyleSheet("QScrollBar:vertical{\n"
"    background: transparent;\n"
"    width: 5px;\n"
"    margin: 0;\n"
"    }\n"
"QScrollBar::handle:vertical{\n"
"    background-color: #5abe41;\n"
"    min-height: 20px;\n"
"    }\n"
"QScrollBar::add-line:vertical{\n"
"    background: transparent;\n"
"    height: 0px;\n"
"    }\n"
"QScrollBar::sub-line:vertical{\n"
"    background: transparent;\n"
"    height: 0px;\n"
"    }\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{\n"
"    background: transparent;\n"
"    height: 0px;\n"
"    }")
        self.LandingArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LandingArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.LandingArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.LandingArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.LandingArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.LandingArea.setWidgetResizable(True)
        self.LandingArea.setAlignment(QtCore.Qt.AlignCenter)
        self.LandingArea.setObjectName("LandingArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 626, 322))
        self.scrollAreaWidgetContents.setStyleSheet("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(-1, 150, -1, 150)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(40)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout.addLayout(self.gridLayout)
        self.LandingArea.setWidget(self.scrollAreaWidgetContents)
        self.ModIDListComboBox = QtWidgets.QComboBox(Dialog)
        self.ModIDListComboBox.setGeometry(QtCore.QRect(350, 30, 271, 51))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        self.ModIDListComboBox.setFont(font)
        self.ModIDListComboBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.ModIDListComboBox.setStyleSheet(" QComboBox {\n"
"    padding-bottom: 30px;\n"
"    color: white;\n"
"    border: transparent;\n"
"    margin: 26px;\n"
"}\n"
" QComboBox::hover {\n"
"    background-color: #05B8CC;\n"
"}\n"
"\n"
" QAbstractItemView {\n"
"    background-color: #141821;\n"
"    border: 1px solid #141821;\n"
"    border-radius: 15px;\n"
"    selection-background-color: transparent;\n"
"    selection-color: #05B8CC;\n"
"    color: white;\n"
"    padding: 10px;\n"
"    outline: 0px;\n"
"}")
        self.ModIDListComboBox.setEditable(False)
        self.ModIDListComboBox.setPlaceholderText("")
        self.ModIDListComboBox.setObjectName("ModIDListComboBox")
        self.update_logo = QtWidgets.QLabel(Dialog)
        self.update_logo.setGeometry(QtCore.QRect(10, 30, 61, 51))
        self.update_logo.setStyleSheet("background-color: none;\n"
"image: url(:/icons/icons/update.png);")
        self.update_logo.setText("")
        self.update_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.update_logo.setObjectName("update_logo")
        self.UpdateTranslationLabel_2 = QtWidgets.QLabel(Dialog)
        self.UpdateTranslationLabel_2.setGeometry(QtCore.QRect(60, 30, 281, 41))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.UpdateTranslationLabel_2.setFont(font)
        self.UpdateTranslationLabel_2.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.UpdateTranslationLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.UpdateTranslationLabel_2.setObjectName("UpdateTranslationLabel_2")
        self.BackgroundFrame.raise_()
        self.UpdateTranslationLabel.raise_()
        self.BottomShadowFrame.raise_()
        self.WindowMoveButton.raise_()
        self.ReferenceButton.raise_()
        self.ExitButton.raise_()
        self.LandingArea.raise_()
        self.ModIDListComboBox.raise_()
        self.update_logo.raise_()
        self.UpdateTranslationLabel_2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Обновление перевода"))
        self.UpdateTranslationLabel_2.setText(_translate("Dialog", "Выбор основного файла"))

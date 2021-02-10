# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Contact.ui'
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
        Dialog.resize(650, 350)
        Dialog.setMinimumSize(QtCore.QSize(650, 350))
        Dialog.setMaximumSize(QtCore.QSize(650, 350))
        Dialog.setStyleSheet("background-color: transparent;")
        self.BackgroundFrame = QtWidgets.QFrame(Dialog)
        self.BackgroundFrame.setGeometry(QtCore.QRect(-20, -10, 687, 360))
        self.BackgroundFrame.setMinimumSize(QtCore.QSize(687, 360))
        self.BackgroundFrame.setMaximumSize(QtCore.QSize(687, 250))
        self.BackgroundFrame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.BackgroundFrame.setStyleSheet("background-image: url(:/backgrounds/backgrounds/Contact.png);")
        self.BackgroundFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BackgroundFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BackgroundFrame.setObjectName("BackgroundFrame")
        self.ExitButton = QtWidgets.QPushButton(Dialog)
        self.ExitButton.setGeometry(QtCore.QRect(620, 0, 21, 21))
        font = QtGui.QFont()
        font.setFamily("laCartoonerie(RUS BY LYAJKA)")
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
        self.InfoLabel_0 = QtWidgets.QLabel(Dialog)
        self.InfoLabel_0.setGeometry(QtCore.QRect(20, 30, 611, 31))
        font = QtGui.QFont()
        font.setFamily("laCartoonerie(RUS BY LYAJKA)")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.InfoLabel_0.setFont(font)
        self.InfoLabel_0.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.InfoLabel_0.setAlignment(QtCore.Qt.AlignCenter)
        self.InfoLabel_0.setObjectName("InfoLabel_0")
        self.ChengerLabel = QtWidgets.QLabel(Dialog)
        self.ChengerLabel.setGeometry(QtCore.QRect(360, 120, 111, 31))
        font = QtGui.QFont()
        font.setFamily("laCartoonerie(RUS BY LYAJKA)")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ChengerLabel.setFont(font)
        self.ChengerLabel.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.ChengerLabel.setText("Chenger1")
        self.ChengerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ChengerLabel.setObjectName("ChengerLabel")
        self.InfoLabel_1 = QtWidgets.QLabel(Dialog)
        self.InfoLabel_1.setGeometry(QtCore.QRect(20, 240, 611, 31))
        font = QtGui.QFont()
        font.setFamily("laCartoonerie(RUS BY LYAJKA)")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.InfoLabel_1.setFont(font)
        self.InfoLabel_1.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.InfoLabel_1.setAlignment(QtCore.Qt.AlignCenter)
        self.InfoLabel_1.setObjectName("InfoLabel_1")
        self.LetisoEmailLine = QtWidgets.QLineEdit(Dialog)
        self.LetisoEmailLine.setGeometry(QtCore.QRect(30, 290, 211, 31))
        font = QtGui.QFont()
        font.setFamily("laCartoonerie(RUS BY LYAJKA)")
        font.setPointSize(11)
        self.LetisoEmailLine.setFont(font)
        self.LetisoEmailLine.setStyleSheet("QLineEdit{\n"
"    background-color: rgba(31, 37, 51, 0);\n"
"    border: 0px;\n"
"    color: #ffffff;\n"
"    }\n"
"QLineEdit:hover{\n"
"    background-color: rgba(56, 57, 61, 10);\n"
"    }\n"
"")
        self.LetisoEmailLine.setText("letisodianta@gmail.com")
        self.LetisoEmailLine.setFrame(False)
        self.LetisoEmailLine.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LetisoEmailLine.setReadOnly(True)
        self.LetisoEmailLine.setObjectName("LetisoEmailLine")
        self.ChengerEmailLine = QtWidgets.QLineEdit(Dialog)
        self.ChengerEmailLine.setGeometry(QtCore.QRect(400, 290, 221, 31))
        font = QtGui.QFont()
        font.setFamily("laCartoonerie(RUS BY LYAJKA)")
        font.setPointSize(11)
        self.ChengerEmailLine.setFont(font)
        self.ChengerEmailLine.setStyleSheet("QLineEdit{\n"
"    background-color: rgba(31, 37, 51, 0);\n"
"    border: 0px;\n"
"    color: #ffffff;\n"
"    }\n"
"QLineEdit:hover{\n"
"    background-color: rgba(56, 57, 61, 10);\n"
"    }\n"
"")
        self.ChengerEmailLine.setText("exs2199@gmail.com")
        self.ChengerEmailLine.setFrame(False)
        self.ChengerEmailLine.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ChengerEmailLine.setReadOnly(True)
        self.ChengerEmailLine.setObjectName("ChengerEmailLine")
        self.InfoLabel_2 = QtWidgets.QLabel(Dialog)
        self.InfoLabel_2.setGeometry(QtCore.QRect(260, 290, 151, 31))
        font = QtGui.QFont()
        font.setFamily("laCartoonerie(RUS BY LYAJKA)")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.InfoLabel_2.setFont(font)
        self.InfoLabel_2.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.InfoLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.InfoLabel_2.setObjectName("InfoLabel_2")
        self.MidLineFrame = QtWidgets.QFrame(Dialog)
        self.MidLineFrame.setGeometry(QtCore.QRect(-20, 210, 700, 20))
        self.MidLineFrame.setMinimumSize(QtCore.QSize(700, 20))
        self.MidLineFrame.setMaximumSize(QtCore.QSize(700, 20))
        self.MidLineFrame.setStyleSheet("background-image: url(:/effects/effects/mid_line.png);")
        self.MidLineFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MidLineFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MidLineFrame.setObjectName("MidLineFrame")
        self.SteamChengerLink = QtWidgets.QLabel(Dialog)
        self.SteamChengerLink.setGeometry(QtCore.QRect(480, 140, 101, 31))
        font = QtGui.QFont()
        font.setFamily("laCartoonerie(RUS BY LYAJKA)")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.SteamChengerLink.setFont(font)
        self.SteamChengerLink.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.SteamChengerLink.setText("<html><head/><body><p><a href=\"https://steamcommunity.com/id/marik0660\"><span style=\" text-decoration: underline; color:#ffffff;\">Steam</span></a></p></body></html>")
        self.SteamChengerLink.setAlignment(QtCore.Qt.AlignCenter)
        self.SteamChengerLink.setOpenExternalLinks(True)
        self.SteamChengerLink.setObjectName("SteamChengerLink")
        self.GitHubChengerLink = QtWidgets.QLabel(Dialog)
        self.GitHubChengerLink.setGeometry(QtCore.QRect(460, 90, 101, 31))
        font = QtGui.QFont()
        font.setFamily("laCartoonerie(RUS BY LYAJKA)")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.GitHubChengerLink.setFont(font)
        self.GitHubChengerLink.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.GitHubChengerLink.setText("<html><head/><body><p><a href=\"https://github.com/Chenger1\"><span style=\" text-decoration: underline; color:#ffffff;\">GitHub</span></a></p></body></html>")
        self.GitHubChengerLink.setAlignment(QtCore.Qt.AlignCenter)
        self.GitHubChengerLink.setOpenExternalLinks(True)
        self.GitHubChengerLink.setObjectName("GitHubChengerLink")
        self.LetisoLabel = QtWidgets.QLabel(Dialog)
        self.LetisoLabel.setGeometry(QtCore.QRect(170, 120, 121, 31))
        font = QtGui.QFont()
        font.setFamily("laCartoonerie(RUS BY LYAJKA)")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.LetisoLabel.setFont(font)
        self.LetisoLabel.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.LetisoLabel.setText("Letiso")
        self.LetisoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LetisoLabel.setObjectName("LetisoLabel")
        self.git_logo_1 = QtWidgets.QLabel(Dialog)
        self.git_logo_1.setGeometry(QtCore.QRect(550, 80, 51, 51))
        self.git_logo_1.setStyleSheet("background-color: none;\n"
"image: url(:/icons/icons/github.png);\n"
"")
        self.git_logo_1.setText("")
        self.git_logo_1.setAlignment(QtCore.Qt.AlignCenter)
        self.git_logo_1.setObjectName("git_logo_1")
        self.steam_logo_1 = QtWidgets.QLabel(Dialog)
        self.steam_logo_1.setGeometry(QtCore.QRect(570, 130, 51, 51))
        self.steam_logo_1.setStyleSheet("background-color: none;\n"
"image: url(:/icons/icons/steam.png);\n"
"")
        self.steam_logo_1.setText("")
        self.steam_logo_1.setAlignment(QtCore.Qt.AlignCenter)
        self.steam_logo_1.setObjectName("steam_logo_1")
        self.TelegramLetisoLink = QtWidgets.QLabel(Dialog)
        self.TelegramLetisoLink.setGeometry(QtCore.QRect(50, 160, 121, 31))
        font = QtGui.QFont()
        font.setFamily("laCartoonerie(RUS BY LYAJKA)")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.TelegramLetisoLink.setFont(font)
        self.TelegramLetisoLink.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.TelegramLetisoLink.setText("<html><head/><body><p><a href=\"https://t.me/Letiso_Dianta\"><span style=\" text-decoration: underline; color:#ffffff;\">Telegram</span></a></p></body></html>")
        self.TelegramLetisoLink.setAlignment(QtCore.Qt.AlignCenter)
        self.TelegramLetisoLink.setOpenExternalLinks(True)
        self.TelegramLetisoLink.setObjectName("TelegramLetisoLink")
        self.telegram_logo_0 = QtWidgets.QLabel(Dialog)
        self.telegram_logo_0.setGeometry(QtCore.QRect(10, 150, 51, 51))
        self.telegram_logo_0.setStyleSheet("background-color: none;\n"
"image: url(:/icons/icons/telegram.png);")
        self.telegram_logo_0.setText("")
        self.telegram_logo_0.setAlignment(QtCore.Qt.AlignCenter)
        self.telegram_logo_0.setObjectName("telegram_logo_0")
        self.SteamLetisoLink = QtWidgets.QLabel(Dialog)
        self.SteamLetisoLink.setGeometry(QtCore.QRect(70, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("laCartoonerie(RUS BY LYAJKA)")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.SteamLetisoLink.setFont(font)
        self.SteamLetisoLink.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.SteamLetisoLink.setText("<html><head/><body><p><a href=\"http://steamcommunity.com/id/letiso\"><span style=\" text-decoration: underline; color:#ffffff;\">Steam</span></a></p></body></html>")
        self.SteamLetisoLink.setAlignment(QtCore.Qt.AlignCenter)
        self.SteamLetisoLink.setOpenExternalLinks(True)
        self.SteamLetisoLink.setObjectName("SteamLetisoLink")
        self.steam_logo_0 = QtWidgets.QLabel(Dialog)
        self.steam_logo_0.setGeometry(QtCore.QRect(30, 110, 51, 51))
        self.steam_logo_0.setStyleSheet("background-color: none;\n"
"image: url(:/icons/icons/steam.png);")
        self.steam_logo_0.setText("")
        self.steam_logo_0.setAlignment(QtCore.Qt.AlignCenter)
        self.steam_logo_0.setObjectName("steam_logo_0")
        self.git_logo_0 = QtWidgets.QLabel(Dialog)
        self.git_logo_0.setGeometry(QtCore.QRect(50, 70, 51, 51))
        self.git_logo_0.setStyleSheet("background-color: none;\n"
"image: url(:/icons/icons/github.png);\n"
"")
        self.git_logo_0.setText("")
        self.git_logo_0.setAlignment(QtCore.Qt.AlignCenter)
        self.git_logo_0.setObjectName("git_logo_0")
        self.GitHubLetisoLink = QtWidgets.QLabel(Dialog)
        self.GitHubLetisoLink.setGeometry(QtCore.QRect(90, 80, 101, 31))
        font = QtGui.QFont()
        font.setFamily("laCartoonerie(RUS BY LYAJKA)")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.GitHubLetisoLink.setFont(font)
        self.GitHubLetisoLink.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.GitHubLetisoLink.setText("<html><head/><body><p><a href=\"https://github.com/Letiso\"><span style=\" color:#ffffff;\">GitHub</span></a></p></body></html>")
        self.GitHubLetisoLink.setAlignment(QtCore.Qt.AlignCenter)
        self.GitHubLetisoLink.setOpenExternalLinks(True)
        self.GitHubLetisoLink.setObjectName("GitHubLetisoLink")
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
        self.BackgroundFrame.raise_()
        self.WindowMoveButton.raise_()
        self.ExitButton.raise_()
        self.InfoLabel_0.raise_()
        self.ChengerLabel.raise_()
        self.InfoLabel_1.raise_()
        self.LetisoEmailLine.raise_()
        self.ChengerEmailLine.raise_()
        self.InfoLabel_2.raise_()
        self.MidLineFrame.raise_()
        self.SteamChengerLink.raise_()
        self.GitHubChengerLink.raise_()
        self.LetisoLabel.raise_()
        self.git_logo_1.raise_()
        self.steam_logo_1.raise_()
        self.TelegramLetisoLink.raise_()
        self.telegram_logo_0.raise_()
        self.SteamLetisoLink.raise_()
        self.steam_logo_0.raise_()
        self.git_logo_0.raise_()
        self.GitHubLetisoLink.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Связь"))
        self.InfoLabel_0.setText(_translate("Dialog", "Вы можете связаться с нами, если пользуетесь:"))
        self.InfoLabel_1.setText(_translate("Dialog", "Также пишите свои вопросы на электронную почту:"))
        self.InfoLabel_2.setText(_translate("Dialog", "либо"))

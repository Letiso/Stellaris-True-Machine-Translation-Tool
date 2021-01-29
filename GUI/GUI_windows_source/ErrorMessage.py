# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ErrorMessage.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from GUI.pictures import resources

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 250)
        Dialog.setMinimumSize(QtCore.QSize(650, 250))
        Dialog.setMaximumSize(QtCore.QSize(650, 250))
        Dialog.setStyleSheet("background-color: transparent;")
        self.AcceptButton = QtWidgets.QPushButton(Dialog)
        self.AcceptButton.setGeometry(QtCore.QRect(250, 190, 151, 31))
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
"    background-color: rgba(56, 57, 61, 50);\n"
"    }\n"
"QPushButton:pressed{\n"
"    background-color: rgba(194, 194, 194, 50);\n"
"    border: #c2c2c2;\n"
"    }")
        self.AcceptButton.setObjectName("AcceptButton")
        self.BackgroundFrame = QtWidgets.QFrame(Dialog)
        self.BackgroundFrame.setGeometry(QtCore.QRect(-20, -10, 687, 264))
        self.BackgroundFrame.setMinimumSize(QtCore.QSize(687, 264))
        self.BackgroundFrame.setMaximumSize(QtCore.QSize(687, 250))
        self.BackgroundFrame.setStyleSheet("background-image: url(:/backgrounds/backgrounds/ErrorMessage.png);")
        self.BackgroundFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BackgroundFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BackgroundFrame.setObjectName("BackgroundFrame")
        self.ErrorLabel = QtWidgets.QLabel(Dialog)
        self.ErrorLabel.setGeometry(QtCore.QRect(480, 30, 131, 41))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ErrorLabel.setFont(font)
        self.ErrorLabel.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.ErrorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ErrorLabel.setObjectName("ErrorLabel")
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
        self.ExitButton = QtWidgets.QPushButton(Dialog)
        self.ExitButton.setGeometry(QtCore.QRect(620, 0, 21, 21))
        self.ExitButton.setMinimumSize(QtCore.QSize(20, 20))
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
        self.InfoLabel = QtWidgets.QLabel(Dialog)
        self.InfoLabel.setGeometry(QtCore.QRect(30, 70, 591, 91))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.InfoLabel.setFont(font)
        self.InfoLabel.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.InfoLabel.setText("Информация")
        self.InfoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.InfoLabel.setObjectName("InfoLabel")
        self.StringsList = QtWidgets.QLabel(Dialog)
        self.StringsList.setGeometry(QtCore.QRect(74, 110, 271, 20))
        self.StringsList.setObjectName("StringsList")
        self.StringsList.raise_()
        self.BackgroundFrame.raise_()
        self.WindowMoveButton.raise_()
        self.AcceptButton.raise_()
        self.ErrorLabel.raise_()
        self.ExitButton.raise_()
        self.InfoLabel.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ошибка"))
        self.AcceptButton.setText(_translate("Dialog", "Понимаю"))
        self.ErrorLabel.setText(_translate("Dialog", "Ошибка"))
        self.StringsList.setText(_translate("Dialog", "В этой модификации нечего переводить\n"
"\n"
"Выберите другую.Перевод уже был записан.Ошибка записи файла: отсутствует перевод.Вы не выбрали мод.Файл перевода поврежден или удален.Моды не найдены.Вы выбрали не тот файл.Вы не ввели ID мода.Строка ID содержит сторонние символы.Мод не найден.В коллекции больше нечего переводить.Не найдено совпадений строк.Файлы идентичны.Выбрать можно только файлы с расширением\n"
"\n"
"* yml * или * txt *.Следует выбрать * старый * и * новый * файлы.Неверный ключ [Для разработчиков]"))

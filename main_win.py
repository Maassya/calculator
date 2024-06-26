# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 620)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(480, 620))
        MainWindow.setMaximumSize(QtCore.QSize(480, 620))
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(" background-color: black;")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: black;")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.line_result = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_result.sizePolicy().hasHeightForWidth())
        self.line_result.setSizePolicy(sizePolicy)
        self.line_result.setMinimumSize(QtCore.QSize(0, 65))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(25)
        self.line_result.setFont(font)
        self.line_result.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.line_result.setStyleSheet("color: black; background-color: white;")
        self.line_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.line_result.setReadOnly(True)
        self.line_result.setObjectName("line_result")
        self.verticalLayout.addWidget(self.line_result)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("color: white; background-color: grey;")
        self.btn_7.setObjectName("btn_7")
        self.horizontalLayout.addWidget(self.btn_7)
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("color: white; background-color: grey;")
        self.btn_8.setObjectName("btn_8")
        self.horizontalLayout.addWidget(self.btn_8)
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("color: white; background-color: grey;")
        self.btn_9.setObjectName("btn_9")
        self.horizontalLayout.addWidget(self.btn_9)
        self.btn_delenie = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delenie.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.btn_delenie.setFont(font)
        self.btn_delenie.setStyleSheet("color: white; background-color: orange;")
        self.btn_delenie.setObjectName("btn_delenie")
        self.horizontalLayout.addWidget(self.btn_delenie)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("color: white; background-color: grey;")
        self.btn_4.setObjectName("btn_4")
        self.horizontalLayout_2.addWidget(self.btn_4)
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("color: white; background-color: grey;")
        self.btn_5.setObjectName("btn_5")
        self.horizontalLayout_2.addWidget(self.btn_5)
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("color: white; background-color: grey;")
        self.btn_6.setObjectName("btn_6")
        self.horizontalLayout_2.addWidget(self.btn_6)
        self.btn_X = QtWidgets.QPushButton(self.centralwidget)
        self.btn_X.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_X.setFont(font)
        self.btn_X.setStyleSheet("color: white; background-color: orange;")
        self.btn_X.setObjectName("btn_X")
        self.horizontalLayout_2.addWidget(self.btn_X)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("color: white; background-color: grey;")
        self.btn_1.setObjectName("btn_1")
        self.horizontalLayout_3.addWidget(self.btn_1)
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("color: white; background-color: grey;")
        self.btn_2.setObjectName("btn_2")
        self.horizontalLayout_3.addWidget(self.btn_2)
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("color: white; background-color: grey;")
        self.btn_3.setObjectName("btn_3")
        self.horizontalLayout_3.addWidget(self.btn_3)
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_minus.setFont(font)
        self.btn_minus.setStyleSheet("color: white; background-color: orange;")
        self.btn_minus.setObjectName("btn_minus")
        self.horizontalLayout_3.addWidget(self.btn_minus)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("color: white; background-color: red;")
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout_4.addWidget(self.btn_clear)
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("color: white; background-color: grey;")
        self.btn_0.setObjectName("btn_0")
        self.horizontalLayout_4.addWidget(self.btn_0)
        self.btn_ravno = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ravno.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_ravno.setFont(font)
        self.btn_ravno.setStyleSheet("color: white; background-color: green;")
        self.btn_ravno.setObjectName("btn_ravno")
        self.horizontalLayout_4.addWidget(self.btn_ravno)
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet("color: white; background-color: orange;")
        self.btn_plus.setObjectName("btn_plus")
        self.horizontalLayout_4.addWidget(self.btn_plus)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.line_result.setPlaceholderText(_translate("MainWindow", "0"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_delenie.setText(_translate("MainWindow", "/"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_X.setText(_translate("MainWindow", "x"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_clear.setText(_translate("MainWindow", "AC"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_ravno.setText(_translate("MainWindow", "="))
        self.btn_plus.setText(_translate("MainWindow", "+"))

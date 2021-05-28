# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(653, 577)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_round = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_round.setFont(font)
        self.label_round.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_round.setAlignment(QtCore.Qt.AlignCenter)
        self.label_round.setObjectName("label_round")
        self.verticalLayout.addWidget(self.label_round)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_userWin = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_userWin.setFont(font)
        self.label_userWin.setStyleSheet("color: rgb(154, 157, 166);")
        self.label_userWin.setAlignment(QtCore.Qt.AlignCenter)
        self.label_userWin.setObjectName("label_userWin")
        self.horizontalLayout.addWidget(self.label_userWin)
        self.label_tie = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_tie.setFont(font)
        self.label_tie.setStyleSheet("color: rgb(154, 157, 166);")
        self.label_tie.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tie.setObjectName("label_tie")
        self.horizontalLayout.addWidget(self.label_tie)
        self.label_aiWin = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_aiWin.setFont(font)
        self.label_aiWin.setStyleSheet("color: rgb(154, 157, 166);")
        self.label_aiWin.setAlignment(QtCore.Qt.AlignCenter)
        self.label_aiWin.setObjectName("label_aiWin")
        self.horizontalLayout.addWidget(self.label_aiWin)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_userWin_score = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_userWin_score.setFont(font)
        self.label_userWin_score.setAlignment(QtCore.Qt.AlignCenter)
        self.label_userWin_score.setObjectName("label_userWin_score")
        self.horizontalLayout_2.addWidget(self.label_userWin_score)
        self.label_tie_score = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_tie_score.setFont(font)
        self.label_tie_score.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tie_score.setObjectName("label_tie_score")
        self.horizontalLayout_2.addWidget(self.label_tie_score)
        self.label_aiWin_score = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_aiWin_score.setFont(font)
        self.label_aiWin_score.setAlignment(QtCore.Qt.AlignCenter)
        self.label_aiWin_score.setObjectName("label_aiWin_score")
        self.horizontalLayout_2.addWidget(self.label_aiWin_score)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_img_user = QtWidgets.QLabel(self.centralwidget)
        self.label_img_user.setText("")
        self.label_img_user.setObjectName("label_img_user")
        self.horizontalLayout_3.addWidget(self.label_img_user)
        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setMaximumSize(QtCore.QSize(16777215, 190))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        self.label_info.setFont(font)
        self.label_info.setText("")
        self.label_info.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_info.setObjectName("label_info")
        self.horizontalLayout_3.addWidget(self.label_info)
        self.label_img_ai = QtWidgets.QLabel(self.centralwidget)
        self.label_img_ai.setText("")
        self.label_img_ai.setObjectName("label_img_ai")
        self.horizontalLayout_3.addWidget(self.label_img_ai)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(50, 10, 0, 20)
        self.horizontalLayout_4.setSpacing(40)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_rock = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rock.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_rock.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_rock.setStyleSheet("")
        self.pushButton_rock.setText("")
        self.pushButton_rock.setObjectName("pushButton_rock")
        self.horizontalLayout_4.addWidget(self.pushButton_rock)
        self.pushButton_paper = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_paper.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_paper.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_paper.setStyleSheet("")
        self.pushButton_paper.setText("")
        self.pushButton_paper.setObjectName("pushButton_paper")
        self.horizontalLayout_4.addWidget(self.pushButton_paper)
        self.pushButton_scissors = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_scissors.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_scissors.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_scissors.setStyleSheet("")
        self.pushButton_scissors.setText("")
        self.pushButton_scissors.setObjectName("pushButton_scissors")
        self.horizontalLayout_4.addWidget(self.pushButton_scissors)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.setStretch(0, 4)
        self.verticalLayout_2.setStretch(1, 10)
        self.verticalLayout_2.setStretch(2, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 653, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_round.setText(_translate("MainWindow", "ROUND 1"))
        self.label_userWin.setText(_translate("MainWindow", "WIN"))
        self.label_tie.setText(_translate("MainWindow", "TIE"))
        self.label_aiWin.setText(_translate("MainWindow", "WIN"))
        self.label_userWin_score.setText(_translate("MainWindow", "0"))
        self.label_tie_score.setText(_translate("MainWindow", "0"))
        self.label_aiWin_score.setText(_translate("MainWindow", "0"))

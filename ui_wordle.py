# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wordle.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1046, 892)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Combined = QWidget(self.centralwidget)
        self.Combined.setObjectName(u"Combined")
        self.Windows = QWidget(self.Combined)
        self.Windows.setObjectName(u"Windows")
        self.Windows.setGeometry(QRect(20, 30, 1017, 531))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Windows.sizePolicy().hasHeightForWidth())
        self.Windows.setSizePolicy(sizePolicy)
        self.Windows.setFocusPolicy(Qt.NoFocus)
        self.Windows.setLayoutDirection(Qt.LeftToRight)
        self.r1c1 = QLabel(self.Windows)
        self.r1c1.setObjectName(u"r1c1")
        self.r1c1.setGeometry(QRect(360, 40, 51, 61))
        self.r1c2 = QLabel(self.Windows)
        self.r1c2.setObjectName(u"r1c2")
        self.r1c2.setGeometry(QRect(420, 40, 51, 61))
        self.r1c3 = QLabel(self.Windows)
        self.r1c3.setObjectName(u"r1c3")
        self.r1c3.setGeometry(QRect(480, 40, 51, 61))
        self.r1c5 = QLabel(self.Windows)
        self.r1c5.setObjectName(u"r1c5")
        self.r1c5.setGeometry(QRect(600, 40, 51, 61))
        self.r1c5.setStyleSheet(u"border: 1px solid black;")
        self.r1c4 = QLabel(self.Windows)
        self.r1c4.setObjectName(u"r1c4")
        self.r1c4.setGeometry(QRect(540, 40, 51, 61))
        self.r2c3 = QLabel(self.Windows)
        self.r2c3.setObjectName(u"r2c3")
        self.r2c3.setGeometry(QRect(480, 120, 51, 61))
        self.r2c4 = QLabel(self.Windows)
        self.r2c4.setObjectName(u"r2c4")
        self.r2c4.setGeometry(QRect(540, 120, 51, 61))
        self.r2c2 = QLabel(self.Windows)
        self.r2c2.setObjectName(u"r2c2")
        self.r2c2.setGeometry(QRect(420, 120, 51, 61))
        self.r2c1 = QLabel(self.Windows)
        self.r2c1.setObjectName(u"r2c1")
        self.r2c1.setGeometry(QRect(360, 120, 51, 61))
        self.r2c5 = QLabel(self.Windows)
        self.r2c5.setObjectName(u"r2c5")
        self.r2c5.setGeometry(QRect(600, 120, 51, 61))
        self.r4c1 = QLabel(self.Windows)
        self.r4c1.setObjectName(u"r4c1")
        self.r4c1.setGeometry(QRect(360, 280, 51, 61))
        self.r3c3 = QLabel(self.Windows)
        self.r3c3.setObjectName(u"r3c3")
        self.r3c3.setGeometry(QRect(480, 200, 51, 61))
        self.r3c4 = QLabel(self.Windows)
        self.r3c4.setObjectName(u"r3c4")
        self.r3c4.setGeometry(QRect(540, 200, 51, 61))
        self.r4c5 = QLabel(self.Windows)
        self.r4c5.setObjectName(u"r4c5")
        self.r4c5.setGeometry(QRect(600, 280, 51, 61))
        self.r3c2 = QLabel(self.Windows)
        self.r3c2.setObjectName(u"r3c2")
        self.r3c2.setGeometry(QRect(420, 200, 51, 61))
        self.r4c4 = QLabel(self.Windows)
        self.r4c4.setObjectName(u"r4c4")
        self.r4c4.setGeometry(QRect(540, 280, 51, 61))
        self.r3c1 = QLabel(self.Windows)
        self.r3c1.setObjectName(u"r3c1")
        self.r3c1.setGeometry(QRect(360, 200, 51, 61))
        self.r3c5 = QLabel(self.Windows)
        self.r3c5.setObjectName(u"r3c5")
        self.r3c5.setGeometry(QRect(600, 200, 51, 61))
        self.r3c5.setStyleSheet(u"border: 1px solid black;")
        self.r4c3 = QLabel(self.Windows)
        self.r4c3.setObjectName(u"r4c3")
        self.r4c3.setGeometry(QRect(480, 280, 51, 61))
        self.r4c2 = QLabel(self.Windows)
        self.r4c2.setObjectName(u"r4c2")
        self.r4c2.setGeometry(QRect(420, 280, 51, 61))
        self.r6c1 = QLabel(self.Windows)
        self.r6c1.setObjectName(u"r6c1")
        self.r6c1.setGeometry(QRect(360, 440, 51, 61))
        self.r5c3 = QLabel(self.Windows)
        self.r5c3.setObjectName(u"r5c3")
        self.r5c3.setGeometry(QRect(480, 360, 51, 61))
        self.r5c4 = QLabel(self.Windows)
        self.r5c4.setObjectName(u"r5c4")
        self.r5c4.setGeometry(QRect(540, 360, 51, 61))
        self.r6c5 = QLabel(self.Windows)
        self.r6c5.setObjectName(u"r6c5")
        self.r6c5.setGeometry(QRect(600, 440, 51, 61))
        self.r5c2 = QLabel(self.Windows)
        self.r5c2.setObjectName(u"r5c2")
        self.r5c2.setGeometry(QRect(420, 360, 51, 61))
        self.r6c4 = QLabel(self.Windows)
        self.r6c4.setObjectName(u"r6c4")
        self.r6c4.setGeometry(QRect(540, 440, 51, 61))
        self.r5c1 = QLabel(self.Windows)
        self.r5c1.setObjectName(u"r5c1")
        self.r5c1.setGeometry(QRect(360, 360, 51, 61))
        self.r5c5 = QLabel(self.Windows)
        self.r5c5.setObjectName(u"r5c5")
        self.r5c5.setGeometry(QRect(600, 360, 51, 61))
        self.r5c5.setStyleSheet(u"border: 1px solid black;")
        self.r6c3 = QLabel(self.Windows)
        self.r6c3.setObjectName(u"r6c3")
        self.r6c3.setGeometry(QRect(480, 440, 51, 61))
        self.r6c2 = QLabel(self.Windows)
        self.r6c2.setObjectName(u"r6c2")
        self.r6c2.setGeometry(QRect(420, 440, 51, 61))
        self.Keyboard = QWidget(self.Combined)
        self.Keyboard.setObjectName(u"Keyboard")
        self.Keyboard.setGeometry(QRect(0, 600, 1017, 221))
        sizePolicy.setHeightForWidth(self.Keyboard.sizePolicy().hasHeightForWidth())
        self.Keyboard.setSizePolicy(sizePolicy)
        self.Backspace = QPushButton(self.Keyboard)
        self.all_buttons = QButtonGroup(MainWindow)
        self.all_buttons.setObjectName(u"all_buttons")
        self.all_buttons.addButton(self.Backspace)
        self.Backspace.setObjectName(u"Backspace")
        self.Backspace.setGeometry(QRect(730, 140, 91, 51))
        self.nn = QPushButton(self.Keyboard)
        self.all_buttons.addButton(self.nn)
        self.nn.setObjectName(u"nn")
        self.nn.setGeometry(QRect(610, 140, 61, 51))
        self.pp = QPushButton(self.Keyboard)
        self.all_buttons.addButton(self.pp)
        self.pp.setObjectName(u"pp")
        self.pp.setGeometry(QRect(760, 40, 61, 51))
        self.vv = QPushButton(self.Keyboard)
        self.all_buttons.addButton(self.vv)
        self.vv.setObjectName(u"vv")
        self.vv.setGeometry(QRect(490, 140, 61, 51))
        self.xx = QPushButton(self.Keyboard)
        self.all_buttons.addButton(self.xx)
        self.xx.setObjectName(u"xx")
        self.xx.setGeometry(QRect(370, 140, 61, 51))
        self.ff = QPushButton(self.Keyboard)
        self.all_buttons.addButton(self.ff)
        self.ff.setObjectName(u"ff")
        self.ff.setGeometry(QRect(430, 90, 61, 51))
        self.zz = QPushButton(self.Keyboard)
        self.all_buttons.addButton(self.zz)
        self.zz.setObjectName(u"zz")
        self.zz.setGeometry(QRect(310, 140, 61, 51))
        self.ee = QPushButton(self.Keyboard)
        self.all_buttons.addButton(self.ee)
        self.ee.setObjectName(u"ee")
        self.ee.setGeometry(QRect(340, 40, 61, 51))
        self.kk = QPushButton(self.Keyboard)
        self.all_buttons.addButton(self.kk)
        self.kk.setObjectName(u"kk")
        self.kk.setGeometry(QRect(670, 90, 61, 51))
        self.hh = QPushButton(self.Keyboard)
        self.all_buttons.addButton(self.hh)
        self.hh.setObjectName(u"hh")
        self.hh.setGeometry(QRect(550, 90, 61, 51))
        self.cc = QPushButton(self.Keyboard)
        self.all_buttons.addButton(self.cc)
        self.cc.setObjectName(u"cc")
        self.cc.setGeometry(QRect(430, 140, 61, 51))
        self.ss = QPushButton(self.Keyboard)
        self.all_buttons.addButton(self.ss)
        self.ss.setObjectName(u"ss")
        self.ss.setGeometry(QRect(310, 90, 61, 51))
        self.aa = QPushButton(self.Keyboard)
        self.all_buttons.addButton(self.aa)
        self.aa.setObjectName(u"aa")
        self.aa.setGeometry(QRect(250, 90, 61, 51))
        self.jj = QPushButton(self.Keyboard)
        self.all_buttons.addButton(self.jj)
        self.jj.setObjectName(u"jj")
        self.jj.setGeometry(QRect(610, 90, 61, 51))
        self.gg = QPushButton(self.Keyboard)
        self.all_buttons.addButton(self.gg)
        self.gg.setObjectName(u"gg")
        self.gg.setGeometry(QRect(490, 90, 61, 51))
        self.oo = QPushButton(self.Keyboard)
        self.all_buttons.addButton(self.oo)
        self.oo.setObjectName(u"oo")
        self.oo.setGeometry(QRect(700, 40, 61, 51))
        self.uu = QPushButton(self.Keyboard)
        self.all_buttons.addButton(self.uu)
        self.uu.setObjectName(u"uu")
        self.uu.setGeometry(QRect(580, 40, 61, 51))
        self.qq = QPushButton(self.Keyboard)
        self.all_buttons.addButton(self.qq)
        self.qq.setObjectName(u"qq")
        self.qq.setGeometry(QRect(220, 40, 61, 51))
        self.rr = QPushButton(self.Keyboard)
        self.all_buttons.addButton(self.rr)
        self.rr.setObjectName(u"rr")
        self.rr.setGeometry(QRect(400, 40, 61, 51))
        self.mm = QPushButton(self.Keyboard)
        self.all_buttons.addButton(self.mm)
        self.mm.setObjectName(u"mm")
        self.mm.setGeometry(QRect(670, 140, 61, 51))
        self.ll = QPushButton(self.Keyboard)
        self.all_buttons.addButton(self.ll)
        self.ll.setObjectName(u"ll")
        self.ll.setGeometry(QRect(730, 90, 61, 51))
        self.enter = QPushButton(self.Keyboard)
        self.all_buttons.addButton(self.enter)
        self.enter.setObjectName(u"enter")
        self.enter.setGeometry(QRect(220, 140, 91, 51))
        self.ii = QPushButton(self.Keyboard)
        self.all_buttons.addButton(self.ii)
        self.ii.setObjectName(u"ii")
        self.ii.setGeometry(QRect(640, 40, 61, 51))
        self.bb = QPushButton(self.Keyboard)
        self.all_buttons.addButton(self.bb)
        self.bb.setObjectName(u"bb")
        self.bb.setGeometry(QRect(550, 140, 61, 51))
        self.dd = QPushButton(self.Keyboard)
        self.all_buttons.addButton(self.dd)
        self.dd.setObjectName(u"dd")
        self.dd.setGeometry(QRect(370, 90, 61, 51))
        self.tt = QPushButton(self.Keyboard)
        self.all_buttons.addButton(self.tt)
        self.tt.setObjectName(u"tt")
        self.tt.setGeometry(QRect(460, 40, 61, 51))
        self.yy = QPushButton(self.Keyboard)
        self.all_buttons.addButton(self.yy)
        self.yy.setObjectName(u"yy")
        self.yy.setGeometry(QRect(520, 40, 61, 51))
        self.ww = QPushButton(self.Keyboard)
        self.all_buttons.addButton(self.ww)
        self.ww.setObjectName(u"ww")
        self.ww.setGeometry(QRect(280, 40, 61, 51))

        self.verticalLayout.addWidget(self.Combined)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1046, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Wordle", None))
        self.r1c1.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: 1px solid black;", None))
        self.r1c1.setText("")
        self.r1c2.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: 1px solid black;", None))
        self.r1c2.setText("")
        self.r1c3.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: 1px solid black;", None))
        self.r1c3.setText("")
        self.r1c5.setText("")
        self.r1c4.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: 1px solid black;", None))
        self.r1c4.setText("")
        self.r2c3.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: 1px solid black;", None))
        self.r2c3.setText("")
        self.r2c4.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: 1px solid black;", None))
        self.r2c4.setText("")
        self.r2c2.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: 1px solid black;", None))
        self.r2c2.setText("")
        self.r2c1.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: 1px solid black;", None))
        self.r2c1.setText("")
        self.r2c5.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: 1px solid black;", None))
        self.r2c5.setText("")
        self.r4c1.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: 1px solid black;", None))
        self.r4c1.setText("")
        self.r3c3.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: 1px solid black;", None))
        self.r3c3.setText("")
        self.r3c4.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: 1px solid black;", None))
        self.r3c4.setText("")
        self.r4c5.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: 1px solid black;", None))
        self.r4c5.setText("")
        self.r3c2.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: 1px solid black;", None))
        self.r3c2.setText("")
        self.r4c4.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: 1px solid black;", None))
        self.r4c4.setText("")
        self.r3c1.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: 1px solid black;", None))
        self.r3c1.setText("")
        self.r3c5.setText("")
        self.r4c3.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: 1px solid black;", None))
        self.r4c3.setText("")
        self.r4c2.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: 1px solid black;", None))
        self.r4c2.setText("")
        self.r6c1.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: 1px solid black;", None))
        self.r6c1.setText("")
        self.r5c3.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: 1px solid black;", None))
        self.r5c3.setText("")
        self.r5c4.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: 1px solid black;", None))
        self.r5c4.setText("")
        self.r6c5.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: 1px solid black;", None))
        self.r6c5.setText("")
        self.r5c2.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: 1px solid black;", None))
        self.r5c2.setText("")
        self.r6c4.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: 1px solid black;", None))
        self.r6c4.setText("")
        self.r5c1.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: 1px solid black;", None))
        self.r5c1.setText("")
        self.r5c5.setText("")
        self.r6c3.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: 1px solid black;", None))
        self.r6c3.setText("")
        self.r6c2.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: 1px solid black;", None))
        self.r6c2.setText("")
        self.Backspace.setText(QCoreApplication.translate("MainWindow", u"Backspace", None))
        self.nn.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.pp.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.vv.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.xx.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.ff.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.zz.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.ee.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.kk.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.hh.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.cc.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.ss.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.aa.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.jj.setText(QCoreApplication.translate("MainWindow", u"J", None))
        self.gg.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.oo.setText(QCoreApplication.translate("MainWindow", u"O", None))
        self.uu.setText(QCoreApplication.translate("MainWindow", u"U", None))
        self.qq.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.rr.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.mm.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.ll.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.enter.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.ii.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.bb.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.dd.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.tt.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.yy.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.ww.setText(QCoreApplication.translate("MainWindow", u"W", None))
    # retranslateUi


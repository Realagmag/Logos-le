# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'how_to_play.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_how_to_play(object):
    def setupUi(self, how_to_play):
        if not how_to_play.objectName():
            how_to_play.setObjectName(u"how_to_play")
        how_to_play.resize(534, 500)
        how_to_play.setMinimumSize(QSize(534, 500))
        how_to_play.setMaximumSize(QSize(534, 500))
        how_to_play.setWindowOpacity(0.950000000000000)
        how_to_play.setSizeGripEnabled(False)
        how_to_play.setModal(False)
        self.verticalLayout = QVBoxLayout(how_to_play)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(how_to_play)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(how_to_play)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(how_to_play)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_6)

        self.label_3 = QLabel(how_to_play)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(70, 16777215))
        font1 = QFont()
        font1.setPointSize(27)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background-color: green; color: white;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(how_to_play)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.label_4 = QLabel(how_to_play)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(70, 16777215))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"background-color: #FFAE20; color: white;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_8 = QLabel(how_to_play)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_8)

        self.label_5 = QLabel(how_to_play)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(70, 16777215))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background-color: grey; color: white;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.buttonBox = QDialogButtonBox(how_to_play)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setMaximumSize(QSize(200, 500))
        self.buttonBox.setLayoutDirection(Qt.RightToLeft)
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 7)
        self.verticalLayout.setStretch(2, 15)
        self.verticalLayout.setStretch(3, 1)

        self.retranslateUi(how_to_play)
        self.buttonBox.accepted.connect(how_to_play.accept)
        self.buttonBox.rejected.connect(how_to_play.reject)

        QMetaObject.connectSlotsByName(how_to_play)
    # setupUi

    def retranslateUi(self, how_to_play):
        how_to_play.setWindowTitle(QCoreApplication.translate("how_to_play", u"How to play", None))
        self.label.setText(QCoreApplication.translate("how_to_play", u"<html><head/><body><p>HOW TO PLAY:</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("how_to_play", u"<html><head/><body><p>Your goal is to guess the word in 6 tries!</p><p>You can enter your guess by typing it using your device's keyboard</p><p>or you can use keyboard diplayed on the bottom.<br/></p><p>Your guess must be a valid 5-letter word.</p><p>After each guess you will get a hint depending on how close your guess was!</p><p>If a letter in your guess:</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("how_to_play", u"Is in the word in correct spot:", None))
        self.label_3.setText(QCoreApplication.translate("how_to_play", u"A", None))
        self.label_7.setText(QCoreApplication.translate("how_to_play", u"Is in the word in different spot:", None))
        self.label_4.setText(QCoreApplication.translate("how_to_play", u"A", None))
        self.label_8.setText(QCoreApplication.translate("how_to_play", u"is not in the word:", None))
        self.label_5.setText(QCoreApplication.translate("how_to_play", u"A", None))
    # retranslateUi


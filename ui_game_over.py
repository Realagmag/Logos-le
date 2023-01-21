# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game_over.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_game_over(object):
    def setupUi(self, game_over):
        if not game_over.objectName():
            game_over.setObjectName(u"game_over")
        game_over.setMinimumSize(QSize(495, 500))
        game_over.setMaximumSize(QSize(495, 500))
        self.verticalLayout = QVBoxLayout(game_over)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(game_over)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.results = QLabel(game_over)
        self.results.setObjectName(u"results")
        font1 = QFont()
        font1.setPointSize(19)
        self.results.setFont(font1)
        self.results.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.results)

        self.link = QTextEdit(game_over)
        self.link.setObjectName(u"link")

        self.verticalLayout.addWidget(self.link)

        self.buttonBox = QDialogButtonBox(game_over)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)

        self.retranslateUi(game_over)
        self.buttonBox.accepted.connect(game_over.accept)
        self.buttonBox.rejected.connect(game_over.reject)

        QMetaObject.connectSlotsByName(game_over)
    # setupUi

    def retranslateUi(self, game_over):
        game_over.setWindowTitle(QCoreApplication.translate("game_over", u"Game Over", None))
        self.label.setText(QCoreApplication.translate("game_over", u"Game Over!", None))
        self.results.setText("")
    # retranslateUi


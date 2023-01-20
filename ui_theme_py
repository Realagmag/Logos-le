# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'theme.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_theme(object):
    def setupUi(self, theme):
        if not theme.objectName():
            theme.setObjectName(u"theme")
        theme.resize(500, 170)
        theme.setMinimumSize(QSize(500, 170))
        theme.setMaximumSize(QSize(500, 170))
        self.verticalLayout = QVBoxLayout(theme)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(theme)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.standard = QPushButton(theme)
        self.theme_buttons = QButtonGroup(theme)
        self.theme_buttons.setObjectName(u"theme_buttons")
        self.theme_buttons.addButton(self.standard)
        self.standard.setObjectName(u"standard")
        self.standard.setMinimumSize(QSize(130, 90))
        self.standard.setMaximumSize(QSize(150, 90))
        font = QFont()
        font.setPointSize(18)
        self.standard.setFont(font)
        self.standard.setStyleSheet(u"background-color: #D8EFC2; color: black; border: 2px solid black;")

        self.horizontalLayout.addWidget(self.standard)

        self.black = QPushButton(theme)
        self.theme_buttons.addButton(self.black)
        self.black.setObjectName(u"black")
        self.black.setMinimumSize(QSize(150, 90))
        self.black.setMaximumSize(QSize(150, 90))
        self.black.setFont(font)
        self.black.setStyleSheet(u"background-color: black; color: white; border: 2px solid black;")

        self.horizontalLayout.addWidget(self.black)

        self.white = QPushButton(theme)
        self.theme_buttons.addButton(self.white)
        self.white.setObjectName(u"white")
        self.white.setMaximumSize(QSize(150, 90))
        self.white.setFont(font)
        self.white.setStyleSheet(u"border: 2px solid black;")

        self.horizontalLayout.addWidget(self.white)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(theme)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(theme)
        self.buttonBox.accepted.connect(theme.accept)
        self.buttonBox.rejected.connect(theme.reject)

        QMetaObject.connectSlotsByName(theme)
    # setupUi

    def retranslateUi(self, theme):
        theme.setWindowTitle(QCoreApplication.translate("theme", u"Theme", None))
        self.label.setText(QCoreApplication.translate("theme", u"Choose theme:", None))
        self.standard.setText(QCoreApplication.translate("theme", u"Standard", None))
        self.black.setText(QCoreApplication.translate("theme", u"Black", None))
        self.white.setText(QCoreApplication.translate("theme", u"White", None))
    # retranslateUi


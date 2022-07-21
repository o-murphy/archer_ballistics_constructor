# -*- coding: utf-8 -*-

from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QDialog, QSizePolicy, QDialogButtonBox, QLabel
from PyQt5.QtCore import Qt, QRect, QMetaObject, QCoreApplication
from modules.lpc_check import check_lpc_driver, install_lpc_driver
from gui.stylesheet import load_qss


class LPC_dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.setStyleSheet(load_qss('qss\dialog.qss'))
        if not check_lpc_driver():
            if self.exec_():
                self.setup_driver()

    def setupUi(self):
        self.setObjectName("LPC_dialog")
        self.resize(300, 80)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addPixmap(QPixmap("gui\\../.rsrc/Icon.ico"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color: rgb(51, 51, 51);\n"
                                 "color: white;")
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setGeometry(QRect(0, 40, 300, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QLabel(self)
        self.label.setGeometry(QRect(0, 0, 300, 31))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")

        self.buttonBox.accepted.connect(self.accept)  # type: ignore
        self.buttonBox.rejected.connect(self.reject)  # type: ignore
        self.retranslateUi(self)
        QMetaObject.connectSlotsByName(self)

    def setup_driver(self):
        install_lpc_driver()

    def retranslateUi(self, dialog):
        _translate = QCoreApplication.translate
        dialog.setWindowTitle(_translate("LPC_dialog", "Form"))
        self.label.setText(_translate("LPC_dialog", "Do you want to install driver?"))

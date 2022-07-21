# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_bookmarksDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("openFromBookmarks")
        Dialog.resize(600, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui_templates\\../.rsrc/Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout()
        Dialog.setLayout(self.gridLayout)
        self.next = QtWidgets.QPushButton(Dialog)
        self.cancel = QtWidgets.QPushButton(Dialog)
        self.gridLayout.addWidget(self.next, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.cancel, 1, 0, 1, 1)
        self.mbox = QtWidgets.QMessageBox(Dialog)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Open from database"))
        self.next.setText(_translate("Dialog", 'Next'))
        self.cancel.setText(_translate("Dialog", 'Cancel'))
        if Dialog.page == 0:
            self.mbox.setText(_translate("Dialog", 'Rifle templates not found'))
        else:
            self.mbox.setText(_translate("Dialog", 'Cartridge templates not found'))

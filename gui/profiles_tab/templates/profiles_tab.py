# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_templates\profiles_tab.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_profilesTab(object):
    def setupUi(self, profilesTab):
        profilesTab.setObjectName("profilesTab")
        profilesTab.resize(463, 604)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(profilesTab.sizePolicy().hasHeightForWidth())
        profilesTab.setSizePolicy(sizePolicy)
        profilesTab.setMinimumSize(QtCore.QSize(0, 0))
        profilesTab.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(profilesTab)
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")

        self.retranslateUi(profilesTab)
        QtCore.QMetaObject.connectSlotsByName(profilesTab)

    def retranslateUi(self, profilesTab):
        _translate = QtCore.QCoreApplication.translate
        profilesTab.setWindowTitle(_translate("profilesTab", "Form"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_templates\catalog_selector.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_catalogSelector(object):
    def setupUi(self, catalogSelector):
        catalogSelector.setObjectName("catalogSelector")
        catalogSelector.resize(550, 475)
        catalogSelector.setMaximumSize(QtCore.QSize(800, 16777215))
        self.gridLayout = QtWidgets.QGridLayout(catalogSelector)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(catalogSelector)
        self.tabWidget.setMinimumSize(QtCore.QSize(550, 0))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.caliber = QtWidgets.QWidget()
        self.caliber.setObjectName("caliber")
        self.tabWidget.addTab(self.caliber, "")
        self.bullets = QtWidgets.QWidget()
        self.bullets.setObjectName("bullets")
        self.tabWidget.addTab(self.bullets, "")
        self.rifles = QtWidgets.QWidget()
        self.rifles.setObjectName("rifles")
        self.tabWidget.addTab(self.rifles, "")
        self.cartridges = QtWidgets.QWidget()
        self.cartridges.setObjectName("cartridges")
        self.tabWidget.addTab(self.cartridges, "")
        self.templates = QtWidgets.QWidget()
        self.templates.setObjectName("templates")
        self.tabWidget.addTab(self.templates, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(catalogSelector)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(catalogSelector)

    def retranslateUi(self, catalogSelector):
        _translate = QtCore.QCoreApplication.translate
        catalogSelector.setWindowTitle(_translate("catalogSelector", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.caliber), _translate("catalogSelector", "Caliber"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.bullets), _translate("catalogSelector", "Bullets"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rifles), _translate("catalogSelector", "Rifles"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cartridges), _translate("catalogSelector", "Cartridges"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.templates), _translate("catalogSelector", "Templates"))

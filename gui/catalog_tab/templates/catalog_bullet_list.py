# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_templates\catalog_bullet_list.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_catalogBulletList(object):
    def setupUi(self, catalogBulletList):
        catalogBulletList.setObjectName("catalogBulletList")
        catalogBulletList.resize(535, 229)
        self.gridLayout = QtWidgets.QGridLayout(catalogBulletList)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(catalogBulletList)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(50)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.retranslateUi(catalogBulletList)
        QtCore.QMetaObject.connectSlotsByName(catalogBulletList)

    def retranslateUi(self, catalogBulletList):
        _translate = QtCore.QCoreApplication.translate
        catalogBulletList.setWindowTitle(_translate("catalogBulletList", "Form"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("catalogBulletList", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("catalogBulletList", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("catalogBulletList", "Weight"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("catalogBulletList", "Lenght"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("catalogBulletList", "Diameter"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("catalogBulletList", "BC"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("catalogBulletList", "Copy"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("catalogBulletList", "Edit"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("catalogBulletList", "Delete"))

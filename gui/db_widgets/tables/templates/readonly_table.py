# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_templates\readonly_table.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_roTable(object):
    def setupUi(self, roTable):
        roTable.setObjectName("roTable")
        roTable.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(roTable)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.tableView = QtWidgets.QTableView(roTable)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)

        self.retranslateUi(roTable)
        QtCore.QMetaObject.connectSlotsByName(roTable)

    def retranslateUi(self, roTable):
        _translate = QtCore.QCoreApplication.translate
        roTable.setWindowTitle(_translate("roTable", "Form"))

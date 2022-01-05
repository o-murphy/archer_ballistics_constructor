# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_templates\profiles_table.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_profilesTable(object):
    def setupUi(self, profilesTable):
        profilesTable.setObjectName("profilesTable")
        profilesTable.resize(426, 118)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(profilesTable.sizePolicy().hasHeightForWidth())
        profilesTable.setSizePolicy(sizePolicy)
        profilesTable.setMinimumSize(QtCore.QSize(426, 1))
        profilesTable.setMaximumSize(QtCore.QSize(426, 16777215))
        profilesTable.setMouseTracking(True)
        profilesTable.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(profilesTable)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(profilesTable)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(426, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(426, 16777215))
        self.tableWidget.setStyleSheet("QTableView {\n"
"    border : 2px solid rgb(78, 78, 78);\n"
"}\n"
"\n"
"QTableWidget {\n"
"    border-color: rgb(76, 76, 76);\n"
"    background-color: rgb(51, 51, 51);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(51, 51, 51);\n"
"    width: 22px;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"\n"
"QTableView::item:hover {\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"\n"
"QTableView::item {\n"
"    background-color: rgb(55, 52, 63);\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"        background-color: rgb(51, 51, 51); /*#2A2929;*/\n"
"        width: 14px;\n"
"        margin: 15px 6px 15px 6px;\n"
"        border: 1px transparent #2A2929;\n"
"        border-radius: 6px;\n"
"    }\n"
"\n"
"QScrollBar:vertical:hover {\n"
"        background-color: rgb(51, 51, 51); /*#2A2929;*/\n"
"        width: 14px;\n"
"        margin: 15px 3px 15px 3px;\n"
"        border: 1px transparent #2A2929;\n"
"        border-radius: 6px;\n"
"    }\n"
"    QScrollBar::handle:vertical\n"
"    {\n"
"        background-color: rgb(78, 78, 78);         /* #605F5F; */\n"
"        min-height: 5px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:vertical\n"
"    {\n"
"        margin: 4px 0px 0px 0px;\n"
"        border: 1px solid rgb(51, 51, 51);\n"
"        border-top-left-radius: 5px;\n"
"        border-top-right-radius: 5px;\n"
"        background-color: rgb(51, 51, 51);\n"
"        color: white;\n"
"        height: 5px;\n"
"        width: 8px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical\n"
"    {\n"
"        margin: 0px 0px 4px 0px;\n"
"        border: 1px solid rgb(51, 51, 51);\n"
"        border-bottom-left-radius: 5px;\n"
"        border-bottom-right-radius: 5px;\n"
"        background-color: rgb(51, 51, 51);\n"
"        color: white;\n"
"        height: 5px;\n"
"        width: 8px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"\n"
"    QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"    {\n"
"        margin: 4px 0px 0px 0px;\n"
"           border: 1px solid rgb(51, 51, 51);\n"
"        border-top-left-radius: 5px;\n"
"        border-top-right-radius: 5px;\n"
"        background-color: rgb(78, 78, 78);\n"
"        height: 5px;\n"
"        width: 8px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"\n"
"\n"
"    QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"    {\n"
"        margin: 0px 0px 4px 0px;\n"
"        border: 1px solid rgb(51, 51, 51);\n"
"        border-bottom-left-radius: 5px;\n"
"        border-bottom-right-radius: 5px;\n"
"        background-color: rgb(78, 78, 78);\n"
"        height: 5px;\n"
"        width: 8px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"    {\n"
"                    background: none;\n"
"    }\n"
"\n"
"    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"    {\n"
"        background: none;\n"
"\n"
"    }\n"
"\n"
"\n"
"")
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(415)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(415)
        self.tableWidget.verticalHeader().setDefaultSectionSize(60)
        self.tableWidget.verticalHeader().setMinimumSectionSize(60)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.retranslateUi(profilesTable)
        QtCore.QMetaObject.connectSlotsByName(profilesTable)

    def retranslateUi(self, profilesTable):
        _translate = QtCore.QCoreApplication.translate
        profilesTable.setWindowTitle(_translate("profilesTable", "Form"))

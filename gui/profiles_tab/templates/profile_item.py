# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_templates\profile_item.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_profileItem(object):
    def setupUi(self, profileItem):
        profileItem.setObjectName("profileItem")
        profileItem.resize(405, 60)
        profileItem.setMinimumSize(QtCore.QSize(405, 60))
        profileItem.setMaximumSize(QtCore.QSize(405, 60))
        profileItem.setStyleSheet("QWidget {\n"
"    background-color: rgb(55, 52, 63);\n"
"    border: 1px solid rgb(78, 78, 78);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QLabel {\n"
"    border: 0;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QSpinBox::up-button, QDoubleSpinBox::up-button { width: 20px; }\n"
"QSpinBox::down-button, QDoubleSpinBox::down-button { width: 20px; }\n"
"QSpinBox, QDoubleSpinBox {\n"
"    background-color: rgb(40, 40, 40);\n"
"    alternate-background-color: rgb(40, 40, 40);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 0;\n"
"}\n"
"QLineEdit, QLabel, QComboBox, QPushButton, QToolButton {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit {\n"
"    border: 0px solid grey;\n"
"    background-color: rgb(40, 40, 40);\n"
"}\n"
"\n"
"\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(profileItem)
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_2 = QtWidgets.QWidget(profileItem)
        self.widget_2.setMinimumSize(QtCore.QSize(50, 50))
        self.widget_2.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(-1)
        self.widget_2.setFont(font)
        self.widget_2.setStyleSheet("QWidget {background-color: black;\n"
"color: black;\n"
"font-size: 16px;\n"
"font-family: \"Bahnschrift Light Condensed\";}\n"
"QLabel {\n"
"    background-color: white;\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.caliberShort_2 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.caliberShort_2.sizePolicy().hasHeightForWidth())
        self.caliberShort_2.setSizePolicy(sizePolicy)
        self.caliberShort_2.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(-1)
        self.caliberShort_2.setFont(font)
        self.caliberShort_2.setStyleSheet("")
        self.caliberShort_2.setAlignment(QtCore.Qt.AlignCenter)
        self.caliberShort_2.setObjectName("caliberShort_2")
        self.verticalLayout_2.addWidget(self.caliberShort_2)
        self.bulletWeight_2 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bulletWeight_2.sizePolicy().hasHeightForWidth())
        self.bulletWeight_2.setSizePolicy(sizePolicy)
        self.bulletWeight_2.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(-1)
        self.bulletWeight_2.setFont(font)
        self.bulletWeight_2.setStyleSheet("")
        self.bulletWeight_2.setAlignment(QtCore.Qt.AlignCenter)
        self.bulletWeight_2.setObjectName("bulletWeight_2")
        self.verticalLayout_2.addWidget(self.bulletWeight_2)
        self.gridLayout.addWidget(self.widget_2, 0, 0, 2, 1)
        self.rifleName = QtWidgets.QLabel(profileItem)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rifleName.sizePolicy().hasHeightForWidth())
        self.rifleName.setSizePolicy(sizePolicy)
        self.rifleName.setMinimumSize(QtCore.QSize(160, 0))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.rifleName.setFont(font)
        self.rifleName.setObjectName("rifleName")
        self.gridLayout.addWidget(self.rifleName, 0, 1, 1, 1)
        self.doubleSpinBox_x = QtWidgets.QDoubleSpinBox(profileItem)
        self.doubleSpinBox_x.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_x.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_x.setSizePolicy(sizePolicy)
        self.doubleSpinBox_x.setMaximumSize(QtCore.QSize(80, 16777215))
        self.doubleSpinBox_x.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.doubleSpinBox_x.setWrapping(False)
        self.doubleSpinBox_x.setFrame(True)
        self.doubleSpinBox_x.setReadOnly(False)
        self.doubleSpinBox_x.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.doubleSpinBox_x.setAccelerated(False)
        self.doubleSpinBox_x.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.doubleSpinBox_x.setKeyboardTracking(False)
        self.doubleSpinBox_x.setMinimum(-200.0)
        self.doubleSpinBox_x.setMaximum(200.0)
        self.doubleSpinBox_x.setSingleStep(0.25)
        self.doubleSpinBox_x.setObjectName("doubleSpinBox_x")
        self.gridLayout.addWidget(self.doubleSpinBox_x, 0, 2, 1, 1)
        self.spinBox_zeroing_distance = QtWidgets.QSpinBox(profileItem)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_zeroing_distance.sizePolicy().hasHeightForWidth())
        self.spinBox_zeroing_distance.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.spinBox_zeroing_distance.setFont(font)
        self.spinBox_zeroing_distance.setStyleSheet("")
        self.spinBox_zeroing_distance.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox_zeroing_distance.setPrefix("")
        self.spinBox_zeroing_distance.setMaximum(10000)
        self.spinBox_zeroing_distance.setSingleStep(10)
        self.spinBox_zeroing_distance.setProperty("value", 100)
        self.spinBox_zeroing_distance.setObjectName("spinBox_zeroing_distance")
        self.gridLayout.addWidget(self.spinBox_zeroing_distance, 0, 3, 2, 1)
        self.cartridgeName = QtWidgets.QLabel(profileItem)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cartridgeName.sizePolicy().hasHeightForWidth())
        self.cartridgeName.setSizePolicy(sizePolicy)
        self.cartridgeName.setMinimumSize(QtCore.QSize(160, 0))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.cartridgeName.setFont(font)
        self.cartridgeName.setObjectName("cartridgeName")
        self.gridLayout.addWidget(self.cartridgeName, 1, 1, 1, 1)
        self.doubleSpinBox_y = QtWidgets.QDoubleSpinBox(profileItem)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_y.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_y.setSizePolicy(sizePolicy)
        self.doubleSpinBox_y.setMaximumSize(QtCore.QSize(80, 16777215))
        self.doubleSpinBox_y.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.doubleSpinBox_y.setMinimum(-200.0)
        self.doubleSpinBox_y.setMaximum(200.0)
        self.doubleSpinBox_y.setSingleStep(0.25)
        self.doubleSpinBox_y.setObjectName("doubleSpinBox_y")
        self.gridLayout.addWidget(self.doubleSpinBox_y, 1, 2, 1, 1)

        self.retranslateUi(profileItem)
        QtCore.QMetaObject.connectSlotsByName(profileItem)

    def retranslateUi(self, profileItem):
        _translate = QtCore.QCoreApplication.translate
        profileItem.setWindowTitle(_translate("profileItem", "Form"))
        self.caliberShort_2.setText(_translate("profileItem", ".223Rem"))
        self.bulletWeight_2.setText(_translate("profileItem", "69"))
        self.rifleName.setText(_translate("profileItem", "223Rem 8TWIST"))
        self.doubleSpinBox_x.setPrefix(_translate("profileItem", "X: "))
        self.spinBox_zeroing_distance.setSuffix(_translate("profileItem", " m"))
        self.cartridgeName.setText(_translate("profileItem", "ABR 69GR SMK"))
        self.doubleSpinBox_y.setPrefix(_translate("profileItem", "Y: "))

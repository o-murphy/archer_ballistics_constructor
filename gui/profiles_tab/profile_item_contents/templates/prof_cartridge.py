# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_templates\prof_cartridge.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cartridge(object):
    def setupUi(self, cartridge):
        cartridge.setObjectName("cartridge")
        cartridge.resize(518, 155)
        self.gridLayout = QtWidgets.QGridLayout(cartridge)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.cartridgeGroupBox = QtWidgets.QGroupBox(cartridge)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cartridgeGroupBox.sizePolicy().hasHeightForWidth())
        self.cartridgeGroupBox.setSizePolicy(sizePolicy)
        self.cartridgeGroupBox.setMinimumSize(QtCore.QSize(500, 155))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cartridgeGroupBox.setFont(font)
        self.cartridgeGroupBox.setStyleSheet("")
        self.cartridgeGroupBox.setFlat(False)
        self.cartridgeGroupBox.setCheckable(False)
        self.cartridgeGroupBox.setObjectName("cartridgeGroupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.cartridgeGroupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_70 = QtWidgets.QLabel(self.cartridgeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_70.sizePolicy().hasHeightForWidth())
        self.label_70.setSizePolicy(sizePolicy)
        self.label_70.setMinimumSize(QtCore.QSize(0, 0))
        self.label_70.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_70.setFont(font)
        self.label_70.setObjectName("label_70")
        self.gridLayout_3.addWidget(self.label_70, 1, 0, 1, 1)
        self.temp = QtWidgets.QSpinBox(self.cartridgeGroupBox)
        self.temp.setMinimumSize(QtCore.QSize(80, 0))
        self.temp.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.temp.setFont(font)
        self.temp.setStyleSheet("")
        self.temp.setProperty("value", 15)
        self.temp.setObjectName("temp")
        self.gridLayout_3.addWidget(self.temp, 2, 1, 1, 1)
        self.cartridgeName = QtWidgets.QLineEdit(self.cartridgeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cartridgeName.sizePolicy().hasHeightForWidth())
        self.cartridgeName.setSizePolicy(sizePolicy)
        self.cartridgeName.setMinimumSize(QtCore.QSize(200, 0))
        self.cartridgeName.setMaximumSize(QtCore.QSize(150, 16777215))
        self.cartridgeName.setSizeIncrement(QtCore.QSize(0, 0))
        self.cartridgeName.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cartridgeName.setFont(font)
        self.cartridgeName.setStyleSheet("")
        self.cartridgeName.setText("")
        self.cartridgeName.setMaxLength(20)
        self.cartridgeName.setFrame(True)
        self.cartridgeName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.cartridgeName.setObjectName("cartridgeName")
        self.gridLayout_3.addWidget(self.cartridgeName, 0, 1, 1, 1)
        self.label_71 = QtWidgets.QLabel(self.cartridgeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_71.sizePolicy().hasHeightForWidth())
        self.label_71.setSizePolicy(sizePolicy)
        self.label_71.setMinimumSize(QtCore.QSize(0, 0))
        self.label_71.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_71.setFont(font)
        self.label_71.setObjectName("label_71")
        self.gridLayout_3.addWidget(self.label_71, 2, 0, 1, 1)
        self.ts = QtWidgets.QDoubleSpinBox(self.cartridgeGroupBox)
        self.ts.setMinimumSize(QtCore.QSize(80, 0))
        self.ts.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ts.setFont(font)
        self.ts.setDecimals(2)
        self.ts.setMaximum(100.0)
        self.ts.setSingleStep(0.01)
        self.ts.setProperty("value", 1.55)
        self.ts.setObjectName("ts")
        self.gridLayout_3.addWidget(self.ts, 3, 1, 1, 1)
        self.label_72 = QtWidgets.QLabel(self.cartridgeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_72.setFont(font)
        self.label_72.setObjectName("label_72")
        self.gridLayout_3.addWidget(self.label_72, 3, 0, 1, 1)
        self.label_69 = QtWidgets.QLabel(self.cartridgeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy)
        self.label_69.setMinimumSize(QtCore.QSize(0, 0))
        self.label_69.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_69.setFont(font)
        self.label_69.setObjectName("label_69")
        self.gridLayout_3.addWidget(self.label_69, 0, 0, 1, 1)
        self.horizontalWidget_16 = QtWidgets.QWidget(self.cartridgeGroupBox)
        self.horizontalWidget_16.setMaximumSize(QtCore.QSize(200, 16777215))
        self.horizontalWidget_16.setObjectName("horizontalWidget_16")
        self.horizontalLayout_50 = QtWidgets.QHBoxLayout(self.horizontalWidget_16)
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName("horizontalLayout_50")
        self.mv = QtWidgets.QSpinBox(self.horizontalWidget_16)
        self.mv.setMinimumSize(QtCore.QSize(80, 0))
        self.mv.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mv.setFont(font)
        self.mv.setStyleSheet("")
        self.mv.setMaximum(10000)
        self.mv.setProperty("value", 868)
        self.mv.setObjectName("mv")
        self.horizontalLayout_50.addWidget(self.mv)
        self.mvQuantity = QtWidgets.QComboBox(self.horizontalWidget_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mvQuantity.sizePolicy().hasHeightForWidth())
        self.mvQuantity.setSizePolicy(sizePolicy)
        self.mvQuantity.setMinimumSize(QtCore.QSize(75, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mvQuantity.setFont(font)
        self.mvQuantity.setStyleSheet("")
        self.mvQuantity.setObjectName("mvQuantity")
        self.mvQuantity.addItem("")
        self.mvQuantity.addItem("")
        self.horizontalLayout_50.addWidget(self.mvQuantity)
        self.mvSwitch = QtWidgets.QToolButton(self.horizontalWidget_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mvSwitch.sizePolicy().hasHeightForWidth())
        self.mvSwitch.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.mvSwitch.setFont(font)
        self.mvSwitch.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui_templates\\../.rsrc/res/drawable/secondarybtn21a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("ui_templates\\../.rsrc/res/drawable/secondarybtn21b.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.mvSwitch.setIcon(icon)
        self.mvSwitch.setIconSize(QtCore.QSize(16, 16))
        self.mvSwitch.setObjectName("mvSwitch")
        self.horizontalLayout_50.addWidget(self.mvSwitch)
        self.gridLayout_3.addWidget(self.horizontalWidget_16, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 2, 4, 1)
        self.gridLayout.addWidget(self.cartridgeGroupBox, 0, 0, 1, 1)

        self.retranslateUi(cartridge)
        QtCore.QMetaObject.connectSlotsByName(cartridge)

    def retranslateUi(self, cartridge):
        _translate = QtCore.QCoreApplication.translate
        cartridge.setWindowTitle(_translate("cartridge", "Form"))
        self.cartridgeGroupBox.setTitle(_translate("cartridge", "Cartridge"))
        self.label_70.setText(_translate("cartridge", "Muzzle Velocity:"))
        self.temp.setSuffix(_translate("cartridge", " °C"))
        self.label_71.setText(_translate("cartridge", "Temperature:"))
        self.ts.setSuffix(_translate("cartridge", " %"))
        self.label_72.setText(_translate("cartridge", "Temperature sensitivity:"))
        self.label_69.setText(_translate("cartridge", "Name:"))
        self.mvQuantity.setItemText(0, _translate("cartridge", "m/s"))
        self.mvQuantity.setItemText(1, _translate("cartridge", "fps"))
        self.mvSwitch.setToolTip(_translate("cartridge", "<font color=black>Convert</font>"))

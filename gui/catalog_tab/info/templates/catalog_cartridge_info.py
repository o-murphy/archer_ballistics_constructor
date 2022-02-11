# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_templates\catalog_cartridge_info.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_catalogCartridgeInfo(object):
    def setupUi(self, catalogCartridgeInfo):
        catalogCartridgeInfo.setObjectName("catalogCartridgeInfo")
        catalogCartridgeInfo.resize(687, 253)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(catalogCartridgeInfo.sizePolicy().hasHeightForWidth())
        catalogCartridgeInfo.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(catalogCartridgeInfo)
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.cartridgeGroupBox = QtWidgets.QGroupBox(catalogCartridgeInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cartridgeGroupBox.sizePolicy().hasHeightForWidth())
        self.cartridgeGroupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cartridgeGroupBox.setFont(font)
        self.cartridgeGroupBox.setStyleSheet("")
        self.cartridgeGroupBox.setFlat(False)
        self.cartridgeGroupBox.setCheckable(False)
        self.cartridgeGroupBox.setObjectName("cartridgeGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.cartridgeGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_74 = QtWidgets.QLabel(self.cartridgeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy)
        self.label_74.setObjectName("label_74")
        self.gridLayout_2.addWidget(self.label_74, 4, 0, 1, 1)
        self.label_73 = QtWidgets.QLabel(self.cartridgeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy)
        self.label_73.setObjectName("label_73")
        self.gridLayout_2.addWidget(self.label_73, 5, 0, 1, 1)
        self.ts = QtWidgets.QLabel(self.cartridgeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ts.sizePolicy().hasHeightForWidth())
        self.ts.setSizePolicy(sizePolicy)
        self.ts.setObjectName("ts")
        self.gridLayout_2.addWidget(self.ts, 3, 1, 1, 1)
        self.cartridgeName = QtWidgets.QLabel(self.cartridgeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cartridgeName.sizePolicy().hasHeightForWidth())
        self.cartridgeName.setSizePolicy(sizePolicy)
        self.cartridgeName.setObjectName("cartridgeName")
        self.gridLayout_2.addWidget(self.cartridgeName, 0, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.mv = QtWidgets.QLabel(self.cartridgeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mv.sizePolicy().hasHeightForWidth())
        self.mv.setSizePolicy(sizePolicy)
        self.mv.setObjectName("mv")
        self.gridLayout_2.addWidget(self.mv, 1, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.temp = QtWidgets.QLabel(self.cartridgeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.temp.sizePolicy().hasHeightForWidth())
        self.temp.setSizePolicy(sizePolicy)
        self.temp.setObjectName("temp")
        self.gridLayout_2.addWidget(self.temp, 2, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.label_72 = QtWidgets.QLabel(self.cartridgeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_72.sizePolicy().hasHeightForWidth())
        self.label_72.setSizePolicy(sizePolicy)
        self.label_72.setObjectName("label_72")
        self.gridLayout_2.addWidget(self.label_72, 3, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_70 = QtWidgets.QLabel(self.cartridgeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_70.sizePolicy().hasHeightForWidth())
        self.label_70.setSizePolicy(sizePolicy)
        self.label_70.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_70.setObjectName("label_70")
        self.gridLayout_2.addWidget(self.label_70, 1, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_71 = QtWidgets.QLabel(self.cartridgeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_71.sizePolicy().hasHeightForWidth())
        self.label_71.setSizePolicy(sizePolicy)
        self.label_71.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_71.setObjectName("label_71")
        self.gridLayout_2.addWidget(self.label_71, 2, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.bullet = QtWidgets.QLabel(self.cartridgeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bullet.sizePolicy().hasHeightForWidth())
        self.bullet.setSizePolicy(sizePolicy)
        self.bullet.setObjectName("bullet")
        self.gridLayout_2.addWidget(self.bullet, 5, 1, 1, 1)
        self.caliber = QtWidgets.QLabel(self.cartridgeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.caliber.sizePolicy().hasHeightForWidth())
        self.caliber.setSizePolicy(sizePolicy)
        self.caliber.setObjectName("caliber")
        self.gridLayout_2.addWidget(self.caliber, 4, 1, 1, 1)
        self.label_75 = QtWidgets.QLabel(self.cartridgeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy)
        self.label_75.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_75.setObjectName("label_75")
        self.gridLayout_2.addWidget(self.label_75, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 6, 0, 1, 1)
        self.gridLayout.addWidget(self.cartridgeGroupBox, 0, 0, 1, 1)

        self.retranslateUi(catalogCartridgeInfo)
        QtCore.QMetaObject.connectSlotsByName(catalogCartridgeInfo)

    def retranslateUi(self, catalogCartridgeInfo):
        _translate = QtCore.QCoreApplication.translate
        catalogCartridgeInfo.setWindowTitle(_translate("catalogCartridgeInfo", "Form"))
        self.cartridgeGroupBox.setTitle(_translate("catalogCartridgeInfo", "Cartridge"))
        self.label_74.setText(_translate("catalogCartridgeInfo", "Caliber:"))
        self.label_73.setText(_translate("catalogCartridgeInfo", "Bullet:"))
        self.ts.setText(_translate("catalogCartridgeInfo", "ts"))
        self.cartridgeName.setText(_translate("catalogCartridgeInfo", "Cartridge name"))
        self.mv.setText(_translate("catalogCartridgeInfo", "mv"))
        self.temp.setText(_translate("catalogCartridgeInfo", "t"))
        self.label_72.setText(_translate("catalogCartridgeInfo", "Temperature sensitivity:"))
        self.label_70.setText(_translate("catalogCartridgeInfo", "Muzzle Velocity:"))
        self.label_71.setText(_translate("catalogCartridgeInfo", "Temperature:"))
        self.bullet.setText(_translate("catalogCartridgeInfo", "bullet"))
        self.caliber.setText(_translate("catalogCartridgeInfo", "caliber"))
        self.label_75.setText(_translate("catalogCartridgeInfo", "Name:"))

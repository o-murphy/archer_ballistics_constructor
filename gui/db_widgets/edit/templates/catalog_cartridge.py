# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_templates\catalog_cartridge.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_catalogCartridge(object):
    def setupUi(self, catalogCartridge):
        catalogCartridge.setObjectName("catalogCartridge")
        catalogCartridge.resize(412, 209)
        catalogCartridge.setMinimumSize(QtCore.QSize(412, 209))
        catalogCartridge.setMaximumSize(QtCore.QSize(16777215, 209))
        self.gridLayout = QtWidgets.QGridLayout(catalogCartridge)
        self.gridLayout.setObjectName("gridLayout")
        self.label_73 = QtWidgets.QLabel(catalogCartridge)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy)
        self.label_73.setMinimumSize(QtCore.QSize(180, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_73.setFont(font)
        self.label_73.setObjectName("label_73")
        self.gridLayout.addWidget(self.label_73, 6, 0, 1, 1)
        self.label_75 = QtWidgets.QLabel(catalogCartridge)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy)
        self.label_75.setMinimumSize(QtCore.QSize(180, 0))
        self.label_75.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_75.setFont(font)
        self.label_75.setObjectName("label_75")
        self.gridLayout.addWidget(self.label_75, 0, 0, 1, 1)
        self.temp = QtWidgets.QSpinBox(catalogCartridge)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.temp.sizePolicy().hasHeightForWidth())
        self.temp.setSizePolicy(sizePolicy)
        self.temp.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.temp.setFont(font)
        self.temp.setStyleSheet("")
        self.temp.setProperty("value", 15)
        self.temp.setObjectName("temp")
        self.gridLayout.addWidget(self.temp, 2, 1, 1, 1)
        self.label_70 = QtWidgets.QLabel(catalogCartridge)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_70.sizePolicy().hasHeightForWidth())
        self.label_70.setSizePolicy(sizePolicy)
        self.label_70.setMinimumSize(QtCore.QSize(180, 0))
        self.label_70.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_70.setFont(font)
        self.label_70.setObjectName("label_70")
        self.gridLayout.addWidget(self.label_70, 1, 0, 1, 1)
        self.label_71 = QtWidgets.QLabel(catalogCartridge)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_71.sizePolicy().hasHeightForWidth())
        self.label_71.setSizePolicy(sizePolicy)
        self.label_71.setMinimumSize(QtCore.QSize(180, 0))
        self.label_71.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_71.setFont(font)
        self.label_71.setObjectName("label_71")
        self.gridLayout.addWidget(self.label_71, 2, 0, 1, 1)
        self.label_72 = QtWidgets.QLabel(catalogCartridge)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_72.sizePolicy().hasHeightForWidth())
        self.label_72.setSizePolicy(sizePolicy)
        self.label_72.setMinimumSize(QtCore.QSize(180, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_72.setFont(font)
        self.label_72.setObjectName("label_72")
        self.gridLayout.addWidget(self.label_72, 3, 0, 1, 1)
        self.label_74 = QtWidgets.QLabel(catalogCartridge)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy)
        self.label_74.setMinimumSize(QtCore.QSize(180, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_74.setFont(font)
        self.label_74.setObjectName("label_74")
        self.gridLayout.addWidget(self.label_74, 4, 0, 1, 1)
        self.ts = QtWidgets.QDoubleSpinBox(catalogCartridge)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ts.sizePolicy().hasHeightForWidth())
        self.ts.setSizePolicy(sizePolicy)
        self.ts.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ts.setFont(font)
        self.ts.setDecimals(2)
        self.ts.setMaximum(100.0)
        self.ts.setSingleStep(0.01)
        self.ts.setProperty("value", 1.55)
        self.ts.setObjectName("ts")
        self.gridLayout.addWidget(self.ts, 3, 1, 1, 1)
        self.caliber = QtWidgets.QComboBox(catalogCartridge)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.caliber.sizePolicy().hasHeightForWidth())
        self.caliber.setSizePolicy(sizePolicy)
        self.caliber.setObjectName("caliber")
        self.gridLayout.addWidget(self.caliber, 4, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(catalogCartridge)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 2, 1, 1)
        self.cartridgeName = QtWidgets.QLineEdit(catalogCartridge)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cartridgeName.sizePolicy().hasHeightForWidth())
        self.cartridgeName.setSizePolicy(sizePolicy)
        self.cartridgeName.setMinimumSize(QtCore.QSize(200, 0))
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
        self.gridLayout.addWidget(self.cartridgeName, 0, 1, 1, 2)
        self.line = QtWidgets.QFrame(catalogCartridge)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 5, 0, 1, 3)
        self.bullet = QtWidgets.QComboBox(catalogCartridge)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bullet.sizePolicy().hasHeightForWidth())
        self.bullet.setSizePolicy(sizePolicy)
        self.bullet.setObjectName("bullet")
        self.gridLayout.addWidget(self.bullet, 6, 1, 1, 2)
        self.mv = QtWidgets.QSpinBox(catalogCartridge)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mv.sizePolicy().hasHeightForWidth())
        self.mv.setSizePolicy(sizePolicy)
        self.mv.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mv.setFont(font)
        self.mv.setStyleSheet("")
        self.mv.setMaximum(10000)
        self.mv.setProperty("value", 0)
        self.mv.setObjectName("mv")
        self.gridLayout.addWidget(self.mv, 1, 1, 1, 1)

        self.retranslateUi(catalogCartridge)
        QtCore.QMetaObject.connectSlotsByName(catalogCartridge)

    def retranslateUi(self, catalogCartridge):
        _translate = QtCore.QCoreApplication.translate
        catalogCartridge.setWindowTitle(_translate("catalogCartridge", "Form"))
        self.label_73.setText(_translate("catalogCartridge", "Bullet:"))
        self.label_75.setText(_translate("catalogCartridge", "Name:"))
        self.temp.setSuffix(_translate("catalogCartridge", " °C"))
        self.label_70.setText(_translate("catalogCartridge", "Muzzle Velocity:"))
        self.label_71.setText(_translate("catalogCartridge", "Temperature:"))
        self.label_72.setText(_translate("catalogCartridge", "Temperature sensitivity:"))
        self.label_74.setText(_translate("catalogCartridge", "Caliber:"))
        self.ts.setSuffix(_translate("catalogCartridge", " %"))
        self.pushButton.setText(_translate("catalogCartridge", "Add"))
        self.cartridgeName.setPlaceholderText(_translate("catalogCartridge", "Cartridge name"))
import res_rc

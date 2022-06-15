# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_templates\prof_rifle.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_rifle(object):
    def setupUi(self, rifle):
        rifle.setObjectName("rifle")
        rifle.resize(500, 290)
        self.gridLayout = QtWidgets.QGridLayout(rifle)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.rifleGroupBox = QtWidgets.QGroupBox(rifle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rifleGroupBox.sizePolicy().hasHeightForWidth())
        self.rifleGroupBox.setSizePolicy(sizePolicy)
        self.rifleGroupBox.setMinimumSize(QtCore.QSize(500, 156))
        self.rifleGroupBox.setMaximumSize(QtCore.QSize(16777215, 156))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        font.setKerning(True)
        self.rifleGroupBox.setFont(font)
        self.rifleGroupBox.setStyleSheet("")
        self.rifleGroupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.rifleGroupBox.setObjectName("rifleGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.rifleGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.rifleName = QtWidgets.QLineEdit(self.rifleGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rifleName.sizePolicy().hasHeightForWidth())
        self.rifleName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rifleName.setFont(font)
        self.rifleName.setStyleSheet("")
        self.rifleName.setText("")
        self.rifleName.setMaxLength(20)
        self.rifleName.setFrame(True)
        self.rifleName.setObjectName("rifleName")
        self.gridLayout_2.addWidget(self.rifleName, 0, 1, 1, 1)
        self.label_67 = QtWidgets.QLabel(self.rifleGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_67.sizePolicy().hasHeightForWidth())
        self.label_67.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_67.setFont(font)
        self.label_67.setObjectName("label_67")
        self.gridLayout_2.addWidget(self.label_67, 2, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.rifleGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 0, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.rifleGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 1, 0, 1, 1)
        self.label_68 = QtWidgets.QLabel(self.rifleGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_68.sizePolicy().hasHeightForWidth())
        self.label_68.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_68.setFont(font)
        self.label_68.setObjectName("label_68")
        self.gridLayout_2.addWidget(self.label_68, 3, 0, 1, 1)
        self.sh = QtWidgets.QSpinBox(self.rifleGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sh.sizePolicy().hasHeightForWidth())
        self.sh.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sh.setFont(font)
        self.sh.setStyleSheet("")
        self.sh.setMaximum(200)
        self.sh.setProperty("value", 90)
        self.sh.setObjectName("sh")
        self.gridLayout_2.addWidget(self.sh, 2, 1, 1, 1)
        self.rightTwist = QtWidgets.QRadioButton(self.rifleGroupBox)
        self.rightTwist.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightTwist.sizePolicy().hasHeightForWidth())
        self.rightTwist.setSizePolicy(sizePolicy)
        self.rightTwist.setStyleSheet("")
        self.rightTwist.setChecked(True)
        self.rightTwist.setObjectName("rightTwist")
        self.gridLayout_2.addWidget(self.rightTwist, 3, 2, 1, 1)
        self.leftTwist = QtWidgets.QRadioButton(self.rifleGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftTwist.sizePolicy().hasHeightForWidth())
        self.leftTwist.setSizePolicy(sizePolicy)
        self.leftTwist.setStyleSheet("")
        self.leftTwist.setObjectName("leftTwist")
        self.gridLayout_2.addWidget(self.leftTwist, 3, 3, 1, 1)
        self.twist = QtWidgets.QSpinBox(self.rifleGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.twist.sizePolicy().hasHeightForWidth())
        self.twist.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.twist.setFont(font)
        self.twist.setStyleSheet("")
        self.twist.setSuffix("")
        self.twist.setMaximum(20)
        self.twist.setProperty("value", 10)
        self.twist.setObjectName("twist")
        self.gridLayout_2.addWidget(self.twist, 3, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.rifleGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 0, 2, 1, 1)
        self.caliberName = QtWidgets.QLineEdit(self.rifleGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.caliberName.sizePolicy().hasHeightForWidth())
        self.caliberName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.caliberName.setFont(font)
        self.caliberName.setStyleSheet("")
        self.caliberName.setText("")
        self.caliberName.setMaxLength(20)
        self.caliberName.setObjectName("caliberName")
        self.gridLayout_2.addWidget(self.caliberName, 1, 1, 1, 1)
        self.caliberShort = QtWidgets.QLineEdit(self.rifleGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.caliberShort.sizePolicy().hasHeightForWidth())
        self.caliberShort.setSizePolicy(sizePolicy)
        self.caliberShort.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.caliberShort.setFont(font)
        self.caliberShort.setStyleSheet("")
        self.caliberShort.setText("")
        self.caliberShort.setMaxLength(8)
        self.caliberShort.setObjectName("caliberShort")
        self.gridLayout_2.addWidget(self.caliberShort, 0, 3, 1, 1)
        self.autoTile = QtWidgets.QPushButton(self.rifleGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autoTile.sizePolicy().hasHeightForWidth())
        self.autoTile.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.autoTile.setFont(font)
        self.autoTile.setIconSize(QtCore.QSize(16, 16))
        self.autoTile.setObjectName("autoTile")
        self.gridLayout_2.addWidget(self.autoTile, 1, 3, 1, 1)
        self.gridLayout.addWidget(self.rifleGroupBox, 0, 0, 1, 1)

        self.retranslateUi(rifle)
        QtCore.QMetaObject.connectSlotsByName(rifle)

    def retranslateUi(self, rifle):
        _translate = QtCore.QCoreApplication.translate
        rifle.setWindowTitle(_translate("rifle", "Form"))
        self.rifleGroupBox.setTitle(_translate("rifle", "Rifle"))
        self.label_67.setText(_translate("rifle", "Sight height:"))
        self.label_22.setText(_translate("rifle", "Name:"))
        self.label_23.setText(_translate("rifle", "Caliber:"))
        self.label_68.setText(_translate("rifle", "Twist:"))
        self.sh.setSuffix(_translate("rifle", " mm"))
        self.rightTwist.setText(_translate("rifle", "Right"))
        self.leftTwist.setText(_translate("rifle", "Left"))
        self.label_24.setText(_translate("rifle", "Tile:"))
        self.autoTile.setToolTip(_translate("rifle", "<font color=black>Convert</font>"))
        self.autoTile.setText(_translate("rifle", "Auto"))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_templates\prof_bullet.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_bullet(object):
    def setupUi(self, bullet):
        bullet.setObjectName("bullet")
        bullet.resize(500, 217)
        self.gridLayout = QtWidgets.QGridLayout(bullet)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.bulletGroupBox = QtWidgets.QGroupBox(bullet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bulletGroupBox.sizePolicy().hasHeightForWidth())
        self.bulletGroupBox.setSizePolicy(sizePolicy)
        self.bulletGroupBox.setMinimumSize(QtCore.QSize(500, 217))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bulletGroupBox.setFont(font)
        self.bulletGroupBox.setStyleSheet("")
        self.bulletGroupBox.setObjectName("bulletGroupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.bulletGroupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.length = QtWidgets.QDoubleSpinBox(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.length.sizePolicy().hasHeightForWidth())
        self.length.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.length.setFont(font)
        self.length.setDecimals(1)
        self.length.setSingleStep(0.1)
        self.length.setProperty("value", 0.9)
        self.length.setObjectName("length")
        self.gridLayout_4.addWidget(self.length, 2, 1, 1, 1)
        self.lengthSwitch = QtWidgets.QToolButton(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lengthSwitch.sizePolicy().hasHeightForWidth())
        self.lengthSwitch.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.lengthSwitch.setFont(font)
        self.lengthSwitch.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui_templates\\../.rsrc/res/drawable/secondarybtn21a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("ui_templates\\../.rsrc/res/drawable/secondarybtn21b.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.lengthSwitch.setIcon(icon)
        self.lengthSwitch.setIconSize(QtCore.QSize(16, 16))
        self.lengthSwitch.setObjectName("lengthSwitch")
        self.gridLayout_4.addWidget(self.lengthSwitch, 2, 3, 1, 1)
        self.diameter = QtWidgets.QDoubleSpinBox(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diameter.sizePolicy().hasHeightForWidth())
        self.diameter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.diameter.setFont(font)
        self.diameter.setDecimals(3)
        self.diameter.setSingleStep(0.001)
        self.diameter.setProperty("value", 0.224)
        self.diameter.setObjectName("diameter")
        self.gridLayout_4.addWidget(self.diameter, 3, 1, 1, 1)
        self.diameterSwitch = QtWidgets.QToolButton(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diameterSwitch.sizePolicy().hasHeightForWidth())
        self.diameterSwitch.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.diameterSwitch.setFont(font)
        self.diameterSwitch.setText("")
        self.diameterSwitch.setIcon(icon)
        self.diameterSwitch.setIconSize(QtCore.QSize(16, 16))
        self.diameterSwitch.setObjectName("diameterSwitch")
        self.gridLayout_4.addWidget(self.diameterSwitch, 3, 3, 1, 1)
        self.lengthQuantity = QtWidgets.QComboBox(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lengthQuantity.sizePolicy().hasHeightForWidth())
        self.lengthQuantity.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lengthQuantity.setFont(font)
        self.lengthQuantity.setStyleSheet("")
        self.lengthQuantity.setObjectName("lengthQuantity")
        self.lengthQuantity.addItem("")
        self.lengthQuantity.addItem("")
        self.gridLayout_4.addWidget(self.lengthQuantity, 2, 2, 1, 1)
        self.bulletName = QtWidgets.QLineEdit(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bulletName.sizePolicy().hasHeightForWidth())
        self.bulletName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bulletName.setFont(font)
        self.bulletName.setStyleSheet("")
        self.bulletName.setText("")
        self.bulletName.setMaxLength(20)
        self.bulletName.setFrame(True)
        self.bulletName.setObjectName("bulletName")
        self.gridLayout_4.addWidget(self.bulletName, 0, 1, 1, 3)
        self.diameterQuantity = QtWidgets.QComboBox(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diameterQuantity.sizePolicy().hasHeightForWidth())
        self.diameterQuantity.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.diameterQuantity.setFont(font)
        self.diameterQuantity.setStyleSheet("")
        self.diameterQuantity.setObjectName("diameterQuantity")
        self.diameterQuantity.addItem("")
        self.diameterQuantity.addItem("")
        self.gridLayout_4.addWidget(self.diameterQuantity, 3, 2, 1, 1)
        self.dragFuncData = QtWidgets.QLineEdit(self.bulletGroupBox)
        self.dragFuncData.setEnabled(False)
        self.dragFuncData.setObjectName("dragFuncData")
        self.gridLayout_4.addWidget(self.dragFuncData, 5, 1, 1, 2)
        self.weight = QtWidgets.QDoubleSpinBox(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weight.sizePolicy().hasHeightForWidth())
        self.weight.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.weight.setFont(font)
        self.weight.setDecimals(2)
        self.weight.setMaximum(1000.0)
        self.weight.setSingleStep(0.01)
        self.weight.setProperty("value", 69.0)
        self.weight.setObjectName("weight")
        self.gridLayout_4.addWidget(self.weight, 1, 1, 1, 1)
        self.label_78 = QtWidgets.QLabel(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_78.setFont(font)
        self.label_78.setObjectName("label_78")
        self.gridLayout_4.addWidget(self.label_78, 5, 0, 1, 1)
        self.label_76 = QtWidgets.QLabel(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_76.sizePolicy().hasHeightForWidth())
        self.label_76.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_76.setFont(font)
        self.label_76.setObjectName("label_76")
        self.gridLayout_4.addWidget(self.label_76, 3, 0, 1, 1)
        self.weightQuantity = QtWidgets.QComboBox(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weightQuantity.sizePolicy().hasHeightForWidth())
        self.weightQuantity.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.weightQuantity.setFont(font)
        self.weightQuantity.setStyleSheet("")
        self.weightQuantity.setObjectName("weightQuantity")
        self.weightQuantity.addItem("")
        self.weightQuantity.addItem("")
        self.gridLayout_4.addWidget(self.weightQuantity, 1, 2, 1, 1)
        self.addDrag = QtWidgets.QToolButton(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addDrag.sizePolicy().hasHeightForWidth())
        self.addDrag.setSizePolicy(sizePolicy)
        self.addDrag.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.addDrag.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons19/res/drawable-xhdpi-v4/addbtn_menu21a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addDrag.setIcon(icon1)
        self.addDrag.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.addDrag.setObjectName("addDrag")
        self.gridLayout_4.addWidget(self.addDrag, 4, 4, 1, 1)
        self.label_73 = QtWidgets.QLabel(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_73.setFont(font)
        self.label_73.setObjectName("label_73")
        self.gridLayout_4.addWidget(self.label_73, 0, 0, 1, 1)
        self.label_75 = QtWidgets.QLabel(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_75.setFont(font)
        self.label_75.setObjectName("label_75")
        self.gridLayout_4.addWidget(self.label_75, 2, 0, 1, 1)
        self.label_74 = QtWidgets.QLabel(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_74.setFont(font)
        self.label_74.setObjectName("label_74")
        self.gridLayout_4.addWidget(self.label_74, 1, 0, 1, 1)
        self.label_77 = QtWidgets.QLabel(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_77.setFont(font)
        self.label_77.setObjectName("label_77")
        self.gridLayout_4.addWidget(self.label_77, 4, 0, 1, 1)
        self.dragType = QtWidgets.QComboBox(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dragType.sizePolicy().hasHeightForWidth())
        self.dragType.setSizePolicy(sizePolicy)
        self.dragType.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dragType.setFont(font)
        self.dragType.setStyleSheet("")
        self.dragType.setObjectName("dragType")
        self.gridLayout_4.addWidget(self.dragType, 4, 1, 1, 3)
        self.weightSwitch = QtWidgets.QToolButton(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weightSwitch.sizePolicy().hasHeightForWidth())
        self.weightSwitch.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.weightSwitch.setFont(font)
        self.weightSwitch.setText("")
        self.weightSwitch.setIcon(icon)
        self.weightSwitch.setIconSize(QtCore.QSize(16, 16))
        self.weightSwitch.setObjectName("weightSwitch")
        self.gridLayout_4.addWidget(self.weightSwitch, 1, 3, 1, 1)
        self.widget = QtWidgets.QWidget(self.bulletGroupBox)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.dragEditor = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dragEditor.sizePolicy().hasHeightForWidth())
        self.dragEditor.setSizePolicy(sizePolicy)
        self.dragEditor.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.dragEditor.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/res/drawable-hdpi-v4/settingsbtn_menu21a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/icons/res/drawable-hdpi-v4/settingsbtn_menu21b.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.dragEditor.setIcon(icon2)
        self.dragEditor.setObjectName("dragEditor")
        self.gridLayout_2.addWidget(self.dragEditor, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.widget, 5, 3, 1, 1)
        self.gridLayout.addWidget(self.bulletGroupBox, 0, 0, 1, 1)

        self.retranslateUi(bullet)
        self.dragType.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(bullet)

    def retranslateUi(self, bullet):
        _translate = QtCore.QCoreApplication.translate
        bullet.setWindowTitle(_translate("bullet", "Form"))
        self.bulletGroupBox.setTitle(_translate("bullet", "Bullet"))
        self.lengthSwitch.setToolTip(_translate("bullet", "<font color=black>Convert</font>"))
        self.diameterSwitch.setToolTip(_translate("bullet", "<font color=black>Convert</font>"))
        self.lengthQuantity.setItemText(0, _translate("bullet", "Inches"))
        self.lengthQuantity.setItemText(1, _translate("bullet", "mm"))
        self.diameterQuantity.setItemText(0, _translate("bullet", "Inches"))
        self.diameterQuantity.setItemText(1, _translate("bullet", "mm"))
        self.label_78.setText(_translate("bullet", "DF info:"))
        self.label_76.setText(_translate("bullet", "Diameter:"))
        self.weightQuantity.setItemText(0, _translate("bullet", "Grains"))
        self.weightQuantity.setItemText(1, _translate("bullet", "Grams"))
        self.addDrag.setToolTip(_translate("bullet", "<font color=black>Edit drag function</font>"))
        self.addDrag.setText(_translate("bullet", "Add"))
        self.label_73.setText(_translate("bullet", "Name:"))
        self.label_75.setText(_translate("bullet", "Length:"))
        self.label_74.setText(_translate("bullet", "Weight:"))
        self.label_77.setText(_translate("bullet", "Drag function:"))
        self.weightSwitch.setToolTip(_translate("bullet", "<font color=black>Convert</font>"))
        self.dragEditor.setToolTip(_translate("bullet", "<font color=black>Edit drag function</font>"))
        self.dragEditor.setText(_translate("bullet", "Edit"))
import res_rc

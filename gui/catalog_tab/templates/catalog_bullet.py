# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_templates\catalog_bullet.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_catalogBullet(object):
    def setupUi(self, catalogBullet):
        catalogBullet.setObjectName("catalogBullet")
        catalogBullet.resize(533, 219)
        catalogBullet.setMinimumSize(QtCore.QSize(533, 219))
        catalogBullet.setMaximumSize(QtCore.QSize(533, 219))
        self.gridLayout = QtWidgets.QGridLayout(catalogBullet)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.bulletGroupBox = QtWidgets.QGroupBox(catalogBullet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bulletGroupBox.sizePolicy().hasHeightForWidth())
        self.bulletGroupBox.setSizePolicy(sizePolicy)
        self.bulletGroupBox.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bulletGroupBox.setFont(font)
        self.bulletGroupBox.setStyleSheet("")
        self.bulletGroupBox.setObjectName("bulletGroupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.bulletGroupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalWidget_19 = QtWidgets.QWidget(self.bulletGroupBox)
        self.horizontalWidget_19.setMinimumSize(QtCore.QSize(220, 0))
        self.horizontalWidget_19.setMaximumSize(QtCore.QSize(200, 16777215))
        self.horizontalWidget_19.setObjectName("horizontalWidget_19")
        self.horizontalLayout_53 = QtWidgets.QHBoxLayout(self.horizontalWidget_19)
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName("horizontalLayout_53")
        self.diameter = QtWidgets.QDoubleSpinBox(self.horizontalWidget_19)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diameter.sizePolicy().hasHeightForWidth())
        self.diameter.setSizePolicy(sizePolicy)
        self.diameter.setMinimumSize(QtCore.QSize(80, 0))
        self.diameter.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.diameter.setFont(font)
        self.diameter.setDecimals(3)
        self.diameter.setSingleStep(0.001)
        self.diameter.setProperty("value", 0.224)
        self.diameter.setObjectName("diameter")
        self.horizontalLayout_53.addWidget(self.diameter)
        self.diameterQuantity = QtWidgets.QComboBox(self.horizontalWidget_19)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diameterQuantity.sizePolicy().hasHeightForWidth())
        self.diameterQuantity.setSizePolicy(sizePolicy)
        self.diameterQuantity.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.diameterQuantity.setFont(font)
        self.diameterQuantity.setStyleSheet("")
        self.diameterQuantity.setObjectName("diameterQuantity")
        self.diameterQuantity.addItem("")
        self.diameterQuantity.addItem("")
        self.horizontalLayout_53.addWidget(self.diameterQuantity)
        self.diameterSwitch = QtWidgets.QToolButton(self.horizontalWidget_19)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui_templates\\../.rsrc/res/drawable/secondarybtn21a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("ui_templates\\../.rsrc/res/drawable/secondarybtn21b.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.diameterSwitch.setIcon(icon)
        self.diameterSwitch.setIconSize(QtCore.QSize(16, 16))
        self.diameterSwitch.setObjectName("diameterSwitch")
        self.horizontalLayout_53.addWidget(self.diameterSwitch)
        self.gridLayout_4.addWidget(self.horizontalWidget_19, 3, 1, 1, 1)
        self.horizontalWidget_17 = QtWidgets.QWidget(self.bulletGroupBox)
        self.horizontalWidget_17.setMinimumSize(QtCore.QSize(220, 0))
        self.horizontalWidget_17.setMaximumSize(QtCore.QSize(200, 16777215))
        self.horizontalWidget_17.setObjectName("horizontalWidget_17")
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout(self.horizontalWidget_17)
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.weight = QtWidgets.QDoubleSpinBox(self.horizontalWidget_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weight.sizePolicy().hasHeightForWidth())
        self.weight.setSizePolicy(sizePolicy)
        self.weight.setMinimumSize(QtCore.QSize(80, 0))
        self.weight.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.weight.setFont(font)
        self.weight.setDecimals(2)
        self.weight.setMaximum(1000.0)
        self.weight.setSingleStep(0.01)
        self.weight.setProperty("value", 69.0)
        self.weight.setObjectName("weight")
        self.horizontalLayout_51.addWidget(self.weight)
        self.weightQuantity = QtWidgets.QComboBox(self.horizontalWidget_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weightQuantity.sizePolicy().hasHeightForWidth())
        self.weightQuantity.setSizePolicy(sizePolicy)
        self.weightQuantity.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.weightQuantity.setFont(font)
        self.weightQuantity.setStyleSheet("")
        self.weightQuantity.setObjectName("weightQuantity")
        self.weightQuantity.addItem("")
        self.weightQuantity.addItem("")
        self.horizontalLayout_51.addWidget(self.weightQuantity)
        self.weightSwitch = QtWidgets.QToolButton(self.horizontalWidget_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
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
        self.horizontalLayout_51.addWidget(self.weightSwitch)
        self.gridLayout_4.addWidget(self.horizontalWidget_17, 1, 1, 1, 1)
        self.horizontalWidget_20 = QtWidgets.QWidget(self.bulletGroupBox)
        self.horizontalWidget_20.setMinimumSize(QtCore.QSize(220, 0))
        self.horizontalWidget_20.setMaximumSize(QtCore.QSize(200, 16777215))
        self.horizontalWidget_20.setObjectName("horizontalWidget_20")
        self.horizontalLayout_54 = QtWidgets.QHBoxLayout(self.horizontalWidget_20)
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")
        self.dragType = QtWidgets.QComboBox(self.horizontalWidget_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dragType.sizePolicy().hasHeightForWidth())
        self.dragType.setSizePolicy(sizePolicy)
        self.dragType.setMinimumSize(QtCore.QSize(160, 0))
        self.dragType.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dragType.setFont(font)
        self.dragType.setStyleSheet("")
        self.dragType.setObjectName("dragType")
        self.dragType.addItem("")
        self.dragType.addItem("")
        self.dragType.addItem("")
        self.dragType.addItem("")
        self.dragType.addItem("")
        self.horizontalLayout_54.addWidget(self.dragType)
        self.dragEditor = QtWidgets.QToolButton(self.horizontalWidget_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dragEditor.sizePolicy().hasHeightForWidth())
        self.dragEditor.setSizePolicy(sizePolicy)
        self.dragEditor.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.dragEditor.setFont(font)
        self.dragEditor.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/res/drawable-hdpi-v4/settingsbtn_menu21a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/icons/res/drawable-hdpi-v4/settingsbtn_menu21b.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.dragEditor.setIcon(icon1)
        self.dragEditor.setObjectName("dragEditor")
        self.horizontalLayout_54.addWidget(self.dragEditor)
        self.gridLayout_4.addWidget(self.horizontalWidget_20, 4, 1, 1, 1)
        self.bcWidget = QtWidgets.QWidget(self.bulletGroupBox)
        self.bcWidget.setMinimumSize(QtCore.QSize(220, 0))
        self.bcWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.bcWidget.setObjectName("bcWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.bcWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_4.addWidget(self.bcWidget, 5, 1, 1, 1)
        self.horizontalWidget_18 = QtWidgets.QWidget(self.bulletGroupBox)
        self.horizontalWidget_18.setMinimumSize(QtCore.QSize(220, 0))
        self.horizontalWidget_18.setMaximumSize(QtCore.QSize(200, 16777215))
        self.horizontalWidget_18.setObjectName("horizontalWidget_18")
        self.horizontalLayout_52 = QtWidgets.QHBoxLayout(self.horizontalWidget_18)
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName("horizontalLayout_52")
        self.length = QtWidgets.QDoubleSpinBox(self.horizontalWidget_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.length.sizePolicy().hasHeightForWidth())
        self.length.setSizePolicy(sizePolicy)
        self.length.setMinimumSize(QtCore.QSize(80, 0))
        self.length.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.length.setFont(font)
        self.length.setDecimals(1)
        self.length.setSingleStep(0.1)
        self.length.setProperty("value", 0.9)
        self.length.setObjectName("length")
        self.horizontalLayout_52.addWidget(self.length)
        self.lengthQuantity = QtWidgets.QComboBox(self.horizontalWidget_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lengthQuantity.sizePolicy().hasHeightForWidth())
        self.lengthQuantity.setSizePolicy(sizePolicy)
        self.lengthQuantity.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lengthQuantity.setFont(font)
        self.lengthQuantity.setStyleSheet("")
        self.lengthQuantity.setObjectName("lengthQuantity")
        self.lengthQuantity.addItem("")
        self.lengthQuantity.addItem("")
        self.horizontalLayout_52.addWidget(self.lengthQuantity)
        self.lengthSwitch = QtWidgets.QToolButton(self.horizontalWidget_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
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
        self.lengthSwitch.setIcon(icon)
        self.lengthSwitch.setIconSize(QtCore.QSize(16, 16))
        self.lengthSwitch.setObjectName("lengthSwitch")
        self.horizontalLayout_52.addWidget(self.lengthSwitch)
        self.gridLayout_4.addWidget(self.horizontalWidget_18, 2, 1, 1, 1)
        self.label_77 = QtWidgets.QLabel(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy)
        self.label_77.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_77.setFont(font)
        self.label_77.setObjectName("label_77")
        self.gridLayout_4.addWidget(self.label_77, 4, 0, 1, 1)
        self.label_74 = QtWidgets.QLabel(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy)
        self.label_74.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_74.setFont(font)
        self.label_74.setObjectName("label_74")
        self.gridLayout_4.addWidget(self.label_74, 1, 0, 1, 1)
        self.label_75 = QtWidgets.QLabel(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy)
        self.label_75.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_75.setFont(font)
        self.label_75.setObjectName("label_75")
        self.gridLayout_4.addWidget(self.label_75, 2, 0, 1, 1)
        self.bulletName = QtWidgets.QLineEdit(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bulletName.sizePolicy().hasHeightForWidth())
        self.bulletName.setSizePolicy(sizePolicy)
        self.bulletName.setMinimumSize(QtCore.QSize(220, 0))
        self.bulletName.setMaximumSize(QtCore.QSize(170, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bulletName.setFont(font)
        self.bulletName.setStyleSheet("")
        self.bulletName.setText("")
        self.bulletName.setMaxLength(20)
        self.bulletName.setFrame(True)
        self.bulletName.setObjectName("bulletName")
        self.gridLayout_4.addWidget(self.bulletName, 0, 1, 1, 1)
        self.label_76 = QtWidgets.QLabel(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_76.sizePolicy().hasHeightForWidth())
        self.label_76.setSizePolicy(sizePolicy)
        self.label_76.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_76.setFont(font)
        self.label_76.setObjectName("label_76")
        self.gridLayout_4.addWidget(self.label_76, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 3, 6, 1)
        self.label_78 = QtWidgets.QLabel(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy)
        self.label_78.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_78.setFont(font)
        self.label_78.setObjectName("label_78")
        self.gridLayout_4.addWidget(self.label_78, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.bulletGroupBox, 0, 0, 1, 1)

        self.retranslateUi(catalogBullet)
        self.dragType.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(catalogBullet)

    def retranslateUi(self, catalogBullet):
        _translate = QtCore.QCoreApplication.translate
        catalogBullet.setWindowTitle(_translate("catalogBullet", "Form"))
        self.bulletGroupBox.setTitle(_translate("catalogBullet", "Bullet"))
        self.diameterQuantity.setItemText(0, _translate("catalogBullet", "Inches"))
        self.diameterQuantity.setItemText(1, _translate("catalogBullet", "mm"))
        self.diameterSwitch.setToolTip(_translate("catalogBullet", "<font color=black>Convert</font>"))
        self.weightQuantity.setItemText(0, _translate("catalogBullet", "Grains"))
        self.weightQuantity.setItemText(1, _translate("catalogBullet", "Grams"))
        self.weightSwitch.setToolTip(_translate("catalogBullet", "<font color=black>Convert</font>"))
        self.dragType.setItemText(0, _translate("catalogBullet", "G1"))
        self.dragType.setItemText(1, _translate("catalogBullet", "G7"))
        self.dragType.setItemText(2, _translate("catalogBullet", "Custom"))
        self.dragType.setItemText(3, _translate("catalogBullet", "G1 Multi BC"))
        self.dragType.setItemText(4, _translate("catalogBullet", "G7 Multi BC"))
        self.dragEditor.setToolTip(_translate("catalogBullet", "<font color=black>Edit drag function</font>"))
        self.lengthQuantity.setItemText(0, _translate("catalogBullet", "Inches"))
        self.lengthQuantity.setItemText(1, _translate("catalogBullet", "mm"))
        self.lengthSwitch.setToolTip(_translate("catalogBullet", "<font color=black>Convert</font>"))
        self.label_77.setText(_translate("catalogBullet", "Drag Function:"))
        self.label_74.setText(_translate("catalogBullet", "Weight:"))
        self.label_75.setText(_translate("catalogBullet", "Length:"))
        self.bulletName.setPlaceholderText(_translate("catalogBullet", "Bullet name"))
        self.label_76.setText(_translate("catalogBullet", "Diameter:"))
        self.label_78.setText(_translate("catalogBullet", "BC:"))
import res_rc

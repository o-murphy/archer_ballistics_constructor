# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_templates\drag_func_edit.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DragFuncEditDialog(object):
    def setupUi(self, DragFuncEditDialog):
        DragFuncEditDialog.setObjectName("DragFuncEditDialog")
        DragFuncEditDialog.setWindowModality(QtCore.Qt.NonModal)
        DragFuncEditDialog.resize(851, 559)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DragFuncEditDialog.sizePolicy().hasHeightForWidth())
        DragFuncEditDialog.setSizePolicy(sizePolicy)
        DragFuncEditDialog.setMinimumSize(QtCore.QSize(851, 559))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui_templates\\../.rsrc/Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DragFuncEditDialog.setWindowIcon(icon)
        DragFuncEditDialog.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(DragFuncEditDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_2 = QtWidgets.QWidget(DragFuncEditDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(6, 0, 6, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Up = QtWidgets.QPushButton(self.widget_2)
        self.Up.setMinimumSize(QtCore.QSize(0, 0))
        self.Up.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Up.setObjectName("Up")
        self.horizontalLayout_2.addWidget(self.Up)
        self.PeakUp = QtWidgets.QPushButton(self.widget_2)
        self.PeakUp.setMinimumSize(QtCore.QSize(0, 0))
        self.PeakUp.setMaximumSize(QtCore.QSize(100, 16777215))
        self.PeakUp.setObjectName("PeakUp")
        self.horizontalLayout_2.addWidget(self.PeakUp)
        self.EndUp = QtWidgets.QPushButton(self.widget_2)
        self.EndUp.setMinimumSize(QtCore.QSize(0, 0))
        self.EndUp.setMaximumSize(QtCore.QSize(100, 16777215))
        self.EndUp.setObjectName("EndUp")
        self.horizontalLayout_2.addWidget(self.EndUp)
        self.gridLayout.addWidget(self.widget_2, 3, 2, 1, 1)
        self.widget = QtWidgets.QWidget(DragFuncEditDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(6, 0, 6, 0)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioDrag = QtWidgets.QRadioButton(self.widget)
        self.radioDrag.setChecked(False)
        self.radioDrag.setObjectName("radioDrag")
        self.horizontalLayout.addWidget(self.radioDrag)
        self.radioDrop = QtWidgets.QRadioButton(self.widget)
        self.radioDrop.setChecked(True)
        self.radioDrop.setObjectName("radioDrop")
        self.horizontalLayout.addWidget(self.radioDrop)
        self.distanceQuantity = QtWidgets.QComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.distanceQuantity.sizePolicy().hasHeightForWidth())
        self.distanceQuantity.setSizePolicy(sizePolicy)
        self.distanceQuantity.setObjectName("distanceQuantity")
        self.distanceQuantity.addItem("")
        self.distanceQuantity.addItem("")
        self.distanceQuantity.addItem("")
        self.horizontalLayout.addWidget(self.distanceQuantity)
        self.holdOffQuantity = QtWidgets.QComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.holdOffQuantity.sizePolicy().hasHeightForWidth())
        self.holdOffQuantity.setSizePolicy(sizePolicy)
        self.holdOffQuantity.setObjectName("holdOffQuantity")
        self.holdOffQuantity.addItem("")
        self.holdOffQuantity.addItem("")
        self.holdOffQuantity.addItem("")
        self.horizontalLayout.addWidget(self.holdOffQuantity)
        self.gridLayout.addWidget(self.widget, 2, 1, 1, 2)
        self.widget_3 = QtWidgets.QWidget(DragFuncEditDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(6, 0, 6, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Down = QtWidgets.QPushButton(self.widget_3)
        self.Down.setMinimumSize(QtCore.QSize(0, 0))
        self.Down.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Down.setObjectName("Down")
        self.horizontalLayout_3.addWidget(self.Down)
        self.PeakDown = QtWidgets.QPushButton(self.widget_3)
        self.PeakDown.setMinimumSize(QtCore.QSize(0, 0))
        self.PeakDown.setMaximumSize(QtCore.QSize(100, 16777215))
        self.PeakDown.setObjectName("PeakDown")
        self.horizontalLayout_3.addWidget(self.PeakDown)
        self.EndDown = QtWidgets.QPushButton(self.widget_3)
        self.EndDown.setMinimumSize(QtCore.QSize(0, 0))
        self.EndDown.setMaximumSize(QtCore.QSize(100, 16777215))
        self.EndDown.setObjectName("EndDown")
        self.horizontalLayout_3.addWidget(self.EndDown)
        self.gridLayout.addWidget(self.widget_3, 3, 1, 1, 1)
        self.widget_4 = QtWidgets.QWidget(DragFuncEditDialog)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout.addWidget(self.widget_4, 1, 0, 1, 4)
        self.Step = QtWidgets.QSpinBox(DragFuncEditDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Step.sizePolicy().hasHeightForWidth())
        self.Step.setSizePolicy(sizePolicy)
        self.Step.setMinimumSize(QtCore.QSize(69, 0))
        self.Step.setMaximum(100)
        self.Step.setObjectName("Step")
        self.gridLayout.addWidget(self.Step, 3, 0, 1, 1)
        self.labelStep = QtWidgets.QLabel(DragFuncEditDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelStep.sizePolicy().hasHeightForWidth())
        self.labelStep.setSizePolicy(sizePolicy)
        self.labelStep.setMinimumSize(QtCore.QSize(69, 0))
        self.labelStep.setObjectName("labelStep")
        self.gridLayout.addWidget(self.labelStep, 2, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(DragFuncEditDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Reset)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 4)
        self.Calculate = QtWidgets.QPushButton(DragFuncEditDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Calculate.sizePolicy().hasHeightForWidth())
        self.Calculate.setSizePolicy(sizePolicy)
        self.Calculate.setObjectName("Calculate")
        self.gridLayout.addWidget(self.Calculate, 2, 3, 1, 1)
        self.SetConditions = QtWidgets.QPushButton(DragFuncEditDialog)
        self.SetConditions.setObjectName("SetConditions")
        self.gridLayout.addWidget(self.SetConditions, 3, 3, 1, 1)
        self.widget_5 = QtWidgets.QWidget(DragFuncEditDialog)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout.addWidget(self.widget_5, 0, 0, 1, 4)
        self.dragTableToolBox = QtWidgets.QWidget(DragFuncEditDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dragTableToolBox.sizePolicy().hasHeightForWidth())
        self.dragTableToolBox.setSizePolicy(sizePolicy)
        self.dragTableToolBox.setObjectName("dragTableToolBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.dragTableToolBox)
        self.horizontalLayout_4.setContentsMargins(6, 0, 6, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.copyTable = QtWidgets.QPushButton(self.dragTableToolBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.copyTable.sizePolicy().hasHeightForWidth())
        self.copyTable.setSizePolicy(sizePolicy)
        self.copyTable.setMinimumSize(QtCore.QSize(0, 0))
        self.copyTable.setMaximumSize(QtCore.QSize(100, 16777215))
        self.copyTable.setObjectName("copyTable")
        self.horizontalLayout_4.addWidget(self.copyTable)
        self.pasteTable = QtWidgets.QPushButton(self.dragTableToolBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pasteTable.sizePolicy().hasHeightForWidth())
        self.pasteTable.setSizePolicy(sizePolicy)
        self.pasteTable.setMinimumSize(QtCore.QSize(0, 0))
        self.pasteTable.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pasteTable.setObjectName("pasteTable")
        self.horizontalLayout_4.addWidget(self.pasteTable)
        self.gridLayout.addWidget(self.dragTableToolBox, 4, 3, 1, 1)

        self.retranslateUi(DragFuncEditDialog)
        QtCore.QMetaObject.connectSlotsByName(DragFuncEditDialog)

    def retranslateUi(self, DragFuncEditDialog):
        _translate = QtCore.QCoreApplication.translate
        DragFuncEditDialog.setWindowTitle(_translate("DragFuncEditDialog", "Drag function editor"))
        self.Up.setText(_translate("DragFuncEditDialog", "Up"))
        self.PeakUp.setText(_translate("DragFuncEditDialog", "Peak Up"))
        self.EndUp.setText(_translate("DragFuncEditDialog", "End Up"))
        self.radioDrag.setText(_translate("DragFuncEditDialog", "Drag"))
        self.radioDrop.setText(_translate("DragFuncEditDialog", "Drop"))
        self.distanceQuantity.setItemText(0, _translate("DragFuncEditDialog", "Mach"))
        self.distanceQuantity.setItemText(1, _translate("DragFuncEditDialog", "m/s"))
        self.distanceQuantity.setItemText(2, _translate("DragFuncEditDialog", "ft/s"))
        self.holdOffQuantity.setItemText(0, _translate("DragFuncEditDialog", "cm"))
        self.holdOffQuantity.setItemText(1, _translate("DragFuncEditDialog", "MIL"))
        self.holdOffQuantity.setItemText(2, _translate("DragFuncEditDialog", "MOA"))
        self.Down.setText(_translate("DragFuncEditDialog", "Down"))
        self.PeakDown.setText(_translate("DragFuncEditDialog", "Peak Down"))
        self.EndDown.setText(_translate("DragFuncEditDialog", "End Down"))
        self.Step.setSuffix(_translate("DragFuncEditDialog", " %"))
        self.labelStep.setText(_translate("DragFuncEditDialog", "Step"))
        self.Calculate.setText(_translate("DragFuncEditDialog", "Calculate"))
        self.SetConditions.setText(_translate("DragFuncEditDialog", "Set current conditions"))
        self.copyTable.setText(_translate("DragFuncEditDialog", "Copy Table"))
        self.pasteTable.setText(_translate("DragFuncEditDialog", "Paste Table"))

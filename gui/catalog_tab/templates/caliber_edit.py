# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_templates\caliber_edit.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_caliberEdit(object):
    def setupUi(self, caliberEdit):
        caliberEdit.setObjectName("caliberEdit")
        caliberEdit.resize(234, 112)
        self.gridLayout = QtWidgets.QGridLayout(caliberEdit)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(caliberEdit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(caliberEdit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.name = QtWidgets.QLineEdit(caliberEdit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 0, 1, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(caliberEdit)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(caliberEdit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.diameter = QtWidgets.QDoubleSpinBox(caliberEdit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diameter.sizePolicy().hasHeightForWidth())
        self.diameter.setSizePolicy(sizePolicy)
        self.diameter.setDecimals(3)
        self.diameter.setSingleStep(0.001)
        self.diameter.setObjectName("diameter")
        self.gridLayout.addWidget(self.diameter, 1, 1, 1, 1)

        self.retranslateUi(caliberEdit)
        self.buttonBox.accepted.connect(caliberEdit.accept) # type: ignore
        self.buttonBox.rejected.connect(caliberEdit.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(caliberEdit)

    def retranslateUi(self, caliberEdit):
        _translate = QtCore.QCoreApplication.translate
        caliberEdit.setWindowTitle(_translate("caliberEdit", "Caliber Edit"))
        self.label_2.setText(_translate("caliberEdit", "Diameter:"))
        self.label.setText(_translate("caliberEdit", "Name:"))
        self.label_3.setText(_translate("caliberEdit", "Inch"))

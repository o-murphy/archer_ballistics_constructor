# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_templates\new_custom_df.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_customDlg(object):
    def setupUi(self, customDlg):
        customDlg.setObjectName("customDlg")
        customDlg.resize(334, 134)
        self.gridLayout = QtWidgets.QGridLayout(customDlg)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(customDlg)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        self.file = QtWidgets.QPushButton(customDlg)
        self.file.setEnabled(False)
        self.file.setObjectName("file")
        self.gridLayout.addWidget(self.file, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(customDlg)
        self.label_2.setEnabled(False)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(customDlg)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(customDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 1)

        self.retranslateUi(customDlg)
        self.buttonBox.accepted.connect(customDlg.accept) # type: ignore
        self.buttonBox.rejected.connect(customDlg.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(customDlg)

    def retranslateUi(self, customDlg):
        _translate = QtCore.QCoreApplication.translate
        customDlg.setWindowTitle(_translate("customDlg", "Dialog"))
        self.comboBox.setItemText(0, _translate("customDlg", "G1"))
        self.comboBox.setItemText(1, _translate("customDlg", "G7"))
        self.comboBox.setItemText(2, _translate("customDlg", "G1 Multi-BC"))
        self.comboBox.setItemText(3, _translate("customDlg", "G7 Multi-BC"))
        self.comboBox.setItemText(4, _translate("customDlg", "Import by file"))
        self.file.setText(_translate("customDlg", "Import from file"))
        self.label_2.setText(_translate("customDlg", "TextLabel"))
        self.label.setText(_translate("customDlg", "What\'s drag function you\'ll use as reference?"))
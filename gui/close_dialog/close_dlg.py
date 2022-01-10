from PyQt5 import QtWidgets, QtCore
from ..stylesheet import load_qss


class CloseDialog(QtWidgets.QMessageBox):
    def __init__(self):
        super(CloseDialog, self).__init__()

        self.setStandardButtons(QtWidgets.QMessageBox.Save|QtWidgets.QMessageBox.Cancel|QtWidgets.QMessageBox.Close)
        self.setStyleSheet(load_qss('qss/dialog.qss'))
        self.retranslateUi(self)

    def retranslateUi(self, CloseDialog):
        _translate = QtCore.QCoreApplication.translate
        CloseDialog.setWindowTitle(_translate("CloseDialog", "File not saved!"))
        self.setText(_translate("CloseDialog", "File not saved.\nDo you want to save changes?"))

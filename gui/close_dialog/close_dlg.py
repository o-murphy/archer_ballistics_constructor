from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMessageBox

from ..stylesheet import load_qss


class CloseDialog(QMessageBox):
    def __init__(self):
        super(CloseDialog, self).__init__()

        self.setStandardButtons(QMessageBox.Save|QMessageBox.Cancel|QMessageBox.Close)
        self.setStyleSheet(load_qss('qss/dialog.qss'))
        self.retranslateUi(self)

    def retranslateUi(self, CloseDialog):
        _translate = QCoreApplication.translate
        CloseDialog.setWindowTitle(_translate("CloseDialog", "File not saved!"))
        self.setText(_translate("CloseDialog", "File not saved.\nDo you want to save changes?"))

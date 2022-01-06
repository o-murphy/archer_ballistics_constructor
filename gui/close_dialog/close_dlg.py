from PyQt5 import QtWidgets
from ..stylesheet import load_qss


class CloseDialog(QtWidgets.QMessageBox):
    def __init__(self):
        super(CloseDialog, self).__init__()
        self.setWindowTitle("File not saved!")
        self.setText('File not saved. Do you want to save changes?')
        self.addButton(QtWidgets.QMessageBox.Save)
        self.addButton(QtWidgets.QMessageBox.Cancel)
        self.addButton(QtWidgets.QMessageBox.Close)
        self.setStyleSheet(load_qss('qss/drag_func_editor.qss'))

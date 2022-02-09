from PyQt5 import QtWidgets, QtCore
from .templates import Ui_bcEdit


class BCEdit(QtWidgets.QDialog, Ui_bcEdit):
    def __init__(self):
        super(BCEdit, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def get(self):
        return self.doubleSpinBox.value()

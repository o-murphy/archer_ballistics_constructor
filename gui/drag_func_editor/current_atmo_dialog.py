from PyQt5 import QtCore, QtGui, QtWidgets
from .templates import Ui_CurrentAtmoDialog
from ..stylesheet import load_qss


class CurrentAtmoDialog(QtWidgets.QDialog, Ui_CurrentAtmoDialog):
    def __init__(self):
        super(CurrentAtmoDialog, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(load_qss('qss/dialog.qss'))

    def get_atmo(self):
        return {sb.objectName(): sb.value() for sb in self.findChildren(QtWidgets.QSpinBox)}

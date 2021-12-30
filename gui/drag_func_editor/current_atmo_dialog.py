from PyQt5 import QtCore, QtGui, QtWidgets
from .templates import Ui_CurrentAtmoDialog


class CurrentAtmoDialog(QtWidgets.QDialog, Ui_CurrentAtmoDialog):
    def __init__(self):
        super(CurrentAtmoDialog, self).__init__()
        self.setupUi(self)

    def get_atmo(self):
        return {sb.objectName(): sb.value() for sb in self.findChildren(QtWidgets.QSpinBox)}

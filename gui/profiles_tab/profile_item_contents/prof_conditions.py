from PyQt5 import QtWidgets
from .templates import Ui_conditions


class Conditions(QtWidgets.QWidget, Ui_conditions):
    def __init__(self, parent=None):
        super(Conditions, self).__init__(parent)
        self.setupUi(self)

    def get(self):
        conditions = self.findChildren(QtWidgets.QSpinBox)
        return {w.objectName(): w.value() for w in conditions}

from PyQt5 import QtWidgets, QtCore
from .templates import Ui_conditions


class Conditions(QtWidgets.QWidget, Ui_conditions):
    def __init__(self, parent=None):
        super(Conditions, self).__init__(parent)
        self.setupUi(self)

        self.groupBox.layout().setAlignment(QtCore.Qt.AlignLeft)

    def get(self):
        conditions = self.findChildren(QtWidgets.QSpinBox)
        return {w.objectName(): w.value() for w in conditions}

    def set(self, data):
        for k, v in data.items():
            if hasattr(self, k):
                w = self.__getattribute__(k)
                w.setValue(v)

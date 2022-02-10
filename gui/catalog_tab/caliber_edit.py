from PyQt5 import QtWidgets
from .templates import Ui_caliberEdit
from gui.stylesheet import load_qss


class CaliberEdit(QtWidgets.QDialog, Ui_caliberEdit):
    def __init__(self, name=None, diameter=None):
        super(CaliberEdit, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(load_qss('qss/dialog.qss'))

        self.n = name
        self.d = diameter
        if name and diameter:
            self.name.setText(self.n)
            self.diameter.setValue(self.d)

    def get(self):
        self.n = self.name.text()
        self.d = self.diameter.value()
        return self

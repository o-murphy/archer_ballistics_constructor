from PyQt5 import QtWidgets
from .templates import Ui_rifle


class Rifle(QtWidgets.QWidget, Ui_rifle):
    def __init__(self, parent=None):
        super(Rifle, self).__init__(parent)
        self.setupUi(self)

from PyQt5 import QtWidgets
from .templates import Ui_profileCurrent


class ProfileCurrent(QtWidgets.QWidget, Ui_profileCurrent):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

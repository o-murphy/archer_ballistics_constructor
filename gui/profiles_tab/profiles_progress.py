from PyQt5 import QtWidgets
from .templates import Ui_profilesProgress


class ProfilesProgress(QtWidgets.QWidget, Ui_profilesProgress):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

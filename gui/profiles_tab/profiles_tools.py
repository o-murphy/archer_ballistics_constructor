from PyQt5 import QtWidgets
from .templates import Ui_profilesTools


class ProfilesTools(QtWidgets.QWidget, Ui_profilesTools):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupConnects()

    def setupConnects(self):
        pass

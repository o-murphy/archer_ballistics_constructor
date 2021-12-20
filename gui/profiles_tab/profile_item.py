from PyQt5 import QtWidgets
from .templates import Ui_profileItem


class ProfileItem(QtWidgets.QWidget, Ui_profileItem):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.profile: dict = {}

    def set_profile(self, data: dict):
        for k, v in data.items():
            self.profile[k] = v

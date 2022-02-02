from PyQt5 import QtWidgets
from .templates import Ui_catalogRifleInfo


class CatalogRifleInfo(QtWidgets.QWidget, Ui_catalogRifleInfo):
    def __init__(self, name):
        super(CatalogRifleInfo, self).__init__()
        self.setupUi(self)
        self.rifleName.setText(name)

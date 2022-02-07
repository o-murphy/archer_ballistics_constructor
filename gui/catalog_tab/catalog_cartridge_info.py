from PyQt5 import QtWidgets
from .templates import Ui_catalogCartridgeInfo


class CatalogCartridgeInfo(QtWidgets.QWidget, Ui_catalogCartridgeInfo):
    def __init__(self, name):
        super(CatalogCartridgeInfo, self).__init__()
        self.setupUi(self)
        self.cartridgeName.setText(name)

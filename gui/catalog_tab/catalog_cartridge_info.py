from PyQt5 import QtWidgets
from .templates import Ui_catalogCartridgeInfo
from dbworker import db


class CatalogCartridgeInfo(QtWidgets.QWidget, Ui_catalogCartridgeInfo):
    def __init__(self, id):
        super(CatalogCartridgeInfo, self).__init__()
        self.setupUi(self)

        cartridge = db.get_cartridge(id)

        self.cartridgeName.setText(cartridge.name)
        self.mv.setText(str(cartridge.mv))
        self.temp.setText(str(cartridge.temp))
        self.ts.setText(str(cartridge.ts))

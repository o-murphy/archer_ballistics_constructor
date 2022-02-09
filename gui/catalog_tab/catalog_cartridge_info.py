from PyQt5 import QtWidgets
from .templates import Ui_catalogCartridgeInfo
from dbworker import db
from dbworker.models import *


class CatalogCartridgeInfo(QtWidgets.QWidget, Ui_catalogCartridgeInfo):
    def __init__(self, id):
        super(CatalogCartridgeInfo, self).__init__()
        self.setupUi(self)

        sess = db.SessMake()

        self.cartridge = sess.query(Cartridge).get(id)

        self.cartridgeName.setText(self.cartridge.name)
        self.mv.setText(str(self.cartridge.mv))
        self.temp.setText(str(self.cartridge.temp))
        self.ts.setText(str(self.cartridge.ts))
        self.bullet.setText(self.cartridge.bullet.name + ', ' + str(self.cartridge.bullet.weight) + ' gr')
        self.caliber.setText(
            self.cartridge.caliber.name + ', d:  ' + str(self.cartridge.caliber.diameter.diameter) + ' inch')

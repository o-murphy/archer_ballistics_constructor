from PyQt5 import QtWidgets
from .templates import Ui_catalogCartridgeInfo
from dbworker import db
from dbworker.models import *


class CatalogCartridgeInfo(QtWidgets.QWidget, Ui_catalogCartridgeInfo):
    def __init__(self):
        super(CatalogCartridgeInfo, self).__init__()
        self.setupUi(self)
        self.cartridge = None
        self.clear()

    def set(self, id):
        if id:
            sess = db.SessMake()
            self.cartridge = sess.query(Cartridge).get(id)
            if self.cartridge:
                self.cartridgeName.setText(self.cartridge.name)
                self.mv.setText(str(self.cartridge.mv) + ' m/s')
                self.temp.setText(str(self.cartridge.temp))
                self.ts.setText(str(self.cartridge.ts) + ' %')
                self.bullet.setText(self.cartridge.bullet.name + ', ' + str(self.cartridge.bullet.weight) + ' gr')
                self.caliber.setText(
                    self.cartridge.caliber.name + ', d:  ' + str(self.cartridge.caliber.diameter.diameter) + ' inch'
                )

    def clear(self):
        self.cartridge = None
        self.cartridgeName.setText('Empty')
        self.mv.setText('Empty')
        self.temp.setText('Empty')
        self.ts.setText('Empty')
        self.bullet.setText('Empty')
        self.caliber.setText('Empty')
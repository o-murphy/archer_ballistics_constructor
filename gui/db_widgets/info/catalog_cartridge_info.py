from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QWidget

from .templates import Ui_catalogCartridgeInfo
from dbworker import db
from dbworker.models import *


class CatalogCartridgeInfo(QWidget, Ui_catalogCartridgeInfo):
    def __init__(self):
        super(CatalogCartridgeInfo, self).__init__()
        self.setupUi(self)
        self.item = None
        self.clear()

    def set(self, id):
        if id:
            sess = db.SessMake()
            self.item = sess.query(Cartridge).get(id)
            if self.item:
                self.cartridgeName.setText(self.item.name)
                self.mv.setText(str(self.item.mv) + ' m/s')
                self.temp.setText(str(self.item.temp))
                self.ts.setText(str(self.item.ts) + ' %')
                self.bullet.setText(self.item.bullet.name + ', ' + str(self.item.bullet.weight) + ' gr')
                self.caliber.setText(
                    self.item.caliber.name + ', d:  ' + str(self.item.caliber.diameter.diameter) + ' inch'
                )

    def clear(self):

        _translate = QCoreApplication.translate
        empty = _translate('catalogCartridgeInfo', 'Empty')

        self.item = None
        self.cartridgeName.setText(empty)
        self.mv.setText(empty)
        self.temp.setText(empty)
        self.ts.setText(empty)
        self.bullet.setText(empty)
        self.caliber.setText(empty)

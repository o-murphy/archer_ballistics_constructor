from PyQt5 import QtWidgets
from .templates import Ui_catalogRifle
from dbworker import db
from dbworker.models import *


class CatalogRifle(QtWidgets.QWidget, Ui_catalogRifle):
    def __init__(self, data=None):
        super(CatalogRifle, self).__init__()
        self.setupUi(self)

        self.n = None
        self.c = None
        self.s = None
        self.t = None
        self.ir = None
        self.tl = None

        self.query_calibers()

        if data:
            self.data = data
            self.rifleName.setText(data.name)
            self.caliberName.setCurrentText(data.caliber.name)
            self.sh.setValue(data.sh)
            self.twist.setValue(data.twist)
            self.rightTwist.setChecked(data.is_right)
            self.caliberShort.setText(data.tile)

    def setConverter(self):
        self.weightQuantity.setItemData(0, self.convert.gr_to_g)
        self.weightQuantity.setItemData(1, self.convert.g_to_gr)
        self.lengthQuantity.setItemData(0, self.convert.inch_to_mm)
        self.lengthQuantity.setItemData(1, self.convert.mm_to_inch)
        self.diameterQuantity.setItemData(0, self.convert.inch_to_mm)
        self.diameterQuantity.setItemData(1, self.convert.mm_to_inch)

    def query_calibers(self):
        sess = db.SessMake()
        self.caliberName.addItems([c.name for c in sess.query(Caliber).all()])

    def get(self):
        self.n = self.rifleName.text()
        self.c = self.caliberName.currentText()
        self.s = self.sh.value()
        self.t = self.twist.value()
        self.ir = self.rightTwist.isChecked()
        self.tl = self.caliberShort.text()
        return self

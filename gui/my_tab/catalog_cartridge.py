from PyQt5 import QtWidgets, QtCore
from .templates import Ui_catalogCartridge
from modules import BConverter
from dbworker import db
from dbworker.models import *


class CatalogCartridge(QtWidgets.QWidget, Ui_catalogCartridge):
    def __init__(self, data: Cartridge = None):
        super(CatalogCartridge, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Cartridge edit')

        self.convert = BConverter()
        self.mvQuantity.setItemData(0, self.convert.mps2fps)
        self.mvQuantity.setItemData(1, self.convert.fps2mps)

        self._translate = QtCore.QCoreApplication.translate

        self.n = None
        self.v = None
        self.t = None
        self.tss = None
        self.b = None
        self.cb = None

        self.set_calibers()

        if data:
            self.cartridgeName.setText(data.name)
            self.mv.setValue(data.mv)
            self.temp.setValue(data.temp)
            self.ts.setValue(data.ts)
            self.caliber.setCurrentText(data.caliber.name + ', ' + f'{data.caliber.diameter.diameter:.3f}inch')
            self.set_bullets()
            self.bullet.setCurrentText(data.bullet.name)
        else:
            self.set_bullets()

        self.caliber.currentIndexChanged.connect(self.set_bullets)
        self.mvSwitch.clicked.connect(self.convert_muzzle_velocity)

    def set_bullets(self):
        sess = db.SessMake()
        caliber = sess.query(Caliber).get(self.caliber.currentData())
        d = sess.query(Diameter).get(caliber.diameter_id)

        bullets = sess.query(Bullet).filter_by(diameter_id=d.id).all()
        for i in range(self.bullet.count()):
            self.bullet.removeItem(i)
        for b in bullets:
            self.bullet.addItem(b.name + ', ' + str(b.weight) + 'gr', b.id)

    def set_calibers(self):
        sess = db.SessMake()
        calibers = sess.query(Caliber).all()
        for c in calibers:
            self.caliber.addItem(c.name + ', ' + f'{c.diameter.diameter:.3f}inch', c.id)

    @staticmethod
    def get_cln(spin: QtWidgets.QSpinBox, combo: QtWidgets.QComboBox):
        return spin.value() if combo.currentIndex() == 0 else combo.currentData()(spin.value())

    def convert_muzzle_velocity(self):
        cur_idx = self.mvQuantity.currentIndex()
        self.mv.setValue(self.mvQuantity.itemData(cur_idx)(self.mv.value()))
        self.mvQuantity.setCurrentIndex(1 if cur_idx == 0 else 0)

    def get(self):
        self.n = self.cartridgeName.text()
        self.v = self.mv.value()
        self.t = self.temp.value()
        self.tss = self.ts.value()
        self.b = self.bullet.currentData()
        self.cb = self.caliber.currentData()
        return self

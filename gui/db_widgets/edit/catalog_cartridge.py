from PyQt5 import QtWidgets, QtCore
from .templates import Ui_catalogCartridge
from modules import BConverter
from dbworker import db
from dbworker.models import *
from .caliber_edit import CaliberEdit



class CatalogCartridge(QtWidgets.QWidget, Ui_catalogCartridge):
    def __init__(self, data: Cartridge = None, call=None):
        super(CatalogCartridge, self).__init__()
        self.setupUi(self)

        self.title = 'Cartridge Edit'

        self.convert = BConverter()
        self.mvQuantity.setItemData(0, self.convert.mps2fps)
        self.mvQuantity.setItemData(1, self.convert.fps2mps)

        self.call = call
        self.data = data

        self.set_calibers()

        if self.data:
            self.cartridgeName.setText(self.data.name)
            self.mv.setValue(self.data.mv)
            self.temp.setValue(self.data.temp)
            self.ts.setValue(self.data.ts)
            self.caliber.setCurrentIndex(self.caliber.findData(self.data.caliber.id))
            self.set_bullets()
            self.bullet.setCurrentIndex(self.bullet.findData(self.data.bullet.id))
        else:
            self.set_bullets()

        self.caliber.currentIndexChanged.connect(self.set_bullets)
        self.mvSwitch.clicked.connect(self.convert_muzzle_velocity)
        self.pushButton.clicked.connect(self.add_caliber)

    def set_bullets(self):
        sess = db.SessMake()
        caliber = sess.query(Caliber).get(self.caliber.currentData())
        d = sess.query(Diameter).get(caliber.diameter_id)

        bullets = sess.query(Bullet).filter_by(diameter_id=d.id, attrs='rw').all()
        self.bullet.clear()
        for b in bullets:
            self.bullet.addItem(b.name + ', ' + str(b.weight) + 'gr', b.id)

    def set_calibers(self):
        self.bullet.clear()
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

        sess = db.SessMake()

        if self.call == 'edit':
            cart: Cartridge = sess.query(Cartridge).get(self.data.id)
            cart.name = self.cartridgeName.text()
            cart.mv = self.mv.value()
            cart.temp = self.temp.value()
            cart.ts = self.ts.value()
            cart.bullet_id = self.bullet.currentData()
            cart.caliber_id = self.caliber.currentData()

        else:
            sess.add(Cartridge(
                self.cartridgeName.text(),
                self.mv.value(),
                self.temp.value(),
                self.ts.value(),
                self.caliber.currentData(),
                self.bullet.currentData(),
                'rw'
            ))
        sess.commit()

    def valid(self):
        if self.mv.value() > 0:
            return True

    def invalid(self):
        msg = QtWidgets.QMessageBox(text="Muzzle velocity can't be 0")
        msg.setWindowTitle('Error!')
        msg.exec_()

    def add_caliber(self):
        ced = CaliberEdit()
        if ced.exec_():
            cal_id = ced.get()
        self.set_calibers()

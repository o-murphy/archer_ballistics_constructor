from PyQt5 import QtWidgets
from .templates import Ui_catalogCartridge
from modules import BConverter


class CatalogCartridge(QtWidgets.QWidget, Ui_catalogCartridge):
    def __init__(self, data: dict = None):
        super(CatalogCartridge, self).__init__()
        self.setupUi(self)
        self.convert = BConverter()
        self.mvQuantity.setItemData(0, self.convert.mps2fps)
        self.mvQuantity.setItemData(1, self.convert.fps2mps)

        if data:
            self.cartridgeName.setText(data['cartridgeName'])
            self.mv.setValue(data['mv'])
            self.temp.setValue(data['temp'])
            self.ts.setValue(data['ts'])

        self.mvSwitch.clicked.connect(self.convert_muzzle_velocity)

    @staticmethod
    def get_cln(spin: QtWidgets.QSpinBox, combo: QtWidgets.QComboBox):
        return spin.value() if combo.currentIndex() == 0 else combo.currentData()(spin.value())

    def convert_muzzle_velocity(self):
        cur_idx = self.mvQuantity.currentIndex()
        self.mv.setValue(self.mvQuantity.itemData(cur_idx)(self.mv.value()))
        self.mvQuantity.setCurrentIndex(1 if cur_idx == 0 else 0)

    def get_data(self):
        return {
            'cartridgeName': self.cartridgeName.text(),
            'mv': self.get_cln(self.mv, self.mvQuantity),
            'temp': self.mv.value(),
            'ts': self.mv.value(),
        }

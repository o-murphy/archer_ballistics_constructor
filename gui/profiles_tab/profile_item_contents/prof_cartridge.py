from PyQt5 import QtWidgets, QtCore
from .templates import Ui_cartridge
from modules import BConverter
from gui.delegates import MuzzleVelocity


class Cartridge(QtWidgets.QWidget, Ui_cartridge):
    def __init__(self, parent=None):
        super(Cartridge, self).__init__(parent)
        self.setupUi(self)
        self.cartridgeGroupBox.layout().setAlignment(QtCore.Qt.AlignLeft)

        self.convert = BConverter()
        self.setConverter()

        self.mv.editingFinished.connect(self.validate_mv)
        self.mvSwitch.clicked.connect(self.convert_muzzle_velocity)

    @staticmethod
    def get_cln(spin: QtWidgets.QSpinBox, combo: QtWidgets.QComboBox):
        return spin.value() if combo.currentIndex() == 0 else combo.currentData()(spin.value())

    def setConverter(self):
        self.mvQuantity.setItemData(0, self.convert.mps2fps)
        self.mvQuantity.setItemData(1, self.convert.fps2mps)

    def convert_muzzle_velocity(self):
        cur_idx = self.mvQuantity.currentIndex()
        self.mv.setValue(self.mvQuantity.itemData(cur_idx)(self.mv.value()))
        self.mvQuantity.setCurrentIndex(1 if cur_idx == 0 else 0)

    def validate_mv(self):
        if self.mv.value() == 0:
            self.mv.setFocus()

    def set(self, data):
        self.mv.setValue(data['mv'])
        self.cartridgeName.setText(data['cartridgeName'])
        self.temp.setValue(data['temp'])
        self.ts.setValue(data['ts'])

    def get(self):
        return {
            self.cartridgeName.objectName(): self.cartridgeName.text(),
            self.mv.objectName(): self.get_cln(self.mv, self.mvQuantity),
            self.temp.objectName(): self.temp.value(),
            self.ts.objectName(): self.ts.value(),
        }
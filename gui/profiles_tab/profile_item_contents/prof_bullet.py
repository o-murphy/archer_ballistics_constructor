from PyQt5 import QtWidgets
from .templates import Ui_bullet
from modules import BConverter


class Bullet(QtWidgets.QWidget, Ui_bullet):
    def __init__(self, parent=None):
        super(Bullet, self).__init__(parent)
        self.setupUi(self)
        self.convert = BConverter()

        self.setConverter()
        self.setupConnects()

    def setConverter(self):
        # self.mvQuantity.setItemData(0, self.convert.mps2fps)
        # self.mvQuantity.setItemData(1, self.convert.fps2mps)
        self.weightQuantity.setItemData(0, self.convert.gr_to_g)
        self.weightQuantity.setItemData(1, self.convert.g_to_gr)
        self.lengthQuantity.setItemData(0, self.convert.inch_to_mm)
        self.lengthQuantity.setItemData(1, self.convert.mm_to_inch)
        self.diameterQuantity.setItemData(0, self.convert.inch_to_mm)
        self.diameterQuantity.setItemData(1, self.convert.mm_to_inch)

    def setupConnects(self):
        self.weightSwitch.clicked.connect(self.convert_bullet_weight)
        self.lengthSwitch.clicked.connect(self.convert_bullet_length)
        self.diameterSwitch.clicked.connect(self.convert_bullet_diameter)

    def convert_bullet_weight(self):
        cur_idx = self.weightQuantity.currentIndex()
        self.weight.setValue(self.weightQuantity.itemData(cur_idx)(self.weight.value()))
        self.weight.setSingleStep(0.01 if cur_idx == 0 else 0.1)
        self.weightQuantity.setCurrentIndex(1 if cur_idx == 0 else 0)

    def convert_bullet_length(self):
        cur_idx = self.lengthQuantity.currentIndex()
        self.length.setValue(self.lengthQuantity.itemData(cur_idx)(self.length.value()))
        self.lengthQuantity.setCurrentIndex(1 if cur_idx == 0 else 0)

    def convert_bullet_diameter(self):
        cur_idx = self.diameterQuantity.currentIndex()
        self.diameter.setValue(self.diameterQuantity.itemData(cur_idx)(self.diameter.value()))
        self.diameterQuantity.setCurrentIndex(1 if cur_idx == 0 else 0)

    @staticmethod
    def get_cln(spin: QtWidgets.QSpinBox, combo: QtWidgets.QComboBox):
        return spin.value() if combo.currentIndex() == 0 else combo.currentData()(spin.value())

    def get(self):
        ret = {
            self.bulletName.objectName(): self.bulletName.text(),
            self.weight.objectName(): self.get_cln(self.weight, self.weightQuantity),
            self.length.objectName(): self.get_cln(self.length, self.lengthQuantity),
            self.diameter.objectName(): self.get_cln(self.diameter, self.diameterQuantity),
            self.dragType.objectName(): self.dragType.currentIndex(),
            "weightTile": str(int(round(self.weight.value(), 0))) + 'gr' if self.weightQuantity.currentIndex() == 0
            else str(round(self.weight.value(), 1)) + 'g',
            # self.multiBC.objectName(): self.multiBC.checkState(),

            # self.bc.objectName(): self.bc.value(),
            # self.bc_table.objectName(): self.bc_table.get_data()
        }
        return ret

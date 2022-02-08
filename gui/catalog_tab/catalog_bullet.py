from PyQt5 import QtWidgets
from .templates import Ui_catalogBullet
from modules import BConverter
# from gui.bc_table import BCTable
from ..single_custom_widgets.no_wheel_sb import BCSpinBox
from dbworker.models import Bullet


class BC(BCSpinBox):
    def __init__(self):
        super(BC, self).__init__()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.setSizePolicy(sizePolicy)
        self.setMaximumHeight(30)
        self.setStyleSheet("")
        self.setPrefix('BC: ')


class CatalogBullet(QtWidgets.QWidget, Ui_catalogBullet):
    """
    TODO:
        add multi_bc
        add drag_func_editor
    """
    def __init__(self, data: Bullet = None):
        super(CatalogBullet, self).__init__()
        self.setupUi(self)
        self.convert = BConverter()

        self.n = None
        self.w = None
        self.ln = None
        self.d = None
        self.w = None
        self.g1 = None
        self.g7 = None
        self.mbc1 = None
        self.mbc7 = None
        self.cdf = None

        self.weightQuantity.setItemData(0, self.convert.gr_to_g)
        self.weightQuantity.setItemData(1, self.convert.g_to_gr)
        self.lengthQuantity.setItemData(0, self.convert.inch_to_mm)
        self.lengthQuantity.setItemData(1, self.convert.mm_to_inch)
        self.diameterQuantity.setItemData(0, self.convert.inch_to_mm)
        self.diameterQuantity.setItemData(1, self.convert.mm_to_inch)

        self.weightSwitch.clicked.connect(lambda: self.convert_values(self.weight, self.weightQuantity))
        self.lengthSwitch.clicked.connect(lambda: self.convert_values(self.length, self.lengthQuantity))
        self.diameterSwitch.clicked.connect(lambda: self.convert_values(self.diameter, self.diameterQuantity))

        if data:
            self.bulletName.setText(data.name)
            self.weight.setValue(data.weight)
            self.length.setValue(data.length)
            self.diameter.setValue(data.diameter.diameter)
            self.bcG1.setValue(data.g1)
            self.bcG7.setValue(data.g7)

    @staticmethod
    def get_cln(spin: QtWidgets.QSpinBox, combo: QtWidgets.QComboBox):
        return spin.value() if combo.currentIndex() == 0 else combo.currentData()(spin.value())

    @staticmethod
    def convert_values(spin: QtWidgets.QSpinBox or QtWidgets.QDoubleSpinBox, combo: QtWidgets.QComboBox):
        cur_idx = combo.currentIndex()
        spin.setValue(combo.itemData(cur_idx)(spin.value()))
        combo.setCurrentIndex(1 if cur_idx == 0 else 0)
        if spin.objectName() == 'weight':
            spin.setSingleStep(0.01 if cur_idx == 0 else 0.1)

    def get(self):
        self.n = self.bulletName.text()
        self.w = self.get_cln(self.weight, self.weightQuantity)
        self.ln = self.get_cln(self.length, self.lengthQuantity)
        self.d = self.get_cln(self.diameter, self.diameterQuantity)
        self.w = self.get_cln(self.weight, self.weightQuantity)
        self.g1 = self.bcG1.value()
        self.g7 = self.bcG7.value()
        self.mbc1 = None  # self.mbcG1edit
        self.mbc7 = None  # self.mbcG7edit
        self.cdf = None  # self.cdf
        return self

from PyQt5 import QtWidgets
from .templates import Ui_profileCurrent
from modules import BConverter
from ..bc_table import BCTable


class ProfileCurrent(QtWidgets.QWidget, Ui_profileCurrent):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setupConnects()
        self.convert = BConverter()
        self.setConverter()
        self.bc_table = BCTable()
        self.bulletGroupBox.layout().addWidget(self.bc_table, 1, 2, 6, 1)
        self.enable_multi_bc(self.multiBC.isChecked())

    def setupConnects(self):
        self.mvSwitch.clicked.connect(self.convert_muzzle_velocity)
        self.weightSwitch.clicked.connect(self.convert_bullet_weight)
        self.lengthSwitch.clicked.connect(self.convert_bullet_length)
        self.diameterSwitch.clicked.connect(self.convert_bullet_diameter)

        # self.caliberShort.editingFinished.connect(
        #     lambda: self.caliberShort.setText(self.caliberShort.text().replace(' ', ''))
        # )

    def setConverter(self):
        self.mvQuantity.setItemData(0, self.convert.mps2fps)
        self.mvQuantity.setItemData(1, self.convert.fps2mps)
        self.weightQuantity.setItemData(0, self.convert.gr_to_g)
        self.weightQuantity.setItemData(1, self.convert.g_to_gr)
        self.lengthQuantity.setItemData(0, self.convert.inch_to_mm)
        self.lengthQuantity.setItemData(1, self.convert.mm_to_inch)
        self.diameterQuantity.setItemData(0, self.convert.inch_to_mm)
        self.diameterQuantity.setItemData(1, self.convert.mm_to_inch)

    def enable_multi_bc(self, is_true):
        self.bc_table.setEnabled(is_true)
        self.bc.setDisabled(is_true)

    def convert_muzzle_velocity(self):
        cur_idx = self.mvQuantity.currentIndex()
        self.mv.setValue(self.mvQuantity.itemData(cur_idx)(self.mv.value()))
        self.mvQuantity.setCurrentIndex(1 if cur_idx == 0 else 0)

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

    def get_conditions(self):
        conditions = self.tab_7.findChildren(QtWidgets.QSpinBox)
        return {w.objectName(): w.value() for w in conditions}

    @staticmethod
    def get_cln(spin: QtWidgets.QSpinBox, combo: QtWidgets.QComboBox):
        return spin.value() if combo.currentIndex() == 0 else combo.currentData()(spin.value())

    def get_bullet(self):
        ret = {
            self.bulletName.objectName(): self.bulletName.text(),
            self.weight.objectName(): self.get_cln(self.weight, self.weightQuantity),
            self.length.objectName(): self.get_cln(self.length, self.lengthQuantity),
            self.diameter.objectName(): self.get_cln(self.diameter, self.diameterQuantity),
            self.dragType.objectName(): self.dragType.currentIndex(),
            "weightTile": str(int(round(self.weight.value(), 0))) + 'gr' if self.weightQuantity.currentIndex() == 0
            else str(round(self.weight.value(), 1)) + 'g',
            self.multiBC.objectName(): self.multiBC.checkState(),

            self.bc.objectName(): self.bc.value(),
            self.bc_table.objectName(): self.bc_table.get_data()
        }
        return ret

    def get_cartridge(self):
        return {
            self.cartridgeName.objectName(): self.cartridgeName.text(),
            self.mv.objectName(): self.get_cln(self.mv, self.mvQuantity),
            self.temp.objectName(): self.temp.value(),
            self.ts.objectName(): self.ts.value(),
        }

    def get_rifle(self):
        return {
            self.rifleName.objectName(): self.rifleName.text(),
            self.caliberName.objectName(): self.caliberName.text(),
            self.sh.objectName(): self.sh.value(),
            self.twist.objectName(): self.twist.value(),
            self.caliberShort.objectName(): self.caliberShort.text(),
            self.rightTwist.objectName(): self.rightTwist.isChecked(),
        }

    @staticmethod
    def set_dirt(data, spin: QtWidgets.QSpinBox, combo: QtWidgets.QComboBox):
        spin.setValue(data[spin.objectName()]
                      if combo.currentIndex() == 0
                      else combo.currentData()(data[spin.objectName()]))

    def set_data(self, data: dict):
        tab_data = {self.__getattribute__(k): v for k, v in data.items() if hasattr(self, k)}.items()
        for k, v in tab_data:
            if isinstance(v, str):
                k.setText(v)
            if isinstance(k, (QtWidgets.QSpinBox, QtWidgets.QDoubleSpinBox)):
                if hasattr(self, f'{k.objectName()}Quantity'):
                    self.set_dirt(data, k, self.__getattribute__(f'{k.objectName()}Quantity'))
                k.setValue(v)
            if isinstance(k, QtWidgets.QComboBox):
                k.setCurrentIndex(v)
            if isinstance(k, QtWidgets.QCheckBox):
                k.setCheckState(v)

        self.rightTwist.click() if data['rightTwist'] else self.leftTwist.click()
        self.bc_table.set_data(data['bcTable'])

    def enable_tabs(self, e: bool):
        for tab in [self.tab_6, self.tab_7, self.tab_8]:
            for w in tab.children():
                w.setEnabled(e)

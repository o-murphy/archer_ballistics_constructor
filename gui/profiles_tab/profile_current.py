from PyQt5 import QtWidgets, QtCore
from .templates import Ui_profileCurrent
from modules.converter import BConverter
from ..drag_func_editor.bc_table import BCTable


class ProfileCurrent(QtWidgets.QWidget, Ui_profileCurrent):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupConnects()
        self.convert = BConverter()
        self.setConverter()
        self.tab_6.layout().setAlignment(QtCore.Qt.AlignTop)
        self.bc_table = BCTable()
        self.bulletGroupBox.layout().addWidget(self.bc_table, 0, 2, 6, 1)
        self.bc_table.set()

    def setupConnects(self):
        self.mvSwitch.clicked.connect(self.convert_muzzle_velocity)
        self.weightSwitch.clicked.connect(self.convert_bullet_weight)
        self.lengthSwitch.clicked.connect(self.convert_bullet_length)
        self.diameterSwitch.clicked.connect(self.convert_bullet_diameter)

        self.caliberShort.textEdited.connect(
            lambda: self.caliberShort.setText(self.caliberShort.text().replace(' ', ''))
        )

    def setConverter(self):
        self.mvQuantity.setItemData(0, self.convert.mps2fps)
        self.mvQuantity.setItemData(1, self.convert.fps2mps)
        self.weightQuantity.setItemData(0, self.convert.gr_to_g)
        self.weightQuantity.setItemData(1, self.convert.g_to_gr)
        self.lengthQuantity.setItemData(0, self.convert.inch_to_mm)
        self.lengthQuantity.setItemData(1, self.convert.mm_to_inch)
        self.diameterQuantity.setItemData(0, self.convert.inch_to_mm)
        self.diameterQuantity.setItemData(1, self.convert.mm_to_inch)

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
        return {
            self.bulletName.objectName(): self.bulletName.text(),
            self.weight.objectName(): self.get_cln(self.weight, self.weightQuantity),
            self.length.objectName(): self.get_cln(self.length, self.lengthQuantity),
            self.diameter.objectName(): self.get_cln(self.diameter, self.diameterQuantity),
            self.dragType.objectName(): self.dragType.currentIndex(),
            self.bc.objectName(): self.bc.value(),
            "weightTile": str(int(round(self.weight.value(), 0))) + 'gr' if self.weightQuantity.currentIndex() == 0
            else str(round(self.weight.value(), 1)) + 'g',
        }

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
        [k.setText(v) for k, v in tab_data if isinstance(v, str)]
        [k.setValue(v) for k, v in tab_data
         if isinstance(k, QtWidgets.QSpinBox) and not hasattr(self, f'{k.objectName()}Quantity')]
        [self.set_dirt(data, k, self.__getattribute__(f'{k.objectName()}Quantity')) for k, v in tab_data
         if isinstance(k, QtWidgets.QSpinBox) and hasattr(self, f'{k.objectName()}Quantity')]
        [k.setCurrentIndex(v) for k, v in tab_data if isinstance(k, QtWidgets.QComboBox)]

    def disable_tabs(self):
        for tab in [self.tab_6, self.tab_7, self.tab_8]:
            for w in tab.children():
                w.setEnabled(False)

    def enable_tabs(self):
        for tab in [self.tab_6, self.tab_7, self.tab_8]:
            for w in tab.children():
                w.setEnabled(True)


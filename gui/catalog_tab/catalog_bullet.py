from PyQt5 import QtWidgets
from .templates import Ui_catalogBullet
from modules import BConverter
from gui.bc_table import BCTable
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

        self.weightQuantity.setItemData(0, self.convert.gr_to_g)
        self.weightQuantity.setItemData(1, self.convert.g_to_gr)
        self.lengthQuantity.setItemData(0, self.convert.inch_to_mm)
        self.lengthQuantity.setItemData(1, self.convert.mm_to_inch)
        self.diameterQuantity.setItemData(0, self.convert.inch_to_mm)
        self.diameterQuantity.setItemData(1, self.convert.mm_to_inch)

        # self.dragType.currentIndexChanged.connect(self.set_drag_type)

        self.weightSwitch.clicked.connect(lambda: self.convert_values(self.weight, self.weightQuantity))
        self.lengthSwitch.clicked.connect(lambda: self.convert_values(self.length, self.lengthQuantity))
        self.diameterSwitch.clicked.connect(lambda: self.convert_values(self.diameter, self.diameterQuantity))

        self.bc_table = BCTable()
        self.bc = BC()

        # self.bulletGroupBox.layout().addWidget(self.bc, 5, 1, 1, 1)
        self.bulletGroupBox.layout().addWidget(self.bc_table, 0, 3, 6, 1)

        if data:
            self.bulletName.setText(data.name)
            self.weight.setValue(data.weight)
            self.length.setValue(data.length)
            self.diameter.setValue(data.diameter.diameter)
            self.dragType.setCurrentIndex(data.drag_type)
            self.bc.setValue(data.bc)
            # bc_table = [
            #     [data.v0, data.bc0],
            #     [data.v1, data.bc1],
            #     [data.v2, data.bc2],
            #     [data.v3, data.bc3],
            #     [data.v4, data.bc4],
            # ]
            # self.bc_table.set_data(bc_table)
            # self.df_data = data.dfdata if hasattr(data, 'dfdata') else None

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

    def set_drag_type(self, value):
        if value in [0, 1]:
            self.bc_table.setVisible(False)
            self.bc.setVisible(True)

        elif value in [3, 4]:
            self.bc_table.setVisible(True)
            self.bc.setVisible(False)
        else:
            self.bc_table.setVisible(False)
            self.bc.setVisible(False)

    def get_data(self):
        return {
            'bulletName': self.bulletName.text(),
            'weight': self.get_cln(self.weight, self.weightQuantity),
            'length': self.get_cln(self.length, self.lengthQuantity),
            'diameter': self.get_cln(self.diameter, self.diameterQuantity),
            'dragType': self.dragType.currentIndex(),
            'bc': self.bc.value(),
            'bcTable': self.bc_table.get_data(),
            'df_data': self.df_data
        }
from PyQt5 import QtWidgets
from .templates import Ui_profileCurrent
from ..drag_func_editor import DragFuncEditDialog
from modules.converter import BConverter


class ProfileCurrent(QtWidgets.QWidget, Ui_profileCurrent):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupConnects()
        self.convert = BConverter()
        self.setConverter()

    def setupConnects(self):
        self.mvToolButton.clicked.connect(self.convert_muzzle_velocity)
        self.weightToolButton.clicked.connect(self.convert_bullet_weight)
        self.lengthToolButton.clicked.connect(self.convert_bullet_length)
        self.diameterToolButton.clicked.connect(self.convert_bullet_diameter)
        self.dragToolButton.clicked.connect(self.drag_func_edit)

    def setConverter(self):
        self.mvComboBox.setItemData(0, self.convert.mps2fps)
        self.mvComboBox.setItemData(1, self.convert.fps2mps)
        self.weightComboBox.setItemData(0, self.convert.gr_to_g)
        self.weightComboBox.setItemData(1, self.convert.g_to_gr)
        self.lengthComboBox.setItemData(0, self.convert.inch_to_mm)
        self.lengthComboBox.setItemData(1, self.convert.mm_to_inch)
        self.diameterComboBox.setItemData(0, self.convert.inch_to_mm)
        self.diameterComboBox.setItemData(1, self.convert.mm_to_inch)

    def drag_func_edit(self):
        drag_func_dlg = DragFuncEditDialog()
        new_drag_func = drag_func_dlg.current_data if drag_func_dlg.exec_() else drag_func_dlg.default_data

    def convert_muzzle_velocity(self):
        cur_idx = self.mvComboBox.currentIndex()
        self.mvSpinBox.setValue(self.mvComboBox.itemData(cur_idx)(self.mvSpinBox.value()))
        self.mvComboBox.setCurrentIndex(1 if cur_idx == 0 else 0)

    def convert_bullet_weight(self):
        cur_idx = self.weightComboBox.currentIndex()
        self.bulletWeight.setValue(self.weightComboBox.itemData(cur_idx)(self.bulletWeight.value()))
        self.bulletWeight.setSingleStep(0.01 if cur_idx == 0 else 0.1)
        self.weightComboBox.setCurrentIndex(1 if cur_idx == 0 else 0)

    def convert_bullet_length(self):
        cur_idx = self.lengthComboBox.currentIndex()
        self.lengthDoubleSpinBox.setValue(self.lengthComboBox.itemData(cur_idx)(self.lengthDoubleSpinBox.value()))
        self.lengthComboBox.setCurrentIndex(1 if cur_idx == 0 else 0)

    def convert_bullet_diameter(self):
        cur_idx = self.diameterComboBox.currentIndex()
        self.diameterDoubleSpinBox.setValue(self.diameterComboBox.itemData(cur_idx)(self.diameterDoubleSpinBox.value()))
        self.diameterComboBox.setCurrentIndex(1 if cur_idx == 0 else 0)

    def get_conditions(self):
        return {
            self.z_temp.objectName(): self.z_temp.value(),
            self.z_angle.objectName(): self.z_angle.value(),
            self.z_pressure.objectName(): self.z_pressure.value(),
            self.z_latitude.objectName(): self.z_latitude.value(),
            self.z_humidity.objectName(): self.z_humidity.value(),
            self.z_azimuth.objectName(): self.z_azimuth.value(),
            self.z_powder_temp.objectName(): self.z_powder_temp.value(),
        }

    def get_bullet(self):
        return {
            self.bulletName.objectName(): self.bulletName.text(),

            self.bulletWeight.objectName():
                self.bulletWeight.value() if self.weightComboBox.currentIndex() == 0
                else self.weightComboBox.currentData()(self.bulletWeight.value()),

            self.lengthDoubleSpinBox.objectName():
                self.lengthDoubleSpinBox.value() if self.lengthComboBox.currentIndex() == 0
                else self.lengthComboBox.currentData()(self.lengthDoubleSpinBox.value()),

            self.diameterDoubleSpinBox.objectName():
                self.diameterDoubleSpinBox.value() if self.diameterComboBox.currentIndex() == 0
                else self.diameterComboBox.currentData(self.diameterDoubleSpinBox.value()),

            self.dragComboBox.objectName(): self.dragComboBox.currentIndex(),
            self.bcDoubleSpinBox.objectName(): self.bcDoubleSpinBox.value(),
        }

    def get_cartridge(self):
        return {
            self.cartridgeName.objectName(): self.cartridgeName.text(),
            self.mvSpinBox.objectName():
                self.mvSpinBox.value() if self.mvComboBox.currentIndex() == 0
                else self.mvComboBox.currentData()(self.mvSpinBox.value()),

            self.temperatureSpinBox.objectName(): self.temperatureSpinBox.value(),
            self.tsDoubleSpinBox.objectName(): self.tsDoubleSpinBox.value(),
        }

    def get_rifle(self):
        return {
            self.rifleName.objectName(): self.rifleName.text(),
            self.caliberName.objectName(): self.caliberName.text(),
            self.shSpinBox.objectName(): self.shSpinBox.value(),
            self.twistSpinBox.objectName(): self.twistSpinBox.value(),
            self.caliberShort.objectName(): self.twistSpinBox.value(),
            self.rightTwist.objectName(): self.rightTwist.isChecked(),
        }

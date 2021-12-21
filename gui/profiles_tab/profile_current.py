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
        self.mvSwitch.clicked.connect(self.convert_muzzle_velocity)
        self.weightSwitch.clicked.connect(self.convert_bullet_weight)
        self.lengthSwitch.clicked.connect(self.convert_bullet_length)
        self.diameterSwitch.clicked.connect(self.convert_bullet_diameter)
        self.dragEditor.clicked.connect(self.drag_func_edit)

    def setConverter(self):
        self.mvQuantity.setItemData(0, self.convert.mps2fps)
        self.mvQuantity.setItemData(1, self.convert.fps2mps)
        self.weighQuantity.setItemData(0, self.convert.gr_to_g)
        self.weighQuantity.setItemData(1, self.convert.g_to_gr)
        self.lengthQuantity.setItemData(0, self.convert.inch_to_mm)
        self.lengthQuantity.setItemData(1, self.convert.mm_to_inch)
        self.diameterQuantity.setItemData(0, self.convert.inch_to_mm)
        self.diameterQuantity.setItemData(1, self.convert.mm_to_inch)

    def drag_func_edit(self):
        drag_func_dlg = DragFuncEditDialog()
        new_drag_func = drag_func_dlg.current_data if drag_func_dlg.exec_() else drag_func_dlg.default_data

    def convert_muzzle_velocity(self):
        cur_idx = self.mvQuantity.currentIndex()
        self.mv.setValue(self.mvQuantity.itemData(cur_idx)(self.mv.value()))
        self.mvQuantity.setCurrentIndex(1 if cur_idx == 0 else 0)

    def convert_bullet_weight(self):
        cur_idx = self.weighQuantity.currentIndex()
        self.weight.setValue(self.weighQuantity.itemData(cur_idx)(self.weight.value()))
        self.weight.setSingleStep(0.01 if cur_idx == 0 else 0.1)
        self.weighQuantity.setCurrentIndex(1 if cur_idx == 0 else 0)

    def convert_bullet_length(self):
        cur_idx = self.lengthQuantity.currentIndex()
        self.length.setValue(self.lengthQuantity.itemData(cur_idx)(self.length.value()))
        self.lengthQuantity.setCurrentIndex(1 if cur_idx == 0 else 0)

    def convert_bullet_diameter(self):
        cur_idx = self.diameterQuantity.currentIndex()
        self.diameter.setValue(self.diameterQuantity.itemData(cur_idx)(self.diameter.value()))
        self.diameterQuantity.setCurrentIndex(1 if cur_idx == 0 else 0)

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

            self.weight.objectName():
                self.weight.value() if self.weighQuantity.currentIndex() == 0
                else self.weighQuantity.currentData()(self.weight.value()),

            self.length.objectName():
                self.length.value() if self.lengthQuantity.currentIndex() == 0
                else self.lengthQuantity.currentData()(self.length.value()),

            self.diameter.objectName():
                self.diameter.value() if self.diameterQuantity.currentIndex() == 0
                else self.diameterQuantity.currentData(self.diameter.value()),

            self.dragType.objectName(): self.dragType.currentIndex(),
            self.bc.objectName(): self.bc.value(),
        }

    def get_cartridge(self):
        return {
            self.cartridgeName.objectName(): self.cartridgeName.text(),
            self.mv.objectName():
                self.mv.value() if self.mvQuantity.currentIndex() == 0
                else self.mvQuantity.currentData()(self.mv.value()),

            self.temp.objectName(): self.temp.value(),
            self.ts.objectName(): self.ts.value(),
        }

    def get_rifle(self):
        return {
            self.rifleName.objectName(): self.rifleName.text(),
            self.caliberName.objectName(): self.caliberName.text(),
            self.sh.objectName(): self.sh.value(),
            self.twist.objectName(): self.twist.value(),
            self.caliberShort.objectName(): self.twist.text(),
            self.rightTwist.objectName(): self.rightTwist.isChecked(),
        }

    def set_data(self, data):
        self.rifleName.setText(data[self.rifleName.objectName()])
        self.caliberName.setText(data[self.caliberName.objectName()])
        self.sh.setValue(data[self.sh.objectName()])
        self.twist.setValue(data[self.twist.objectName()])
        self.caliberShort.setText(data[self.caliberShort.objectName()])
        self.rightTwist.setChecked(data[self.rightTwist.objectName()])

        self.cartridgeName.setText(data[self.caliberName.objectName()])
        self.mv.setValue(data[self.mv.objectName()] if self.mvQuantity.currentIndex() == 0
                         else self.mvQuantity.currentData()(data[self.mv.objectName()]))
        self.temp.setValue(data[self.temp.objectName()])
        self.ts.setValue(data[self.ts.objectName()])

        self.bulletName.setText(data[self.bulletName.objectName()])
        self.weight.setValue(data[self.weight.objectName()] if self.weighQuantity.currentIndex() == 0
                             else self.weighQuantity.currentData()(data[self.weight.objectName()]))
        self.length.setValue(data[self.length.objectName()] if self.lengthQuantity.currentIndex() == 0
                             else self.lengthQuantity.currentData()(data[self.length.objectName()]))
        self.diameter.setValue(data[self.diameter.objectName()] if self.diameterQuantity.currentIndex() == 0
                               else self.diameterQuantity.currentData()(data[self.diameter.objectName()]))
        self.dragType.setCurrentIndex(data[self.dragType.objectName()])
        self.bc.setValue(data[self.bc.objectName()])

        self.z_temp.setValue(data[self.z_temp.objectName()])
        self.z_angle.setValue(data[self.z_angle.objectName()])
        self.z_pressure.setValue(data[self.z_pressure.objectName()])
        self.z_latitude.setValue(data[self.z_latitude.objectName()])
        self.z_humidity.setValue(data[self.z_humidity.objectName()])
        self.z_azimuth.setValue(data[self.z_azimuth.objectName()])
        self.z_powder_temp.setValue(data[self.z_powder_temp.objectName()])

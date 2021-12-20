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

    def setupConnects(self):
        self.mvToolButton.clicked.connect(self.convert_muzzle_velocity)
        self.weightToolButton.clicked.connect(self.convert_bullet_weight)
        self.lengthToolButton.clicked.connect(self.convert_bullet_length)
        self.diameterToolButton.clicked.connect(self.convert_bullet_diameter)
        self.dragToolButton.clicked.connect(self.drag_func_edit)

    def drag_func_edit(self):
        drag_func_dlg = DragFuncEditDialog()
        new_drag_func = drag_func_dlg.current_data if drag_func_dlg.exec_() else drag_func_dlg.default_data

    def convert_muzzle_velocity(self):
        if self.mvComboBox.currentIndex() == 0:
            self.mvSpinBox.setValue(self.convert.mps2fps(self.mvSpinBox.value()))
            self.mvComboBox.setCurrentIndex(1)
        else:
            self.mvSpinBox.setValue(self.convert.fps2mps(self.mvSpinBox.value()))
            self.mvComboBox.setCurrentIndex(0)

    def convert_bullet_weight(self):
        if self.weightComboBox.currentIndex() == 0:
            self.bulletWeight.setValue(self.convert.gr_to_g(self.bulletWeight.value()))
            self.bulletWeight.setSingleStep(0.01)
            self.weightComboBox.setCurrentIndex(1)
        else:
            self.bulletWeight.setValue(self.convert.g_to_gr(self.bulletWeight.value()))
            self.bulletWeight.setSingleStep(0.1)
            self.weightComboBox.setCurrentIndex(0)

    def convert_bullet_length(self):
        if self.lengthComboBox.currentIndex() == 0:
            self.lengthDoubleSpinBox.setValue(self.convert.inch_to_mm(self.lengthDoubleSpinBox.value()))
            self.lengthComboBox.setCurrentIndex(1)
        else:
            self.lengthDoubleSpinBox.setValue(self.convert.mm_to_inch(self.lengthDoubleSpinBox.value()))
            self.lengthComboBox.setCurrentIndex(0)

    def convert_bullet_diameter(self):
        if self.diameterComboBox.currentIndex() == 0:
            self.diameterDoubleSpinBox.setValue(self.convert.inch_to_mm(self.diameterDoubleSpinBox.value()))
            self.diameterComboBox.setCurrentIndex(1)
        else:
            self.diameterDoubleSpinBox.setValue(self.convert.mm_to_inch(self.diameterDoubleSpinBox.value()))
            self.diameterComboBox.setCurrentIndex(0)

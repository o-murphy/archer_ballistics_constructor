from PyQt5 import QtWidgets, QtCore
from .templates import Ui_cartridge

from py_ballisticcalc.lib.bmath.unit import Velocity, VelocityMPS, Temperature, TemperatureCelsius
from gui.app_settings import AppSettings


class Cartridge(QtWidgets.QWidget, Ui_cartridge):
    def __init__(self, parent=None):
        super(Cartridge, self).__init__(parent)
        self.setupUi(self)
        self.cartridgeGroupBox.layout().setAlignment(QtCore.Qt.AlignLeft)

        self.mvQuantity.setVisible(False)
        self.mvSwitch.setVisible(False)

        self._mv = Velocity(0, VelocityMPS)
        self._temp = Temperature(0, TemperatureCelsius)

        self.units = None
        self.setUnits()

        self.mv.valueChanged.connect(self.validate_mv)
        self.temp.valueChanged.connect(self.temp_changed)

    def temp_changed(self, value):
        self._temp = Temperature(value, self.units.tempUnits.currentData())

    def validate_mv(self, value):
        if self.mv.value() == 0:
            self.mv.setFocus()
        else:
            self._mv = Velocity(value, self.units.vUnits.currentData())

    def setUnits(self):
        self.units = AppSettings()

        self.mv.setValue(self._mv.get_in(self.units.vUnits.currentData()))
        self.temp.setValue(self._temp.get_in(self.units.tempUnits.currentData()))
        self.mv.setSuffix(self.units.vUnits.currentText())
        self.temp.setSuffix(self.units.tempUnits.currentText())

    def set(self, data):

        self._mv = Velocity(data['mv'], VelocityMPS)
        self._temp = Temperature(data['temp'], TemperatureCelsius)

        self.setUnits()

        self.cartridgeName.setText(data['cartridgeName'])
        self.ts.setValue(data['ts'])

    def get(self):
        return {
            self.cartridgeName.objectName(): self.cartridgeName.text(),
            self.mv.objectName(): self._mv.get_in(VelocityMPS),
            self.temp.objectName(): self._temp.get_in(TemperatureCelsius),
            self.ts.objectName(): self.ts.value(),
        }

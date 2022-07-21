from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from .templates import Ui_conditions

from py_ballisticcalc.lib.bmath.unit import Pressure, PressureMmHg, Temperature, TemperatureCelsius
from py_ballisticcalc.lib.bmath.unit import Angular, AngularDegree
from gui.app_settings import AppSettings


class Conditions(QWidget, Ui_conditions):
    def __init__(self, parent=None):
        super(Conditions, self).__init__(parent)
        self.setupUi(self)

        self.groupBox.layout().setAlignment(Qt.AlignLeft)

        self._z_pressure = Pressure(0, PressureMmHg)
        self._z_temp = Temperature(0, TemperatureCelsius)
        self._z_powder_temp = Temperature(0, TemperatureCelsius)
        self._z_angle = Angular(0, AngularDegree)
        self._z_azimuth = Angular(0, AngularDegree)
        self._z_latitude = Angular(0, AngularDegree)

        self.units = None
        self.setUnits()

        self.z_pressure.valueChanged.connect(self.z_pressure_changed)
        self.z_temp.valueChanged.connect(self.z_temp_changed)
        self.z_powder_temp.valueChanged.connect(self.z_powder_temp_changed)
        self.z_angle.valueChanged.connect(self.z_angle_changed)
        self.z_azimuth.valueChanged.connect(self.z_azimuth_changed)
        self.z_latitude.valueChanged.connect(self.z_latitude_changed)

    def z_temp_changed(self, value):
        self._z_temp = Temperature(value, self.units.tempUnits.currentData())

    def z_powder_temp_changed(self, value):
        self._z_powder_temp = Temperature(value, self.units.tempUnits.currentData())

    def z_angle_changed(self, value):
        self._z_angle = Angular(value, self.units.angleUnits.currentData())

    def z_azimuth_changed(self, value):
        self._z_azimuth = Angular(value, self.units.angleUnits.currentData())

    def z_latitude_changed(self, value):
        self._z_latitude = Angular(value, self.units.angleUnits.currentData())

    def z_pressure_changed(self, value):
        self._z_pressure = Pressure(value, self.units.pUnits.currentData())

    def setUnits(self):
        self.units = AppSettings()

        self.z_pressure.setValue(self._z_pressure.get_in(self.units.pUnits.currentData()))
        self.z_temp.setValue(self._z_temp.get_in(self.units.tempUnits.currentData()))
        self.z_powder_temp.setValue(self._z_powder_temp.get_in(self.units.tempUnits.currentData()))
        self.z_angle.setValue(self._z_angle.get_in(self.units.angleUnits.currentData()))
        self.z_azimuth.setValue(self._z_azimuth.get_in(self.units.angleUnits.currentData()))
        self.z_latitude.setValue(self._z_latitude.get_in(self.units.angleUnits.currentData()))

        self.z_pressure.setSuffix(self.units.pUnits.currentText())
        self.z_temp.setSuffix(self.units.tempUnits.currentText())
        self.z_powder_temp.setSuffix(self.units.tempUnits.currentText())
        self.z_angle.setSuffix(self.units.angleUnits.currentText())
        self.z_azimuth.setSuffix(self.units.angleUnits.currentText())
        self.z_latitude.setSuffix(self.units.angleUnits.currentText())

    def get(self):
        return {
            'z_pressure': self._z_pressure.get_in(PressureMmHg),
            'z_temp': self._z_temp.get_in(TemperatureCelsius),
            'z_powder_temp': self._z_powder_temp.get_in(TemperatureCelsius),
            'z_angle': self._z_angle.get_in(AngularDegree),
            'z_azimuth': self._z_azimuth.get_in(AngularDegree),
            'z_latitude': self._z_latitude.get_in(AngularDegree),
            'z_humidity': self.z_humidity.value()
        }

    def set(self, data):
        self._z_pressure = Pressure(data['z_pressure'], PressureMmHg)
        self._z_angle = Angular(data['z_angle'], AngularDegree)
        self._z_temp = Temperature(data['z_temp'], TemperatureCelsius)
        self._z_azimuth = Angular(data['z_azimuth'], AngularDegree)
        self._z_latitude = Angular(data['z_latitude'], AngularDegree)
        self._z_powder_temp = Temperature(data['z_powder_temp'], TemperatureCelsius)
        self.z_humidity.setValue(data['z_humidity'])
        self.setUnits()

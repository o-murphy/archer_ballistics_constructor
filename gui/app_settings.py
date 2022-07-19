# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore
from gui.templates import Ui_AppSettings
from modules.lpc_check import lpcRunThread, UsbStatusCode, check_lpc_driver
import configparser
import os
from modules.env_update import CONFIG_PATH
from gui.stylesheet import load_qss


from py_ballisticcalc.lib.bmath.unit import *


class AppSettings(QtWidgets.QDialog, Ui_AppSettings):
    def __init__(self):
        super(AppSettings, self).__init__()
        self.setupUi(self)
        self.init_units_tab()
        self.load_settings()

    def init_units_tab(self):
        self.shUnits.addItem('inch', DistanceInch)
        self.shUnits.addItem('cm', DistanceCentimeter)
        self.shUnits.addItem('mm', DistanceMillimeter)
        self.shUnits.addItem('ln', DistanceLine)

        self.twistUnits.addItem('inch', DistanceInch)
        self.twistUnits.addItem('cm', DistanceCentimeter)
        self.twistUnits.addItem('mm', DistanceMillimeter)
        self.twistUnits.addItem('ln', DistanceLine)

        self.vUnits.addItem('m/s', VelocityMPS)
        self.vUnits.addItem('km/h', VelocityKMH)
        self.vUnits.addItem('ft/s', VelocityFPS)
        self.vUnits.addItem('mph', VelocityMPH)
        self.vUnits.addItem('kt', VelocityKT)

        self.distUnits.addItem('m', DistanceMeter)
        self.distUnits.addItem('ft', DistanceFoot)
        self.distUnits.addItem('yd', DistanceYard)
        self.distUnits.addItem('km', DistanceKilometer)
        self.distUnits.addItem('mi', DistanceMile)
        self.distUnits.addItem('nm', DistanceNauticalMile)

        self.tempUnits.addItem('°C', TemperatureCelsius)
        self.tempUnits.addItem('°F', TemperatureFahrenheit)
        self.tempUnits.addItem('°K', TemperatureKelvin)
        self.tempUnits.addItem('°R', TemperatureRankin)

        self.wUnits.addItem('gr', WeightGrain)
        self.wUnits.addItem('g', WeightGram)
        self.wUnits.addItem('kg', WeightKilogram)
        self.wUnits.addItem('lb', WeightPound)
        # self.wUnits.addItem('N', WeightNewton)
        # self.wUnits.addItem('oz', WeightOunce)

        self.lnUnits.addItem('inch', DistanceInch)
        self.lnUnits.addItem('cm', DistanceCentimeter)
        self.lnUnits.addItem('mm', DistanceMillimeter)
        self.lnUnits.addItem('ln', DistanceLine)

        self.dUnits.addItem('inch', DistanceInch)
        self.dUnits.addItem('cm', DistanceCentimeter)
        self.dUnits.addItem('mm', DistanceMillimeter)
        self.dUnits.addItem('ln', DistanceLine)

        self.pUnits.addItem('mmHg', PressureMmHg)
        self.pUnits.addItem('inHg', PressureInHg)
        self.pUnits.addItem('bar', PressureBar)
        self.pUnits.addItem('hPa', PressureHP)
        self.pUnits.addItem('psi', PressurePSI)

        self.dropUnits.addItem('inch', DistanceInch)
        self.dropUnits.addItem('cm', DistanceCentimeter)
        self.dropUnits.addItem('mm', DistanceMillimeter)
        self.dropUnits.addItem('ln', DistanceLine)
        self.dropUnits.addItem('m', DistanceMeter)
        self.dropUnits.addItem('yd', DistanceYard)
        self.dropUnits.addItem('ft', DistanceFoot)

        self.angleUnits.addItem('rad', AngularRadian)
        self.angleUnits.addItem('°', AngularDegree)

        self.angleUnits.addItem('mrad', AngularMRad)
        self.angleUnits.addItem('ths', AngularThousand)

        self.pathUnits.addItem('moa', AngularMOA)
        self.pathUnits.addItem('mil', AngularMil)
        self.pathUnits.addItem('cm/100m', AngularCmPer100M)
        self.pathUnits.addItem('in/100yd', AngularInchesPer100Yd)

        self.eUnits.addItem('ft*lb', EnergyFootPound)
        self.eUnits.addItem('J', EnergyJoule)

    def load_settings(self):
        config = configparser.ConfigParser()
        config.read(CONFIG_PATH)

        widgets = self.findChildren(QtWidgets.QComboBox)

        for i in config['Units']:
            for w in widgets:
                if i == w.objectName().lower():
                    w.setCurrentIndex(w.findData(config['Units'][i]))

    def save_settings(self):
        print(CONFIG_PATH)
        config = configparser.ConfigParser()
        config.read(CONFIG_PATH)
        if 'Units' not in config:
            config.add_section('Units')
        for w in self.findChildren(QtWidgets.QComboBox):
            config.set('Units', w.objectName(), str(w.currentData()))
        with open(CONFIG_PATH, 'w') as fp:
            config.write(fp)

    def accept(self) -> None:
        self.save_settings()
        super().accept()

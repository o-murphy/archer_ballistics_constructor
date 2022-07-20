# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore
from gui.templates import Ui_AppSettings
import configparser
import os
from modules.env_update import CONFIG_PATH
from gui.stylesheet import load_qss


from py_ballisticcalc.lib.bmath.unit import *


inch = (' inch', DistanceInch)

ln = (' ln', DistanceLine)
yd = (' yd', DistanceYard)
ft = (' ft', DistanceFoot)
mm = (' mm', DistanceMillimeter)
cm = (' cm', DistanceCentimeter)
m = (' m', DistanceMeter)
km = (' km', DistanceKilometer)
mi = (' mi', DistanceMile)
nm = (' nm', DistanceNauticalMile)
rad = (' rad', AngularRadian)
deg = (' °', AngularDegree)
mrad = (' mrad', AngularMRad)
ths = (' ths', AngularThousand)
mil = (' mil', AngularMil)
moa = (' moa', AngularMOA)
cm100m = (' cm/100m', AngularCmPer100M)
in100yd = (' in/100yd', AngularInchesPer100Yd)
ftlb = (' ft*lb', EnergyFootPound)
j = (' J', EnergyJoule)
mmhg = (' mmHg', PressureMmHg)
inhg = (' inHg', PressureInHg)
bar = (' bar', PressureBar)
hpa = (' hPa', PressureHP)
psi = (' psi', PressurePSI)
gr = (' gr', WeightGrain)
g = (' g', WeightGram)
kg = (' kg', WeightKilogram)
lb = (' lb', WeightPound)
n = (' N', WeightNewton)
oz = (' oz', WeightOunce)
c = (' °C', TemperatureCelsius)
f = (' °F', TemperatureFahrenheit)
k = (' °K', TemperatureKelvin)
r = (' °R', TemperatureRankin)
mps = (' m/s', VelocityMPS)
kmh = (' km/h', VelocityKMH)
fps = (' ft/s', VelocityFPS)
mph = (' mph', VelocityMPH)
kt = (' kt', VelocityKT)


class AppSettings(QtWidgets.QDialog, Ui_AppSettings):

    def __init__(self):
        super(AppSettings, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(load_qss('qss/dialog.qss'))
        self.init_general_tab()
        self.init_units_tab()

        self.load_general_settings()
        self.load_unit_settings()

    def init_general_tab(self):
        self.languages = ['en', 'ua', 'ru']
        for i, lang in enumerate(self.languages):
            self.Language.setItemData(i, lang)

    def init_units_tab(self):
        self.shUnits.addItem(*mm)
        self.shUnits.addItem(*inch)
        self.shUnits.addItem(*cm)
        self.shUnits.addItem(*ln)

        self.twistUnits.addItem(*inch)
        self.twistUnits.addItem(*cm)
        self.twistUnits.addItem(*mm)
        self.twistUnits.addItem(*ln)

        self.vUnits.addItem(*mps)
        self.vUnits.addItem(*kmh)
        self.vUnits.addItem(*fps)
        self.vUnits.addItem(*mph)
        self.vUnits.addItem(*kt)

        self.distUnits.addItem(*m)
        self.distUnits.addItem(*ft)
        self.distUnits.addItem(*yd)
        self.distUnits.addItem(*km)
        self.distUnits.addItem(*mi)
        self.distUnits.addItem(*nm)

        self.tempUnits.addItem(*c)
        self.tempUnits.addItem(*f)
        self.tempUnits.addItem(*k)
        self.tempUnits.addItem(*r)

        self.wUnits.addItem(*gr)
        self.wUnits.addItem(*g)
        self.wUnits.addItem(*kg)
        self.wUnits.addItem(*lb)
        # self.wUnits.addItem(*n)
        # self.wUnits.addItem(*oz)

        self.lnUnits.addItem(*inch)
        self.lnUnits.addItem(*cm)
        self.lnUnits.addItem(*mm)
        self.lnUnits.addItem(*ln)

        self.dUnits.addItem(*inch)
        self.dUnits.addItem(*cm)
        self.dUnits.addItem(*mm)
        self.dUnits.addItem(*ln)

        self.pUnits.addItem(*mmhg)
        self.pUnits.addItem(*inhg)
        self.pUnits.addItem(*bar)
        self.pUnits.addItem(*hpa)
        self.pUnits.addItem(*psi)

        self.dropUnits.addItem(*cm)
        self.dropUnits.addItem(*inch)
        self.dropUnits.addItem(*mm)
        self.dropUnits.addItem(*ln)
        self.dropUnits.addItem(*m)
        self.dropUnits.addItem(*yd)
        self.dropUnits.addItem(*ft)

        self.angleUnits.addItem(*deg)
        self.angleUnits.addItem(*rad)
        self.angleUnits.addItem(*mrad)
        self.angleUnits.addItem(*ths)

        self.pathUnits.addItem(*mil)
        self.pathUnits.addItem(*moa)
        self.pathUnits.addItem(*mrad)
        self.pathUnits.addItem(*ths)
        self.pathUnits.addItem(*cm100m)
        self.pathUnits.addItem(*in100yd)

        self.eUnits.addItem(*ftlb)
        self.eUnits.addItem(*j)

    def load_general_settings(self):
        config = configparser.ConfigParser()
        config.read(CONFIG_PATH)
        if 'Locale' in config:
            locale = config['Locale']['current']
            self.Language.setCurrentIndex(self.languages.index(locale))
        else:
            self.save_language_settings()

        if 'General' in config:
            exp_dfed = True if config['General']['exp_dfed'] == 'True' else False
            self.xdfed.setChecked(exp_dfed)
        else:
            self.save_exp_dfed()

    def load_unit_settings(self):
        config = configparser.ConfigParser()
        config.read(CONFIG_PATH)

        widgets = self.findChildren(QtWidgets.QComboBox)
        if 'Units' in config:
            for i in config['Units']:
                for w in widgets:
                    if i == w.objectName().lower():
                        w.setCurrentIndex(w.findData(config['Units'][i]))
        else:
            self.save_units_settings()

    def save_exp_dfed(self):
        exp_dfed = self.xdfed.isChecked()
        config = configparser.ConfigParser()
        config.read(CONFIG_PATH)
        if not 'General' in config:
            config.add_section('General')
        config.set('General', 'exp_dfed', str(exp_dfed))
        with open(CONFIG_PATH, 'w') as fp:
            config.write(fp)

    def save_language_settings(self):
        locale = self.Language.currentData()
        config = configparser.ConfigParser()
        config.read(CONFIG_PATH)
        config.set('Locale', 'system', QtCore.QLocale.system().name().split('_')[1].lower())
        if locale != 'en':
            if os.path.isfile(f'translate/eng-{locale}.qm'):
                config.set('Locale', 'current', locale)
            else:
                locale = config['Locale']['system']
                config.set('Locale', 'current', locale)
        else:
            config.set('Locale', 'current', locale)
        with open(CONFIG_PATH, 'w') as fp:
            config.write(fp)

    def save_units_settings(self):
        config = configparser.ConfigParser()
        config.read(CONFIG_PATH)
        if 'Units' not in config:
            config.add_section('Units')
        for w in self.tabUnits.findChildren(QtWidgets.QComboBox):
            config.set('Units', w.objectName(), str(w.currentData()))
        with open(CONFIG_PATH, 'w') as fp:
            config.write(fp)

    def accept(self) -> None:
        self.save_language_settings()
        self.save_exp_dfed()
        self.save_units_settings()
        super().accept()

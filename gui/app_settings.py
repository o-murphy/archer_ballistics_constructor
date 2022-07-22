# -*u.- coding: utf-8 -*u.-

from PyQt5.QtCore import QCoreApplication, QLocale
from PyQt5.QtWidgets import QDialog, QComboBox

from gui.templates import Ui_AppSettings
import configparser
import os
from modules.env_update import CONFIG_PATH
from gui.stylesheet import load_qss


from py_ballisticcalc.lib.bmath.unit import *


class AppSettings(QDialog, Ui_AppSettings):

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

        self.xdfed.setChecked(True)

    def init_units_tab(self):

        u = self

        self.shUnits.addItem(*u.mm)
        self.shUnits.addItem(*u.inch)
        self.shUnits.addItem(*u.cm)
        self.shUnits.addItem(*u.ln)

        self.twistUnits.addItem(*u.inch)
        self.twistUnits.addItem(*u.cm)
        self.twistUnits.addItem(*u.mm)
        self.twistUnits.addItem(*u.ln)

        self.vUnits.addItem(*u.mps)
        self.vUnits.addItem(*u.kmh)
        self.vUnits.addItem(*u.fps)
        self.vUnits.addItem(*u.mph)
        self.vUnits.addItem(*u.kt)

        self.distUnits.addItem(*u.m)
        self.distUnits.addItem(*u.ft)
        self.distUnits.addItem(*u.yd)
        self.distUnits.addItem(*u.km)
        self.distUnits.addItem(*u.mi)
        self.distUnits.addItem(*u.nm)

        self.tempUnits.addItem(*u.c)
        self.tempUnits.addItem(*u.f)
        self.tempUnits.addItem(*u.k)
        self.tempUnits.addItem(*u.r)

        self.wUnits.addItem(*u.gr)
        self.wUnits.addItem(*u.g)
        self.wUnits.addItem(*u.kg)
        self.wUnits.addItem(*u.lb)
        # self.wUnits.addItem(*u.n)
        # self.wUnits.addItem(*u.oz)

        self.lnUnits.addItem(*u.inch)
        self.lnUnits.addItem(*u.cm)
        self.lnUnits.addItem(*u.mm)
        self.lnUnits.addItem(*u.ln)

        self.dUnits.addItem(*u.inch)
        self.dUnits.addItem(*u.cm)
        self.dUnits.addItem(*u.mm)
        self.dUnits.addItem(*u.ln)

        self.pUnits.addItem(*u.mmhg)
        self.pUnits.addItem(*u.inhg)
        self.pUnits.addItem(*u.bar)
        self.pUnits.addItem(*u.hpa)
        self.pUnits.addItem(*u.psi)

        self.dropUnits.addItem(*u.cm)
        self.dropUnits.addItem(*u.inch)
        self.dropUnits.addItem(*u.mm)
        self.dropUnits.addItem(*u.ln)
        self.dropUnits.addItem(*u.m)
        self.dropUnits.addItem(*u.yd)
        self.dropUnits.addItem(*u.ft)

        self.angleUnits.addItem(*u.deg)
        self.angleUnits.addItem(*u.rad)
        self.angleUnits.addItem(*u.mrad)
        self.angleUnits.addItem(*u.ths)

        self.pathUnits.addItem(*u.mil)
        self.pathUnits.addItem(*u.moa)
        self.pathUnits.addItem(*u.mrad)
        self.pathUnits.addItem(*u.ths)
        self.pathUnits.addItem(*u.cm100m)
        self.pathUnits.addItem(*u.in100yd)

        self.eUnits.addItem(*u.ftlb)
        self.eUnits.addItem(*u.j)

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

        widgets = self.findChildren(QComboBox)
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
        config.set('Locale', 'system', QLocale.system().name().split('_')[1].lower())
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
        for w in self.tabUnits.findChildren(QComboBox):
            config.set('Units', w.objectName(), str(w.currentData()))
        with open(CONFIG_PATH, 'w') as fp:
            config.write(fp)

    def accept(self) -> None:
        self.save_language_settings()
        self.save_exp_dfed()
        self.save_units_settings()
        super().accept()

    def retranslateUi(self, AppSettings):
        super().retranslateUi(AppSettings)
        _translate = QCoreApplication.translate
        self.inch = (_translate('AppSettings', ' inch'), DistanceInch)
        self.ln = (_translate('AppSettings', ' ln'), DistanceLine)
        self.yd = (_translate('AppSettings', ' yd'), DistanceYard)
        self.ft = (_translate('AppSettings', ' ft'), DistanceFoot)
        self.mm = (_translate('AppSettings', ' mm'), DistanceMillimeter)
        self.cm = (_translate('AppSettings', ' cm'), DistanceCentimeter)
        self.m = (_translate('AppSettings', ' m'), DistanceMeter)
        self.km = (_translate('AppSettings', ' km'), DistanceKilometer)
        self.mi = (_translate('AppSettings', ' mi'), DistanceMile)
        self.nm = (_translate('AppSettings', ' nm'), DistanceNauticalMile)
        self.rad = (_translate('AppSettings', ' rad'), AngularRadian)
        self.deg = (_translate('AppSettings', ' °'), AngularDegree)
        self.mrad = (_translate('AppSettings', ' mrad'), AngularMRad)
        self.ths = (_translate('AppSettings', ' ths'), AngularThousand)
        self.mil = (_translate('AppSettings', ' mil'), AngularMil)
        self.moa = (_translate('AppSettings', ' moa'), AngularMOA)
        self.cm100m = (_translate('AppSettings', ' cm/100m'), AngularCmPer100M)
        self.in100yd = (_translate('AppSettings', ' in/100yd'), AngularInchesPer100Yd)
        self.ftlb = (_translate('AppSettings', ' ft*lb'), EnergyFootPound)
        self.j = (_translate('AppSettings', ' J'), EnergyJoule)
        self.mmhg = (_translate('AppSettings', ' mmHg'), PressureMmHg)
        self.inhg = (_translate('AppSettings', ' inHg'), PressureInHg)
        self.bar = (_translate('AppSettings', ' bar'), PressureBar)
        self.hpa = (_translate('AppSettings', ' hPa'), PressureHP)
        self.psi = (_translate('AppSettings', ' psi'), PressurePSI)
        self.gr = (_translate('AppSettings', ' gr'), WeightGrain)
        self.g = (_translate('AppSettings', ' g'), WeightGram)
        self.kg = (_translate('AppSettings', ' kg'), WeightKilogram)
        self.lb = (_translate('AppSettings', ' lb'), WeightPound)
        self.n = (_translate('AppSettings', ' N'), WeightNewton)
        self.oz = (_translate('AppSettings', ' oz'), WeightOunce)
        self.c = (_translate('AppSettings', ' °C'), TemperatureCelsius)
        self.f = (_translate('AppSettings', ' °F'), TemperatureFahrenheit)
        self.k = (_translate('AppSettings', ' °K'), TemperatureKelvin)
        self.r = (_translate('AppSettings', ' °R'), TemperatureRankin)
        self.mps = (_translate('AppSettings', ' m/s'), VelocityMPS)
        self.kmh = (_translate('AppSettings', ' km/h'), VelocityKMH)
        self.fps = (_translate('AppSettings', ' ft/s'), VelocityFPS)
        self.mph = (_translate('AppSettings', ' mph'), VelocityMPH)
        self.kt = (_translate('AppSettings', ' kt'), VelocityKT)

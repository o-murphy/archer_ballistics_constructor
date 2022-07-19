from PyQt5 import QtWidgets, QtCore
from .templates import Ui_rifle
import configparser
import os
from modules.env_update import CONFIG_PATH

from py_ballisticcalc.lib.bmath.unit import Distance, DistanceMillimeter, DistanceInch
from gui.app_settings import AppSettings


class Rifle(QtWidgets.QWidget, Ui_rifle):
    def __init__(self, parent=None):
        super(Rifle, self).__init__(parent)
        self.setupUi(self)
        self.rifleGroupBox.layout().setAlignment(QtCore.Qt.AlignLeft)
        self.autoTile.clicked.connect(self.auto_tile)

        self._sh = Distance(0, DistanceMillimeter)
        self._twist = Distance(0, DistanceInch)

        self.units = None
        self.setUnits()

        self.sh.valueChanged.connect(self.sh_changed)
        self.twist.valueChanged.connect(self.twist_changed)

    def sh_changed(self, value):
        self._sh = Distance(value, self.units.shUnits.currentData())

    def twist_changed(self, value):
        self._twist = Distance(value, self.units.twistUnits.currentData())

    def setUnits(self):
        self.units = AppSettings()

        self.sh.setValue(self._sh.get_in(self.units.shUnits.currentData()))
        self.sh.setSuffix(self.units.shUnits.currentText())
        self.twist.setValue(self._twist.get_in(self.units.twistUnits.currentData()))
        self.twist.setSuffix(self.units.twistUnits.currentText())

    def auto_tile(self):
        self.caliberShort.setText(
            self.caliberName.text().replace(' ', '').strip()[:7]
        )

    def set(self, data):
        self._sh = Distance(data['sh'], DistanceMillimeter)
        self._twist = Distance(data['twist'], DistanceInch)

        self.setUnits()

        self.rifleName.setText(data['rifleName'])
        self.caliberName.setText(data['caliberName'])
        self.caliberShort.setText(data['caliberShort'])
        self.rightTwist.setChecked(data['rightTwist'])

    def get(self):

        return {
            self.rifleName.objectName(): self.rifleName.text(),
            self.caliberName.objectName(): self.caliberName.text(),
            self.sh.objectName(): self._sh.get_in(DistanceMillimeter),
            self.twist.objectName(): self._twist.get_in(DistanceInch),
            self.caliberShort.objectName(): self.caliberShort.text(),
            self.rightTwist.objectName(): self.rightTwist.isChecked(),
        }

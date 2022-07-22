from PyQt5.QtWidgets import QDialog

from .templates import Ui_caliberEdit
from dbworker import db
from dbworker.models import Caliber, Diameter

from gui.stylesheet import load_qss

from py_ballisticcalc.lib.bmath.unit import Distance, DistanceInch
from gui.app_settings import AppSettings


class CaliberEdit(QDialog, Ui_caliberEdit):
    def __init__(self):
        super(CaliberEdit, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(load_qss('qss\dialog.qss'))
        self.units = AppSettings()
        self.diameter.setSuffix(self.units.dUnits.currentText())

    def get(self):
        sess = db.SessMake()
        diam = sess.query(Diameter).filter_by(diameter=self.diameter.value()).first()
        if not diam:
            diam = Diameter(Distance(self.diameter.value(), self.units.dUnits.currentData()).get_in(DistanceInch))
            sess.add(diam)
            sess.commit()
        cal = Caliber(self.name.text(), diam.id)
        sess.add(cal)
        sess.commit()
        return cal.id

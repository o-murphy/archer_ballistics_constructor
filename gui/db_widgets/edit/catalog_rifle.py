from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QWidget

from .templates import Ui_catalogRifle
from dbworker import db
from dbworker.models import *
from .caliber_edit import CaliberEdit


from py_ballisticcalc.lib.bmath.unit import Distance, DistanceInch, DistanceMillimeter
from gui.app_settings import AppSettings


class CatalogRifle(QWidget, Ui_catalogRifle):
    def __init__(self, data=None, call=None):
        super(CatalogRifle, self).__init__()
        self.setupUi(self)

        self.title = ''

        self.data = data
        self.call = call

        self.query_calibers()

        self.units = AppSettings()

        # if data:
        #     self.data = data
        #     self.rifleName.setText(data.name)
        #
        #     self.caliberName.setCurrentIndex(self.caliberName.findData(data.caliber.id))
        #     self.caliberName.setCurrentText(data.caliber.name)
        #     self.sh.setValue(data.sh)
        #     self.twist.setValue(data.twist)
        #     self.rightTwist.setChecked(data.is_right)
        #     self.caliberShort.setText(data.tile)

        self.set_widget_data()

        self.pushButton.clicked.connect(self.add_caliber)

        self.retranslateUi(self)

    def set_widget_data(self):
        if self.data:
            self.rifleName.setText(self.data.name)
            self.caliberName.setCurrentIndex(self.caliberName.findData(self.data.caliber.id))
            self.caliberName.setCurrentText(self.data.caliber.name)
            self.rightTwist.setChecked(self.data.is_right)
            self.caliberShort.setText(self.data.tile)

            self.sh.setValue(Distance(self.data.sh, DistanceMillimeter).get_in(self.units.shUnits.currentData()))
            self.twist.setValue(Distance(self.data.twist, DistanceInch).get_in(self.units.twistUnits.currentData()))
            self.sh.setSuffix(self.units.shUnits.currentText())
            self.twist.setSuffix(self.units.twistUnits.currentText())

    def setConverter(self):
        self.weightQuantity.setItemData(0, self.convert.gr_to_g)
        self.weightQuantity.setItemData(1, self.convert.g_to_gr)
        self.lengthQuantity.setItemData(0, self.convert.inch_to_mm)
        self.lengthQuantity.setItemData(1, self.convert.mm_to_inch)
        self.diameterQuantity.setItemData(0, self.convert.inch_to_mm)
        self.diameterQuantity.setItemData(1, self.convert.mm_to_inch)

    def query_calibers(self):
        self.caliberName.clear()
        sess = db.SessMake()
        for c in sess.query(Caliber).all():
            self.caliberName.addItem(c.name, c.id)

    def get(self):
        sess = db.SessMake()

        if self.call == 'edit':
            rifle = sess.query(Rifle).get(self.data.id)
            rifle.name = self.rifleName.text()
            rifle.caliber_id = self.caliberName.currentData()
            rifle.sh = Distance(self.sh.value(), self.units.shUnits.currentData()).get_in(DistanceMillimeter)
            rifle.twist = Distance(self.twist.value(), self.units.twistUnits.currentData()).get_in(DistanceInch)
            rifle.is_right = self.rightTwist.isChecked()
            rifle.tile = self.caliberShort.text()
        else:
            sess.add(
                    Rifle(
                        self.rifleName.text(),
                        self.caliberName.currentData(),
                        self.sh.value(),
                        self.twist.value(),
                        self.rightTwist.isChecked(),
                        self.caliberShort.text(),
                        'rw'
                    )
                )
        sess.commit()

    def valid(self):
        return True

    def invalid(self):
        return False

    def add_caliber(self):
        ced = CaliberEdit()
        if ced.exec_():
            ced.get()
        self.query_calibers()

    def retranslateUi(self, catalogRifle):
        super(CatalogRifle, self).retranslateUi(catalogRifle)
        _translate = QCoreApplication.translate
        self.title = _translate("catalogRifle", 'Rifle Edit')

from PyQt5 import QtWidgets
from .templates import Ui_catalogRifle
from dbworker import db
from dbworker.models import *
from .caliber_edit import CaliberEdit


class CatalogRifle(QtWidgets.QWidget, Ui_catalogRifle):
    def __init__(self, data=None, call=None):
        super(CatalogRifle, self).__init__()
        self.setupUi(self)
        self.title = 'Rifle Edit'

        self.data = data
        self.call = call

        self.query_calibers()

        if data:
            self.data = data
            self.rifleName.setText(data.name)

            self.caliberName.setCurrentIndex(self.caliberName.findData(data.caliber.id))
            self.caliberName.setCurrentText(data.caliber.name)
            self.sh.setValue(data.sh)
            self.twist.setValue(data.twist)
            self.rightTwist.setChecked(data.is_right)
            self.caliberShort.setText(data.tile)

        self.pushButton.clicked.connect(self.add_caliber)

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
            rifle.sh = self.sh.value()
            rifle.twist = self.twist.value()
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

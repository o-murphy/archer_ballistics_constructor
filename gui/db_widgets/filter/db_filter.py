from PyQt5 import QtWidgets
from .templates import Ui_filter
from dbworker import db
from dbworker.models import *


class Filter(QtWidgets.QWidget, Ui_filter):
    def __init__(self):
        super(Filter, self).__init__()
        self.setupUi(self)
        self.update_calibers()

        self.applyFilter.clicked.connect(self.apply_filter)

    def update_calibers(self):
        sess = db.SessMake()
        calibers = sess.query(Caliber).all()
        for i in range(self.caliber.count()):
            self.caliber.removeItem(i)
        self.caliber.addItem("None", None)
        for cal in calibers:
            self.caliber.addItem(f"{cal.name}, {cal.diameter.diameter:.3f}inch", cal.id)

    def apply_filter(self):
        filter_by = {}

        if self.name.text() != "":
            filter_by['name'] = self.name.text()
        # if self.caliber.currentData():
        #     filter.update({'caliber_id', self.caliber.currentData()})
        # if self.diameter.value() > 0:
        #     filter.update({'diameter', self.diameter.value()})
        # if self.weight.value() > 0:
        #     filter.update({'weight', self.weight.value()})

        sess = db.SessMake()
        rifles = sess.query(Rifle).filter_by(**filter_by).all()
        # rifles = Rifle.query.filter(Rifle.name.contains('sub_string')).all()

        for r in rifles:
            print(r.name)


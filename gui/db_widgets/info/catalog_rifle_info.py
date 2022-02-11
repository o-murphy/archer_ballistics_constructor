from PyQt5 import QtWidgets
from .templates import Ui_catalogRifleInfo
from dbworker import db
from dbworker.models import *


class CatalogRifleInfo(QtWidgets.QWidget, Ui_catalogRifleInfo):
    def __init__(self):
        super(CatalogRifleInfo, self).__init__()
        self.setupUi(self)
        self.item = None
        self.clear()

    def set(self, id):
        if id:
            sess = db.SessMake()
            self.item = sess.query(Rifle).get(id)
            if self.item:
                self.rifleName.setText(self.item.name)
                self.caliber.setText(self.item.caliber.name)
                self.sh.setText(str(self.item.sh))
                self.twist.setText(
                    f'1:{self.item.twist} Right' if self.item.is_right else f'1:{self.item.twist} Left'
                )
                self.caliberShort.setText(self.item.tile)

    def clear(self):
        self.item = None
        self.rifleName.setText('Empty')
        self.caliber.setText('Empty')
        self.sh.setText('Empty')
        self.twist.setText('Empty')
        self.caliberShort.setText('Empty')

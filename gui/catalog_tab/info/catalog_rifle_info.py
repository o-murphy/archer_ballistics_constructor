from PyQt5 import QtWidgets
from .templates import Ui_catalogRifleInfo
from dbworker import db
from dbworker.models import *


class CatalogRifleInfo(QtWidgets.QWidget, Ui_catalogRifleInfo):
    def __init__(self):
        super(CatalogRifleInfo, self).__init__()
        self.setupUi(self)
        self.rifle = None

    def set(self, id):
        if id:
            sess = db.SessMake()
            self.rifle = sess.query(Rifle).get(id)
            if self.rifle:
                self.rifleName.setText(self.rifle.name)
                self.caliber.setText(self.rifle.caliber.name)
                self.sh.setText(str(self.rifle.sh))
                self.twist.setText(
                    f'1:{self.rifle.twist} Right' if self.rifle.is_right else f'1:{self.rifle.twist} Left'
                )
                self.caliberShort.setText(self.rifle.tile)

    def clear(self):
        self.rifle = None
        self.rifleName.setText('Empty')
        self.caliber.setText('Empty')
        self.sh.setText('Empty')
        self.twist.setText('Empty')
        self.caliberShort.setText('Empty')

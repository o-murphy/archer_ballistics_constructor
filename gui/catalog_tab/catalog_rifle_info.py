from PyQt5 import QtWidgets
from .templates import Ui_catalogRifleInfo
from dbworker import db
from dbworker.models import *


class CatalogRifleInfo(QtWidgets.QWidget, Ui_catalogRifleInfo):
    def __init__(self, id):
        super(CatalogRifleInfo, self).__init__()
        self.setupUi(self)

        sess = db.SessMake()

        self.rifle = sess.query(Rifle).get(id)

        self.rifleName.setText(self.rifle.name)
        self.caliber.setText(self.rifle.caliber.name)
        self.sh.setText(str(self.rifle.sh))
        self.twist.setText(
            f'1:{self.rifle.twist} Right' if self.rifle.is_right else f'1:{self.rifle.twist} Left'
        )
        self.caliberShort.setText(self.rifle.tile)

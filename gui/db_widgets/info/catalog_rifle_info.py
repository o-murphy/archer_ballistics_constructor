from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QWidget

from .templates import Ui_catalogRifleInfo
from dbworker import db
from dbworker.models import *


class CatalogRifleInfo(QWidget, Ui_catalogRifleInfo):
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

                _translate = QCoreApplication.translate
                twist_str = _translate(
                    'catalogRifleInfo', 'Right'
                ) if self.item.is_right else _translate('catalogRifleInfo', 'Left')

                self.twist.setText(
                    f'1:{self.item.twist} {twist_str}'
                )
                self.caliberShort.setText(self.item.tile)

    def clear(self):
        _translate = QCoreApplication.translate
        empty = _translate('catalogRifleInfo', 'Empty')

        self.item = None
        self.rifleName.setText(empty)
        self.caliber.setText(empty)
        self.sh.setText(empty)
        self.twist.setText(empty)
        self.caliberShort.setText(empty)

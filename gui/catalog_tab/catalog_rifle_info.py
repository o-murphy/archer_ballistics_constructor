from PyQt5 import QtWidgets
from .templates import Ui_catalogRifleInfo
from dbworker import db


class CatalogRifleInfo(QtWidgets.QWidget, Ui_catalogRifleInfo):
    def __init__(self, id):
        super(CatalogRifleInfo, self).__init__()
        self.setupUi(self)

        rifle = db.get_rifle(id)

        self.rifleName.setText(rifle.name)
        self.caliber.setText(rifle.caliber.name)
        self.sh.setText(str(rifle.sh))
        self.twist.setText(
            f'1:{rifle.twist} Right' if rifle.is_right else f'1:{rifle.twist} Left'
        )

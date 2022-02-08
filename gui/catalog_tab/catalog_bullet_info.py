from PyQt5 import QtWidgets
from .templates import Ui_catalogBulletInfo
from dbworker import db
from dbworker.models import Bullet


class CatalogBulletInfo(QtWidgets.QWidget, Ui_catalogBulletInfo):
    def __init__(self, id):
        super(CatalogBulletInfo, self).__init__()
        self.setupUi(self)

        bullet: Bullet = db.get_bullet(id)

        self.bulletName.setText(bullet.name)
        self.diameter.setText(str(bullet.diameter.diameter) + ' inch')
        self.lenght.setText(str(bullet.length) + ' inch')
        self.weight.setText(str(bullet.weight) + ' inch')

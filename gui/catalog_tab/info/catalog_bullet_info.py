from PyQt5 import QtWidgets
from .templates import Ui_catalogBulletInfo
from dbworker import db
from dbworker.models import *


class CatalogBulletInfo(QtWidgets.QWidget, Ui_catalogBulletInfo):
    def __init__(self):
        super(CatalogBulletInfo, self).__init__()
        self.setupUi(self)
        self.bullet = None
        self.clear()

    def set(self, id):
        if id:
            sess = db.SessMake()
            self.bullet = sess.query(Bullet).get(id)
            if self.bullet:
                self.bulletName.setText(self.bullet.name)
                self.diameter.setText(str(self.bullet.diameter.diameter) + ' inch')
                self.lenght.setText(str(self.bullet.length) + ' inch')
                self.weight.setText(str(self.bullet.weight) + ' inch')

                g1 = sess.query(DragFunc).filter_by(bullet_id=id).filter_by(drag_type='G1').first()
                g7 = sess.query(DragFunc).filter_by(bullet_id=id).filter_by(drag_type='G7').first()
                self.g1.setText(f'{g1.data:.3f}' if g1 else 'Empty')
                self.g7.setText(f'{g7.data:.3f}' if g7 else 'Empty')

    def clear(self):
        self.bullet = None
        self.bulletName.setText('Empty')
        self.diameter.setText('Empty')
        self.lenght.setText('Empty')
        self.weight.setText('Empty')
        self.g1.setText('Empty')
        self.g7.setText('Empty')

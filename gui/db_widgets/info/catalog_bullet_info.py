from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QWidget

from .templates import Ui_catalogBulletInfo
from dbworker import db
from dbworker.models import *


class CatalogBulletInfo(QWidget, Ui_catalogBulletInfo):
    def __init__(self):
        super(CatalogBulletInfo, self).__init__()
        self.setupUi(self)
        self.item = None
        self.clear()

    def set(self, id):
        if id:
            sess = db.SessMake()
            self.item = sess.query(Bullet).get(id)
            if self.item:
                self.bulletName.setText(self.item.name)
                self.diameter.setText(str(self.item.diameter.diameter) + ' inch')
                self.lenght.setText(str(self.item.length) + ' inch')
                self.weight.setText(str(self.item.weight) + ' inch')

                g1 = sess.query(DragFunc).filter_by(bullet_id=id).filter_by(drag_type='G1').first()
                g7 = sess.query(DragFunc).filter_by(bullet_id=id).filter_by(drag_type='G7').first()

                _translate = QCoreApplication.translate
                empty = _translate('catalogBulletInfo', 'Empty')

                self.g1.setText(f'{g1.data:.3f}' if g1 else empty)
                self.g7.setText(f'{g7.data:.3f}' if g7 else empty)

    def clear(self):

        _translate = QCoreApplication.translate
        empty = _translate('catalogBulletInfo', 'Empty')

        self.bulletName.setText(empty)
        self.diameter.setText(empty)
        self.lenght.setText(empty)
        self.weight.setText(empty)
        self.g1.setText(empty)
        self.g7.setText(empty)
        self.item = None

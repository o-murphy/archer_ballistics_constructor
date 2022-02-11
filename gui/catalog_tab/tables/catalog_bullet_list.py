from .templates import Ui_catalogBulletList
from .catalog_list import CatalogList

from dbworker import db
from dbworker.models import *


class CatalogBulletList(CatalogList, Ui_catalogBulletList):
    def __init__(self):
        super(CatalogBulletList, self).__init__()
        self.setupUi(self)

        self.data = []
        self.setupTable()
        self.set_data()

    def set_data(self):
        self.data = []
        sess = db.SessMake()
        bullets = sess.query(Bullet).filter_by(attrs='r').all()
        for i in bullets:
            self.data.append([i.id, i.name, i.weight, i.length, i.diameter.diameter])
        self.update_table()

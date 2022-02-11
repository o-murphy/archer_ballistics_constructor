from .templates import Ui_catalogRifleList
from .catalog_list import CatalogList

from dbworker import db
from dbworker.models import *


class CatalogRifleList(CatalogList, Ui_catalogRifleList):
    def __init__(self):
        super(CatalogRifleList, self).__init__()
        self.setupUi(self)

        self.data = []
        self.setupTable()
        self.set_data()

    def set_data(self):
        self.data = []
        sess = db.SessMake()
        rifles = sess.query(Rifle).filter_by(attrs='r').all()
        for i in rifles:
            self.data.append([i.id, i.name, i.caliber.name, i.sh, i.twist])
        self.update_table()

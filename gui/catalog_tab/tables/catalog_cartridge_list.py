from .templates import Ui_catalogCartridgeList
from .catalog_list import CatalogList

from dbworker import db
from dbworker.models import *


class CatalogCartridgeList(CatalogList, Ui_catalogCartridgeList):
    def __init__(self):
        super(CatalogCartridgeList, self).__init__()
        self.setupUi(self)

        self.data = []
        self.setupTable()
        self.set_data()

    def set_data(self):
        self.data = []
        sess = db.SessMake()
        cartridges = sess.query(Cartridge).all()
        for i in cartridges:
            self.data.append([i.id, i.name, i.caliber.name, i.bullet.name, i.mv])
        self.update_table()

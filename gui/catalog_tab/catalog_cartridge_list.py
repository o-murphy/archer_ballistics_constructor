from .templates import Ui_catalogCartridgeList
from .catalog_list import CatalogList
from .catalog_cartridge import CatalogCartridge
from dbworker import db


class CatalogCartridgeList(CatalogList, Ui_catalogCartridgeList):
    def __init__(self):
        super(CatalogCartridgeList, self).__init__()
        self.setupUi(self)
        self.editor = CatalogCartridge

        self.data = []
        self.setupTable()
        self.set_data()
        self.update_table()

    def set_data(self):
        self.data = []
        cartridges = db.get_cartridges()
        print(cartridges)
        for i in cartridges:
            self.data.append([i.id, i.name, i.mv, i.temp])

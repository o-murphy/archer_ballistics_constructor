from .templates import Ui_catalogCartridgeList
from .catalog_list import CatalogList


class CatalogCartridgeList(CatalogList, Ui_catalogCartridgeList):
    def __init__(self, model=None, attrs=None):
        super(CatalogCartridgeList, self).__init__(model, attrs)
        self.setupUi(self)

        self.setupTable()
        self.set_data()

    def parse_data(self, items):
        self.data = []
        for i in items:
            self.data.append([i.id, i.name, i.caliber.name, i.bullet.name, i.mv])


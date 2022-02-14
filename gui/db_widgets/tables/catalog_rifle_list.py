from .templates import Ui_catalogRifleList
from .catalog_list import CatalogList
from ..edit import CatalogRifle


class CatalogRifleList(CatalogList, Ui_catalogRifleList):
    def __init__(self, model=None, attrs=None):
        super(CatalogRifleList, self).__init__(model, attrs, CatalogRifle)
        self.setupUi(self)

        self.setupTable()
        self.set_data()

    def parse_data(self, items):
        self.data = []
        for i in items:
            self.data.append([i.id, i.name, i.caliber.name, i.sh, i.twist])

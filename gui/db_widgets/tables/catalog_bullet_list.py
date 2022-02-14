from .templates import Ui_catalogBulletList
from .catalog_list import CatalogList
from ..edit import CatalogBullet


class CatalogBulletList(CatalogList, Ui_catalogBulletList):
    def __init__(self, model=None, attrs=None):
        super(CatalogBulletList, self).__init__(model, attrs, CatalogBullet)
        self.setupUi(self)

        self.setupTable()
        self.set_data()

    def parse_data(self, items):
        self.data = []
        for i in items:
            self.data.append([i.id, i.name, i.weight, i.length, i.diameter.diameter])

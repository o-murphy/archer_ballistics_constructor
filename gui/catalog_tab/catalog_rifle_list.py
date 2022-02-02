from .templates import Ui_catalogRifleList
from .catalog_list import CatalogList
from .catalog_rifle import CatalogRifle


class CatalogRifleList(CatalogList, Ui_catalogRifleList):
    def __init__(self):
        super(CatalogRifleList, self).__init__()
        self.setupUi(self)
        self.editor = CatalogRifle
        self.setupTable()

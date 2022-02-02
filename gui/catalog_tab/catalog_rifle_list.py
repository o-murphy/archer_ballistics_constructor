from .templates import Ui_catalogRifleList
from .catalog_list import CatalogList


class CatalogRifleList(CatalogList, Ui_catalogRifleList):
    def __init__(self):
        super(CatalogRifleList, self).__init__()
        self.setupUi(self)
        self.setupTable()


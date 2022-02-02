from .templates import Ui_catalogCartridgeList
from .catalog_list import CatalogList
from .catalog_cartridge import CatalogCartridge


class CatalogCartridgeList(CatalogList, Ui_catalogCartridgeList):
    def __init__(self):
        super(CatalogCartridgeList, self).__init__()
        self.setupUi(self)
        self.editor = CatalogCartridge
        self.setupTable()

from ..tables import CatalogCartridgeList
from ..info import CatalogCartridgeInfo
from .tab import Tab


class CartridgesTab(Tab):
    def __init__(self):
        super(CartridgesTab, self).__init__()
        self.list = CatalogCartridgeList()
        self.info = CatalogCartridgeInfo()
        self.set()

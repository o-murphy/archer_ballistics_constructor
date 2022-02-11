from .tab import Tab
from ..tables import CatalogCartridgeList
from ..info import CatalogCartridgeInfo


class CartridgesTab(Tab):
    def __init__(self, model=None, attrs=None):
        super(CartridgesTab, self).__init__()
        self.list = CatalogCartridgeList(model, attrs)
        self.info = CatalogCartridgeInfo()
        self.set()

from .tab import Tab
from ..tables import CatalogRifleList
from ..info import CatalogRifleInfo


class RiflesTab(Tab):
    def __init__(self, model=None, attrs=None):
        super(RiflesTab, self).__init__()
        self.list = CatalogRifleList(model, attrs)
        self.info = CatalogRifleInfo()
        self.set()
        self.enable_filter()

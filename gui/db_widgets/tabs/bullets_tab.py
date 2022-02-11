from .tab import Tab
from ..tables import CatalogBulletList
from ..info import CatalogBulletInfo


class BulletsTab(Tab):
    def __init__(self, model=None, attrs=None):
        super(BulletsTab, self).__init__()
        self.list = CatalogBulletList(model, attrs)
        self.info = CatalogBulletInfo()
        self.set()

from .tab import Tab
from ..tables import CatalogBulletList
from ..info import CatalogBulletInfo


class BulletsTab(Tab):
    def __init__(self):
        super(BulletsTab, self).__init__()
        self.list = CatalogBulletList()
        self.info = CatalogBulletInfo()
        self.set()

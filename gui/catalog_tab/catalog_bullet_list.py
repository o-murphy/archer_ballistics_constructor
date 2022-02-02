from .templates import Ui_catalogBulletList
from .catalog_list import CatalogList
from .catalog_bullet import CatalogBullet


class CatalogBulletList(CatalogList, Ui_catalogBulletList):
    def __init__(self):
        super(CatalogBulletList, self).__init__()
        self.setupUi(self)
        self.editor = CatalogBullet
        self.setupTable()

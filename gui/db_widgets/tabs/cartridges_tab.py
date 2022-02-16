from .tab import Tab
from ..tables import CatalogCartridgeList
from ..info import CatalogCartridgeInfo
from ...db_widgets.tables.catalog_list import CatalogList
from dbworker import db
from dbworker.models import *


class CartridgesTab(Tab):
    def __init__(self, model=None, attrs=None):
        super(CartridgesTab, self).__init__()
        self.list = CatalogCartridgeList(model, attrs)
        self.info = CatalogCartridgeInfo()
        self.set()

    def add_template(self):
        print('add', self.info.item.name)
        if self.info.item:
            sess = db.SessMake()

            item = sess.query(self.list.model).get(self.info.item.id)

            bullet = item.bullet

            new_bullet = Bullet(bullet.name, bullet.weight, bullet.length, bullet.diameter_id, 'rw')
            sess.add(new_bullet)
            sess.commit()

            new_item = Cartridge(item.name, mv=item.mv, temp=item.temp, ts=item.ts,
                                 caliber_id=item.caliber_id, bullet_id=new_bullet.id, attrs='rw')

            sess.add(new_item)
            sess.commit()

            for table in self.window().my_tab.findChildren(CatalogList):
                table.set_data()

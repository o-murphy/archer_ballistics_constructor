from .tab import Tab
from ..tables import CatalogBulletList
from ..info import CatalogBulletInfo
from ...db_widgets.tables.catalog_list import CatalogList
from dbworker import db
from dbworker.models import *


class BulletsTab(Tab):
    def __init__(self, model=None, attrs=None):
        super(BulletsTab, self).__init__()
        self.list = CatalogBulletList(model, attrs)
        self.info = CatalogBulletInfo()
        self.set()

    def add_template(self):
        if self.info.item:
            sess = db.SessMake()

            item = sess.query(self.list.model).get(self.info.item.id)

            drags = item.drag_func

            db.make_transient(item)
            new_item = Bullet(name=item.name, weight=item.weight, length=item.length,
                              diameter_id=item.diameter_id, attrs='rw')
            sess.add(new_item)
            sess.commit()

            for d in drags:
                sess.add(DragFunc(
                    d.drag_type, d.data, d.comment, new_item.id, 'rw'
                ))
            sess.commit()

            for table in self.window().my_tab.findChildren(CatalogList):
                table.set_data()

from .catalog_list import CatalogList
from ..edit import CatalogBullet


class CatalogBulletList(CatalogList):
    def __init__(self, model=None, attrs=None):
        super(CatalogBulletList, self).__init__(model, attrs, CatalogBullet)

        self.set_data()
        self.table_model.setHorizontalHeaderLabels(['id', 'Name', 'Weight', 'Length', 'Diameter'])
        self.gridLayout.addWidget(self.tableView)
        self.set_header()

    def parse_data(self, items):
        self.data = []
        for i in items:
            self.data.append([i.id, i.name, i.weight, i.length, i.diameter.diameter])

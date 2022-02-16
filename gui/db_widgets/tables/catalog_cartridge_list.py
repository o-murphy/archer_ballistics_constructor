from .catalog_list import CatalogList
from ..edit import CatalogCartridge


class CatalogCartridgeList(CatalogList):
    def __init__(self, model=None, attrs=None):
        super(CatalogCartridgeList, self).__init__(model, attrs, CatalogCartridge)

        self.set_data()
        self.table_model.setHorizontalHeaderLabels(['id', 'Name', 'Caliber', 'Bullet', 'Weight', 'Velocity'])
        self.gridLayout.addWidget(self.tableView)
        self.set_header()

    def parse_data(self, items):
        self.data = []
        for i in items:
            self.data.append([i.id, i.name, i.caliber.name, i.bullet.name, i.bullet.weight, i.mv])


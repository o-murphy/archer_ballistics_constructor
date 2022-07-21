from PyQt5.QtCore import QCoreApplication

from .catalog_list import CatalogList
from ..edit import CatalogCartridge


class CatalogCartridgeList(CatalogList):
    def __init__(self, model=None, attrs=None):
        super(CatalogCartridgeList, self).__init__(model, attrs, CatalogCartridge)

        self.labels = []
        self.set_data()
        self.retranslateUi(self)
        self.table_model.setHorizontalHeaderLabels(self.labels)
        self.gridLayout.addWidget(self.tableView)
        self.set_header()

    def parse_data(self, items):
        self.data = []
        for i in items:
            self.data.append([i.id, i.name, i.caliber.name, i.bullet.name, i.bullet.weight, i.mv])

    def retranslateUi(self, roTable):
        super(CatalogList, self).retranslateUi(roTable)
        _translate = QCoreApplication.translate
        self.labels = [
             _translate('roTable', 'id'),
             _translate('roTable', 'Name'),
             _translate('roTable', 'Caliber'),
             _translate('roTable', 'Bullet'),
             _translate('roTable', 'Weight'),
             _translate('roTable', 'Velocity'),
        ]

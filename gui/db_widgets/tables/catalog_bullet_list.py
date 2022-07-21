from PyQt5.QtCore import QCoreApplication

from .catalog_list import CatalogList
from ..edit import CatalogBullet


class CatalogBulletList(CatalogList):
    def __init__(self, model=None, attrs=None):
        super(CatalogBulletList, self).__init__(model, attrs, CatalogBullet)

        self.labels = []
        self.set_data()
        self.retranslateUi(self)
        self.table_model.setHorizontalHeaderLabels(self.labels)
        self.gridLayout.addWidget(self.tableView)
        self.retranslateUi(self)
        self.set_header()

    def parse_data(self, items):
        self.data = []
        for i in items:
            self.data.append([i.id, i.name, i.weight, i.length, i.diameter.diameter])

    def retranslateUi(self, roTable):
        super(CatalogList, self).retranslateUi(roTable)
        _translate = QCoreApplication.translate
        self.labels = [
            _translate('roTable', 'id'),
            _translate('roTable', 'Name'),
            _translate('roTable', 'Weight'),
            _translate('roTable', 'Length'),
            _translate('roTable', 'Diameter')
        ]

from PyQt5.QtCore import QCoreApplication, QSortFilterProxyModel, Qt

from .catalog_list import CatalogList
from ..edit import CatalogRifle


class CatalogRifleList(CatalogList):
    def __init__(self, model=None, attrs=None):
        super(CatalogRifleList, self).__init__(model, attrs, CatalogRifle)

        self.labels = []
        self.set_data()
        self.retranslateUi(self)
        self.table_model.setHorizontalHeaderLabels(self.labels)
        self.proxy_filter = self.set_proxy_filter
        self.gridLayout.addWidget(self.tableView)
        self.retranslateUi(self)
        self.set_header()

    def parse_data(self, items):
        self.data = []
        for i in items:
            self.data.append([i.id, i.name, i.caliber.name, i.sh, i.twist, i.caliber.diameter.diameter])

    def set_proxy_filter(self):
        # set proxy filter
        self.proxy_model1 = QSortFilterProxyModel()
        self.proxy_model1.setFilterKeyColumn(1)  # Search all columns.
        self.proxy_model1.setSourceModel(self.table_model)
        self.proxy_model1.sort(0, Qt.AscendingOrder)

        self.proxy_model2 = QSortFilterProxyModel()
        self.proxy_model2.setFilterKeyColumn(5)
        self.proxy_model2.setSourceModel(self.proxy_model1)
        self.proxy_model2.sort(0, Qt.AscendingOrder)

        self.tableView.setModel(self.proxy_model2)

        self.tableView.horizontalHeader().setSectionHidden(5, True)

        # self.search_name = QtWidgets.QLineEdit()
        # self.search_name.textChanged.connect(self.proxy_model1.setFilterFixedString)
        #
        # self.gridLayout.addWidget(self.search_name)
        #
        # self.search_caliber = QtWidgets.QLineEdit()
        # self.search_caliber.textChanged.connect(self.proxy_model2.setFilterFixedString)
        #
        # self.gridLayout.addWidget(self.search_caliber)

    def retranslateUi(self, roTable):
        super(CatalogList, self).retranslateUi(roTable)
        _translate = QCoreApplication.translate
        self.labels = [
             _translate('roTable', 'id'),
             _translate('roTable', 'Name'),
             _translate('roTable', 'Caliber'),
             _translate('roTable', 'Height'),
             _translate('roTable', 'Twist'),
             _translate('roTable', 'Diameter')
        ]

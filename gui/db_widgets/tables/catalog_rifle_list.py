from PyQt5 import QtCore, QtWidgets
from .catalog_list import CatalogList
from ..edit import CatalogRifle


class CatalogRifleList(CatalogList):
    def __init__(self, model=None, attrs=None):
        super(CatalogRifleList, self).__init__(model, attrs, CatalogRifle)

        self.set_data()
        self.proxy_filter = self.set_proxy_filter
        self.set_data()
        self.table_model.setHorizontalHeaderLabels(['id', 'Name', 'Caliber', 'Height', 'Twist'])
        self.gridLayout.addWidget(self.tableView)
        self.set_header()

    def parse_data(self, items):
        self.data = []
        for i in items:
            self.data.append([i.id, i.name, i.caliber.name, i.sh, i.twist, i.caliber.diameter.diameter])

    def set_proxy_filter(self):
        # set proxy filter
        self.proxy_model1 = QtCore.QSortFilterProxyModel()
        self.proxy_model1.setFilterKeyColumn(1)  # Search all columns.
        self.proxy_model1.setSourceModel(self.table_model)
        self.proxy_model1.sort(0, QtCore.Qt.AscendingOrder)

        self.proxy_model2 = QtCore.QSortFilterProxyModel()
        self.proxy_model2.setFilterKeyColumn(5)
        self.proxy_model2.setSourceModel(self.proxy_model1)
        self.proxy_model2.sort(0, QtCore.Qt.AscendingOrder)

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

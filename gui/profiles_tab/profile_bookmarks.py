from PyQt5 import QtWidgets, QtCore
from gui.db_widgets.tables.catalog_rifle_list import CatalogRifleList
from gui.db_widgets.tables.catalog_cartridge_list import CatalogCartridgeList
from dbworker.models import *


class BookMarks(QtWidgets.QDialog):
    def __init__(self, parent=None, page=0, cal=None):
        super(BookMarks, self).__init__(parent)

        self.resize(600, 400)
        self.gridLayout = QtWidgets.QGridLayout()
        self.setLayout(self.gridLayout)

        self.page = page
        self.selected = None
        self.cal = cal
        self.cart = None

        if self.page == 0:
            self.table = CatalogRifleList(Rifle, 'rw')
        else:

            self.table = CatalogCartridgeList(Cartridge, 'rw')
            self.proxy_model = QtCore.QSortFilterProxyModel()
            self.proxy_model.setFilterKeyColumn(2)  # Search all columns.
            self.proxy_model.setSourceModel(self.table.table_model)
            self.proxy_model.sort(0, QtCore.Qt.AscendingOrder)
            self.proxy_model.setFilterFixedString(self.cal)
            self.table.tableView.setModel(self.proxy_model)

        self.table.tableView.setCurrentIndex(
            self.table.tableView.model().index(0, 0)
        )

        self.next = QtWidgets.QPushButton(self)
        self.cancel = QtWidgets.QPushButton(self)
        self.next.setText('Next')
        self.cancel.setText('Cancel')

        self.gridLayout.addWidget(self.table)
        self.gridLayout.addWidget(self.next)
        self.gridLayout.addWidget(self.cancel)

        self.next.clicked.connect(self.next_bm)
        self.cancel.clicked.connect(self.reject)

    def next_bm(self):
        row = self.table.tableView.currentIndex().row()
        if row != -1:
            idx = self.table.tableView.model().index(row, 0)
            self.selected = self.table.tableView.model().itemData(idx)[0]
            if self.page == 0:
                idx = self.table.tableView.model().index(row, 2)
                self.cal = self.table.tableView.model().itemData(idx)[0]
            self.accept()

    def exec_(self) -> int:
        if self.table.tableView.model().rowCount() == 0:
            mbox = QtWidgets.QMessageBox()
            mbox.setText('Rifle templates not found' if self.page == 0 else 'Cartridge templates not found')
            mbox.exec_()

            self.reject()
            return 0
        return super().exec_()

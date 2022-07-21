from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtWidgets import QDialog
from gui.db_widgets.tables.catalog_rifle_list import CatalogRifleList
from gui.db_widgets.tables.catalog_cartridge_list import CatalogCartridgeList
from dbworker.models import *
from .templates import Ui_bookmarksDialog


class BookMarks(QDialog, Ui_bookmarksDialog):
    def __init__(self, parent=None, page=0, cal=None):
        super(BookMarks, self).__init__(parent)


        self.page = page
        self.selected = None
        self.cal = cal
        self.cart = None

        self.setupUi(self)


        if self.page == 0:
            self.table = CatalogRifleList(Rifle, 'rw')
        else:

            self.table = CatalogCartridgeList(Cartridge, 'rw')
            self.proxy_model = QSortFilterProxyModel()
            self.proxy_model.setFilterKeyColumn(2)  # Search all columns.
            self.proxy_model.setSourceModel(self.table.table_model)
            self.proxy_model.sort(0, Qt.AscendingOrder)
            self.proxy_model.setFilterFixedString(self.cal)
            self.table.tableView.setModel(self.proxy_model)

        self.table.tableView.setCurrentIndex(
            self.table.tableView.model().index(0, 0)
        )

        self.gridLayout.addWidget(self.table, 0, 0, 1, 2)

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
            self.retranslateUi(self)
            self.mbox.exec_()

            self.reject()
            return 0
        return super().exec_()

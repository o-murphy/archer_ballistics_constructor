from PyQt5 import QtWidgets
from .templates import Ui_catalogSelector
from .tabs import RiflesTab, CartridgesTab, BulletsTab


class CatalogSelector(QtWidgets.QWidget, Ui_catalogSelector):
    def __init__(self):
        super(CatalogSelector, self).__init__()
        self.setupUi(self)

        self.rifles = RiflesTab()
        self.bullets = BulletsTab()
        self.cartridges = CartridgesTab()

        self.tabWidget.addTab(self.rifles, 'Rifles', )
        self.tabWidget.addTab(self.bullets, 'Bullets', )
        self.tabWidget.addTab(self.cartridges, 'Cartridges', )

        self.rifles.table.clicked.connect(lambda index: self.set_info(index.row(), self.rifles.info))
        self.rifles.table.currentCellChanged.connect(lambda row: self.set_info(row, self.rifles.info))

        self.cartridges.table.clicked.connect(lambda index: self.set_info(index.row(), self.cartridges.info))
        self.cartridges.table.currentCellChanged.connect(lambda row: self.set_info(row, self.cartridges.info))

        self.bullets.table.clicked.connect(lambda index: self.set_info(index.row(), self.bullets.info))
        self.bullets.table.currentCellChanged.connect(lambda row: self.set_info(row, self.bullets.info))

    def set_info(self, row, info: QtWidgets.QWidget):
        if row == -1:
            info.clear()
        else:
            item = self.sender().item(row, 0)
            if item:
                info.set(item.text())

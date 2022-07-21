from PyQt5.QtWidgets import QWidget

from .templates import Ui_catalogSelector
from ..db_widgets.tabs import RiflesTab, CartridgesTab, BulletsTab
from dbworker.models import *
from ..db_widgets.contexts import CatalogMenu


class CatalogSelector(QWidget, Ui_catalogSelector):
    def __init__(self):
        super(CatalogSelector, self).__init__()
        self.setupUi(self)

        self.rifles = RiflesTab(Rifle, 'r')
        self.bullets = BulletsTab(Bullet, 'r')
        self.cartridges = CartridgesTab(Cartridge, 'r')

        self.rifles.list.set_context_menu(CatalogMenu())
        self.bullets.list.set_context_menu(CatalogMenu())
        self.cartridges.list.set_context_menu(CatalogMenu())

        self.tabWidget.addTab(self.rifles, 'Rifles', )
        self.tabWidget.addTab(self.bullets, 'Bullets', )
        self.tabWidget.addTab(self.cartridges, 'Cartridges', )

        self.rifles.table.selectionModel().selectionChanged.connect(
            lambda sel, desel: self.select(sel, desel, self.rifles.info)
        )

        self.bullets.table.selectionModel().selectionChanged.connect(
            lambda sel, desel: self.select(sel, desel, self.bullets.info)
        )

        self.cartridges.table.selectionModel().selectionChanged.connect(
            lambda sel, desel: self.select(sel, desel, self.cartridges.info)
        )

    def select(self, select, deselect, info: QWidget):
        if select:
            indexes = select.first().indexes()
            if indexes:
                index = indexes[0]
                item = self.sender().model().itemData(index)
                if item:
                    info.set(item[0])

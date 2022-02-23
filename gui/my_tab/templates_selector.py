from PyQt5 import QtWidgets, QtCore
from .templates import Ui_myTabSelector
from ..db_widgets.tabs import RiflesTab, CartridgesTab, BulletsTab
from dbworker.models import *
from ..db_widgets.contexts import TemplatesMenu


class MyTabSelector(QtWidgets.QWidget, Ui_myTabSelector):
    def __init__(self):
        super(MyTabSelector, self).__init__()
        self.setupUi(self)

        self.rifles = RiflesTab(Rifle, 'rw')
        self.bullets = BulletsTab(Bullet, 'rw')
        self.cartridges = CartridgesTab(Cartridge, 'rw')

        self.rifles.list.set_context_menu(TemplatesMenu())
        self.bullets.list.set_context_menu(TemplatesMenu())
        self.cartridges.list.set_context_menu(TemplatesMenu())

        self.rifles.list.tableView.doubleClicked.connect(self.rifles.list.edit_item)
        self.bullets.list.tableView.doubleClicked.connect(self.bullets.list.edit_item)
        self.cartridges.list.tableView.doubleClicked.connect(self.cartridges.list.edit_item)

        self.tabWidget.addTab(self.rifles, 'Rifles')
        self.tabWidget.addTab(self.bullets, 'Bullets')
        self.tabWidget.addTab(self.cartridges, 'Cartridges')

        self.rifles.table.selectionModel().selectionChanged.connect(
            lambda sel, desel: self.select(sel, desel, self.rifles.info)
        )

        self.bullets.table.selectionModel().selectionChanged.connect(
            lambda sel, desel: self.select(sel, desel, self.bullets.info)
        )

        self.cartridges.table.selectionModel().selectionChanged.connect(
            lambda sel, desel: self.select(sel, desel, self.cartridges.info)
        )

        self.retranslateUi(self)

    def select(self, select, deselect, info: QtWidgets.QWidget):
        if select:
            indexes = select.first().indexes()
            if indexes:
                index = indexes[0]
                item = self.sender().model().itemData(index)
                if item:
                    info.set(item[0])

    def retranslateUi(self, catalogSelector):
        _translate = QtCore.QCoreApplication.translate

        self.tabWidget.setTabText(0, _translate('MyTabSelector', 'Rifles'))
        self.tabWidget.setTabText(1, _translate('MyTabSelector', 'Bullets'))
        self.tabWidget.setTabText(2, _translate('MyTabSelector', 'Cartridges'))

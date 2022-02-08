from PyQt5 import QtWidgets, QtCore
from .templates import Ui_catalogTab
from .catalog_selector import CatalogSelector
from .catalog_info import CatalogInfo

from gui.stylesheet import load_qss


class CatalogTab(QtWidgets.QWidget, Ui_catalogTab):
    def __init__(self):
        super(CatalogTab, self).__init__()
        self.setupUi(self)

        self.setStyleSheet(load_qss('qss/application.qss') +
                           """
                                QTabBar::tab {
                                    height: 100px;
                                    width: 30px;
                                    font-size: 15px;
                                    border-bottom-left-radius: 8px;
                                    border-top-left-radius: 8px;
                                    border-bottom-right-radius: 0px;
                                    border-top-right-radius: 0px;
                                }
                                QGroupBox {
                                    color: rgb(255, 255, 255);
                                    border: 1px solid rgb(78, 78, 78);
                                    padding-top: 0px;
                                }
                                QTableCornerButton::section {
                                    background: rgb(51, 51, 51);
                                }
                                """
                           )

        self.selector = CatalogSelector()
        self.info = CatalogInfo()
        self.gridLayout.setAlignment(QtCore.Qt.AlignLeft)
        self.gridLayout.addWidget(self.selector, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.info, 0, 1, 1, 1)

        self.selector.rifle_list.tableWidget.currentCellChanged.connect(self.show_rifle_info)
        self.selector.cartridge_list.tableWidget.currentCellChanged.connect(self.show_cartridge_info)
        self.selector.bullet_list.tableWidget.currentCellChanged.connect(self.show_bullet_info)

        self.selector.tabWidget.currentChanged.connect(self.show_templates)

        self.selector.rifle_list.tableWidget.setCurrentCell(0, 0)
        self.selector.cartridge_list.tableWidget.setCurrentCell(0, 0)
        self.selector.bullet_list.tableWidget.setCurrentCell(0, 0)

    def show_rifle_info(self, row, col, prow, pcol):
        if row >= 0:
            r = self.selector.rifle_list.tableWidget.item(row, 0).text()
            self.info.show_rifle(r)

    def show_cartridge_info(self, row, col, prow, pcol):
        if row >= 0:
            r = self.selector.cartridge_list.tableWidget.item(row, 0).text()
            self.info.show_cartridge(r)

    def show_bullet_info(self, row, col, prow, pcol):
        if row >= 0:
            r = self.selector.bullet_list.tableWidget.item(row, 0).text()
            self.info.show_bullet(r)

    def show_templates(self, index):
        print('tab:', index)

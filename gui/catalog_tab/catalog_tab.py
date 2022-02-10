from PyQt5 import QtWidgets, QtCore
from .templates import Ui_catalogTab
from .catalog_selector import CatalogSelector
from .info import CatalogInfo
from .toolbar import InfoTools

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
                                QTableCornerButton::section {
                                    background: rgb(51, 51, 51);
                                }
                                QTableWidget {
                                    background-image: url(:/icons/res/drawable-hdpi-v4/addbtn_menu21b.png);
                                    background-repeat: no-repeat; 
                                    background-position: center;
                                }
                                """
                           )

        self.selector = CatalogSelector()
        self.info = CatalogInfo()
        self.gridLayout.setAlignment(QtCore.Qt.AlignLeft)
        self.gridLayout.addWidget(self.selector, 0, 0, 2, 1)
        self.gridLayout.addWidget(self.info, 0, 1, 1, 1)

        self.info_tools = InfoTools()
        self.gridLayout.addWidget(self.info_tools, 1, 1, 1, 1)

        # self.selector.rifle_list.tableWidget.currentCellChanged.connect(self.show_rifle_info)
        # self.selector.cartridge_list.tableWidget.currentCellChanged.connect(self.show_cartridge_info)

        self.selector.rifle_list.tableWidget.setCurrentCell(0, 0)
        self.selector.cartridge_list.tableWidget.setCurrentCell(0, 0)
        self.selector.bullet_list.tableWidget.setCurrentCell(0, 0)

    # def show_rifle_info(self, row, col, prow, pcol):
    #     if row >= 0:
    #         item = self.selector.rifle_list.tableWidget.item(
    #             self.selector.rifle_list.viewport_row(), 0
    #         )
    #         id = int(item.text()) if item else None
    #         if id:
    #             self.info.show_rifle(id)
    #     else:
    #         self.info.remove_rifle()
    #
    # def show_cartridge_info(self, row, col, prow, pcol):
    #     if row >= 0:
    #         item = self.selector.cartridge_list.tableWidget.item(
    #             self.selector.cartridge_list.viewport_row(), 0
    #         )
    #         id = int(item.text()) if item else None
    #         if id:
    #             self.info.show_cartridge(id)
    #     else:
    #         self.info.remove_cartridge()

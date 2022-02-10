from PyQt5 import QtWidgets, QtCore
from .templates import Ui_catalogSelector
from .tables import CatalogRifleList, CatalogCartridgeList, CatalogBulletList
from .info import CatalogBulletInfo, CatalogCartridgeInfo, CatalogRifleInfo


class CatalogSelector(QtWidgets.QWidget, Ui_catalogSelector):
    def __init__(self):
        super(CatalogSelector, self).__init__()
        self.setupUi(self)

        # rifles
        self.rifleLayout = QtWidgets.QGridLayout()
        self.rifleLayout.setContentsMargins(0, 0, 0, 0)
        self.rifleLayout.setAlignment(QtCore.Qt.AlignTop)
        self.rifles.setLayout(self.rifleLayout)

        self.rifle_list = CatalogRifleList()
        self.rifle_info = CatalogRifleInfo()
        self.rifles.layout().addWidget(self.rifle_list, 0, 0, 1, 1)
        self.rifles.layout().addWidget(self.rifle_info, 0, 1, 1, 1)

        self.rifle_list.tableWidget.clicked.connect(lambda index: self.set_info(index.row(), self.rifle_info))
        self.rifle_list.tableWidget.currentCellChanged.connect(lambda row: self.set_info(row, self.rifle_info))

        # cartridges
        self.cartridgeLayout = QtWidgets.QGridLayout()
        self.cartridgeLayout.setContentsMargins(0, 0, 0, 0)
        self.cartridges.setLayout(self.cartridgeLayout)

        self.cartridge_list = CatalogCartridgeList()
        self.cartridge_info = CatalogCartridgeInfo()
        self.cartridges.layout().addWidget(self.cartridge_list, 0, 0, 1, 1)
        self.cartridges.layout().addWidget(self.cartridge_info, 0, 1, 1, 1)

        self.cartridge_list.tableWidget.clicked.connect(lambda index: self.set_info(index.row(), self.cartridge_info))
        self.cartridge_list.tableWidget.currentCellChanged.connect(lambda row: self.set_info(row, self.cartridge_info))

        # bullets
        self.bulletLayout = QtWidgets.QGridLayout()
        self.bulletLayout.setContentsMargins(0, 0, 0, 0)
        self.bullets.setLayout(self.bulletLayout)

        self.bullet_list = CatalogBulletList()
        self.bullet_info = CatalogBulletInfo()
        self.bullets.layout().addWidget(self.bullet_list, 0, 0, 1, 1)
        self.bullets.layout().addWidget(self.bullet_info, 0, 1, 1, 1)

        self.bullet_list.tableWidget.clicked.connect(lambda index: self.set_info(index.row(), self.bullet_info))
        self.bullet_list.tableWidget.currentCellChanged.connect(lambda row: self.set_info(row, self.bullet_info))

    def set_info(self, row, info: QtWidgets.QWidget):
        if row == -1:
            info.clear()
        else:
            item = self.sender().item(row, 0)
            if item:
                info.set(item.text())

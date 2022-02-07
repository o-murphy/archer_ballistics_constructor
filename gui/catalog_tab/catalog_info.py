from PyQt5 import QtWidgets, QtCore
from .templates import Ui_catalogInfo
from .catalog_rifle_info import CatalogRifleInfo
from .catalog_cartridge_info import CatalogCartridgeInfo
from .catalog_bullet_info import CatalogBulletInfo

from dbworker.base import Base, engine
Base.metadata.create_all(engine)


class CatalogInfo(QtWidgets.QWidget, Ui_catalogInfo):
    def __init__(self):
        super(CatalogInfo, self).__init__()
        self.setupUi(self)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(self.gridLayout)

    def show_rifle(self, r):
        if self.findChild(CatalogRifleInfo):
            self.gridLayout.removeWidget(self.findChild(CatalogRifleInfo))
        self.gridLayout.addWidget(CatalogRifleInfo(r), 0, 0, 1, 1)

    def show_cartridge(self, r):
        if self.findChild(CatalogRifleInfo):
            self.gridLayout.removeWidget(self.findChild(CatalogCartridgeInfo))
        self.gridLayout.addWidget(CatalogCartridgeInfo(r), 1, 0, 1, 1)

    def show_bullet(self, r):
        if self.findChild(CatalogRifleInfo):
            self.gridLayout.removeWidget(self.findChild(CatalogBulletInfo))
        self.gridLayout.addWidget(CatalogBulletInfo(r), 2, 0, 1, 1)

from PyQt5 import QtWidgets, QtCore
from .templates import Ui_catalogInfo
from .catalog_rifle_info import CatalogRifleInfo
from .catalog_cartridge_info import CatalogCartridgeInfo
from .catalog_bullet_info import CatalogBulletInfo
from .catalog_info_tools import InfoTools

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

        self.info_tools = InfoTools()

        self.gridLayout.addWidget(self.info_tools, 2, 0, 1, 1)

    def show_rifle(self, r):
        self.remove_rifle()
        self.gridLayout.addWidget(CatalogRifleInfo(r), 0, 0, 1, 1)

    def remove_rifle(self):
        if self.findChild(CatalogRifleInfo):
            self.gridLayout.removeWidget(self.findChild(CatalogRifleInfo))

    def show_cartridge(self, r):
        self.remove_cartridge()
        self.gridLayout.addWidget(CatalogCartridgeInfo(r), 1, 0, 1, 1)

    def remove_cartridge(self):
        if self.findChild(CatalogRifleInfo):
            self.gridLayout.removeWidget(self.findChild(CatalogCartridgeInfo))

    def show_bullet(self, r):
        self.remove_bullet()
        self.gridLayout.addWidget(CatalogBulletInfo(r), 2, 0, 1, 1)

    def remove_bullet(self):
        if self.findChild(CatalogRifleInfo):
            self.gridLayout.removeWidget(self.findChild(CatalogBulletInfo))


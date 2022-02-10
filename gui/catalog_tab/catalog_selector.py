from PyQt5 import QtWidgets
from .templates import Ui_catalogSelector
from .tables import CatalogRifleList, CatalogCartridgeList, CatalogBulletList


class CatalogSelector(QtWidgets.QWidget, Ui_catalogSelector):
    def __init__(self):
        super(CatalogSelector, self).__init__()
        self.setupUi(self)

        self.rifle_list = CatalogRifleList()
        self.rifleLayout = QtWidgets.QGridLayout()
        self.rifleLayout.setContentsMargins(0, 0, 0, 0)
        self.rifles.setLayout(self.rifleLayout)
        self.rifles.layout().addWidget(self.rifle_list)

        self.cartridge_list = CatalogCartridgeList()
        self.cartridgeLayout = QtWidgets.QGridLayout()
        self.cartridgeLayout.setContentsMargins(0, 0, 0, 0)
        self.cartridges.setLayout(self.cartridgeLayout)
        self.cartridges.layout().addWidget(self.cartridge_list)

        self.bullet_list = CatalogBulletList()
        self.bulletLayout = QtWidgets.QGridLayout()
        self.bulletLayout.setContentsMargins(0, 0, 0, 0)
        self.bullets.setLayout(self.bulletLayout)
        self.bullets.layout().addWidget(self.bullet_list)

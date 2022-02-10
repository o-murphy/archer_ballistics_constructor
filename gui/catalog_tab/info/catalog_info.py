from PyQt5 import QtWidgets, QtCore
from .templates import Ui_catalogInfo
from .catalog_rifle_info import CatalogRifleInfo
from .catalog_cartridge_info import CatalogCartridgeInfo
from dbworker import db
from dbworker.models import *

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
        self.remove_rifle()
        self.gridLayout.addWidget(CatalogRifleInfo(r), 0, 0, 1, 1)

    def remove_rifle(self):
        if self.findChild(CatalogRifleInfo):
            self.gridLayout.removeWidget(self.findChild(CatalogRifleInfo))

    def show_cartridge(self, r):
        self.remove_cartridge()
        self.gridLayout.addWidget(CatalogCartridgeInfo(r), 1, 0, 1, 1)

    def remove_cartridge(self):
        if self.findChild(CatalogCartridgeInfo):
            self.gridLayout.removeWidget(self.findChild(CatalogCartridgeInfo))

    def create_template(self):
        r = self.findChild(CatalogRifleInfo)
        c = self.findChild(CatalogCartridgeInfo)
        rifle = r.rifle if r else None
        cartridge = c.cartridge if c else None
        if rifle and cartridge:

            name = rifle.name + ' / ' + cartridge.name
            drag_func_id = c.drag_func.currentData()

            sess = db.SessMake()
            t = Template(name, rifle.id, cartridge.id, drag_func_id)
            sess.add(t)
            sess.commit()

            return rifle, cartridge



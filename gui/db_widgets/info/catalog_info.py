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
        self.item = None
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(self.gridLayout)

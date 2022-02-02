from PyQt5 import QtWidgets
from .templates import Ui_catalogSelector
from .catalog_rifle_list import CatalogRifleList


class CatalogSelector(QtWidgets.QWidget, Ui_catalogSelector):
    def __init__(self):
        super(CatalogSelector, self).__init__()
        self.setupUi(self)

        self.rifle_list = CatalogRifleList()
        self.rifleLayout = QtWidgets.QGridLayout()
        self.rifleLayout.setContentsMargins(0, 0, 0, 0)
        self.rifles.setLayout(self.rifleLayout)
        self.rifles.layout().addWidget(self.rifle_list)

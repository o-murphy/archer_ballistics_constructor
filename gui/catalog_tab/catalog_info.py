from PyQt5 import QtWidgets, QtCore
from .templates import Ui_catalogInfo
from .catalog_rifle_info import CatalogRifleInfo


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
        label = QtWidgets.QLabel('added cartridge' + r)
        label.setObjectName('cartridge')

        prev_label = self.findChild(QtWidgets.QLabel, name='cartridge')
        if prev_label:
            self.gridLayout.removeWidget(prev_label)
        self.gridLayout.addWidget(label, 1, 0, 1, 1)

    def show_bullet(self, r):
        label = QtWidgets.QLabel('added bullet' + r)
        label.setObjectName('bullet')

        prev_label = self.findChild(QtWidgets.QLabel, name='bullet')
        if prev_label:
            self.gridLayout.removeWidget(prev_label)
        self.gridLayout.addWidget(label, 2, 0, 1, 1)

from PyQt5 import QtWidgets, QtCore
from .templates import Ui_profileCurrent
from modules import BConverter
from ..bc_table import BCTable
from .profile_item_contents import Bullet, Rifle, Cartridge, Conditions
from .add_btn import AddBtn


class ProfileCurrent(QtWidgets.QWidget, Ui_profileCurrent):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.convert = BConverter()
        self.bc_table = BCTable()

        self.tab_6.layout().setAlignment(QtCore.Qt.AlignTop)
        self.tab_7.layout().setAlignment(QtCore.Qt.AlignTop)

    def set_current(self, cur):
        [r.hide() for r in self.findChildren(Rifle)]
        [b.hide() for b in self.findChildren(Bullet)]
        [c.hide() for c in self.findChildren(Cartridge)]
        [cd.hide() for cd in self.findChildren(Conditions)]

        if not isinstance(cur, AddBtn):
            self.tab_6.layout().addWidget(cur.rifle, 0, 0, 1, 1)
            self.tab_6.layout().addWidget(cur.cartridge, 1, 0, 1, 1)
            self.tab_6.layout().addWidget(cur.bullet, 2, 0, 1, 1)

            self.tab_7.layout().addWidget(cur.conditions, 0, 0, 1, 1)

            cur.rifle.show()
            cur.bullet.show()
            cur.cartridge.show()
            cur.conditions.show()

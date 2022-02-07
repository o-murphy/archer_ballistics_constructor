from PyQt5 import QtWidgets
from .templates import Ui_catalogBulletInfo


class CatalogBulletInfo(QtWidgets.QWidget, Ui_catalogBulletInfo):
    def __init__(self, name):
        super(CatalogBulletInfo, self).__init__()
        self.setupUi(self)
        self.bulletName.setText(name)

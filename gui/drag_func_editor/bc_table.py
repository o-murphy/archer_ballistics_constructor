from PyQt5 import QtWidgets
from .templates import Ui_BCTable
from modules.converter import BConverter

rnd = BConverter.auto_rnd


class BCTable(Ui_BCTable):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.verticalHeader().setVisible(False)
        self.verticalHeader().setDefaultSectionSize(26)
        self.verticalHeader().setMinimumSectionSize(26)
        self.verticalHeader().setMinimumHeight(26)
        self.verticalHeader().setMaximumHeight(26)
        self.setMaximumHeight(156)

    def set(self):
        for i in range(5):
            self.insertRow(i)
            self.setItem(i, 0, QtWidgets.QTableWidgetItem())

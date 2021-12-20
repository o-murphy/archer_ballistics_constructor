from PyQt5 import QtWidgets
from .templates import Ui_BCTable
from modules.converter import BConverter

rnd = BConverter.auto_rnd


class BCTable(Ui_BCTable):
    def __init__(self):
        super().__init__()
        self.setupUi()

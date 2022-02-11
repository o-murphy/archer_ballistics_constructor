from PyQt5 import QtWidgets
from .templates import Ui_catalogInfoTools


class InfoTools(QtWidgets.QWidget, Ui_catalogInfoTools):
    def __init__(self):
        super(InfoTools, self).__init__()
        self.setupUi(self)

from PyQt5.QtWidgets import QWidget

from .templates import Ui_catalogInfoTools


class InfoTools(QWidget, Ui_catalogInfoTools):
    def __init__(self):
        super(InfoTools, self).__init__()
        self.setupUi(self)

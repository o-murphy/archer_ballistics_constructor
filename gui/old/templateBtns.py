from PyQt5 import QtWidgets
from .templates import Ui_templateBtns


class TemplateBtns(QtWidgets.QWidget, Ui_templateBtns):
    def __init__(self, ):
        super(TemplateBtns, self).__init__()
        self.setupUi(self)

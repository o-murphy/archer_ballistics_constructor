from PyQt5 import QtWidgets, QtGui
from .templates import Ui_tWidget


class AddBtn(QtWidgets.QWidget, Ui_tWidget):
    def __init__(self):
        super(AddBtn, self).__init__()
        self.setupUi(self)

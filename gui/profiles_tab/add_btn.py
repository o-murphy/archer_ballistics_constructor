from PyQt5.QtWidgets import QWidget
from .templates import Ui_tWidget


class AddBtn(QWidget, Ui_tWidget):
    def __init__(self):
        super(AddBtn, self).__init__()
        self.setupUi(self)

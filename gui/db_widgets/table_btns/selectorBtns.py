from PyQt5 import QtWidgets
from .templates import Ui_selectorBtns


class SelectBtn(QtWidgets.QWidget, Ui_selectorBtns):
    def __init__(self, model=None, editor=None):
        super(SelectBtn, self).__init__()
        self.setupUi(self)
        self.model = model
        self.editor = editor

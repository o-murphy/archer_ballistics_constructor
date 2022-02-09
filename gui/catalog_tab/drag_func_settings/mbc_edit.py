from PyQt5 import QtWidgets, QtCore
from .templates import Ui_mbcEdit
from gui.bc_table import BCTable


class MBCEdit(QtWidgets.QDialog, Ui_mbcEdit):
    def __init__(self):
        super(MBCEdit, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.bc_table = BCTable()

        self.gridLayout.addWidget(self.bc_table)
        self.gridLayout.addWidget(self.buttonBox)

    def get(self) -> tuple[list, str]:
        return self.bc_table.get_data(), self.lineEdit.text()

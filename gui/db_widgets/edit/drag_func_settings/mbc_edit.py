from PyQt5 import QtWidgets, QtCore
from .templates import Ui_mbcEdit
from gui.bc_table import BCTable
from gui.delegates import BallisticCoefficient, MuzzleVelocity


class MBCEdit(QtWidgets.QDialog, Ui_mbcEdit):
    def __init__(self):
        super(MBCEdit, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # self.bc_table = BCTable()
        self.bc_table = QtWidgets.QTableWidget()
        self.bc_table.setRowCount(5)
        self.bc_table.setColumnCount(2)
        self.ballistics_coeff = BallisticCoefficient()
        self.muzzle_velocity = MuzzleVelocity()
        self.bc_table.setItemDelegateForColumn(0, self.ballistics_coeff)
        self.bc_table.setItemDelegateForColumn(1, self.muzzle_velocity)

        self.gridLayout.addWidget(self.bc_table)
        self.gridLayout.addWidget(self.buttonBox)

    def get(self) -> tuple[list, str]:
        return self.bc_table.get_data(), self.lineEdit.text()

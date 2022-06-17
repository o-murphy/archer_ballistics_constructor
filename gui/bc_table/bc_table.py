from PyQt5 import QtWidgets, QtCore
from modules.converter import BConverter
from gui.delegates import BallisticCoefficient, MuzzleVelocity


rnd = BConverter.auto_rnd


class BCTable(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("bcTable")

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.gridLayout)
        self.setMinimumSize(QtCore.QSize(140, 0))
        self.setMaximumSize(QtCore.QSize(140, 16777215))

        self.bc_table = QtWidgets.QTableWidget()

        self.bc_table.verticalHeader().setVisible(False)
        self.bc_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.bc_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.bc_table.setRowCount(5)
        self.bc_table.setColumnCount(2)

        self.bc_table.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem('BC'))
        self.bc_table.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem('V'))
        self.bc_table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.bc_table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        self.ballistics_coefficient = BallisticCoefficient(self.parent())
        self.muzzle_velocity = MuzzleVelocity(self.parent())
        self.bc_table.setItemDelegateForColumn(1, self.ballistics_coefficient)
        self.bc_table.setItemDelegateForColumn(0, self.muzzle_velocity)

        self.gridLayout.addWidget(self.bc_table)

        self.set()

    def set(self):
        for i in range(self.bc_table.rowCount()):
            self.bc_table.setItem(i, 0, QtWidgets.QTableWidgetItem())
            self.bc_table.setItem(i, 1, QtWidgets.QTableWidgetItem())
            self.bc_table.item(i, 0).setData(QtCore.Qt.EditRole, 0)
            self.bc_table.item(i, 1).setData(QtCore.Qt.EditRole, 0)

    def get_data(self):
        ret = [
            (self.bc_table.item(r, 0).data(QtCore.Qt.EditRole), self.bc_table.item(r, 1).data(QtCore.Qt.EditRole))
            for r in range(self.bc_table.rowCount())
        ]
        return ret

    def set_data(self, data: tuple[tuple]):
        for i, (bc, v) in enumerate(data):
            self.bc_table.item(i, 0).setData(QtCore.Qt.EditRole, bc)
            self.bc_table.item(i, 1).setData(QtCore.Qt.EditRole, v)

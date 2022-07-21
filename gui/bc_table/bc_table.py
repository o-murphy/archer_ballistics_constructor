from PyQt5.QtCore import QSize, Qt, QCoreApplication
from PyQt5.QtWidgets import QWidget, QTableWidget, QGridLayout, QHeaderView, QTableWidgetItem

from gui.delegates import BallisticCoefficient, MuzzleVelocity


from gui.app_settings import AppSettings
from py_ballisticcalc.lib.bmath import Velocity, VelocityMPS


class BCTable(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("bcTable")

        self.gridLayout = QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.gridLayout)
        self.setMinimumSize(QSize(140, 0))
        self.setMaximumSize(QSize(140, 16777215))

        self.bc_table = QTableWidget()

        self.bc_table.verticalHeader().setVisible(False)
        self.bc_table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.bc_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.bc_table.setRowCount(5)
        self.bc_table.setColumnCount(2)

        # self.bc_table.setHorizontalHeaderItem(0, QTableWidgetItem('BC'))
        # self.bc_table.setHorizontalHeaderItem(1, QTableWidgetItem('V'))
        self.bc_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.bc_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

        self.ballistics_coefficient = BallisticCoefficient(self.parent())
        self.muzzle_velocity = MuzzleVelocity(self.parent())
        self.bc_table.setItemDelegateForColumn(0, self.ballistics_coefficient)
        self.bc_table.setItemDelegateForColumn(1, self.muzzle_velocity)

        self.gridLayout.addWidget(self.bc_table)

        self.units = None
        self.setUnits()

        self.retranslateUi(self)

        self.bc_table.setRowCount(5)
        self.set()

    def setUnits(self):
        self.units = AppSettings()

    def set(self):
        for i in range(self.bc_table.rowCount()):
            self.bc_table.setItem(i, 0, QTableWidgetItem())
            self.bc_table.setItem(i, 1, QTableWidgetItem())
            self.bc_table.item(i, 0).setData(Qt.EditRole, 0)
            self.bc_table.item(i, 1).setData(Qt.EditRole, 0)

    def get_data(self):
        ret = []
        for r in range(self.bc_table.rowCount()):
            bc = self.bc_table.item(r, 0).data(Qt.EditRole)
            v = self.bc_table.item(r, 1).data(Qt.EditRole)
            v = Velocity(v, self.units.vUnits.currentData()).get_in(VelocityMPS)
            if bc > 0 and v > 0:
                ret.append((bc, v))

        return ret

    def set_data(self, data: [tuple[tuple], list]):
        for i, (bc, v) in enumerate(data):
            v = Velocity(v, VelocityMPS).get_in(self.units.vUnits.currentData())
            self.bc_table.item(i, 0).setData(Qt.EditRole, bc)
            self.bc_table.item(i, 1).setData(Qt.EditRole, round(v, 1))

    def retranslateUi(self, BCTable):
        _translate = QCoreApplication.translate
        BCTable.setWindowTitle(_translate("BCTable", "Form"))

        bc_col_text = _translate("BCTable", "BC")
        v_col_text = _translate("BCTable", "V")

        BCTable.bc_table.setHorizontalHeaderItem(0, QTableWidgetItem(
            f'{bc_col_text} ({BCTable.units.vUnits.currentText().strip()})'
        ))

        BCTable.bc_table.setHorizontalHeaderItem(1, QTableWidgetItem(
            f'{v_col_text} ({BCTable.units.vUnits.currentText().strip()})'
        ))

from PyQt5 import QtWidgets, QtCore
from .templates import Ui_mbcEdit
from gui.delegates import BallisticCoefficient, MuzzleVelocity
from typing import Optional
from gui.stylesheet import load_qss



class MBCEdit(QtWidgets.QDialog, Ui_mbcEdit):
    def __init__(self, data=None, comment=None):
        super(MBCEdit, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.setStyleSheet(load_qss('qss/dialog.qss') + """
            QDialog {border: 1px solid rgb(76, 76, 76)}
        """)

        self.bc_table = QtWidgets.QTableWidget()

        self.bc_table.setRowCount(5)
        self.bc_table.setColumnCount(2)

        self.bc_table.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem('BC'))
        self.bc_table.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem('V'))
        self.bc_table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.bc_table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        self.ballistics_coefficient = BallisticCoefficient()
        self.muzzle_velocity = MuzzleVelocity()
        self.bc_table.setItemDelegateForColumn(0, self.ballistics_coefficient)
        self.bc_table.setItemDelegateForColumn(1, self.muzzle_velocity)

        empty_data = [(0, 0) for i in range(5)]

        if data:
            for i, (bc, v) in enumerate(data):
                empty_data[i] = (bc, v)

        self.set_data(empty_data)

        if comment:
            self.lineEdit.setText(comment)

        self.gridLayout.addWidget(self.bc_table)
        self.gridLayout.addWidget(self.buttonBox)

    def set_data(self, data):
        data.sort(reverse=True)
        self.bc_table.setRowCount(len(data))
        for i, (bc, v) in enumerate(data):
            self.bc_table.setItem(i, 0, QtWidgets.QTableWidgetItem())
            self.bc_table.setItem(i, 1, QtWidgets.QTableWidgetItem())
            self.bc_table.item(i, 0).setData(QtCore.Qt.EditRole, bc)
            self.bc_table.item(i, 1).setData(QtCore.Qt.EditRole, v)

    def get_data(self) -> Optional[list[tuple]]:
        data = []
        for i in range(self.bc_table.rowCount()):
            bc = self.bc_table.item(i, 0).data(QtCore.Qt.EditRole)
            v = self.bc_table.item(i, 1).data(QtCore.Qt.EditRole)
            if v > 0 and bc == 0:
                message_box = QtWidgets.QMessageBox()
                message_box.setText('BC cannot be 0, if velocity > 0')
                message_box.exec_()
                return
            elif v != 0 and bc != 0:
                data.append((bc, v))

        if len(data) == 0:
            message_box = QtWidgets.QMessageBox()
            message_box.setText("BC-table can't be empty")
            message_box.exec_()
            return

        data.sort(reverse=True)
        return data if data else None

    def accept(self) -> None:
        data = self.get_data()
        if not data:
            return
        else:
            super().accept()

    def get(self) -> tuple[list, str]:
        return self.get_data(), self.lineEdit.text()

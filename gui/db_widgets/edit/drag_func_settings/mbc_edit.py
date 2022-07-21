from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox

from .templates import Ui_mbcEdit
from gui.delegates import BallisticCoefficient, MuzzleVelocity
from typing import Optional
from gui.stylesheet import load_qss

from gui.app_settings import AppSettings
from py_ballisticcalc.lib.bmath import Velocity, VelocityMPS


class MBCEdit(QDialog, Ui_mbcEdit):
    def __init__(self, data=None, comment=None):
        super(MBCEdit, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.setStyleSheet(load_qss('qss/dialog.qss') + """
            QDialog {border: 1px solid rgb(76, 76, 76)}
        """)

        self.bc_table = QTableWidget()

        self.bc_table.setRowCount(5)
        self.bc_table.setColumnCount(2)

        self.bc_table.setHorizontalHeaderItem(0, QTableWidgetItem('BC'))
        self.bc_table.setHorizontalHeaderItem(1, QTableWidgetItem('V'))
        self.bc_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.bc_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

        self.ballistics_coefficient = BallisticCoefficient()
        self.muzzle_velocity = MuzzleVelocity()
        self.bc_table.setItemDelegateForColumn(0, self.ballistics_coefficient)
        self.bc_table.setItemDelegateForColumn(1, self.muzzle_velocity)

        self.message_box = QMessageBox()

        self.units = None
        self.setUnits()

        self.bc_table.setHorizontalHeaderItem(1, QTableWidgetItem(
            f'V ({self.units.vUnits.currentText().strip()})'
        ))

        empty_data = [(0, 0) for i in range(5)]

        if data:
            for i, (bc, v) in enumerate(data):
                empty_data[i] = (bc, v)

        self.set_data(empty_data)

        if comment:
            self.lineEdit.setText(comment)

        self.gridLayout.addWidget(self.bc_table)
        self.gridLayout.addWidget(self.buttonBox)

    def setUnits(self):
        self.units = AppSettings()

    def set_data(self, data):
        data.sort(reverse=True)
        self.bc_table.setRowCount(len(data))
        for i, (bc, v) in enumerate(data):
            v = Velocity(v, VelocityMPS).get_in(self.units.vUnits.currentData())
            self.bc_table.setItem(i, 0, QTableWidgetItem())
            self.bc_table.setItem(i, 1, QTableWidgetItem())
            self.bc_table.item(i, 0).setData(Qt.EditRole, bc)
            self.bc_table.item(i, 1).setData(Qt.EditRole, round(v, 1))

    def get_data(self) -> Optional[list[tuple]]:
        data = []
        for i in range(self.bc_table.rowCount()):
            bc = self.bc_table.item(i, 0).data(Qt.EditRole)
            v = self.bc_table.item(i, 1).data(Qt.EditRole)
            v = Velocity(v, self.units.vUnits.currentData()).get_in(VelocityMPS)
            if v > 0 and bc == 0:
                self.message_box.exec_()
                return
            elif v != 0 and bc != 0:
                data.append((bc, v))

        if len(data) == 0:
            self.retranslateUi(self)
            self.message_box.exec_()
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

    def retranslateUi(self, mbcEdit):
        super(MBCEdit, self).retranslateUi(mbcEdit)
        _translate = QCoreApplication.translate
        if hasattr(mbcEdit, 'message_box'):
            self.message_box.setText(_translate('mbcEdit', "BC-table can't be empty"))

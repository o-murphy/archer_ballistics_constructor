from PyQt5 import QtWidgets, QtCore
from .templates import Ui_dropTable
from gui.delegates import Distance, Drop, DropCorrection


class DropTable(QtWidgets.QWidget, Ui_dropTable):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.distance_delegate = Distance(parent)
        self.drop_delegate = Drop()
        self.correction_delegate = DropCorrection()
        self.tableWidget.setItemDelegateForColumn(0, self.distance_delegate)
        self.tableWidget.setItemDelegateForColumn(1, self.drop_delegate)
        self.tableWidget.setItemDelegateForColumn(2, self.correction_delegate)

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

    def set(self):
        for i in range(5):
            self.insert_row()

    def insert_row(self):
        r_count = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(r_count + 1)

        self.tableWidget.setItem(r_count, 0, QtWidgets.QTableWidgetItem())
        self.tableWidget.setItem(r_count, 1, QtWidgets.QTableWidgetItem())
        self.tableWidget.setItem(r_count, 2, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(r_count, 0).setData(QtCore.Qt.EditRole, (r_count + 1) * 100)

    def remove_row(self):
        if self.tableWidget.currentItem():
            row = self.tableWidget.currentRow()
            self.tableWidget.removeRow(row)
            if self.tableWidget.item(row, 1):
                self.tableWidget.item(row, 1).setSelected(True)
            elif self.tableWidget.item(row - 1, 1):
                self.tableWidget.item(row - 1, 1).setSelected(True)

    def get_current_distance(self):
        item = self.tableWidget.item(self.tableWidget.currentRow(), 0)
        if item:
            return item.data(QtCore.Qt.EditRole)

    def get_current_drop(self):
        item = self.tableWidget.item(self.tableWidget.currentRow(), 1)
        if item:
            return item.data(QtCore.Qt.EditRole)

    def set_item_data(self, r, c, v):
        item = self.tableWidget.item(r, c)
        if item:
            item.setData(QtCore.Qt.EditRole, v)

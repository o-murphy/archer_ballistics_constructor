from PyQt5 import QtWidgets
from .templates import Ui_profilesTable
from .profile_item import ProfileItem


class ProfilesTable(QtWidgets.QWidget, Ui_profilesTable):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def add_row(self):
        row_count = self.tableWidget.rowCount()
        if row_count < 20:
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            self.tableWidget.setItem(row_count, 0, QtWidgets.QTableWidgetItem())
            self.tableWidget.setCellWidget(row_count, 0, ProfileItem())

    def remove_row(self):
        self.tableWidget.removeRow(self.tableWidget.currentRow())

    def remove_all(self):
        for i in range(self.tableWidget.rowCount(), -1, -1):
            self.tableWidget.removeRow(i)
        # self.current_item = None

    def move_up(self):
        row = self.tableWidget.currentRow()
        column = self.tableWidget.currentColumn();
        if row > 0:
            w = self.tableWidget.cellWidget(row, column)
            self.tableWidget.insertRow(row-1)
            for i in range(self.tableWidget.columnCount()):
               self.tableWidget.setItem(row-1, i, self.tableWidget.takeItem(row+1, i))
               self.tableWidget.setCellWidget(row-1, i, w)
               self.tableWidget.setCurrentCell(row-1, column)
            self.tableWidget.removeRow(row+1)

    def move_down(self):
        row = self.tableWidget.currentRow()
        column = self.tableWidget.currentColumn();
        if row < self.tableWidget.rowCount() - 1:
            w = self.tableWidget.cellWidget(row, column)
            self.tableWidget.insertRow(row + 2)
            for i in range(self.tableWidget.columnCount()):
                self.tableWidget.setItem(row + 2, i, self.tableWidget.takeItem(row, i))
                self.tableWidget.setCellWidget(row + 2, i, w)
                self.tableWidget.setCurrentCell(row + 2, column)
            self.tableWidget.removeRow(row)

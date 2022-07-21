from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QWidget, QHeaderView, QTableWidgetItem
from .templates import Ui_dropTable
from gui.delegates import Distance as DistanceDelegate
from gui.delegates import Drop, DropCorrection


from py_ballisticcalc.lib.bmath.unit import Distance, DistanceMeter
from gui.app_settings import AppSettings


class DropTable(QWidget, Ui_dropTable):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.distance_delegate = DistanceDelegate(parent)
        self.drop_delegate = Drop()
        self.correction_delegate = DropCorrection()
        self.tableWidget.setItemDelegateForColumn(0, self.distance_delegate)
        self.tableWidget.setItemDelegateForColumn(1, self.drop_delegate)
        self.tableWidget.setItemDelegateForColumn(2, self.correction_delegate)

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)

        self.units = None
        self.setUnits()

        self.retranslateUi(self)

    def setUnits(self):
        self.units = AppSettings()

    def set(self):
        for i in range(21):
            self.insert_row()

    def insert_row(self):
        r_count = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(r_count + 1)

        self.tableWidget.setItem(r_count, 0, QTableWidgetItem())
        self.tableWidget.setItem(r_count, 1, QTableWidgetItem())
        self.tableWidget.setItem(r_count, 2, QTableWidgetItem())
        self.tableWidget.item(r_count, 0).setData(Qt.EditRole, r_count * 100)

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
            return item.data(Qt.EditRole)

    def get_current_drop(self):
        item = self.tableWidget.item(self.tableWidget.currentRow(), 1)
        if item:
            return item.data(Qt.EditRole)

    def set_item_data(self, r, c, v):
        item = self.tableWidget.item(r, c)
        if item:
            item.setData(Qt.EditRole, v)

    def retranslateUi(self, dropTable):
        _translate = QCoreApplication.translate

        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem(
            # f'Dist. ({self.units.distUnits.currentText().strip()})'
            f'{_translate("dropTable", "Dist.")} (m)'
        ))

        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem(
            # f'Drop. ({self.units.dropUnits.currentText().strip()})'
            f'{_translate("dropTable", "Drop.")} (cm)'
        ))
        super(DropTable, self).retranslateUi(dropTable)

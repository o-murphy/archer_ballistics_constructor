from PyQt5 import QtWidgets
from .templates import Ui_DropTable


class NoWheelDoubleSpinBox(QtWidgets.QDoubleSpinBox):
    def wheelEvent(self, event):
        event.ignore()


class NoWheelSpinBox(QtWidgets.QSpinBox):
    def wheelEvent(self, event):
        event.ignore()


class DropTable(Ui_DropTable):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.current_row = None

        self.clicked.connect(lambda item: self.set_item(item))

    def set(self):
        for i in range(0, 2):
            self.insert_row()

    def insert_row(self):
        row_index = self.rowCount()
        self.insertRow(self.rowCount())
        dist = QtWidgets.QTableWidgetItem()
        self.setItem(row_index, 0, dist)
        sb = NoWheelSpinBox()
        sb.setMinimum(0)
        sb.setMaximum(5000)
        sb.setSingleStep(1)
        sb.setValue((row_index + 1) * 100)
        self.item(row_index, 0)
        self.setCellWidget(row_index, 0, sb)

        vz = QtWidgets.QTableWidgetItem()
        self.setItem(row_index, 1, vz)

        corr = QtWidgets.QTableWidgetItem()
        self.setItem(row_index, 2, corr)
        sb = NoWheelDoubleSpinBox()
        self.setCellWidget(row_index, 2, sb)

    def set_item(self, item):
        self.current_row = item.row()

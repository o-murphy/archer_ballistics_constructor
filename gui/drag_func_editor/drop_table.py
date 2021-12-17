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

    def set_drop_table(self):
        for i in range(0, 10):
            self.insertRow(i)
            dist = QtWidgets.QTableWidgetItem()
            self.setItem(i, 0, dist)
            sb = NoWheelSpinBox()
            sb.setMinimum(0)
            sb.setMaximum(5000)
            sb.setSingleStep(1)
            sb.setValue((i+1)*100)
            self.item(i, 0)
            self.setCellWidget(i, 0, sb)

            vz = QtWidgets.QTableWidgetItem()
            self.setItem(i, 1, vz)

            corr = QtWidgets.QTableWidgetItem()
            self.setItem(i, 2, corr)
            sb = NoWheelDoubleSpinBox()
            self.setCellWidget(i, 2, sb)

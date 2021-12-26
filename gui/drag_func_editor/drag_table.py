from PyQt5 import QtWidgets, QtCore
from .templates import Ui_DragTable
from modules.converter import BConverter

rnd = BConverter.auto_rnd


class DragTable(Ui_DragTable):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def set(self, current_data, default_data):
        for i in range(self.columnCount()):
            self.removeColumn(0)
        data = current_data if current_data else default_data
        if data:
            for k, v in enumerate(data):
                self.insertColumn(k)
                iv = QtWidgets.QTableWidgetItem()
                ivw = QtWidgets.QLineEdit()
                ivw.setEnabled(False)
                ivw.setText(str(rnd(v[0])))
                self.setItem(0, k, iv)
                self.setCellWidget(0, k, ivw)

                ii = QtWidgets.QTableWidgetItem()
                iiw = QtWidgets.QLineEdit()
                iiw.setEnabled(False)
                iiw.setText(str(rnd(v[1])))
                self.setItem(1, k, ii)
                self.setCellWidget(1, k, iiw)

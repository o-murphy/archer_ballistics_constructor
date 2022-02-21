from PyQt5 import QtWidgets, QtCore
from .templates import Ui_DragTable
from modules.converter import BConverter
from gui.delegates import Velocity, DragCoefficient


rnd = BConverter.auto_rnd


class DragTable(Ui_DragTable):
    def __init__(self):
        super().__init__()
        self.setupUI()

        self.velocity_delegates = Velocity()
        self.drag_coefficient = DragCoefficient()
        self.setItemDelegateForRow(0, self.velocity_delegates)
        self.setItemDelegateForRow(1, self.drag_coefficient)

        item = self.verticalHeaderItem(0)
        item.setText("V")
        item = self.verticalHeaderItem(1)
        item.setText("CD")

    def set(self, current_data, default_data):
        data = current_data if current_data else default_data
        if data:
            self.setColumnCount(len(data))
            for i, (v, c) in enumerate(data):
                self.setItem(0, i, QtWidgets.QTableWidgetItem())
                self.setItem(1, i, QtWidgets.QTableWidgetItem())
                self.item(0, i).setData(QtCore.Qt.EditRole, rnd(v))
                self.item(1, i).setData(QtCore.Qt.EditRole, rnd(c))

    def readonly(self):
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

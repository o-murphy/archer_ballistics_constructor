from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView

from .templates import Ui_DragTable
from gui.delegates import Velocity, DragCoefficient


class DragTable(Ui_DragTable):
    def __init__(self):
        super().__init__()
        self.setupUI()

        self.velocity_delegates = Velocity()
        self.drag_coefficient = DragCoefficient()
        self.setItemDelegateForRow(0, self.velocity_delegates)
        self.setItemDelegateForRow(1, self.drag_coefficient)

    def set(self, current_data, default_data):
        data = current_data if current_data else default_data
        data.sort()
        if data:
            self.setColumnCount(len(data))
            for i, (v, c) in enumerate(data):
                self.setItem(0, i, QTableWidgetItem())
                self.setItem(1, i, QTableWidgetItem())
                self.item(0, i).setData(Qt.EditRole, round(v, 2))
                self.item(1, i).setData(Qt.EditRole, round(c, 4))

    def readonly(self):
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionMode(QAbstractItemView.SingleSelection)

from PyQt5 import QtWidgets
from .templates import Ui_DropTable
from ..single_custom_widgets.no_wheel_sb import DSpinbox, DropSpinBox, DropRoSpinBox, DropRoSBw


class DropTable(Ui_DropTable):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.setStyleSheet(
            """
            QTableWidget::item:selected {
                background-color: rgb(255, 170, 0);
                color: black;
            }
            
            QTableView::item:hover {
                background-color: rgb(255, 170, 0);
                color: black;
            }"""
        )

    def set(self):
        for i in range(0, 5):
            self.insert_row()

    def insert_row(self):
        row_count = self.rowCount()

        self.insertRow(self.rowCount())

        self.setItem(row_count, 0, QtWidgets.QTableWidgetItem())
        sb = DSpinbox()
        sb.setValue((row_count + 1) * 100)
        self.setCellWidget(row_count, 0, sb)

        self.setItem(row_count, 1, QtWidgets.QTableWidgetItem())
        self.setCellWidget(row_count, 1, DropRoSBw())

        # self.cellWidget(row_count, 1).setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)

        self.setItem(row_count, 2, QtWidgets.QTableWidgetItem())
        self.setCellWidget(row_count, 2, DropSpinBox())
        self.setCurrentItem(self.item(row_count, 0))

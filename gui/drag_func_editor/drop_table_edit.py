from PyQt5 import QtWidgets
from .templates.drop_table_edit import Ui_dropTableEdit
from .drop_table import DropTable


class DropTableEdit(QtWidgets.QWidget, Ui_dropTableEdit):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.drop_table = DropTable()
        self.gridLayout.addWidget(self.drop_table, 0, 0, 1, 2)

        self.addRow.clicked.connect(self.add_row)
        self.removeRow.clicked.connect(self.remove_row)

    def add_row(self):
        self.drop_table.insert_row()

    def remove_row(self):
        if self.drop_table.current_row:
            self.drop_table.removeRow(self.drop_table.current_row)
            self.drop_table.current_row = None

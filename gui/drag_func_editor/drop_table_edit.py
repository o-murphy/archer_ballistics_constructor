from PyQt5.QtWidgets import QWidget
from .templates.drop_table_edit import Ui_dropTableEdit
from .drop_table import DropTable


class DropTableEdit(QWidget, Ui_dropTableEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.drop_table = DropTable(parent)
        self.gridLayout.addWidget(self.drop_table, 0, 0, 1, 2)
        self.removeRow.clicked.connect(self.remove_row)

    def add_row(self):
        self.drop_table.insert_row()

    def remove_row(self):
        self.drop_table.remove_row()

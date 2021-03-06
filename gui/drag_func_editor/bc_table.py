from .templates import Ui_BCTable
from modules.converter import BConverter
from ..single_custom_widgets.no_wheel_sb import BVSpinBox, BCSpinBox

rnd = BConverter.auto_rnd


class BCTable(Ui_BCTable):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.set()

    def set(self):
        for i in range(5):
            self.insertRow(i)
            self.setCellWidget(i, 0, BVSpinBox())
            self.setCellWidget(i, 1, BCSpinBox())
            self.cellWidget(i, 0).setValue(-1)
            self.cellWidget(i, 1).setValue(0)

    def get_data(self):
        return [[self.cellWidget(r, 0).value(), self.cellWidget(r, 1).value()]
                for r in range(self.rowCount())]

    def set_data(self, data: list[list]):
        for i, (v, bc) in enumerate(data):
            self.cellWidget(i, 0).setValue(v)
            self.cellWidget(i, 1).setValue(bc)

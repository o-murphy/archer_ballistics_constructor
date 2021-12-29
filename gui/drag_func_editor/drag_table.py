from .templates import Ui_DragTable
from ..single_custom_widgets.no_wheel_sb import DisabledDoubleSpinBox
from modules.converter import BConverter

rnd = BConverter.auto_rnd


class DragTable(Ui_DragTable):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.setStyleSheet("""
            QDoubleSpinBox:hover {
                background: rgb(255, 170, 0);
                color: black;
            }
        """)

    def set(self, current_data, default_data):
        row_count = self.columnCount()
        if len(default_data) != row_count:
            for i in range(self.columnCount()):
                self.removeColumn(0)
            if default_data:
                for i, v in enumerate(default_data):
                    self.insertColumn(i)
                    self.setCellWidget(0, i, DisabledDoubleSpinBox())
                    self.setCellWidget(1, i, DisabledDoubleSpinBox())
                    self.cellWidget(0, i).setDecimals(2)
                    self.cellWidget(1, i).setDecimals(4)

        data = current_data if current_data else default_data
        if data:
            for i, v in enumerate(data):
                self.cellWidget(0, i).setValue(v[0])
                self.cellWidget(1, i).setValue(v[1])


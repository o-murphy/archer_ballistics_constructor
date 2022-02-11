from PyQt5 import QtWidgets, QtCore
from .templates import Ui_cdfEdit
from gui.drag_func_editor.drag_table import DragTable
from modules.converter import BConverter

rnd = BConverter().auto_rnd


class CDFEdit(QtWidgets.QDialog, Ui_cdfEdit):
    def __init__(self):
        super(CDFEdit, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.cdf_table = DragTable()

        self.gridLayout.addWidget(self.cdf_table, 2, 0, 1, 5)
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 5)

        self.copyTable.clicked.connect(self.copy_table)
        self.pasteTable.clicked.connect(self.paste_table)

    def copy_table(self):
        # datasheet = '\n'.join([f'{str(rnd(v)).replace(".", ",")}\t{str(rnd(i)).replace(".", ",")}' for v, i in (
        #     self.state.current_data if self.state.current_data else self.state.default_data
        # )])
        # cb = QtWidgets.QApplication.clipboard()
        # cb.clear(mode=cb.Clipboard)
        # cb.setText(datasheet, mode=cb.Clipboard)
        pass

    def paste_table(self):
        cb = QtWidgets.QApplication.clipboard()
        lines = cb.text().split('\n')
        pairs = [i.split('\t') for i in lines if len(i.split('\t')) == 2]
        float_pairs = [[float(i.replace(',', '.')), float(j.replace(',', '.'))] for i, j in pairs]
        float_pairs.sort(reverse=False)
        self.cdf_table.setColumnCount(len(float_pairs))
        for i, (k, v) in enumerate(float_pairs):
            self.cdf_table.setItem(0, i, QtWidgets.QTableWidgetItem(str(k)))
            self.cdf_table.setItem(1, i, QtWidgets.QTableWidgetItem(str(v)))

    def get_data(self):
        data = [
            [float(self.cdf_table.item(0, i).text()), float(self.cdf_table.item(1, i).text())]
            for i in range(self.cdf_table.columnCount())
        ]
        return data

    def get(self) -> tuple[list, str]:
        return self.get_data(), self.lineEdit.text()

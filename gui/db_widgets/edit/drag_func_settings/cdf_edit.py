from PyQt5 import QtWidgets, QtCore
from .templates import Ui_cdfEdit
from gui.drag_func_editor.drag_table import DragTable
from modules.converter import BConverter
from gui.delegates import Velocity, DragCoefficient
from gui.stylesheet import load_qss
from modules.env_update import USER_RECENT
from modules.file_parse import FileParse


rnd = BConverter().auto_rnd


class CDFEdit(QtWidgets.QDialog, Ui_cdfEdit):
    def __init__(self, data=None):
        super(CDFEdit, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.setStyleSheet(load_qss('qss/dialog.qss') + """
            QDialog {border: 1px solid rgb(76, 76, 76)}
        """)

        self.cdf_table = DragTable()
        # self.velocity_delegate = Velocity()
        # self.df_delegate = DragCoefficient()
        # self.cdf_table.setItemDelegateForRow(0, self.velocity_delegate)
        # self.cdf_table.setItemDelegateForRow(1, self.df_delegate)

        self.gridLayout.addWidget(self.cdf_table, 2, 0, 1, 6)
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 6)

        self.copyTable.clicked.connect(self.copy_table)
        self.pasteTable.clicked.connect(self.paste_table)
        self.Add.clicked.connect(lambda: self.cdf_table.setColumnCount(self.cdf_table.columnCount() + 1))
        self.Remove.clicked.connect(lambda: self.cdf_table.removeColumn(self.cdf_table.currentColumn()))
        self.Clear.clicked.connect(self.clear_table)

        self.importTable.clicked.connect(self.import_table)

        if data:
            self.set_data(data)

    def clear_table(self):
        while self.cdf_table.columnCount():
            self.cdf_table.removeColumn(0)

    def copy_table(self):
        data = self.get_data()
        datasheet = []
        for (v, c) in data:
            datasheet.append(f"{str(v).replace(r'.', r',')}\t{str(c).replace(r'.', r',')}")
        datasheet = '\n'.join(datasheet)

        cb = QtWidgets.QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(datasheet, mode=cb.Clipboard)

    def paste_table(self):
        cb = QtWidgets.QApplication.clipboard()
        lines = cb.text().split('\n')
        pairs = [i.split('\t') for i in lines if len(i.split('\t')) == 2]
        float_pairs = [[float(i.replace(',', '.')), float(j.replace(',', '.'))] for i, j in pairs]
        self.set_data(float_pairs)

    def import_table(self):
        options = QtWidgets.QFileDialog.Options()
        fileName, fileFormat = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "QFileDialog.getOpenFileName()",
            USER_RECENT,
            "Drag function (*.drg;*.snr;*.ardrg)",
            options=options
        )
        if fileName:
            from modules import FileParse
            fp = FileParse()
            data, comment = fp.open_format(fileFormat, fileName)
            if data:
                self.set_data(data)
                self.lineEdit.setText(comment.replace('\n', ''))

    def export_table(self, fileName=None):
        data = self.get_data()
        if data:

            options = QtWidgets.QFileDialog.Options()
            fileName, fileFormat = QtWidgets.QFileDialog.getSaveFileName(
                self,
                "QFileDialog.getSaveFileName()",
                rf'{USER_RECENT}\{fileName}' if fileName else rf'{USER_RECENT}\recent_',
                "Drag function (*.drg;*.snr;*.ardrg)",
                options=options
            )
            if fileName:
                from modules import FileParse
                fp = FileParse()
                result = fp.save_format(fileFormat, fileName, data, fileName)

    def set_data(self, data):
        data.sort(reverse=False)
        self.cdf_table.setColumnCount(len(data))
        for i, (v, c) in enumerate(data):
            self.cdf_table.setItem(0, i, QtWidgets.QTableWidgetItem())
            self.cdf_table.setItem(1, i, QtWidgets.QTableWidgetItem())
            self.cdf_table.item(0, i).setData(QtCore.Qt.EditRole, v)
            self.cdf_table.item(1, i).setData(QtCore.Qt.EditRole, c)

    def get_data(self) -> list[tuple]:
        data = []
        for i in range(self.cdf_table.columnCount()):
            v_item = self.cdf_table.item(0, i)
            c_item = self.cdf_table.item(1, i)
            if v_item and c_item:
                v = v_item.data(QtCore.Qt.EditRole)
                c = c_item.data(QtCore.Qt.EditRole)

                data.append((v, c))
        data.sort(reverse=False)
        return data

    def get(self) -> tuple[list, str]:
        return self.get_data(), self.lineEdit.text()

from PyQt5 import QtWidgets, QtGui
from .templates import Ui_catalogBullet
from modules import BConverter

from .drag_func_settings import BCEdit
from .drag_func_settings import MBCEdit
from .drag_func_settings import CDFEdit

# from gui.bc_table import BCTable
from ..single_custom_widgets.no_wheel_sb import BCSpinBox
from dbworker.models import *
from .selectorBtns import SelectBtn


# class BC(BCSpinBox):
#     def __init__(self):
#         super(BC, self).__init__()
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
#         self.setSizePolicy(sizePolicy)
#         self.setMaximumHeight(30)
#         self.setStyleSheet("")
#         self.setPrefix('BC: ')


class DFCombo(QtWidgets.QComboBox):
    def __init__(self):
        super(DFCombo, self).__init__()
        self.addItems(['G1', 'G7', 'G1 Multi-BC', 'G7 Multi-BC', 'Custom'])


class DFDelBtn(QtWidgets.QPushButton):
    def __init__(self):
        super(DFDelBtn, self).__init__()
        # self.setText('X')
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons19/res/drawable-xhdpi-v4/deletebtn21a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon1)


class CatalogBullet(QtWidgets.QWidget, Ui_catalogBullet):
    """
    TODO:
        add multi_bc
        add drag_func_editor
    """
    def __init__(self, data: Bullet = None, drags: list = None):
        super(CatalogBullet, self).__init__()
        self.setupUi(self)
        self.convert = BConverter()

        self.n = None
        self.w = None
        self.ln = None
        self.d = None
        self.df = []

        if data:
            self.bulletName.setText(data.name)
            self.weight.setValue(data.weight)
            self.length.setValue(data.length)
            self.diameter.setValue(data.diameter.diameter)

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)

        print(drags)
        if drags:
            if len(drags) > 0:
                for df in drags:
                    self.add(df)
            else:
                self.add()
        else:
            self.add()

        self.weightQuantity.setItemData(0, self.convert.gr_to_g)
        self.weightQuantity.setItemData(1, self.convert.g_to_gr)
        self.lengthQuantity.setItemData(0, self.convert.inch_to_mm)
        self.lengthQuantity.setItemData(1, self.convert.mm_to_inch)
        self.diameterQuantity.setItemData(0, self.convert.inch_to_mm)
        self.diameterQuantity.setItemData(1, self.convert.mm_to_inch)

        self.weightSwitch.clicked.connect(lambda: self.convert_values(self.weight, self.weightQuantity))
        self.lengthSwitch.clicked.connect(lambda: self.convert_values(self.length, self.lengthQuantity))
        self.diameterSwitch.clicked.connect(lambda: self.convert_values(self.diameter, self.diameterQuantity))
        self.Add.clicked.connect(self.add)
        self.tableWidget.clicked.connect(self.set_cell_data)

    @staticmethod
    def get_cln(spin: QtWidgets.QSpinBox, combo: QtWidgets.QComboBox):
        return spin.value() if combo.currentIndex() == 0 else combo.currentData()(spin.value())

    @staticmethod
    def convert_values(spin: QtWidgets.QSpinBox or QtWidgets.QDoubleSpinBox, combo: QtWidgets.QComboBox):
        cur_idx = combo.currentIndex()
        spin.setValue(combo.itemData(cur_idx)(spin.value()))
        combo.setCurrentIndex(1 if cur_idx == 0 else 0)
        if spin.objectName() == 'weight':
            spin.setSingleStep(0.01 if cur_idx == 0 else 0.1)

    def viewport_row(self):
        cursor = self.tableWidget.viewport().mapFromGlobal(QtGui.QCursor().pos())
        return self.tableWidget.indexAt(cursor).row()

    def add(self, df=None):
        idx = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(idx+1)
        self.tableWidget.setCellWidget(idx, 0, DFCombo())
        self.tableWidget.setItem(idx, 1, QtWidgets.QTableWidgetItem(''))

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/res/drawable-hdpi-v4/settingsbtn_menu21a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.tableWidget.item(idx, 1).setIcon(icon1)

        self.tableWidget.item(idx, 1).state = None
        self.tableWidget.setItem(idx, 2, QtWidgets.QTableWidgetItem(''))
        self.tableWidget.setCellWidget(idx, 3, DFDelBtn())
        self.tableWidget.cellWidget(idx, 3).clicked.connect(self.del_df)

        if df:
            print(df)
            self.tableWidget.cellWidget(idx, 0).setCurrentText(df.drag_type)
            data, comment = df.data, df.comment
            if df.drag_type in ['G1', 'G7']:
                bc = str(df.data)
            elif df.drag_type.endswith('Multi-BC'):
                bc = 'Points: ' + str(len([(bc, v) for (bc, v) in df.data if bc > 0 and v >= 0])) \
                    if isinstance(df.data, list) else 'Points: 0'
            else:
                bc = 'DFL: ' + str(len(df.data)) if isinstance(df.data, list) else 'DFL: 0'
            self.tableWidget.item(idx, 1).setText(bc)
            self.tableWidget.item(idx, 1).state = data
            self.tableWidget.item(idx, 2).setText(comment)

        self.tableWidget.cellWidget(idx, 0).currentIndexChanged.connect(lambda *args: print(args))

    def del_df(self):
        if self.tableWidget.rowCount() > 1:
            self.tableWidget.removeRow(self.viewport_row())

    def set_cell_data(self, index):
        row = index.row() if not isinstance(index, int) else index
        drag_type = self.tableWidget.cellWidget(row, 0).currentText()
        if drag_type in ['G1', 'G7']:
            bc_edit = BCEdit()
            if bc_edit.exec_():
                data = bc_edit.get()
                self.tableWidget.item(row, 1).setText(str(data))
                self.tableWidget.item(row, 1).state = data if data else 0

        elif drag_type.endswith('Multi-BC'):
            mbc_edit = MBCEdit()
            if mbc_edit.exec_():
                data, comment = mbc_edit.get()
                count = [(bc, v) for (bc, v) in data if bc > 0 and v >= 0]

                self.tableWidget.item(row, 1).setText('Points: ' + str(len(count)))
                self.tableWidget.item(row, 1).state = data if data else []
                self.tableWidget.item(row, 2).setText(comment)
        else:
            cdf_edit = CDFEdit()
            if cdf_edit.exec_():
                data, comment = cdf_edit.get()
                self.tableWidget.item(row, 1).setText('DFL: ' + str(len(data)))
                self.tableWidget.item(row, 1).state = data if data else []
                self.tableWidget.item(row, 2).setText(comment)

    def get(self):
        for i in range(self.tableWidget.rowCount()):
            row = [
                self.tableWidget.cellWidget(i, 0).currentText(),
                self.tableWidget.item(i, 1).state,
                self.tableWidget.item(i, 2).text()
            ]
            self.df.append(row)
            print(self.df)

        self.n = self.bulletName.text()
        self.w = self.get_cln(self.weight, self.weightQuantity)
        self.ln = self.get_cln(self.length, self.lengthQuantity)
        self.d = self.get_cln(self.diameter, self.diameterQuantity)
        return self

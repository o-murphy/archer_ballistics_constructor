from PyQt5 import QtWidgets, QtGui, QtCore
from .templates import Ui_catalogBullet
from modules import BConverter

from .drag_func_settings import BCEdit
from .drag_func_settings import MBCEdit
from .drag_func_settings import CDFEdit
from .df_type_dlg import DFTypeDlg

from dbworker.models import *
from dbworker import db


class DFDelBtn(QtWidgets.QPushButton):
    def __init__(self):
        super(DFDelBtn, self).__init__()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons19/res/drawable-xhdpi-v4/deletebtn21a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon1)


class CatalogBullet(QtWidgets.QWidget, Ui_catalogBullet):
    """
    TODO:
        add multi_bc
        add drag_func_editor
    """
    def __init__(self, data: Bullet = None, call=None):
        super(CatalogBullet, self).__init__()
        self.setupUi(self)
        self.title = 'Bullet Edit'

        self.convert = BConverter()
        self.data = data
        self.call = call

        self.n = None
        self.w = None
        self.ln = None
        self.d = None
        self.df = []
        self.drags = None

        if self.data:
            self.bulletName.setText(self.data.name)
            self.weight.setValue(self.data.weight)
            self.length.setValue(self.data.length)
            self.diameter.setValue(self.data.diameter.diameter)

            sess = db.SessMake()
            self.drags = self.data.drag_func

        if self.drags:
            if len(self.drags) > 0:
                for df in self.drags:
                    self.add(df)
            else:
                self.add()
        else:
            self.add()

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)

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

    def add_row(self):
        idx = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(idx+1)
        self.tableWidget.setItem(idx, 0, QtWidgets.QTableWidgetItem(''))
        self.tableWidget.setItem(idx, 1, QtWidgets.QTableWidgetItem(''))
        self.tableWidget.setItem(idx, 2, QtWidgets.QTableWidgetItem(''))
        self.tableWidget.setCellWidget(idx, 3, DFDelBtn())
        self.tableWidget.cellWidget(idx, 3).clicked.connect(self.del_df)

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/res/drawable-hdpi-v4/settingsbtn_menu21a.png"),
                        QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.tableWidget.item(idx, 1).setIcon(icon1)
        return idx

    def add(self, df=None):
        if not df:
            df_type = DFTypeDlg()

            if df_type.exec_():

                idx = self.add_row()

                drag_type = df_type.combo.currentText()
                self.tableWidget.item(idx, 0).setText(drag_type)
                self.tableWidget.item(idx, 1).state = None
                if drag_type in ['G1', 'G7']:
                    self.tableWidget.item(idx, 1).setText(f'{0.1:.3f}')
                elif drag_type.endswith('Multi-BC'):
                    self.tableWidget.item(idx, 1).setText('Points: 0')
                else:
                    self.tableWidget.item(idx, 1).setText('DFL: 0')

                if not self.set_cell_data(idx):
                    self.tableWidget.removeRow(idx)
        else:
            idx = self.add_row()
            data, comment = df.data, df.comment
            if df.drag_type in ['G1', 'G7']:
                bc = f'{data:.3f}' if data else f'{0.1:.3f}'
            elif df.drag_type.endswith('Multi-BC'):
                bc = 'Points: ' + str(len([(bc, v) for (bc, v) in df.data if bc > 0 and v >= 0])) \
                    if isinstance(df.data, list) else 'Points: 0'
            else:
                bc = 'DFL: ' + str(len(df.data)) if isinstance(df.data, list) else 'DFL: 0'

            self.tableWidget.item(idx, 0).setText(df.drag_type)
            self.tableWidget.item(idx, 1).setText(bc)
            self.tableWidget.item(idx, 1).state = data
            self.tableWidget.item(idx, 2).setText(comment)

    def del_df(self):
        if self.tableWidget.rowCount() > 1:
            self.tableWidget.removeRow(self.viewport_row())

    def set_cell_data(self, index):

        if isinstance(index, int):
            row = index
        elif isinstance(index, QtCore.QModelIndex) and (index.column() == 1):
            row = index.row()
        else:
            return

        if row is not None and (row >= 0):

            drag_type = self.tableWidget.item(row, 0).text()
            state = self.tableWidget.item(row, 1).state
            data = state if state else None
            if drag_type in ['G1', 'G7']:
                bc_edit = BCEdit(data)
                if bc_edit.exec_():
                    data = bc_edit.get()
                    self.tableWidget.item(row, 1).setText(str(data))
                    self.tableWidget.item(row, 1).state = data if data else 0

            elif drag_type.endswith('Multi-BC'):
                mbc_edit = MBCEdit(data)
                if mbc_edit.exec_():
                    data, comment = mbc_edit.get()
                    count = [(bc, v) for (bc, v) in data if bc > 0 and v >= 0]

                    self.tableWidget.item(row, 1).setText('Points: ' + str(len(count)))
                    self.tableWidget.item(row, 1).state = data if data else []
                    self.tableWidget.item(row, 2).setText(comment)
            else:
                cdf_edit = CDFEdit(data)
                if cdf_edit.exec_():
                    data, comment = cdf_edit.get()
                    self.tableWidget.item(row, 1).setText('DFL: ' + str(len(data)))
                    self.tableWidget.item(row, 1).state = data if data else []
                    self.tableWidget.item(row, 2).setText(comment)
            return data

    def get(self):
        sess = db.SessMake()

        dimeter = self.get_cln(self.diameter, self.diameterQuantity)
        diam = sess.query(Diameter).filter_by(diameter=dimeter).first()
        if not diam:
            diam = Diameter(dimeter)
            sess.add(diam)
            sess.commit()
        for i in range(self.tableWidget.rowCount()):
            row = [
                self.tableWidget.item(i, 0).text(),
                self.tableWidget.item(i, 1).state,
                self.tableWidget.item(i, 2).text()
            ]
            self.df.append(row)

        if self.call == 'edit':
            bullet = sess.query(Bullet).get(self.data.id)
            bullet.name = self.bulletName.text()
            bullet.weight = self.weight.value()
            bullet.length = self.length.value()
            bullet.diameter_id = diam.id

            dfs = sess.query(DragFunc).filter_by(bullet_id=bullet.id).all()
            print(dfs)
            for df in dfs:
                sess.delete(df)

            for df in self.df:
                sess.add(DragFunc(*df, bullet_id=bullet.id, attrs='rw'))
        else:

            new_bullet = Bullet(self.bulletName.text(), self.weight.value(), self.length.value(), diam.id, 'rw')
            sess.add(new_bullet)
            sess.commit()
            for df in self.df:
                sess.add(DragFunc(*df, bullet_id=new_bullet.id, attrs='rw'))
        sess.commit()


    def valid(self):
        return True

    def invalid(self):
        return False
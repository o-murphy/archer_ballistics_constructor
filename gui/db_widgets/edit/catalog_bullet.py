from PyQt5.QtCore import QModelIndex, QCoreApplication
from PyQt5.QtGui import QIcon, QPixmap, QCursor
from PyQt5.QtWidgets import QPushButton, QWidget, QHeaderView, QTableWidgetItem

from .templates import Ui_catalogBullet

from .drag_func_settings import BCEdit
from .drag_func_settings import MBCEdit
from .drag_func_settings import CDFEdit
from .df_type_dlg import DFTypeDlg

from dbworker.models import *
from dbworker import db


class DFDelBtn(QPushButton):
    def __init__(self):
        super(DFDelBtn, self).__init__()
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/icons19/res/drawable-xhdpi-v4/deletebtn21a.png"), QIcon.Normal, QIcon.Off)
        self.setIcon(icon1)


class CatalogBullet(QWidget, Ui_catalogBullet):
    """
    TODO:
        add multi_bc
        add drag_func_editor
    """
    def __init__(self, data: Bullet = None, call=None):
        super(CatalogBullet, self).__init__()
        self.setupUi(self)

        self.data = data
        self.call = call

        self.n = None
        self.w = None
        self.ln = None
        self.d = None
        self.df = []
        self.drags = None

        self._ch_df_text = {}

        if self.data:
            self.bulletName.setText(self.data.name)
            self.weight.setValue(self.data.weight)
            self.length.setValue(self.data.length)
            self.diameter.setValue(self.data.diameter.diameter)

            # sess = db.SessMake()
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
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)

        self.Add.clicked.connect(self.add)
        self.tableWidget.clicked.connect(self.set_cell_data)

    def viewport_row(self):
        cursor = self.tableWidget.viewport().mapFromGlobal(QCursor().pos())
        return self.tableWidget.indexAt(cursor).row()

    def add_row(self):
        idx = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(idx+1)
        self.tableWidget.setItem(idx, 0, QTableWidgetItem(''))
        self.tableWidget.setItem(idx, 1, QTableWidgetItem(''))
        self.tableWidget.setItem(idx, 2, QTableWidgetItem(''))
        self.tableWidget.setCellWidget(idx, 3, DFDelBtn())
        self.tableWidget.cellWidget(idx, 3).clicked.connect(self.del_df)

        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/icons/res/drawable-hdpi-v4/settingsbtn_menu21a.png"),
                        QIcon.Normal,
                        QIcon.Off)
        self.tableWidget.item(idx, 1).setIcon(icon1)
        return idx

    def add(self, df=None):

        self.retranslateUi(self)

        if not df:
            df_type = DFTypeDlg()

            if df_type.exec_():

                idx = self.add_row()

                drag_type = df_type.combo.currentText()
                self.tableWidget.item(idx, 0).setText(drag_type)
                self.tableWidget.item(idx, 1).state = None
                if drag_type in ['G1', 'G7']:
                    self.tableWidget.item(idx, 1).setText(f'{self._ch_df_text["bc"]}: {0.1:.3f}')
                elif drag_type.endswith('Multi-BC'):
                    self.tableWidget.item(idx, 1).setText(f'{self._ch_df_text["point"]}: 0')
                else:
                    self.tableWidget.item(idx, 1).setText(f'{self._ch_df_text["dfl"]}: 0')

                if not self.set_cell_data(idx):
                    self.tableWidget.removeRow(idx)
        else:
            idx = self.add_row()
            data, comment = df.data, df.comment
            if df.drag_type in ['G1', 'G7']:
                bc = f'{data:.3f}' if data else f'{self._ch_df_text["bc"]}: {0.1:.3f}'
            elif df.drag_type.endswith('Multi-BC'):
                bc = 'Points: ' + str(len([(bc, v) for (bc, v) in df.data if bc > 0 and v >= 0])) \
                    if isinstance(df.data, list) else f'{self._ch_df_text["point"]}: 0'
            else:
                bc = 'DFL: ' + str(len(df.data)) if isinstance(df.data, list) else f'{self._ch_df_text["dfl"]}: 0'

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
        elif isinstance(index, QModelIndex) and (index.column() == 1):
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

                    self.tableWidget.item(row, 1).setText(f'{self._ch_df_text["points"]}: ' + str(len(count)))
                    self.tableWidget.item(row, 1).state = data if data else []
                    self.tableWidget.item(row, 2).setText(comment)
            else:
                cdf_edit = CDFEdit(data)
                if cdf_edit.exec_():
                    data, comment = cdf_edit.get()
                    self.tableWidget.item(row, 1).setText(f'{self._ch_df_text["dfl"]}: ' + str(len(data)))
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

    def retranslateUi(self, catalogBullet):
        super(CatalogBullet, self).retranslateUi(catalogBullet)
        _translate = QCoreApplication.translate
        catalogBullet.setWindowTitle(_translate("catalogBullet", 'Bullet Edit'))
        self._ch_df_text = {
            'bc': _translate("bullet", 'BC'),
            'points': _translate("bullet", 'Points'),
            'dfl': _translate("bullet", 'DFL')
        }

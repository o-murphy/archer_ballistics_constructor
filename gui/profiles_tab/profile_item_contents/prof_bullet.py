from PyQt5 import QtWidgets, QtCore
from .templates import Ui_bullet
from gui.db_widgets.edit.df_type_dlg import DFTypeDlg
from gui.db_widgets.edit.drag_func_settings import BCEdit
from gui.db_widgets.edit.drag_func_settings import MBCEdit
from gui.db_widgets.edit.drag_func_settings import CDFEdit
from dbworker.models import DragFunc

from py_ballisticcalc.lib.bmath.unit import Weight, WeightGrain, Distance, DistanceInch
from gui.app_settings import AppSettings


class Bullet(QtWidgets.QWidget, Ui_bullet):
    itemEvent = QtCore.pyqtSignal(object)

    def __init__(self, parent=None):
        super(Bullet, self).__init__(parent)
        self.setupUi(self)
        self.bulletGroupBox.layout().setAlignment(QtCore.Qt.AlignLeft)

        self._weight = Weight(0, WeightGrain)
        self._length = Distance(0, DistanceInch)
        self._diameter = Distance(0, DistanceInch)

        self.units = None
        self.setUnits()

        self.drag_functions = []

        self.weight.valueChanged.connect(self.weight_changed)
        self.length.valueChanged.connect(self.length_changed)
        self.diameter.valueChanged.connect(self.diameter_changed)
        self.dragType.currentIndexChanged.connect(self.df_changed)

    def setUnits(self):
        self.units = AppSettings()

        self.weight.setSuffix(self.units.wUnits.currentText())
        self.length.setSuffix(self.units.lnUnits.currentText())
        self.diameter.setSuffix(self.units.dUnits.currentText())

        self.weight.setValue(self._weight.get_in(self.units.wUnits.currentData()))
        self.length.setValue(self._length.get_in(self.units.lnUnits.currentData()))
        self.diameter.setValue(self._diameter.get_in(self.units.dUnits.currentData()))

    def weight_changed(self, value):
        self._weight = Weight(value, self.units.wUnits.currentData())

    def length_changed(self, value):
        self._length = Distance(value, self.units.lnUnits.currentData())

    def diameter_changed(self, value):
        self._diameter = Distance(value, self.units.dUnits.currentData())

    def set(self, data):
        self.bulletName.setText(data['bulletName'])

        self._weight = Weight(data['weight'], WeightGrain)
        self._length = Distance(data['length'], DistanceInch)
        self._diameter = Distance(data['diameter'], DistanceInch)

        self.setUnits()

        for i, df in enumerate(data['drags']):
            if isinstance(df, DragFunc):
                self.dragType.addItem(df.drag_type + ', ' + df.comment, i)
                self.drag_functions.append(df)
            else:
                self.save_new_df(df['drag_type'], df['data'], df['comment'])

        self.dragType.setCurrentIndex(self.dragType.findData(data['drag_idx']))
        self.df_changed(data['drag_idx'])

    def df_changed(self, idx):
        if self.drag_functions:
            cur_df = self.drag_functions[idx]

            if cur_df.drag_type in ['G1', 'G7']:
                text = f'BC: {cur_df.data:.3f}'
            elif cur_df.drag_type.endswith('Multi-BC'):
                count = [(bc, v) for (bc, v) in cur_df.data if bc > 0 and v >= 0]
                text = 'Points: ' + str(len(count))
            else:
                text = 'DFL: ' + str(len(cur_df.data))

            self.dragFuncData.setText(text)
            self.dragType.setToolTip(cur_df.comment)

    def edit_drag(self, data=None, comment=''):
        idx = self.dragType.currentIndex()
        cur_df = self.drag_functions[idx]

        if cur_df.drag_type in ['G1', 'G7']:
            bc_edit = BCEdit(cur_df.data)
            if bc_edit.exec_():
                data = bc_edit.get()
                return data

        elif cur_df.drag_type.endswith('Multi-BC'):
            bc_edit = MBCEdit(cur_df.data, comment)
            if bc_edit.exec_():
                data = bc_edit.get()
                return data

        elif cur_df.drag_type == 'Custom':
            edit = CDFEdit(cur_df.data)
            if edit.exec_():
                data = edit.get()
                return data

        # else:
        #     return cur_df

        # if data:
        #     cur_df.data = data
        #     cur_df.comment = comment
        #     self.df_changed(idx)
        #     self.dragType.setCurrentText(cur_df.drag_type + ', ' + cur_df.comment)

    def add_drag(self, data=None, comment=''):
        df_type = DFTypeDlg()

        if df_type.exec_():
            drag_type = df_type.combo.currentText()

            if drag_type in ['G1', 'G7']:
                bc_edit = BCEdit(data)
                if bc_edit.exec_():
                    data = bc_edit.get()

            elif drag_type.endswith('Multi-BC'):
                mbc_edit = MBCEdit(data)
                if mbc_edit.exec_():
                    data, comment = mbc_edit.get()

            elif drag_type == 'Custom':
                edit = CDFEdit(data)
                if edit.exec_():
                    data, comment = edit.get()

            self.save_new_df(drag_type, data, comment)

            return drag_type

    def save_new_df(self, drag_type, data, comment):
        if data:
            new_df = DragFunc(drag_type, data, comment, None, 'rw')
            self.drag_functions.append(new_df)
            idx = len(self.drag_functions) - 1
            self.dragType.addItem(new_df.drag_type + ', ' + new_df.comment, idx)
            self.dragType.setCurrentIndex(idx)

    def save_cur_df(self, data, comment, df_type=None):
        idx = self.dragType.currentIndex()
        cur_df = self.drag_functions[idx]

        cur_df.drag_type = df_type if df_type else cur_df.drag_type

        if data:
            cur_df.data = data
            cur_df.comment = comment
            self.df_changed(idx)
            self.dragType.setItemText(idx, cur_df.drag_type + ', ' + cur_df.comment)
            # self.dragType.setCurrentText(cur_df.drag_type + ', ' + cur_df.comment)

    # def weightTile(self):
    #     if self.weightQuantity.currentIndex() == 0:
    #         return str(int(round(self.weight.value(), 0))) + 'gr'
    #     else:
    #         return str(round(self.weight.value(), 1)) + 'g'

    def get(self):
        drags = []
        for df in self.drag_functions:
            drags.append({
                'drag_type': df.drag_type,
                'data': df.data,
                'comment': df.comment
            })

        ret = {
            self.bulletName.objectName(): self.bulletName.text(),
            'weight': self._weight.get_in(WeightGrain),
            'length': self._length.get_in(DistanceInch),
            'diameter': self._diameter.get_in(DistanceInch),
            # "weightTile": self.weightTile(),
            "drags": drags,
            "drag_idx": self.dragType.currentData()
        }
        return ret

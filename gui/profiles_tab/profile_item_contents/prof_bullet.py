from PyQt5 import QtWidgets, QtCore, QtGui
from .templates import Ui_bullet
from modules import BConverter
from gui.db_widgets.edit.df_type_dlg import DFTypeDlg
from gui.db_widgets.edit.drag_func_settings import BCEdit
from gui.db_widgets.edit.drag_func_settings import MBCEdit
from gui.db_widgets.edit.drag_func_settings import CDFEdit
from dbworker.models import DragFunc

from gui.drag_func_editor import DragFuncEditDialog


class Bullet(QtWidgets.QWidget, Ui_bullet):
    itemEvent = QtCore.pyqtSignal(object)

    def __init__(self, parent=None):
        super(Bullet, self).__init__(parent)
        self.setupUi(self)
        self.bulletGroupBox.layout().setAlignment(QtCore.Qt.AlignLeft)
        self.convert = BConverter()

        self.drag_functions = []

        self.setConverter()
        self.setupConnects()

    def setConverter(self):
        # self.mvQuantity.setItemData(0, self.convert.mps2fps)
        # self.mvQuantity.setItemData(1, self.convert.fps2mps)
        self.weightQuantity.setItemData(0, self.convert.gr_to_g)
        self.weightQuantity.setItemData(1, self.convert.g_to_gr)
        self.lengthQuantity.setItemData(0, self.convert.inch_to_mm)
        self.lengthQuantity.setItemData(1, self.convert.mm_to_inch)
        self.diameterQuantity.setItemData(0, self.convert.inch_to_mm)
        self.diameterQuantity.setItemData(1, self.convert.mm_to_inch)

    def setupConnects(self):
        self.weightSwitch.clicked.connect(self.convert_bullet_weight)
        self.lengthSwitch.clicked.connect(self.convert_bullet_length)
        self.diameterSwitch.clicked.connect(self.convert_bullet_diameter)

        self.dragType.currentIndexChanged.connect(self.df_changed)
        # self.addDrag.clicked.connect(self.add_drag)
        # self.dragEditor.clicked.connect(self.edit_drag)

    def convert_bullet_weight(self):
        cur_idx = self.weightQuantity.currentIndex()
        self.weight.setValue(self.weightQuantity.itemData(cur_idx)(self.weight.value()))
        self.weight.setSingleStep(0.01 if cur_idx == 0 else 0.1)
        self.weightQuantity.setCurrentIndex(1 if cur_idx == 0 else 0)

    def convert_bullet_length(self):
        cur_idx = self.lengthQuantity.currentIndex()
        self.length.setValue(self.lengthQuantity.itemData(cur_idx)(self.length.value()))
        self.lengthQuantity.setCurrentIndex(1 if cur_idx == 0 else 0)

    def convert_bullet_diameter(self):
        cur_idx = self.diameterQuantity.currentIndex()
        self.diameter.setValue(self.diameterQuantity.itemData(cur_idx)(self.diameter.value()))
        self.diameterQuantity.setCurrentIndex(1 if cur_idx == 0 else 0)

    @staticmethod
    def get_cln(spin: QtWidgets.QSpinBox, combo: QtWidgets.QComboBox):
        return spin.value() if combo.currentIndex() == 0 else combo.currentData()(spin.value())

    def set(self, data):
        self.bulletName.setText(data['bulletName'])
        self.weight.setValue(data['weight'])
        self.length.setValue(data['length'])
        self.diameter.setValue(data['diameter'])

        for i, df in enumerate(data['drags']):
            self.dragType.addItem(df.drag_type + ', ' + df.comment, i)
            self.drag_functions.append(df)

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

        elif cur_df.drag_type.endswith('Multi-BC'):
            return cur_df
        else:
            return cur_df

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

            self.save_new_df(drag_type, data, comment)

            return drag_type

    def save_new_df(self, drag_type, data, comment):
        if data:
            new_df = DragFunc(drag_type, data, comment, None, 'rw')
            self.drag_functions.append(new_df)
            idx = len(self.drag_functions) - 1
            self.dragType.addItem(new_df.drag_type + ', ' + new_df.comment, idx)
            self.dragType.setCurrentIndex(idx)

    def save_cur_df(self, data, comment):
        idx = self.dragType.currentIndex()
        cur_df = self.drag_functions[idx]

        if data:
            cur_df.data = data
            cur_df.comment = comment
            self.df_changed(idx)
            self.dragType.setCurrentText(cur_df.drag_type + ', ' + cur_df.comment)

    def weightTile(self):
        if self.weightQuantity.currentIndex() == 0:
            return str(int(round(self.weight.value(), 0))) + 'gr'
        else:
            return str(round(self.weight.value(), 1)) + 'g'

    def get(self):
        ret = {
            self.bulletName.objectName(): self.bulletName.text(),
            self.weight.objectName(): self.get_cln(self.weight, self.weightQuantity),
            self.length.objectName(): self.get_cln(self.length, self.lengthQuantity),
            self.diameter.objectName(): self.get_cln(self.diameter, self.diameterQuantity),
            "weightTile": self.weightTile(),
            "drags": self.drag_functions,
            "drag_idx": self.dragType.currentIndex()
        }
        return ret

import sys

from PyQt5 import QtWidgets, QtCore
from .templates import Ui_profileItem
from ..single_custom_widgets import NoWheelDoubleSpinBox
from ..stylesheet import load_qss

from .profile_item_contents import Bullet, Cartridge, Rifle, Conditions

from ..drag_func_editor import DragFuncEditDialog as DFED
from ..drag_func_editor.drag_func_edit_new import DragFuncEditDialog as ExperimentalDFED

from gui.app_settings import AppSettings
from py_ballisticcalc.lib.bmath.unit import Distance, DistanceMeter

from .default_data import get_defaults


class ProfileItem(QtWidgets.QWidget, Ui_profileItem):
    def __init__(self, parent=None):
        super(ProfileItem, self).__init__(parent)
        self.setupUi(self)
        self.setStyleSheet(load_qss('qss/profile_item.qss'))

        self.z_x = NoWheelDoubleSpinBox()
        self.z_x.setPrefix('X: ')
        self.z_y = NoWheelDoubleSpinBox()
        self.z_y.setPrefix('Y: ')
        self.z_d = NoWheelDoubleSpinBox()
        self.z_d.setMaximum(10000)
        self.z_x.setObjectName('z_x')
        self.z_y.setObjectName('z_y')
        self.z_d.setObjectName('z_d')
        self.gridLayout.addWidget(self.z_x, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.z_y, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.z_d, 0, 3, 2, 1)

        self.rifle = Rifle()
        self.cartridge = Cartridge()
        self.bullet = Bullet()
        self.conditions = Conditions()

        self.rifleName.setText(self.rifle.rifleName.text())
        self.caliberShort.setText(self.rifle.caliberShort.text())
        self.cartridgeName.setText(self.cartridge.cartridgeName.text())
        self.weightTile.setText(self.bullet.weightTile())

        self._z_d = Distance(100, DistanceMeter)

        self.units = None
        self.setUnits()

        self.z_d.valueChanged.connect(self.z_d_changed)
        self.setupConnects()

    def z_d_changed(self, value):
        self._z_d = Distance(value, self.units.distUnits.currentData())

    def setUnits(self):
        self.units = AppSettings()

        self.z_d.setValue(self._z_d.get_in(self.units.distUnits.currentData()))
        self.z_d.setSuffix(self.units.distUnits.currentText())

    def setupConnects(self):
        self.rifle.rifleName.textChanged.connect(lambda text: self.rifleName.setText(text))
        self.cartridge.cartridgeName.textChanged.connect(lambda text: self.cartridgeName.setText(text))
        self.rifle.caliberShort.textChanged.connect(lambda text: self.caliberShort.setText(text))
        self.bullet.weight.valueChanged.connect(lambda: self.weightTile.setText(self.bullet.weightTile()))
        self.bullet.weightQuantity.currentIndexChanged.connect(
            lambda: self.weightTile.setText(self.bullet.weightTile())
        )

        self.bullet.addDrag.clicked.connect(self.add_drag_data)
        self.bullet.dfDataEditor.clicked.connect(self.edit_drag_data)
        self.bullet.dragEditor.clicked.connect(self.open_df_editor)

    def add_drag_data(self):
        drag_type = self.bullet.add_drag()

    def edit_drag_data(self):

        state = self.get()
        cur_df = state['drags'][state['drag_idx']]
        df_data = cur_df['data']
        df_type = cur_df['drag_type']
        df_comment = cur_df['comment']

        new_data = self.bullet.edit_drag(df_data, df_comment)
        if new_data:

            if df_type in ['G1', 'G7']:
                self.bullet.save_cur_df(new_data, df_comment)

            elif df_type.endswith('Multi-BC'):
                self.bullet.save_cur_df(*new_data)

            elif df_type == 'Custom':
                self.bullet.save_cur_df(*new_data)

    def open_df_editor(self):
        state = self.get()
        cur_df = state['drags'][state['drag_idx']]
        state['df_data'] = cur_df['data']
        state['df_type'] = cur_df['drag_type']
        state['df_comment'] = cur_df['comment']

        app = QtCore.QCoreApplication.instance()
        if '-experiment' in app.arguments():
            cdf_edit = ExperimentalDFED(state=state)
        else:
            cdf_edit = DFED(state=state)
        if cdf_edit.exec_():
            edited_df = cdf_edit.__getstate__()
            self.bullet.save_cur_df(edited_df['df_data'], edited_df['df_comment'], edited_df['df_type'])

    def get(self) -> dict:
        data = {}
        data.update(**self.rifle.get())
        data.update(**self.bullet.get())
        data.update(**self.cartridge.get())
        data.update(**self.conditions.get())
        data.update(**{
            self.z_d.objectName(): self._z_d.get_in(DistanceMeter),
            self.z_x.objectName(): self.z_x.value(),
            self.z_y.objectName(): self.z_y.value()
        })
        return data

    def set(self, input_data):
        defaults = get_defaults()
        if input_data:
            defaults.update(input_data)
            data = defaults
        else:
            data = defaults
        # if data:
        self.rifle.set(data)
        self.cartridge.set(data)
        self.bullet.set(data)
        self.conditions.set(data)

        self._z_d = Distance(data['z_d'], DistanceMeter)
        self.z_x.setValue(data['z_x'])
        self.z_y.setValue(data['z_y'])

        self.setUnits()

from PyQt5 import QtWidgets
from .templates import Ui_profileItem
from ..single_custom_widgets import NoWheelSpinBox, NoWheelDoubleSpinBox
from ..stylesheet import load_qss

from .profile_item_contents import Bullet, Cartridge, Rifle, Conditions
from ..drag_func_editor import DragFuncEditDialog
from .profile_item_contents import CustomDLG

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
        self.z_d = NoWheelSpinBox()
        self.z_d.setSuffix(' M')
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

        self.setupConnects()

        self.bullet.addDrag.clicked.connect(self.add_drag)
        self.bullet.dragEditor.clicked.connect(self.edit_drag)

    def setupConnects(self):
        self.rifle.rifleName.textChanged.connect(lambda text: self.rifleName.setText(text))
        self.cartridge.cartridgeName.textChanged.connect(lambda text: self.cartridgeName.setText(text))
        self.rifle.caliberShort.textChanged.connect(lambda text: self.caliberShort.setText(text))
        self.bullet.weight.valueChanged.connect(lambda: self.weightTile.setText(self.bullet.weightTile()))
        self.bullet.weightQuantity.currentIndexChanged.connect(
            lambda: self.weightTile.setText(self.bullet.weightTile())
        )

    def add_drag(self):
        drag_type = self.bullet.add_drag()

        if drag_type == 'Custom':
            state = self.get()
            state['drag_idx'] = -1
            state['df_data'] = None
            state['df_type'] = drag_type
            state['df_comment'] = 'Default G1'

            cdf_edit = DragFuncEditDialog(state=state)
            cdf_edit.exec_()

            self.bullet.save_new_df(
                cdf_edit.state.df_type,
                cdf_edit.state.current_data
                if cdf_edit.state.current_data
                else cdf_edit.state.default_data,
                cdf_edit.dfComment.text()
            )

    def edit_drag(self):
        if self.bullet.edit_drag():
            state = self.get()
            cur_df = state['drags'][state['drag_idx']]
            state['df_data'] = cur_df.data
            state['df_type'] = cur_df.drag_type
            state['df_comment'] = cur_df.comment

            cdf_edit = DragFuncEditDialog(state=state)
            cdf_edit.exec_()

            if cdf_edit.state.df_type == 'Custom':

                self.bullet.save_cur_df(
                    cdf_edit.state.current_data
                    if cdf_edit.state.current_data
                    else cdf_edit.state.default_data,
                    cdf_edit.dfComment.text()
                )
            else:
                self.bullet.save_cur_df(
                    cdf_edit.mbc.get_data(),
                    cdf_edit.dfComment.text()
                )

    def get(self) -> dict:
        data = {}
        data.update(**self.rifle.get())
        data.update(**self.bullet.get())
        data.update(**self.cartridge.get())
        data.update(**self.conditions.get())
        data.update(**{
            self.z_d.objectName(): self.z_d.value(),
            self.z_x.objectName(): self.z_x.value(),
            self.z_y.objectName(): self.z_y.value()
        })
        return data

    def set(self, data):
        if not data:
            data = get_defaults()
        if data:
            self.rifle.set(data)
            self.cartridge.set(data)
            self.bullet.set(data)
            self.conditions.set(data)

    def drag_func_edit(self):

        drag_func_dlg = DragFuncEditDialog(state=self.profiles_table.get_current_item().state.__dict__)
        new_state = drag_func_dlg.__getstate__() if drag_func_dlg.exec_() else None

        if new_state:
            cell = self.profiles_table.get_current_item()
            cell.updateState(**new_state)
            self.profile_current.set_data(cell.state.__dict__)

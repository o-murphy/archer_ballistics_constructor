from PyQt5 import QtWidgets, QtCore
from .templates import Ui_profilesTab
from .profiles_table import ProfilesTable
from .profile_current import ProfileCurrent
from .profiles_tools import ProfilesTools
from ..drag_func_editor import DragFuncEditDialog
# from .profiles_progress import ProfilesProgress
from ..profile_item import WProfileItem


class CurrentState(object):
    def __init__(self,
                 profiles_file: str = None,
                 cur_item: WProfileItem = None):
        self.profiles_file = profiles_file
        self.cur_item = cur_item


class EmptyProfilesTab(QtWidgets.QWidget, Ui_profilesTab):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.state = CurrentState()

        self.profiles_table = ProfilesTable()
        self.profiles_tools = ProfilesTools()
        self.profile_current = ProfileCurrent()

        self.setupWidgets()
        self.setupConnects()

    def setupWidgets(self):
        self.profile_current.disable_tabs()
        self.gridLayout.addWidget(self.profiles_table, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.profiles_tools, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.profile_current, 0, 1, 2, 1)

    def setupConnects(self):
        self.profiles_tools.newProfileButton.clicked.connect(self.profiles_table.add_row)
        self.profiles_tools.removeProfileButton.clicked.connect(self.remove_profile_item)
        self.profiles_tools.clearAllProfiles.clicked.connect(self.remove_all_profiles)
        self.profiles_tools.downProfile.clicked.connect(self.profiles_table.move_down)
        self.profiles_tools.upProfile.clicked.connect(self.profiles_table.move_up)

        self.profiles_table.tableWidget.clicked.connect(self.table_clicked)
        self.profile_current.dragEditor.clicked.connect(self.drag_func_edit)

        self.profile_current.multiBC.clicked.connect(self.enable_multi_bc)

        widget_connect_list = []
        for le in self.profile_current.findChildren(QtWidgets.QLineEdit):
            widget_connect_list.append(le.textEdited)
            widget_connect_list.append(le.editingFinished)

        [widget_connect_list.append(sb.valueChanged) for sb in self.profile_current.findChildren(QtWidgets.QSpinBox)]
        [widget_connect_list.append(sb.valueChanged) for sb in self.profile_current.findChildren(QtWidgets.QDoubleSpinBox)]
        [widget_connect_list.append(cb.currentIndexChanged) for cb in self.profile_current.findChildren(QtWidgets.QComboBox)]
        [widget_connect_list.append(rb.clicked) for rb in self.profile_current.findChildren(QtWidgets.QRadioButton)]
        [widget_connect_list.append(cb.clicked) for cb in self.profile_current.findChildren(QtWidgets.QCheckBox)]
        [widget_connect_list.append(cb.clicked) for cb in self.profile_current.findChildren(QtWidgets.QCheckBox)]

        [i.connect(lambda: self.set_profile()) for i in widget_connect_list]

    def enable_multi_bc(self):
        self.profile_current.enable_multi_bc(self.profile_current.multiBC.isChecked())

    def remove_profile_item(self):
        self.profiles_table.remove_row()
        if not self.profiles_table.get_current_item():
            self.profile_current.disable_tabs()

    def remove_all_profiles(self):
        self.profiles_table.remove_all()
        self.profile_current.disable_tabs()

    def table_clicked(self):
        if self.profiles_table.get_current_item():
            self.profile_current.enable_tabs()

    def set_profile(self, item=None):
        if not item:
            item = self.profiles_table.tableWidget.cellWidget(
                self.profiles_table.tableWidget.currentRow(),
                self.profiles_table.tableWidget.currentColumn()
            )
        if item:
            item.set_profile(self.profile_current.get_rifle())
            item.set_profile(self.profile_current.get_bullet())
            item.set_profile(self.profile_current.get_cartridge())
            item.set_profile(self.profile_current.get_conditions())
            item.set_z_data()

    def drag_func_edit(self):
        drag_func_dlg = DragFuncEditDialog(self.profiles_table.get_current_item())
        new_drag_func = drag_func_dlg.current_data if drag_func_dlg.exec_() else drag_func_dlg.default_data
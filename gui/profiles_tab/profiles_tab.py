from PyQt5 import QtWidgets, QtCore
from .templates import Ui_profilesTab
from .profiles_table import ProfilesTable
from .profile_current import ProfileCurrent
from .profiles_tools import ProfilesTools
from ..drag_func_editor import DragFuncEditDialog
# from .profiles_progress import ProfilesProgress
from ..profile_item import WProfileItem
from datetime import datetime

from modules.env_update import USER_RECENT


class CurrentState(object):
    def __init__(self,
                 profiles_file: str = None,
                 cur_item: WProfileItem = None):
        self.profiles_file = profiles_file
        self.cur_item = cur_item


class EmptyProfilesTab(QtWidgets.QWidget, Ui_profilesTab):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.current_file = ''

        self.widget_connect_list = []
        self.profiles_table = ProfilesTable()

        self.recent_table = self.get_recent_profile_table()

        self.profiles_tools = ProfilesTools()
        self.profile_current = ProfileCurrent()

        self.setupWidgets()
        self.setupConnects()
        if len(args) > 1:
            try:
                self.open_file(args[1])
            except FileExistsError:
                pass
            except FileNotFoundError:
                pass

    def setupWidgets(self):
        self.profile_current.disable_tabs()
        self.gridLayout.addWidget(self.profiles_table, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.profiles_tools, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.profile_current, 0, 1, 2, 1)

    def setupConnects(self):
        self.profiles_tools.newProfileButton.clicked.connect(self.add_profile)
        self.profiles_tools.removeProfileButton.clicked.connect(self.remove_profile_item)
        self.profiles_tools.clearAllProfiles.clicked.connect(self.remove_all_profiles)
        self.profiles_tools.downProfile.clicked.connect(self.profiles_table.move_down)
        self.profiles_tools.upProfile.clicked.connect(self.profiles_table.move_up)

        self.profiles_tools.saveAsButton.clicked.connect(self.save_as_file_dialog)
        self.profiles_tools.saveButton.clicked.connect(self.save_file_dialog)
        self.profiles_tools.openFile.clicked.connect(self.open_file_dialog)

        self.profiles_table.tableWidget.clicked.connect(self.set_current)
        self.profile_current.dragEditor.clicked.connect(self.drag_func_edit)

        self.profile_current.multiBC.clicked.connect(self.enable_multi_bc)

        for le in self.profile_current.findChildren(QtWidgets.QLineEdit):
            self.widget_connect_list.append(le.textEdited)
            self.widget_connect_list.append(le.editingFinished)

        [self.widget_connect_list.append(sb.valueChanged) for sb in self.profile_current.findChildren(QtWidgets.QSpinBox)]
        [self.widget_connect_list.append(sb.valueChanged) for sb in
         self.profile_current.findChildren(QtWidgets.QDoubleSpinBox)]
        [self.widget_connect_list.append(cb.currentIndexChanged) for cb in
         self.profile_current.findChildren(QtWidgets.QComboBox)]
        [self.widget_connect_list.append(rb.clicked) for rb in self.profile_current.findChildren(QtWidgets.QRadioButton)]
        [self.widget_connect_list.append(cb.clicked) for cb in self.profile_current.findChildren(QtWidgets.QCheckBox)]
        [self.widget_connect_list.append(cb.clicked) for cb in self.profile_current.findChildren(QtWidgets.QCheckBox)]

        self.connectEvts()

    def connectEvts(self):
        [i.connect(self.set_profile) for i in self.widget_connect_list]

    def disconnectEvts(self):
        for i in self.widget_connect_list:
            try:
                i.disconnect(self.set_profile)
            except TypeError:
                pass

    def set_current(self):
        self.disconnectEvts()
        self.profile_current.set_data(self.profiles_table.select().profile)
        self.enable_multi_bc()
        self.connectEvts()

    def enable_multi_bc(self):
        self.profile_current.enable_multi_bc(self.profile_current.multiBC.isChecked())

    def remove_profile_item(self):
        self.profiles_table.remove_row()
        if not self.profiles_table.get_current_item():
            self.profile_current.disable_tabs()

    def remove_all_profiles(self):
        self.profiles_table.remove_all()
        self.profile_current.disable_tabs()

    def enable_widgets(self):
        if self.profiles_table.get_current_item():
            self.profile_current.enable_tabs()
            self.enable_multi_bc()

    def set_profile(self):
        if self.profiles_table.tableWidget.currentItem():
            item = self.profiles_table.tableWidget.cellWidget(
                self.profiles_table.tableWidget.currentRow(),
                self.profiles_table.tableWidget.currentColumn()
            )
            item.set_profile(self.profile_current.get_rifle())
            item.set_profile(self.profile_current.get_bullet())
            item.set_profile(self.profile_current.get_cartridge())
            item.set_profile(self.profile_current.get_conditions())
            item.set_z_data()

        if self.recent_table != self.get_recent_profile_table():
            self.window().setWindowTitle('ArcherBC - *' + self.current_file)

    def drag_func_edit(self):
        drag_func_dlg = DragFuncEditDialog(
            self.profiles_table.get_current_item(),
            self.profile_current.bc_table if self.profile_current.multiBC.isChecked() else self.profile_current.bc
        )
        new_drag_func = drag_func_dlg.current_data if drag_func_dlg.exec_() else drag_func_dlg.default_data
        if self.profile_current.multiBC.isChecked():
            self.profile_current.bulletGroupBox.layout().addWidget(self.profile_current.bc_table, 0, 2, 6, 1)
        else:
            self.profile_current.bcWidget.layout().addWidget(self.profile_current.bc, 0)

    def get_recent_profile_table(self):
        profiles = []
        for i in range(self.profiles_table.tableWidget.rowCount()):
            p = self.profiles_table.tableWidget.cellWidget(i, 0).profile
            profiles.append(p)
        return profiles

    def add_profile(self):
        self.profiles_table.add_row()
        self.set_profile()
        self.enable_widgets()

    @staticmethod
    def get_datetime():
        return datetime.now().strftime("%y-%m-%d_%H-%M-%S")

    def save_as_file_dialog(self, fileName=None):
        """SaveAsDialog Native"""
        options = QtWidgets.QFileDialog.Options()
        fileName, fileFormat = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "QFileDialog.getSaveFileName()",
            rf'{USER_RECENT}\{fileName}' if fileName else rf'{USER_RECENT}\recent_{self.get_datetime()}',
            "ArcherBC Profiles (*.arbcp);;JSON (*.json);;All Files (*);;Text Files (*.txt)",
            options=options
        )
        if fileName:
            self.save_profiles(fileName)

    def save_profiles(self, fileName):

        import json
        with open(fileName, 'w') as fp:
            json.dump(self.get_recent_profile_table(), fp)
        self.current_file = fileName
        self.window().setWindowTitle('ArcherBC - ' + self.current_file)
        self.recent_table = self.get_recent_profile_table()

    def save_file_dialog(self):
        """SaveAsDialog Native"""
        if self.current_file != '':
            self.save_profiles(self.current_file)
        else:
            self.save_as_file_dialog()

    def open_file_dialog(self):
        """OpenFileDialog Native"""
        options = QtWidgets.QFileDialog.Options()
        fileName, fileFormat = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "QFileDialog.getOpenFileName()",
            USER_RECENT,
            "ArcherBC Profiles (*.arbcp);;JSON (*.json);;All Files (*);;Python Files (*.py)",
            options=options
        )
        if fileName:
            self.open_file(fileName)

    def open_file(self, fileName):
        with open(fileName, 'r') as fp:
            import json
            data = json.load(fp)
        for d in data:
            self.disconnectEvts()
            self.profiles_table.add_row()

            self.profile_current.set_data(d)
            self.set_profile()
            self.connectEvts()
            self.enable_widgets()

        self.current_file = fileName
        self.window().setWindowTitle('ArcherBC - ' + self.current_file)

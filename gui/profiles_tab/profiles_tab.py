from PyQt5 import QtWidgets, QtCore
from .templates import Ui_profilesTab
from .profiles_table import ProfilesTable
from .profile_current import ProfileCurrent
from .profiles_tools import ProfilesTools
from .add_btn import AddBtn
from ..drag_func_editor import DragFuncEditDialog
from ..close_dialog import CloseDialog
from datetime import datetime

from modules.env_update import USER_RECENT
import os


class CurrentState(object):
    def __init__(self,
                 profiles_file: str = None):
        self.profiles_file = profiles_file


class EmptyProfilesTab(QtWidgets.QWidget, Ui_profilesTab):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)

        self.title = 'ArcherBC'

        self.current_file = ''
        self.is_saved = True

        self.widget_connect_list = []
        self.profiles_table = ProfilesTable()

        self.profiles_tools = ProfilesTools()
        self.profile_current = ProfileCurrent()

        self.add_btn = AddBtn()

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
        self.profile_current.enable_tabs(False)
        self.gridLayout.addWidget(self.profiles_table, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.profiles_tools, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.profile_current, 0, 1, 2, 1)
        self.insert_add_btn(0)

    def setupConnects(self):
        self.profiles_tools.newProfileButton.clicked.connect(self.add_profile)
        self.add_btn.add.clicked.connect(self.add_profile)

        self.profiles_tools.removeProfileButton.clicked.connect(self.remove_profile)
        self.profiles_tools.downProfile.clicked.connect(self.move_profile_down)
        self.profiles_tools.upProfile.clicked.connect(self.move_profile_up)

        self.profiles_tools.saveAsButton.clicked.connect(self.save_as_file_dialog)
        self.profiles_tools.saveButton.clicked.connect(self.save_file_dialog)
        self.profiles_tools.openFile.clicked.connect(self.open_file_dialog)
        self.profiles_tools.closeFile.clicked.connect(self.close_file)

        self.profiles_table.tableWidget.currentCellChanged.connect(self.on_current_profile_change)

        self.profile_current.dragEditor.clicked.connect(self.drag_func_edit)
        self.profile_current.multiBC.stateChanged.connect(self.enable_multi_bc)

        [self.widget_connect_list.append(le.textEdited) for le in
         self.profile_current.findChildren(QtWidgets.QLineEdit)]

        [self.widget_connect_list.append(sb.valueChanged) for sb in
         self.profile_current.findChildren(QtWidgets.QSpinBox)]
        [self.widget_connect_list.append(sb.valueChanged) for sb in
         self.profile_current.findChildren(QtWidgets.QDoubleSpinBox)]
        [self.widget_connect_list.append(cb.currentIndexChanged) for cb in
         self.profile_current.findChildren(QtWidgets.QComboBox)]
        [self.widget_connect_list.append(rb.clicked) for rb in
         self.profile_current.findChildren(QtWidgets.QRadioButton)]
        [self.widget_connect_list.append(cb.clicked) for cb in self.profile_current.findChildren(QtWidgets.QCheckBox)]
        [self.widget_connect_list.append(cb.clicked) for cb in self.profile_current.findChildren(QtWidgets.QCheckBox)]

        self.connectEvts()

    def connectEvts(self):
        [i.connect(self.update_profile) for i in self.widget_connect_list]

    def disconnectEvts(self):
        for i in self.widget_connect_list:
            try:
                i.disconnect(self.update_profile)
            except TypeError:
                pass

    def set_current(self, e):
        r = None
        if isinstance(e, QtCore.QModelIndex):
            r = e.row()
        elif isinstance(e, int) and e >= 0:
            r = e
        if r >= 0:
            cell = self.profiles_table.tableWidget.cellWidget(r, 0)
            if cell.profile:
                self.profile_current.set_data(cell.profile)
                cell.set_tile()

    def enable_multi_bc(self, event):
        self.profile_current.enable_multi_bc(event)

    def on_current_profile_change(self, e):
        if not self.profiles_table.tableWidget.currentItem():
            self.profile_current.enable_tabs(False)

        elif isinstance(e, int):
            if e >= 0:
                self.profile_current.enable_tabs(True)
                cell = self.profiles_table.tableWidget.cellWidget(e, 0)
                if cell:
                    if not isinstance(cell, AddBtn):
                        if cell.profile:
                            self.disconnectEvts()
                            self.set_current(e)
                            self.connectEvts()
            else:
                self.profile_current.enable_tabs(False)

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
        for i in range(self.profiles_table.tableWidget.rowCount() - 1):
            p = self.profiles_table.tableWidget.cellWidget(i, 0).profile
            profiles.append(p)
        return profiles

    def set_is_saved(self, e: bool):
        self.is_saved = e
        if not e:
            self.window().setWindowTitle(self.title + ' - *' + self.current_file)
        else:
            if not self.current_file == '':
                self.window().setWindowTitle(self.title + ' - ' + self.current_file)
            else:
                self.window().setWindowTitle(self.title)

    def insert_add_btn(self, last_row):
        self.profiles_table.tableWidget.insertRow(last_row)
        self.profiles_table.tableWidget.setCellWidget(last_row, 0, self.add_btn)

    def add_profile(self, e=None):

        if self.profiles_table.tableWidget.rowCount() < 21:
            self.profiles_table.add_row()
            self.set_profile()
            self.set_is_saved(False)

            last_row = self.profiles_table.tableWidget.rowCount()
            self.insert_add_btn(last_row)
            self.profiles_table.tableWidget.removeRow(last_row - 2)

    def remove_profile(self):
        if self.profiles_table.tableWidget.rowCount() > 0:
            self.profiles_table.remove_row()
            self.set_is_saved(False)

    def move_profile_up(self):
        if self.profiles_table.tableWidget.rowCount() > 0:
            self.profiles_table.move_up()

    def move_profile_down(self):
        if self.profiles_table.tableWidget.currentRow() < self.profiles_table.tableWidget.rowCount() - 2:
            if self.profiles_table.tableWidget.rowCount() > 0:
                self.profiles_table.move_down()

    def set_profile(self, z_data=None):
        item = self.profiles_table.select()
        if item:
            new_profile = {}
            profile = self.profile_current
            for func in [profile.get_rifle, profile.get_bullet, profile.get_cartridge, profile.get_conditions]:
                new_profile.update(func())
            item.set_profile(new_profile)
            item.set_z_data(z_data=z_data)

    def update_profile(self):

        item = self.profiles_table.select()
        if item:
            s = self.sender()
            k = s.objectName()

            if isinstance(s, QtWidgets.QSpinBox) or isinstance(s, QtWidgets.QDoubleSpinBox):
                v = s.value()
            elif isinstance(s, QtWidgets.QLineEdit) and not k.startswith('qt_spinbox_lineedit'):
                v = s.text()
            elif isinstance(s, QtWidgets.QComboBox):
                v = s.currentIndex()
            elif isinstance(s, QtWidgets.QRadioButton):
                v = s.isChecked()
            elif isinstance(s, QtWidgets.QCheckBox):
                v = s.checkState()
            else:
                v = None
            item.profile[k] = v
            item.set_tile()

            self.set_is_saved(False)

    @staticmethod
    def get_datetime():
        return datetime.now().strftime("%y-%m-%d_%H-%M-%S")

    def save_as_file_dialog(self, fileName=None):
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
        self.set_is_saved(True)

    def save_file_dialog(self):
        if self.current_file != '':
            if os.path.isfile(self.current_file):
                self.save_profiles(self.current_file)
            else:
                self.save_as_file_dialog(self.current_file)
        else:
            self.save_as_file_dialog()

    def open_file_dialog(self):
        self.close_file()
        if self.is_saved:
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
            self.add_profile()
            self.profile_current.set_data(d)
            print(d)
            self.set_profile(d)
            self.connectEvts()

        self.current_file = fileName
        self.set_is_saved(True)

    def close_file(self):
        choice = QtWidgets.QMessageBox.Cancel
        if not self.is_saved:
            choice = CloseDialog().exec_()
            if choice == QtWidgets.QMessageBox.Save:
                self.save_file_dialog()
            if choice == QtWidgets.QMessageBox.Close:
                self.set_is_saved(True)
        if self.is_saved:
            self.profiles_table.remove_all()
            self.current_file = ''
            self.set_is_saved(True)
        return choice

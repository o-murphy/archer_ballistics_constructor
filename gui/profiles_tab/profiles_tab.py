from PyQt5 import QtWidgets, QtCore
from .templates import Ui_profilesTab
from .profiles_table import ProfilesTable
from .profile_current import ProfileCurrent
from .profiles_tools import ProfilesTools
from .add_btn import AddBtn
from ..drag_func_editor import DragFuncEditDialog
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
        self.is_saved = True

        self.widget_connect_list = []
        self.profiles_table = ProfilesTable()

        self.recent_table = self.get_recent_profile_table()

        self.profiles_tools = ProfilesTools()
        self.profile_current = ProfileCurrent()
        # self.add_btn = None

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

    def setupConnects(self):
        self.profiles_tools.newProfileButton.clicked.connect(self.profiles_table.add_row())
        self.profiles_tools.removeProfileButton.clicked.connect(self.profiles_table.remove_row())
        # self.profiles_tools.clearAllProfiles.clicked.connect(self.profiles_table.remove_all())
        self.profiles_tools.downProfile.clicked.connect(self.profiles_table.move_down)
        self.profiles_tools.upProfile.clicked.connect(self.profiles_table.move_up)
        #
        # self.profiles_tools.saveAsButton.clicked.connect(self.save_as_file_dialog)
        # self.profiles_tools.saveButton.clicked.connect(self.save_file_dialog)
        # self.profiles_tools.openFile.clicked.connect(self.open_file_dialog)
        # self.profiles_tools.closeFile.clicked.connect(self.close_file)
        #
        # self.profiles_table.tableWidget.clicked.connect(self.set_current)
        # # self.profiles_table.tableWidget.currentCellChanged.connect(self.add_add_btn)
        self.profiles_table.tableWidget.currentCellChanged.connect(self.on_current_profile_change)
        # self.profile_current.dragEditor.clicked.connect(self.drag_func_edit)
        #
        # self.profile_current.multiBC.clicked.connect(self.enable_multi_bc)
        #
        # for le in self.profile_current.findChildren(QtWidgets.QLineEdit):
        #     self.widget_connect_list.append(le.textEdited)
        #     self.widget_connect_list.append(le.editingFinished)
        #
        # [self.widget_connect_list.append(sb.valueChanged) for sb in self.profile_current.findChildren(QtWidgets.QSpinBox)]
        # [self.widget_connect_list.append(sb.valueChanged) for sb in
        #  self.profile_current.findChildren(QtWidgets.QDoubleSpinBox)]
        # [self.widget_connect_list.append(cb.currentIndexChanged) for cb in
        #  self.profile_current.findChildren(QtWidgets.QComboBox)]
        # [self.widget_connect_list.append(rb.clicked) for rb in self.profile_current.findChildren(QtWidgets.QRadioButton)]
        # [self.widget_connect_list.append(cb.clicked) for cb in self.profile_current.findChildren(QtWidgets.QCheckBox)]
        # [self.widget_connect_list.append(cb.clicked) for cb in self.profile_current.findChildren(QtWidgets.QCheckBox)]
        #
        # self.connectEvts()

    def connectEvts(self):
        [i.connect(self.set_profile) for i in self.widget_connect_list]

    def disconnectEvts(self):
        for i in self.widget_connect_list:
            try:
                i.disconnect(self.set_profile)
            except TypeError:
                pass

    # def set_current(self, event):
    #     if isinstance(event, QtCore.QModelIndex):
    #         r, c = event.row(), event.column()
    #         self.disconnectEvts()
    #         self.profile_current.set_data(self.profiles_table.tableWidget.cellWidget(r, c).profile)
    #         self.enable_multi_bc(self.profile_current.multiBC.isChecked())
    #         self.connectEvts()

    # def enable_multi_bc(self, event):
    #     self.profile_current.enable_multi_bc(event)

    def on_current_profile_change(self, e):
        if isinstance(e, int):
            if e >= 0:
                self.profile_current.enable_tabs(True)
            if e < 0:
                self.profile_current.enable_tabs(False)

            # self.profile_current.set_data(self.profiles_table.tableWidget.cellWidget(e, 0).profile)
            # self.enable_multi_bc(self.profile_current.multiBC.isChecked())

    # def set_profile(self):
    #     if self.profiles_table.select():
    #         item = self.profiles_table.select()
    #         item.set_profile(self.profile_current.get_rifle())
    #         item.set_profile(self.profile_current.get_bullet())
    #         item.set_profile(self.profile_current.get_cartridge())
    #         item.set_profile(self.profile_current.get_conditions())
    #         item.set_z_data()
    #
    #     if self.recent_table != self.get_recent_profile_table():
    #         self.window().setWindowTitle('ArcherBC - *' + self.current_file)
    #         self.is_saved = False

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

    # def get_recent_profile_table(self):
    #     profiles = []
    #     for i in range(self.profiles_table.tableWidget.rowCount()):
    #         p = self.profiles_table.tableWidget.cellWidget(i, 0).profile
    #         profiles.append(p)
    #     return profiles

    # def add_profile(self):
    #     self.set_profile()

    # @staticmethod
    # def get_datetime():
    #     return datetime.now().strftime("%y-%m-%d_%H-%M-%S")
    #
    # def save_as_file_dialog(self, fileName=None):
    #     options = QtWidgets.QFileDialog.Options()
    #     fileName, fileFormat = QtWidgets.QFileDialog.getSaveFileName(
    #         self,
    #         "QFileDialog.getSaveFileName()",
    #         rf'{USER_RECENT}\{fileName}' if fileName else rf'{USER_RECENT}\recent_{self.get_datetime()}',
    #         "ArcherBC Profiles (*.arbcp);;JSON (*.json);;All Files (*);;Text Files (*.txt)",
    #         options=options
    #     )
    #     if fileName:
    #         self.save_profiles(fileName)
    #
    # def save_profiles(self, fileName):
    #
    #     import json
    #     with open(fileName, 'w') as fp:
    #         json.dump(self.get_recent_profile_table(), fp)
    #     self.current_file = fileName
    #     self.window().setWindowTitle('ArcherBC - ' + self.current_file)
    #     self.is_saved = True
    #     self.recent_table = self.get_recent_profile_table()
    #
    # def save_file_dialog(self):
    #     if self.current_file != '':
    #         if not self.current_file.startswith(fr'*{USER_RECENT}'):
    #             self.save_as_file_dialog(self.current_file)
    #         else:
    #             self.save_profiles(self.current_file)
    #     else:
    #         self.save_as_file_dialog()
    #
    # def open_file_dialog(self):
    #     self.close_file()
    #     if self.is_saved:
    #         options = QtWidgets.QFileDialog.Options()
    #         fileName, fileFormat = QtWidgets.QFileDialog.getOpenFileName(
    #             self,
    #             "QFileDialog.getOpenFileName()",
    #             USER_RECENT,
    #             "ArcherBC Profiles (*.arbcp);;JSON (*.json);;All Files (*);;Python Files (*.py)",
    #             options=options
    #         )
    #         if fileName:
    #             self.open_file(fileName)
    #
    # def open_file(self, fileName):
    #     with open(fileName, 'r') as fp:
    #         import json
    #         data = json.load(fp)
    #     for d in data:
    #         self.disconnectEvts()
    #         self.profiles_table.add_row()
    #
    #         self.profile_current.set_data(d)
    #         self.set_profile()
    #         self.connectEvts()
    #
    #     self.current_file = fileName
    #     self.window().setWindowTitle('ArcherBC - ' + self.current_file)
    #     self.is_saved = True
    #
    # def close_file(self):
    #     if not self.is_saved:
    #         msgbox = QtWidgets.QMessageBox()
    #         msgbox.setWindowTitle("File not saved!")
    #         msgbox.setText('File not saved. Do you want to save changes?')
    #         msgbox.addButton(QtWidgets.QMessageBox.Save)
    #         msgbox.addButton(QtWidgets.QMessageBox.Cancel)
    #         msgbox.addButton(QtWidgets.QMessageBox.Close)
    #         choice = msgbox.exec_()
    #         if choice == QtWidgets.QMessageBox.Save:
    #             self.save_file_dialog()
    #         if choice == QtWidgets.QMessageBox.Close:
    #             self.is_saved = True
    #     if self.is_saved:
    #         self.profiles_table.remove_all()
    #         self.current_file = ''
    #         self.window().setWindowTitle('ArcherBC')


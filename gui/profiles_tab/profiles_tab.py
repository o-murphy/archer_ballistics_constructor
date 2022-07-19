from PyQt5 import QtWidgets
from .templates import Ui_profilesTab
from .profiles_table import ProfilesTable
from .profile_current import ProfileCurrent
from .profiles_tools import ProfilesTools
from .profile_item import ProfileItem

from .add_btn import AddBtn
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

        self.profiles_table_widget = ProfilesTable(self)
        self.profiles_table = self.profiles_table_widget.tableWidget

        self.profiles_tools = ProfilesTools(self)
        self.profile_current = ProfileCurrent(self)

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
        self.gridLayout.addWidget(self.profiles_table_widget, 1, 0, 1, 1)
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
        self.profiles_table.currentCellChanged.connect(self.current_cell_changed)

        self.profiles_tools.loadBookMark.clicked.connect(self.load_bookmark)

    def current_cell_changed(self, row, col, prow, pcol):
        cur = self.profiles_table.cellWidget(row, col)
        self.profile_current.set_current(cur)

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
        self.profiles_table.insertRow(last_row)
        self.profiles_table.setCellWidget(last_row, 0, self.add_btn)

    def add_profile(self, data=None):
        if self.profiles_table.rowCount() < 21:
            new_item = ProfileItem(self)

            new_item.set(data)
            self.profiles_table_widget.add_row(new_item)

            self.set_is_saved(False)
            last_row = self.profiles_table.rowCount()
            self.insert_add_btn(last_row)
            self.profiles_table.removeRow(last_row - 2)

    def remove_profile(self):
        if self.profiles_table.rowCount() > 0:
            self.profiles_table_widget.remove_row()
            self.set_is_saved(False)

    def move_profile_up(self):
        if self.profiles_table.rowCount() > 0:
            self.profiles_table_widget.move_up()

    def move_profile_down(self):
        if self.profiles_table.currentRow() < self.profiles_table.rowCount() - 2:
            if self.profiles_table.rowCount() > 0:
                self.profiles_table_widget.move_down()

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

    def get_recent_profile_table(self):
        profiles = []
        for i in range(self.profiles_table.rowCount() - 1):
            p = self.profiles_table.cellWidget(i, 0).get()
            profiles.append(p)
        return profiles

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
            self.add_profile(data=d)

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
            self.profiles_table_widget.remove_all()
            self.current_file = ''
            self.set_is_saved(True)
        return choice

    def load_bookmark(self):
        from .profile_bookmarks import BookMarks
        from .default_data import get_templates

        rifles = BookMarks(self, 0)

        if rifles.exec_():
            rifle_id = rifles.selected
            if rifle_id:
                cartridges = BookMarks(self, 1, cal=rifles.cal)
                if cartridges.exec_():
                    cart_id = cartridges.selected
                    if cart_id:
                        data = get_templates(rifle_id, cart_id)

                        self.add_profile(data)


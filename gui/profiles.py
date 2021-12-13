# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore
from gui.templates import UiProfilesTab
import math
from datetime import datetime
import os
from modules.env_update import USER_RECENT, USER_BACKUP
from gui import DrugFuncEditDialog
from gui.recent_dlg import RecentDialog
from gui.profile_item import WProfileItem


class CurrentState(object):
    def __init__(self,
                 profiles_file: str = None,
                 cur_item: WProfileItem = None):
        self.profiles_file = profiles_file
        self.cur_item = cur_item


class ProfilesTab(UiProfilesTab):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.state = CurrentState()

        recent_list = os.listdir(USER_RECENT)
        if len(recent_list) > 0:

            recent_dialog = RecentDialog(recent_list)
            if recent_dialog.exec_():
                recent_file = recent_dialog.get_filename()
                print(recent_file)
                if recent_file:
                    self.open_file(rf'{USER_RECENT}\{recent_file}')

        self.scrollAreaWidgetContents.layout().setAlignment(QtCore.Qt.AlignTop)
        self.mvToolButton.clicked.connect(self.convert_muzzle_velocity)
        self.weightToolButton.clicked.connect(self.convert_bullet_weight)
        self.lengthToolButton.clicked.connect(self.convert_bullet_length)
        self.diameterToolButton.clicked.connect(self.convert_bullet_diameter)
        self.newProfileButton.clicked.connect(self.add_profile)
        self.removeProfileButton.clicked.connect(self.remove_profile)
        self.clearAllProfiles.clicked.connect(self.remove_all_profiles)

        self.downProfile.clicked.connect(self.move_profile_down)
        self.upProfile.clicked.connect(self.move_profile_up)

        self.saveButton.clicked.connect(self.save_file_dialog)
        self.saveAsButton.clicked.connect(self.save_as_file_dialog)
        self.openFile.clicked.connect(self.open_file_dialog)
        self.newFile.clicked.connect(self.new_file)
        self.closeFile.clicked.connect(self.close_file)

        self.dragToolButton.clicked.connect(self.drug_func_edit)

        for le in self.tabWidget_2.findChildren(QtWidgets.QLineEdit):
            le.textEdited.connect(self.update_current_profile)
            le.editingFinished.connect(self.update_current_profile)
        for sb in self.tabWidget_2.findChildren(QtWidgets.QSpinBox) + self.tabWidget_2.findChildren(
                QtWidgets.QDoubleSpinBox):
            sb.valueChanged.connect(self.update_current_profile)
        for cb in self.tabWidget_2.findChildren(QtWidgets.QComboBox):
            cb.currentIndexChanged.connect(self.update_current_profile)
        for rb in self.findChildren(QtWidgets.QRadioButton):
            rb.clicked.connect(self.update_current_profile)

    def drug_func_edit(self):
        drug_func_dlg = DrugFuncEditDialog()
        new_drug_func = drug_func_dlg.current_data if drug_func_dlg.exec_() else drug_func_dlg.default_data

    @staticmethod
    def get_datetime():
        return datetime.now().strftime("%y-%m-%d_%H-%M-%S")

    def new_file(self):
        self.close_file()
        self.save_as_file_dialog()

    def close_file(self):
        self.window().setWindowTitle('ArcherBC')
        self.state.profiles_file = None
        self.remove_all_profiles()

    def open_file_dialog(self):
        """OpenFileDialog Native"""
        options = QtWidgets.QFileDialog.Options()
        fileName, fileFormat = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "QFileDialog.getOpenFileName()",
            USER_RECENT,
            "JSON (*.json);;Profiles (*.prof);;All Files (*);;Python Files (*.py)",
            options=options
        )
        if fileName:
            self.open_file(fileName)

    def open_file(self, fileName):
        with open(fileName, 'r') as fp:
            import json
            data = json.load(fp)
        for i, d in enumerate(data):
            self.progressBar.setValue(int(100 * (i + 1) / len(data)))
            self.add_profile()
            item = self.scrollAreaWidgetContents.layout().itemAt(i).widget()
            for k, v in d.items():
                item.cst.__setattr__(k, v)
            item.mousePressEvent()
        self.window().setWindowTitle('ArcherBC'+10*' '+fileName)
        self.state.profiles_file = fileName
        self.progressBar.setValue(0)

    def save_profiles(self, fileName):
        profiles = []
        for item in self.scrollArea.findChildren(WProfileItem):
            profiles.append(item.cst.__dict__)
        import json
        with open(fileName, 'w') as fp:
            json.dump(profiles, fp)
        self.window().setWindowTitle('ArcherBC'+10*' '+fileName)
        self.state.profiles_file = fileName

    def save_file_dialog(self):
        """SaveAsDialog Native"""
        if self.state.profiles_file:
            self.save_profiles(self.state.profiles_file)
        else:
            self.save_as_file_dialog()

    def save_as_file_dialog(self, fileName=None):
        """SaveAsDialog Native"""
        options = QtWidgets.QFileDialog.Options()
        fileName, fileFormat = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "QFileDialog.getSaveFileName()",
            rf'{USER_RECENT}\{fileName}' if fileName else rf'{USER_RECENT}\recent_{self.get_datetime()}',
            "JSON (*.json);;Profiles (*.prof);;All Files (*);;Text Files (*.txt)",
            options=options
        )
        if fileName:
            self.save_profiles(fileName)

    def move_profile_down(self):
        if self.state.cur_item:
            layout = self.scrollAreaWidgetContents.layout()
            idx = layout.indexOf(self.state.cur_item)
            if idx + 1 < layout.count():
                layout.addWidget(layout.itemAt(idx + 1).widget())
                for i in range(idx - 1, layout.count() - 2):
                    layout.addWidget(layout.itemAt(idx).widget())

    def move_profile_up(self):
        if self.state.cur_item:
            layout = self.scrollAreaWidgetContents.layout()
            idx = layout.indexOf(self.state.cur_item)
            if idx > 0:
                layout.addWidget(layout.itemAt(idx - 1).widget())
                for i in range(idx, layout.count() - 1):
                    layout.addWidget(layout.itemAt(idx).widget())

    def convert_muzzle_velocity(self):
        """velocity convertion"""
        if self.mvComboBox.currentIndex() == 0:
            self.mvSpinBox.setValue(math.ceil(self.mvSpinBox.value() * 3.28))
            self.mvComboBox.setCurrentIndex(1)
        else:
            self.mvSpinBox.setValue(math.floor(self.mvSpinBox.value() / 3.28))
            self.mvComboBox.setCurrentIndex(0)

    def convert_bullet_weight(self):
        """weight convertion"""
        if self.weightComboBox.currentIndex() == 0:
            self.bulletWeight.setValue(self.gr_to_g(self.bulletWeight.value()))
            self.bulletWeight.setSingleStep(0.01)
            self.weightComboBox.setCurrentIndex(1)
        else:
            self.bulletWeight.setValue(self.g_to_gr(self.bulletWeight.value()))
            self.bulletWeight.setSingleStep(0.1)
            self.weightComboBox.setCurrentIndex(0)

    @staticmethod
    def inch_to_mm(cur_val):
        return cur_val * 25.4

    @staticmethod
    def mm_to_inch(cur_val):
        return cur_val / 25.4

    @staticmethod
    def gr_to_g(cur_val):
        return round(cur_val * 0.06479891, 2)

    @staticmethod
    def g_to_gr(cur_val):
        return round(cur_val / 0.06479891, 1)

    def convert_bullet_length(self):
        if self.lengthComboBox.currentIndex() == 0:
            self.lengthDoubleSpinBox.setValue(self.inch_to_mm(self.lengthDoubleSpinBox.value()))
            self.lengthComboBox.setCurrentIndex(1)
        else:
            self.lengthDoubleSpinBox.setValue(self.mm_to_inch(self.lengthDoubleSpinBox.value()))
            self.lengthComboBox.setCurrentIndex(0)

    def convert_bullet_diameter(self):
        if self.diameterComboBox.currentIndex() == 0:
            self.diameterDoubleSpinBox.setValue(self.inch_to_mm(self.diameterDoubleSpinBox.value()))
            self.diameterComboBox.setCurrentIndex(1)
        else:
            self.diameterDoubleSpinBox.setValue(self.mm_to_inch(self.diameterDoubleSpinBox.value()))
            self.diameterComboBox.setCurrentIndex(0)

    def update_current_profile(self):
        if self.state.cur_item:
            self.state.cur_item.update_profile()

    def add_profile(self):
        """
        adding w_prifile_widget to scrollArea
        :return:
        """
        layout = self.scrollAreaWidgetContents.layout()
        if layout.count() < 21:
            new_item = WProfileItem(layout.count(), self, parent=self)
            self.__setattr__(new_item.objectName(), new_item)
            item = self.__getattribute__(new_item.objectName())
            layout.addWidget(item)
            item.set_current()
            item.update_profile()

    def remove_profile(self):
        """
        :return:
        """
        layout = self.scrollAreaWidgetContents.layout()
        if layout.count() > 0 and self.state.cur_item:
            item = self.state.cur_item
            if layout.count() > 1 and layout.indexOf(item) > 0:
                new_focus = layout.itemAt(layout.indexOf(item) - 1).widget()
                new_focus.set_current()
            elif layout.count() > 1 and layout.indexOf(item) == 0:
                new_focus = layout.itemAt(1).widget()
                new_focus.set_current()
            elif layout.count() == 1:
                self.state.cur_item = None
            item.deleteLater()

    def remove_all_profiles(self):
        for item in self.scrollArea.findChildren(WProfileItem):
            self.state.cur_item = None
            item.deleteLater()

    def save_backup(self):
        recent_list = [item for item in os.listdir(USER_BACKUP) if item.startswith('backup_')]
        while len(recent_list) >= 15:
            recent_modified = [os.path.getmtime(rf'{USER_BACKUP}\{item}') for item in recent_list]
            os.remove(rf'{USER_BACKUP}\{recent_list[recent_modified.index(min(recent_modified))]}')
            recent_list = [item for item in os.listdir(USER_BACKUP) if item.startswith('backup_')]
        self.save_profiles(rf'{USER_BACKUP}\backup_{self.get_datetime()}.json')


if __name__ == '__main__':
    pass

from PyQt5 import QtWidgets, QtCore
from .templates import Ui_profilesTools


class ProfilesTools(QtWidgets.QWidget, Ui_profilesTools):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.saveButton.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.saveButton.customContextMenuRequested.connect(self.on_context_menu)
        self.saveButtonMenu = QtWidgets.QMenu(self)
        self.saveAsAction = QtWidgets.QAction('Save as...', self)
        self.saveButtonMenu.addAction(self.saveAsAction)

    def on_context_menu(self, point):
        # show context menu
        action = self.saveButtonMenu.exec_(self.saveButton.mapToGlobal(point))
        if action == self.saveAsAction:
            self.parent().save_as_file_dialog()

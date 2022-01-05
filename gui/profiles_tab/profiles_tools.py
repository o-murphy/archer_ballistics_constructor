from PyQt5 import QtWidgets, QtCore, QtGui
from .templates import Ui_profilesTools


class ProfilesTools(QtWidgets.QWidget, Ui_profilesTools):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.saveButton.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.saveButton.customContextMenuRequested.connect(self.on_context_menu)
        self.saveButtonMenu = QtWidgets.QMenu(self)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("ui_templates\\../.rsrc/res/drawable/saveasbtn_menu21a.png"),
                        QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.saveAsAction = QtWidgets.QAction('Save as... (CTRL+Shift+S)', self)
        self.saveAsAction.setIcon(icon9)
        self.saveButtonMenu.addAction(self.saveAsAction)

    def on_context_menu(self, point):
        action = self.saveButtonMenu.exec_(self.saveButton.mapToGlobal(point))
        if action == self.saveAsAction:
            self.parent().save_as_file_dialog()

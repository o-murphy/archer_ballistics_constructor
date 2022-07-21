from PyQt5.QtWidgets import QMenu, QAction, QWidget
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from .templates import Ui_profilesTools


class ProfilesTools(QWidget, Ui_profilesTools):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.saveButton.setContextMenuPolicy(Qt.CustomContextMenu)
        self.saveButton.customContextMenuRequested.connect(self.on_context_menu)
        self.saveButtonMenu = QMenu(self)
        icon9 = QIcon()
        icon9.addPixmap(QPixmap("ui_templates\\../.rsrc/res/drawable/saveasbtn_menu21a.png"),
                        QIcon.Normal,
                        QIcon.Off)
        self.saveAsAction = QAction('Save as... (CTRL+Shift+S)', self)
        self.saveAsAction.setIcon(icon9)
        self.saveButtonMenu.addAction(self.saveAsAction)

    def on_context_menu(self, point):
        action = self.saveButtonMenu.exec_(self.saveButton.mapToGlobal(point))
        if action == self.saveAsAction:
            self.parent().save_as_file_dialog()

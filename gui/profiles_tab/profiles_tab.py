from PyQt5 import QtWidgets, QtCore
from .templates import Ui_profilesTab
from .profiles_table import ProfilesTable
from .profile_current import ProfileCurrent
from .profiles_tools import ProfilesTools
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
        # self.profiles_progress = ProfilesProgress()

        self.setupWidgets()

        self.setupConnects()

    def setupWidgets(self):
        self.profile_current.tab_6.layout().setAlignment(QtCore.Qt.AlignTop)

        self.gridLayout.addWidget(self.profiles_table, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.profiles_tools, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.profile_current, 0, 1, 2, 1)
        # self.gridLayout.addWidget(self.profiles_progress, 3, 1, 1, 1)

    def setupConnects(self):
        self.profiles_tools.newProfileButton.clicked.connect(self.profiles_table.add_row)
        self.profiles_tools.removeProfileButton.clicked.connect(self.profiles_table.remove_row)
        self.profiles_tools.clearAllProfiles.clicked.connect(self.profiles_table.remove_all)

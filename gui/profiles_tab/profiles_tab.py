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

        self.profiles_tools.downProfile.clicked.connect(self.profiles_table.move_down)
        self.profiles_tools.upProfile.clicked.connect(self.profiles_table.move_up)

        widget_connect_list = []
        for le in self.profile_current.findChildren(QtWidgets.QLineEdit):
            widget_connect_list.append(le.textEdited)
            widget_connect_list.append(le.editingFinished)

        # [i.connect(self.set_current_tile) for i in widget_connect_list]

        [widget_connect_list.append(sb.valueChanged) for sb in self.profile_current.findChildren(QtWidgets.QSpinBox)]
        [widget_connect_list.append(sb.valueChanged) for sb in self.profile_current.findChildren(QtWidgets.QDoubleSpinBox)]
        [widget_connect_list.append(cb.currentIndexChanged) for cb in self.profile_current.findChildren(QtWidgets.QComboBox)]
        [widget_connect_list.append(rb.clicked) for rb in self.profile_current.findChildren(QtWidgets.QRadioButton)]

        [i.connect(lambda: self.set_profile()) for i in widget_connect_list]

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

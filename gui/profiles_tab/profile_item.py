from PyQt5 import QtWidgets, QtCore
from .templates import Ui_profileItem
from ..single_custom_widgets import NoWheelSpinBox, NoWheelDoubleSpinBox
from ..stylesheet import load_qss
from gui.custom_widget import State, StateUpdated


class ProfileItem(QtWidgets.QWidget, Ui_profileItem):
    def __init__(self, parent):
        super(ProfileItem, self).__init__()
        self.parent = parent
        self.setupUi(self)
        self.setStyleSheet(load_qss('qss/profile_item.qss'))

        self.profile: dict = {}

        self.state = None
        self.init_state()

        self.z_x = NoWheelDoubleSpinBox()
        self.z_x.setPrefix('X: ')
        self.z_y = NoWheelDoubleSpinBox()
        self.z_y.setPrefix('Y: ')
        self.z_d = NoWheelSpinBox()
        self.z_d.setSuffix(' M')

        self.setupWidgets()
        self.setupConnects()

    def init_state(self):
        self.state = State(self)
        # self.onStateUpdate.connect(lambda e: print(e.key, e.value))
        self.onStateUpdate.connect(lambda e: self.state_did_update(e))

    def setupWidgets(self):
        self.z_x.setObjectName('z_x')
        self.z_y.setObjectName('z_y')
        self.z_d.setObjectName('z_d')
        self.gridLayout.addWidget(self.z_x, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.z_y, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.z_d, 0, 3, 2, 1)

    def setupConnects(self):
        # self.z_x.valueChanged.connect(self.set_z_data)
        # self.z_y.valueChanged.connect(self.set_z_data)
        # self.z_d.valueChanged.connect(self.set_z_data)
        self.z_x.valueChanged.connect(lambda value: self.setState(z_x=value))
        self.z_y.valueChanged.connect(lambda value: self.setState(z_y=value))
        self.z_d.valueChanged.connect(lambda value: self.setState(z_d=value))

    def set_profile(self, data: dict):
        for k, v in data.items():
            self.profile[k] = v
        # self.set_tile()

        """ new way """
        # self.setState(data)

    def set_tile(self):
        """"""

        """ temp """
        for k, v in self.profile.items():
            if hasattr(self, k):
                w = self.__getattribute__(k)
                if isinstance(w, QtWidgets.QLabel):
                    w.setText(v)
                if isinstance(w, QtWidgets.QSpinBox) or isinstance(w, QtWidgets.QDoubleSpinBox):
                    w.setValue(v)

        """ new way """
        for k, v in self.state.__dict__.items():
            if hasattr(self, k):
                w = self.__getattribute__(k)
                if isinstance(w, QtWidgets.QLabel):
                    w.setText(v)
                if isinstance(w, QtWidgets.QSpinBox) or isinstance(w, QtWidgets.QDoubleSpinBox):
                    w.setValue(v)

    def set_z_data(self, e=None, z_data=None):
        if z_data:
            self.z_x.setValue(z_data['z_x'])
            self.z_y.setValue(z_data['z_y'])
            self.z_d.setValue(z_data['z_d'])

        # if e and (isinstance(self.sender(), NoWheelDoubleSpinBox) or isinstance(self.sender(), NoWheelSpinBox)):
        #     self.profile[self.sender().objectName()] = e
        #
        #     """ new way """
        #     self.setState({self.sender().objectName(): e})

    def state_did_update(self, e=None, z_data=None):
        if isinstance(e, StateUpdated):
            print(e.key, e.value)

            """temp"""
            self.profile[e.key] = e.value

            self.set_tile()

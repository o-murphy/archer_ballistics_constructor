from PyQt5 import QtWidgets
from .templates import Ui_profileItem
from ..single_custom_widgets import NoWheelSpinBox, NoWheelDoubleSpinBox
from ..stylesheet import load_qss
from modules import State, StateDidUpdate, StateDidSet


class ProfileItem(QtWidgets.QWidget, Ui_profileItem):
    def __init__(self):
        super(ProfileItem, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(load_qss('qss/profile_item.qss'))

        self.state = State(self)
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
        self.onStateUpdate.connect(lambda e: self.state_did_update(e))
        self.onStateSet.connect(lambda e: self.state_did_set(e))

    def setupWidgets(self):
        self.z_x.setObjectName('z_x')
        self.z_y.setObjectName('z_y')
        self.z_d.setObjectName('z_d')
        self.gridLayout.addWidget(self.z_x, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.z_y, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.z_d, 0, 3, 2, 1)

    def setupConnects(self):
        self.z_x.valueChanged.connect(self.state_will_update)
        self.z_y.valueChanged.connect(self.state_will_update)
        self.z_d.valueChanged.connect(self.state_will_update)

    def state_will_update(self, value):
        self.setState(**{self.sender().objectName(): value})

    def state_did_set(self, e=None):
        if isinstance(e, StateDidSet):
            if e.key in ['rifleName', 'cartridgeName', 'caliberShort']:
                self.findChild(QtWidgets.QWidget, e.key).setText(e.value)

    def state_did_update(self, e=None):
        if isinstance(e, StateDidUpdate):
            if e.key in ['rifleName', 'cartridgeName', 'caliberShort']:
                self.findChild(QtWidgets.QWidget, e.key).setText(e.value)


from PyQt5 import QtWidgets, QtCore
from .templates import Ui_profileItem
from ..single_custom_widgets import NoWheelSpinBox, NoWheelDoubleSpinBox
from ..stylesheet import load_qss
from gui.custom_widget import State, StateUpdated


class ProfileItem(QtWidgets.QWidget, Ui_profileItem):
    def __init__(self):
        super(ProfileItem, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(load_qss('qss/profile_item.qss'))

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
        self.onStateUpdate.connect(lambda e: self.state_did_update(e))

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
        self.setState({self.sender().objectName(): value})

    def state_did_update(self, e=None, z_data=None, *args, **kwargs):
        if isinstance(e, StateUpdated):
            print(e.key, e.value)
            if e.key in ['rifleName', 'cartridgeName', 'caliberShort']:
                self.findChild(QtWidgets.QWidget, e.key).setText(e.value)
            # if e.key == 'weight':
            #     # temporary
            #     self.weightTile.setText(
            #         str(int(round(e.value(), 0))) + 'gr'
            #         if self.state.weightQuantity == 0
            #         else str(round(e.value(), 1)) + 'g'
            #     )

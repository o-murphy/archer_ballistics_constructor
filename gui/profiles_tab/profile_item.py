from PyQt5 import QtWidgets
from .templates import Ui_profileItem
from ..single_custom_widgets import NoWheelSpinBox, NoWheelDoubleSpinBox


class ProfileItem(QtWidgets.QWidget, Ui_profileItem):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.profile: dict = {}
        self.z_x = NoWheelDoubleSpinBox()
        self.z_y = NoWheelDoubleSpinBox()
        self.z_d = NoWheelSpinBox()
        self.setupWidgets()
        self.setupConnects()

    def setupWidgets(self):
        self.z_x.setObjectName('z_x')
        self.z_y.setObjectName('z_y')
        self.z_d.setObjectName('z_d')
        self.gridLayout.addWidget(self.z_x, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.z_y, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.z_d, 0, 5, 2, 1)

    def setupConnects(self):
        self.z_x.valueChanged.connect(self.set_z_data)
        self.z_y.valueChanged.connect(self.set_z_data)
        self.z_d.valueChanged.connect(self.set_z_data)

    def set_profile(self, data: dict):
        for k, v in data.items():
            self.profile[k] = v
            if hasattr(self, k):
                self.__getattribute__(k).setText(v)

    def set_z_data(self):
        self.profile[self.z_x.objectName()] = self.z_x.value()
        self.profile[self.z_y.objectName()] = self.z_y.value()
        self.profile[self.z_d.objectName()] = self.z_d.value()
        # print(self.profile)

    def init_data(self, data):
        pass

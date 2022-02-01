from PyQt5 import QtWidgets, QtCore
from .templates import Ui_catalogTab
from .catalog_selector import CatalogSelector
from .catalog_info import CatalogInfo
from .catalog_rifle import CatalogRifle
from .catalog_bullet import CatalogBullet
from .catalog_cartridge import CatalogCartridge
from .catalog_item_edit import CatalogItemEdit
from gui.stylesheet import load_qss


class CatalogTab(QtWidgets.QWidget, Ui_catalogTab):
    def __init__(self):
        super(CatalogTab, self).__init__()
        self.setupUi(self)



        self.setStyleSheet(load_qss('qss/application.qss') + """
            QTabBar::tab {
                height: 140px;
                width: 50px;
                font-size: 15px;
                border-bottom-left-radius: 8px;
                border-top-left-radius: 8px;
                border-bottom-right-radius: 0px;
                border-top-right-radius: 0px;
            }
            QGroupBox {
                color: rgb(255, 255, 255);
                border: 1px solid rgb(78, 78, 78);
                padding-top: 0px;
            }
        """)

        self.selector = CatalogSelector()
        self.info = CatalogInfo()
        self.gridLayout.addWidget(self.selector, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.info, 0, 1, 1, 1)

        # self.info.gridLayout.addWidget(CatalogRifle())
        # self.info.gridLayout.addWidget(CatalogCartridge())
        # self.info.gridLayout.addWidget(CatalogBullet())

        self.data = {
            "rifleName": "G7 template",
            "caliberName": ".224 Remington",
            "sh": 90,
            "twist": 10,
            "caliberShort": ".224",
            "rightTwist": True,
            "bulletName": "",
            "weight": 175.0,
            "length": 0.9,
            "diameter": 0.224,
            "dragType": 1,
            "weightTile": "175gr",
            "multiBC": 2,
            "bc": 0.169,
            "bcTable": [
                [
                    914,
                    0
                ],
                [
                    762,
                    0
                ],
                [
                    609,
                    0
                ],
                [
                    457,
                    0
                ],
                [
                    0,
                    0
                ]
            ],
            "cartridgeName": "",
            "mv": 800,
            "temp": 15,
            "ts": 1.55,
            "z_pressure": 750,
            "z_angle": 0,
            "z_humidity": 50,
            "z_temp": 15,
            "z_azimuth": 270,
            "z_powder_temp": 15,
            "z_latitude": 0,
            "z_x": 0,
            "z_y": 0,
            "z_d": 100,
            "": 0.246
        }

        self.selector.tabWidget.currentChanged.connect(self.edit_item)

    def edit_item(self, index):
        item = self.selector.tabWidget.widget(index).objectName()
        print(item)
        if item == 'rifles':
            item_edit = CatalogItemEdit(item.upper()[:-1], CatalogRifle(self.data))
        elif item == 'cartridges':
            item_edit = CatalogItemEdit(item.upper()[:-1], CatalogCartridge(self.data))
        elif item == 'bullets':
            item_edit = CatalogItemEdit(item.upper()[:-1], CatalogBullet(self.data))
        else:
            item_edit = None

        if item_edit:
            if item_edit.exec_():
                print(item_edit.get_data())


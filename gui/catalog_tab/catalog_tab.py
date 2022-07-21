from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from .templates import Ui_catalogTab
from .catalog_selector import CatalogSelector

from gui.stylesheet import load_qss


class CatalogTab(QWidget, Ui_catalogTab):
    def __init__(self):
        super(CatalogTab, self).__init__()
        self.setupUi(self)

        self.setStyleSheet(load_qss('qss/application.qss') +
                           """
                                QTabBar::tab {
                                    height: 100px;
                                    width: 30px;
                                    font-size: 15px;
                                    border-bottom-left-radius: 8px;
                                    border-top-left-radius: 8px;
                                    border-bottom-right-radius: 0px;
                                    border-top-right-radius: 0px;
                                }
                                QTableCornerButton::section {
                                    background: rgb(51, 51, 51);
                                }

                                """
                           #         QTableWidget {
                           #             background-image: url(:/icons/res/drawable-hdpi-v4/addbtn_menu21b.png);
                           #             background-repeat: no-repeat;
                           #             background-position: center;
                           #         }
                           )

        self.selector = CatalogSelector()
        self.gridLayout.setAlignment(Qt.AlignLeft)
        self.gridLayout.addWidget(self.selector, 0, 0, 1, 1)

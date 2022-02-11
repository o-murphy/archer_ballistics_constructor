from PyQt5 import QtWidgets, QtCore
from .templates import Ui_myTab
from .templates_selector import MyTabSelector

from gui.stylesheet import load_qss


class MyTab(QtWidgets.QWidget, Ui_myTab):
    def __init__(self):
        super(MyTab, self).__init__()
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

                                """)

        self.selector = MyTabSelector()
        self.gridLayout.setAlignment(QtCore.Qt.AlignLeft)
        self.gridLayout.addWidget(self.selector, 0, 0, 1, 1)

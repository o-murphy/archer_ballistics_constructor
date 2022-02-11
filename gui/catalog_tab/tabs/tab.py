from PyQt5 import QtWidgets, QtCore
from ..toolbar import InfoTools


class Tab(QtWidgets.QWidget):
    def __init__(self):
        super(Tab, self).__init__()
        self.setStyleSheet("""QLabel {font-size: 16px;}""")

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(self.gridLayout)

        self.list = None
        self.info = None
        self.table = None
        self.tools = InfoTools()

    def set(self):
        if self.list and self.info:
            self.table = self.list.tableWidget
            self.gridLayout.addWidget(self.list, 0, 0, 2, 1)
            self.gridLayout.addWidget(self.info, 0, 1, 1, 1)
            self.gridLayout.addWidget(self.tools, 1, 1, 1, 1)


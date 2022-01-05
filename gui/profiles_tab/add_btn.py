from PyQt5 import QtWidgets
from .templates import Ui_tWidget


class AddBtn(QtWidgets.QWidget, Ui_tWidget):
    def __init__(self):
        super(AddBtn, self).__init__()
        self.setupUi(self)
        self.def_size = self.minimumSize()
        self.def_style = self.styleSheet()
        self.max_style = """
        QWidget#zWidget, QWidget#tWidget {
            background: transparent;
            border: 0px;
        }
        
        QPushButton {
            background: transparent;
            border: 0px;
            border-radius: 8px; 
        }
        
        QPushButton::hover {
            background-color: rgb(75, 75, 75);
        }
        """

    def minimize(self):
        self.add.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.add.setMinimumSize(self.def_size)
        self.setStyleSheet(self.def_style)

    def maximize(self):
        self.add.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.add.setMinimumWidth(426)
        self.setStyleSheet(self.max_style)

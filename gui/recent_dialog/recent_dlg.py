# -*- coding: utf-8 -*-

from gui.templates import Ui_RecentDialog
from PyQt5 import QtWidgets, QtCore
import sys


class listWidget(QtWidgets.QListWidget):
    def mouseDoubleClickEvent(self, event):
        if self.currentIndex().data():
            self.parent().accept()


class RecentDialog(QtWidgets.QDialog, Ui_RecentDialog):
    def __init__(self, recent_list):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('ArcherBC (Recent files)')
        self.list_double_click = listWidget(self)
        self.list_double_click.setGeometry(QtCore.QRect(10, 41, 241, 161))
        self.list_double_click.setObjectName("listWidget")
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setText("Open")
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).setText("Empty")
        self.list_double_click.addItems(recent_list)

    def get_filename(self):
            return self.list_double_click.currentIndex().data()

    def closeEvent(self, event) -> None:
        sys.exit()


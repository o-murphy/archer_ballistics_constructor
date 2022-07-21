# -*- coding: utf-8 -*-

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QDialog, QListWidget, QDialogButtonBox
import sys
from .templates import Ui_RecentDialog


class listWidget(QListWidget):
    def mouseDoubleClickEvent(self, event):
        if self.currentIndex().data():
            self.parent().accept()


class RecentDialog(QDialog, Ui_RecentDialog):
    def __init__(self, recent_list):
        super().__init__()
        self.setupUi(self)
        self.recent_list = recent_list
        self.list_double_click = listWidget(self)
        self.list_double_click.setGeometry(QRect(10, 41, 241, 161))
        self.list_double_click.setObjectName("listWidget")
        self.buttonBox.button(QDialogButtonBox.Ok).setText("Open")
        self.buttonBox.button(QDialogButtonBox.Cancel).setText("Empty")
        self.list_double_click.addItems(self.recent_list)

    def get_filename(self):
            return self.list_double_click.currentIndex().data()

    def closeEvent(self, event) -> None:
        sys.exit()


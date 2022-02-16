from PyQt5 import QtWidgets
from .templates import Ui_catalogItemEdit
from gui.stylesheet import load_qss


class CatalogItemEdit(QtWidgets.QDialog, Ui_catalogItemEdit):
    def __init__(self, widget: QtWidgets.QWidget):
        super(CatalogItemEdit, self).__init__()
        self.setupUi(self)

        self.setWindowTitle(widget.title)
        self.setStyleSheet(load_qss('qss/dialog.qss'))
        self.widget = widget
        self.widget.setStyleSheet(load_qss('qss/application.qss'))

        self.setMaximumSize(self.widget.maximumWidth(), self.widget.maximumHeight()+47)

        self.gridLayout.addWidget(self.widget)
        self.gridLayout.addWidget(self.buttonBox)

    def get(self):
        return self.widget.get()

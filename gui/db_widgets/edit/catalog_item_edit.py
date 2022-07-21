from PyQt5.QtWidgets import QDialog, QWidget

from .templates import Ui_catalogItemEdit
from gui.stylesheet import load_qss


class CatalogItemEdit(QDialog, Ui_catalogItemEdit):
    def __init__(self, widget: QWidget):
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

    def accept(self) -> None:
        if self.widget.valid():
            return super().accept()
        self.widget.invalid()

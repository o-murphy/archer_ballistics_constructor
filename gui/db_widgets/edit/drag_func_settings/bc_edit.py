from PyQt5 import QtWidgets, QtCore
from .templates import Ui_bcEdit
from typing import Optional


class BCEdit(QtWidgets.QDialog, Ui_bcEdit):
    def __init__(self, data=None):
        super(BCEdit, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        if data:
            self.doubleSpinBox.setValue(data)

    def get(self) -> Optional[float]:
        value = self.doubleSpinBox.value()
        if value > 0:
            return value
        else:
            message_box = QtWidgets.QMessageBox()
            message_box.setText('BC cannot be 0')
            message_box.exec_()
            return

    def accept(self) -> None:
        if self.get():
            super().accept()
        else:
            return

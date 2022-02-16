from PyQt5 import QtWidgets, QtCore
from .templates import Ui_bcEdit
from typing import Optional
from gui.stylesheet import load_qss


class BCEdit(QtWidgets.QDialog, Ui_bcEdit):
    def __init__(self, data=None):
        super(BCEdit, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.setStyleSheet(load_qss('qss/dialog.qss') + """
            QDialog {border: 1px solid rgb(76, 76, 76)}
        """)

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

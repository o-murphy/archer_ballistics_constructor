from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QDialog, QMessageBox

from .templates import Ui_bcEdit
from typing import Optional
from gui.stylesheet import load_qss


class BCEdit(QDialog, Ui_bcEdit):
    def __init__(self, data=None):
        super(BCEdit, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.message_box = QMessageBox()

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
            self.retranslateUi(self)
            self.message_box.exec_()
            return

    def accept(self) -> None:
        if self.get():
            super().accept()
        else:
            return

    def retranslateUi(self, bcEdit):
        super(BCEdit, self).retranslateUi(bcEdit)
        _translate = QCoreApplication.translate
        self.message_box.setText(_translate('bcEdit', 'BC cannot be 0'))

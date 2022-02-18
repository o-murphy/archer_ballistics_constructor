from PyQt5 import QtWidgets
from .templates import Ui_rifle


class Rifle(QtWidgets.QWidget, Ui_rifle):
    def __init__(self, parent=None):
        super(Rifle, self).__init__(parent)
        self.setupUi(self)

    def set(self, data):
        self.rifleName.setText(data.rifleName)
        self.caliberName.setText(data.caliberName)
        self.sh.setValue(data.sh)
        self.twist.setValue(data.twist)
        self.caliberShort.setText(data.caliberShort)
        self.twist.setValue(data.twist)
        self.rightTwist.setChecked(data.rightTwist)

    def get(self):
        return {
            self.rifleName.objectName(): self.rifleName.text(),
            self.caliberName.objectName(): self.caliberName.text(),
            self.sh.objectName(): self.sh.value(),
            self.twist.objectName(): self.twist.value(),
            self.caliberShort.objectName(): self.caliberShort.text(),
            self.rightTwist.objectName(): self.rightTwist.isChecked(),
        }

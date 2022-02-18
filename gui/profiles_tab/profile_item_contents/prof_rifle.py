from PyQt5 import QtWidgets, QtCore
from .templates import Ui_rifle


class Rifle(QtWidgets.QWidget, Ui_rifle):
    def __init__(self, parent=None):
        super(Rifle, self).__init__(parent)
        self.setupUi(self)

        self.rifleGroupBox.layout().setAlignment(QtCore.Qt.AlignLeft)

        self.autoTile.clicked.connect(self.auto_tile)

    def auto_tile(self):
        self.caliberShort.setText(
            self.caliberName.text().replace(' ', '').strip()[:7]
        )

    def set(self, data):
        self.rifleName.setText(data['rifleName'])
        self.caliberName.setText(data['caliberName'])
        self.sh.setValue(data['sh'])
        self.twist.setValue(data['twist'])
        self.caliberShort.setText(data['caliberShort'])
        self.rightTwist.setChecked(data['rightTwist'])

    def get(self):
        return {
            self.rifleName.objectName(): self.rifleName.text(),
            self.caliberName.objectName(): self.caliberName.text(),
            self.sh.objectName(): self.sh.value(),
            self.twist.objectName(): self.twist.value(),
            self.caliberShort.objectName(): self.caliberShort.text(),
            self.rightTwist.objectName(): self.rightTwist.isChecked(),
        }

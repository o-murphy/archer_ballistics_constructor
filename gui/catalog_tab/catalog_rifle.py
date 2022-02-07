from PyQt5 import QtWidgets
from .templates import Ui_catalogRifle


class CatalogRifle(QtWidgets.QWidget, Ui_catalogRifle):
    def __init__(self, data):
        super(CatalogRifle, self).__init__()
        self.setupUi(self)

        if data:
            self.data = data
            self.rifleName.setText(data.name)
            self.caliberName.setText(data.caliber.name)
            self.sh.setValue(data.sh)
            self.twist.setValue(data.twist)
            self.rightTwist.setChecked(data.is_right)
            # self.data = data
            # self.rifleName.setText(data['rifleName'])
            # self.caliberName.setText(data['caliberName'])
            # self.sh.setValue(data['sh'])
            # self.twist.setValue(data['twist'])
            # self.rightTwist.setChecked(data['rightTwist'])
            # self.caliberShort.setText(data['caliberShort'])

    def setConverter(self):
        self.weightQuantity.setItemData(0, self.convert.gr_to_g)
        self.weightQuantity.setItemData(1, self.convert.g_to_gr)
        self.lengthQuantity.setItemData(0, self.convert.inch_to_mm)
        self.lengthQuantity.setItemData(1, self.convert.mm_to_inch)
        self.diameterQuantity.setItemData(0, self.convert.inch_to_mm)
        self.diameterQuantity.setItemData(1, self.convert.mm_to_inch)

    def get_data(self):
        return {
            'rifleName': self.rifleName.text(),
            'caliberName': self.caliberName.text(),
            'sh': self.sh.value(),
            'twist': self.twist.value(),
            'rightTwist': self.rightTwist.isChecked(),
            'caliberShort': self.caliberShort.text(),
        }

from PyQt5.QtCore import Qt, QRegExp

from .tab import Tab
from ..tables import CatalogRifleList
from ..info import CatalogRifleInfo


class RiflesTab(Tab):
    def __init__(self, model=None, attrs=None):
        super(RiflesTab, self).__init__()
        self.list = CatalogRifleList(model, attrs)
        self.info = CatalogRifleInfo()
        self.set()
        self.enable_filter()

        self.filter_widget.resetFilter.clicked.connect(self.reset_filter)
        self.filter_widget.caliber.currentIndexChanged.connect(self.set_diameter)

        self.filter_widget.name.textChanged.connect(self.apply_filter)
        self.filter_widget.diameter.valueChanged.connect(self.apply_filter)

    def set_diameter(self):
        data = self.filter_widget.caliber.currentData()
        if data:
            self.filter_widget.diameter.setValue(data.diameter.diameter)
            self.apply_filter()
        else:
            self.filter_widget.diameter.setValue(0)
            self.reset_filter()

    def apply_filter(self):
        text = self.filter_widget.name.text()
        if text:
            regexp = QRegExp(text, Qt.CaseInsensitive)
            self.list.proxy_model1.setFilterRegExp(regexp)

        value = self.filter_widget.diameter.value()
        self.list.proxy_model2.setFilterFixedString(str(value))

    def reset_filter(self):
        self.filter_widget.name.setText('')
        self.filter_widget.caliber.setCurrentText('None')
        self.filter_widget.diameter.setValue(0)
        self.filter_widget.weight.setValue(0)
        self.list.set_data()

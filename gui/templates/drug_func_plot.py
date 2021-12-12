from PyQt5 import QtWidgets
import pyqtgraph as pg


class Ui_Plot(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.verticalLayout = QtWidgets.QHBoxLayout(self)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setSpacing(4)
        self.graphWidget = pg.PlotWidget()
        self.verticalLayout.addWidget(self.graphWidget)

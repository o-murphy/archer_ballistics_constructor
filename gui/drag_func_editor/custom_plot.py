from PyQt5 import QtCore, QtWidgets
import pyqtgraph as pg


class CustomPlot(QtWidgets.QWidget):
    def __init__(self, name):
        super().__init__()
        self.setObjectName(name)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QHBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(4)
        self.graphWidget = pg.PlotWidget()

        self.x = None
        self.def_y = None
        self.cur_y = None
        self.cur_x = None

        self.x_quantity = None
        self.x_q_label = None
        self.y_quantity = None
        self.y_q_label = None

        self.verticalLayout.addWidget(self.graphWidget)

        self.graphWidget.showGrid(x=True, y=True, alpha=0.3)

        self.default_plot = self.graphWidget.plot(pen=pg.mkPen(color='w'))
        self.init_plot = self.graphWidget.plot(pen=pg.mkPen(color='r', style=QtCore.Qt.DotLine))
        self.current_plot = self.graphWidget.plot(pen=pg.mkPen(color=(255, 170, 0)))

        self.current_point = self.graphWidget.plot()
        self.current_point_text = pg.TextItem(text="", color=(255, 255, 255), anchor=(0, 1))

        self.text_item = pg.TextItem(text="", color=(0, 255, 255), anchor=(1, 1))
        self.peak_line = pg.InfiniteLine(pen=pg.mkPen(color='w', style=QtCore.Qt.DotLine))
        self.peak_line.setVisible(False)

        self.cd_at_distance = pg.InfiniteLine(pen=pg.mkPen(color='r', style=QtCore.Qt.DashLine))
        self.cd_at_distance.setVisible(False)
        self.cd_at_distance_text = pg.TextItem(text="", color='r', anchor=(0, 1))

        self.graphWidget.addItem(self.peak_line)
        self.graphWidget.addItem(self.text_item)
        self.graphWidget.addItem(self.current_point_text)
        self.graphWidget.addItem(self.cd_at_distance)
        self.graphWidget.addItem(self.cd_at_distance_text)

        self.setMouseTracking(True)
        self.graphWidget.scene().sigMouseMoved.connect(self.onMouseMoved)

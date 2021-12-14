from PyQt5 import QtCore, QtWidgets
import pyqtgraph as pg


class DragPlot(QtWidgets.QWidget):
    def __init__(self, name):
        super().__init__()
        self.setObjectName(name)
        self.setMaximumHeight(300)

        self.verticalLayout = QtWidgets.QHBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(4)
        self.graphWidget = pg.PlotWidget()
        self.verticalLayout.addWidget(self.graphWidget)

        self.graphWidget.showGrid(x=True, y=True, alpha=0.3)

        self.default_plot = self.graphWidget.plot(pen=pg.mkPen(color='w'))
        self.current_plot = self.graphWidget.plot(pen=pg.mkPen(color=(255, 170, 0)))

        self.current_point = self.graphWidget.plot()
        self.current_point_text = pg.TextItem(text="", color=(255, 255, 255), anchor=(0, 1))
        self.text_item = pg.TextItem(text="", color=(0, 255, 255), anchor=(1, 1))
        self.peak_line = pg.InfiniteLine(pen=pg.mkPen(color='w', style=QtCore.Qt.DotLine))

        self.graphWidget.addItem(self.peak_line)
        self.graphWidget.addItem(self.text_item)
        self.graphWidget.addItem(self.current_point_text)

        self.setMouseTracking(True)
        self.graphWidget.scene().sigMouseMoved.connect(self.onMouseMoved)

    def onMouseMoved(self, point):
        """

        Временное решение

        :param point:
        :return:
        """
        if self.parent():
            self.current_point.setData()
            p = self.graphWidget.plotItem.vb.mapSceneToView(point)
            ox, oy = self.parent().parse_data(self.parent().current_data)  # !!! temporary
            ix, x = min(enumerate(ox), key=lambda n: abs(p.x() - n[1]))
            text = 'x: {}, y: {}'.format(round(x, 4), round(oy[ix], 4))
            self.current_point.setData(x=[round(x, 4)], y=[round(oy[ix], 4)],
                                       symbolSize=10,
                                       symbolBrush=pg.mkBrush(100, 100, 255, 100))
            self.current_point_text.setPos(round(x, 4), round(oy[ix], 4))
            self.current_point_text.setText(text)

    def set_limits(self, ox, oy):
        self.graphWidget.getViewBox().setLimits(
            xMin=min(ox)-0.1, xMax=max(ox)+0.1,
            yMin=min(oy)-0.025, yMax=max(oy)+0.025,
            minXRange=(max(ox)+0.2)/1000, maxXRange=max(ox)+0.2,
            minYRange=(max(oy)+0.05)/1000, maxYRange=max(oy)+0.05
        )

    def set_text(self, x, y, dy):
        coeff = round(y/dy*100-100, 0)
        idx = f'+{coeff}' if coeff > 0 else abs(coeff) if coeff == 0 else coeff
        self.text_item.setText("Idx: {}".format(idx))
        self.text_item.setPos(x, y)

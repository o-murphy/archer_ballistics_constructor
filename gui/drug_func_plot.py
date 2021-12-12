from gui.templates import Ui_DragPlot
import pyqtgraph as pg
import random


class DrugPlot(Ui_DragPlot):
    def __init__(self):
        super().__init__()
        self.setMaximumHeight(300)
        self.graphWidget.showGrid(x=True, y=True, alpha=0.3)

        self.default_plot = self.graphWidget.plot(pen=pg.mkPen(color='w'))
        self.current_plot = self.graphWidget.plot(pen=pg.mkPen(color='red'))

        self.current_point = self.graphWidget.plot()
        self.current_point_text = pg.TextItem(text="", color=(0, 255, 255), anchor=(0, 1))
        self.text_item = pg.TextItem(text="", color=(0, 255, 255), anchor=(0, 1))

        self.graphWidget.addItem(self.text_item)
        self.graphWidget.addItem(self.current_point_text)

        self.setMouseTracking(True)
        self.graphWidget.scene().sigMouseMoved.connect(self.onMouseMoved)

    def onMouseMoved(self, point):
        self.current_point.setData()
        p = self.graphWidget.plotItem.vb.mapSceneToView(point)
        ox, oy = self.parent().split_current_data()
        ix, x = min(enumerate(ox), key=lambda n: abs(p.x() - n[1]))
        text = 'x: {}, y: {}'.format(round(x, 4), round(oy[ix], 4))
        self.current_point.setData(x=[round(x, 4)], y=[round(oy[ix], 4)],
                                   symbolSize=10,
                                   symbolBrush=pg.mkBrush(100, 100, 255, 100))
        self.current_point_text.setPos(round(x, 4), round(oy[ix], 4))
        self.current_point_text.setText(text)

    def set_limits(self, max_x, min_x, max_y, min_y):
        self.graphWidget.getViewBox().setLimits(
            xMin=min_x-0.1, xMax=max_x+0.1,
            yMin=min_y-0.025, yMax=max_y+0.025,
            minXRange=(max_x+0.2)/1000, maxXRange=max_x+0.2,
            minYRange=(max_y+0.05)/1000, maxYRange=max_y+0.05
        )

    def set_text(self, x, y, dy):
        coeff = round(y/dy*100-100, 0)
        idx = f'+{coeff}' if coeff > 0 else abs(coeff) if coeff == 0 else coeff
        self.text_item.setText("Idx: {}".format(idx))
        self.text_item.setPos(x, y)

    def set_point(self):
        self.current_point = self.graphWidget.plot()

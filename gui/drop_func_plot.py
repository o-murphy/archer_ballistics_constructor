from PyQt5 import QtCore, QtWidgets
from .drag_func_plot import DragPlot, rnd4
import pyqtgraph as pg


class DropPlot(DragPlot):

    def onMouseMoved(self, point):
        """

        Временное решение

        :param point:
        :return:
        """
        if self.parent():
            self.current_point.setData()
            p = self.graphWidget.plotItem.vb.mapSceneToView(point)
            ox, oy = self.parent().distances, self.parent().current_drop

            ix, x = min(enumerate(ox), key=lambda n: abs(p.x() - n[1]))
            text = 'x: {},\ny: {}'.format(rnd4(x), rnd4(oy[ix]))
            self.current_point.setData(x=[rnd4(x)], y=[rnd4(oy[ix])],
                                       symbolSize=10,
                                       symbolBrush=pg.mkBrush(100, 100, 255, 100))
            self.current_point_text.setPos(rnd4(x), rnd4(oy[ix]))
            self.current_point_text.setText(text)

    def set_limits(self, ox, oy):
        vb = self.graphWidget.getViewBox()
        vb.setXRange(0, 1100)
        vb.setYRange(0, oy[ox.index(1100)])
        vb.setLimits(
            xMin=-50, xMax=max(ox)+350,
            yMin=min(oy)-5000, yMax=max(oy)+1000,
            minXRange=(max(ox)+500)/10, maxXRange=max(ox)+500,
            minYRange=(max(oy)+6000)/100, maxYRange=max(oy)+6000
        )

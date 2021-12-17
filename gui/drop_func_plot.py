from .drag_func_plot import DragPlot
import pyqtgraph as pg
from modules import BConverter

rnd = BConverter.auto_rnd


class DropPlot(DragPlot):
    def __init__(self, name):
        super().__init__(name)
        self.q_func = BConverter.nothing

    def onMouseMoved(self, point):
        """

        Временное решение

        :param point:
        :return:
        """
        if self.parent():
            self.current_point.setData()
            p = self.graphWidget.plotItem.vb.mapSceneToView(point)
            ox = self.parent().distances
            data = self.parent().current_drop if self.parent().current_drop else self.parent().default_drop

            oy = [self.q_func(v, ox[k]) for k, v in enumerate(data)]

            ix, x = min(enumerate(ox), key=lambda n: abs(p.x() - n[1]))

            text = '{} {},\n{} M'.format(rnd(x), self.y_q_label, rnd(oy[ix]))
            self.current_point.setData(x=[rnd(x)], y=[rnd(oy[ix])],
                                       symbolSize=10,
                                       symbolBrush=pg.mkBrush(100, 100, 255, 100))
            self.current_point_text.setPos(rnd(x), rnd(oy[ix]))
            self.current_point_text.setText(text)

    def set_limits(self, ox, oy):
        vb = self.graphWidget.getViewBox()
        vb.setLimits(
            xMin=min(ox)-max(ox)*0.05, xMax=max(ox)*1.05,
            yMin=min(oy)-max(oy)*0.1, yMax=max(oy)*1.1,
            minXRange=max(ox)*1.2/10, maxXRange=max(ox)*1.2,
            minYRange=max(oy)*1.2/100, maxYRange=max(oy)*1.2
        )

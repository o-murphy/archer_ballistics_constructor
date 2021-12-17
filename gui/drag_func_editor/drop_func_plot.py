from .custom_plot import CustomPlot, pg, rnd, BConverter


class DropPlot(CustomPlot):
    def __init__(self, name):
        super().__init__(name)
        self.q_func = BConverter.nothing
        self.graphWidget.getPlotItem().vb.invertY(True)


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

    def set_hold_off_quantity(self, quantity, distances, default_drop, current_drop, *args, **kwargs):
        y_axis = self.graphWidget.getPlotItem().getAxis('left')
        if quantity == 1:
            self.y_q_label = 'MIL'
            self.q_func = BConverter.cm2mil
        elif quantity == 2:
            self.y_q_label = 'MOA'
            self.q_func = BConverter.cm2moa
        else:
            self.y_q_label = 'sm'
            self.q_func = BConverter.nothing
        y_axis.setLabel(self.y_q_label)

        default = [self.q_func(v, distances[k]) for k, v in enumerate(default_drop)]
        self.set_limits(distances, default)
        self.default_plot.setData(distances, default)

        if current_drop:
            current = [self.q_func(v, distances[k]) for k, v in enumerate(current_drop)]
            self.set_limits(distances, current + default)
            self.current_plot.setData(distances, current)

    def reset_current_plot(self, quantity, distances, default_drop, current_drop):
        self.current_plot.setData()
        self.current_point_text.setColor(color=(255, 255, 255))
        self.set_hold_off_quantity(quantity, distances, default_drop, current_drop)

    def draw_custom_plot(self, quantity, distances, default_drop, current_drop):
        self.current_point_text.setColor(color=(255, 170, 0))
        self.set_hold_off_quantity(**{k: v for k, v in locals().items() if k != 'self'})

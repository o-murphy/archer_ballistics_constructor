from .custom_plot import CustomPlot, pg, rnd


class DragPlot(CustomPlot):
    def __init__(self, name):
        super().__init__(name)
        self.peak_line.setVisible(True)

    def onMouseMoved(self, point):
        """

        Временное решение

        :param point:
        :return:
        """
        if self.parent():
            self.current_point.setData()
            p = self.graphWidget.plotItem.vb.mapSceneToView(point)
            data = self.parent().current_data if self.parent().current_data else self.parent().default_data
            ox, oy = self.parent().parse_data(data)  # !!! temporary
            ix, x = min(enumerate(ox), key=lambda n: abs(p.x() - n[1]))

            text = '{} {}, {}'.format(rnd(x * self.x_quantity), self.x_q_label, rnd(oy[ix]))
            self.current_point.setData(x=[rnd(x)], y=[rnd(oy[ix])],
                                       symbolSize=10,
                                       symbolBrush=pg.mkBrush(100, 100, 255, 100))
            self.current_point_text.setPos(rnd(x), rnd(oy[ix]))
            self.current_point_text.setText(text)

    def set_limits(self, ox, oy):
        self.graphWidget.getViewBox().setLimits(
            xMin=min(ox)-max(ox)*0.05, xMax=max(ox)*1.05,
            yMin=min(oy)-0.025, yMax=max(oy)+0.025,
            minXRange=(max(ox)*1.2)/1000, maxXRange=max(ox)*1.2,
            minYRange=(max(oy)*1.2)/1000, maxYRange=max(oy)*1.2
        )

    def set_distance_quantity(self, quantity):
        x_axis = self.graphWidget.getPlotItem().getAxis('bottom')
        self.x_quantity, self.x_q_label = 1, 'Mach'
        if quantity == 1:
            self.x_quantity, self.x_q_label = 343, 'm/s'
        if quantity == 2:
            self.x_quantity, self.x_q_label = 343 * 3.281, 'ft/s'
        x_axis.setScale(self.x_quantity)
        x_axis.setLabel(f"Velocity ({self.x_q_label})")

    def set_text(self, x, y, dy):
        coeff = round(y/dy*100-100, 0)
        idx = f'+{coeff}' if coeff > 0 else abs(coeff) if coeff == 0 else coeff
        self.text_item.setText("Idx: {}".format(idx))
        self.text_item.setPos(x, y)

    def draw_plot(self, plot, ox, oy, clear=False):
        plot.setData() if clear else plot.setData(ox, oy)
        self.set_limits(ox, oy)
        self.set_text(ox[oy.index(max(oy))], max(oy), max(oy))
        self.peak_line.setPos((ox[oy.index(max(oy))], 0))

    def draw_default_plot(self, ox, oy):
        self.draw_plot(self.default_plot, ox, oy)

    def draw_current_plot(self, ox, oy):
        self.draw_plot(self.current_plot, ox, oy)
        self.current_point_text.setColor(color=(255, 170, 0))

    def reset_current_plot(self, ox, oy):
        self.draw_plot(self.current_plot, ox, oy, True)
        self.current_point_text.setColor(color=(255, 255, 255))
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
            data = self.parent().state.current_data \
                if self.parent().state.current_data \
                else self.parent().state.default_data
            ox, oy = self.parent().parse_data(data)  # !!! temporary
            ix, x = min(enumerate(ox), key=lambda n: abs(p.x() - n[1]))

            text = '{} {}, {}'.format(rnd(x * self.x_quantity), self.x_q_label, rnd(oy[ix]))
            self.current_point.setData(x=[rnd(x)], y=[rnd(oy[ix])],
                                       symbolSize=10,
                                       symbolBrush=pg.mkBrush(100, 100, 255, 100))
            self.current_point_text.setPos(rnd(x), rnd(oy[ix]))
            self.current_point_text.setText(text)

    def set_limits(self, oy):
        self.graphWidget.getViewBox().setLimits(
            xMin=min(self.x)-max(self.x)*0.05, xMax=max(self.x)*1.05,
            yMin=min(oy)-0.025, yMax=max(oy)+0.025,
            minXRange=(max(self.x)*1.2)/1000, maxXRange=max(self.x)*1.2,
            minYRange=(max(oy)*1.2)/1000, maxYRange=max(oy)*1.2
        )

    def set_distance_quantity(self):
        x_axis = self.graphWidget.getPlotItem().getAxis('bottom')
        x_axis.setScale(self.x_quantity)
        x_axis.setLabel(f"Velocity ({self.x_q_label})")

    def set_text(self, x, y, dy):
        coeff = round(y/dy*100-100, 0)
        idx = f'+{coeff}' if coeff > 0 else abs(coeff) if coeff == 0 else coeff
        self.text_item.setText("Idx: {}".format(idx))
        self.text_item.setPos(x, y)

    def draw_default_plot(self, ox, oy):
        self.x, self.def_y = ox, oy
        self.set_limits(self.def_y)
        self.default_plot.setData(self.x, self.def_y)

    def draw_current_plot(self, ox, oy):
        self.cur_y = oy
        self.set_limits(self.cur_y + self.def_y)
        if len(self.x) != len(self.cur_y):
            self.cur_x = ox
            self.current_plot.setData(self.cur_x, self.cur_y)
        else:
            self.current_plot.setData(self.x, self.cur_y)
        self.current_point_text.setColor(color=(255, 170, 0))

    def reset_current_plot(self):
        self.cur_y = None
        self.set_limits(self.def_y)
        self.current_plot.setData()
        self.current_point_text.setColor(color=(255, 255, 255))

    def set_cd_at_distance(self, x, y):
        self.cd_at_distance.setVisible(True)
        self.cd_at_distance.setPos((x, y))
        self.cd_at_distance_text.setText(f'{str(x * self.x_quantity)} {self.x_q_label}')
        self.cd_at_distance_text.setPos(x, y)

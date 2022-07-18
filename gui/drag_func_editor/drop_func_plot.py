from .custom_plot import CustomPlot, pg, rnd, BConverter


class DropPlot(CustomPlot):
    def __init__(self, name):
        super().__init__(name)
        self.y_quantity = BConverter.nothing
        self.graphWidget.getPlotItem().vb.invertY(True)

    def onMouseMoved(self, point):
        """

        Временное решение

        :param point:
        :return:
        """
        if self.parent() and self.x:
            self.current_point.setData()
            p = self.graphWidget.plotItem.vb.mapSceneToView(point)
            ox = self.x
            data = self.cur_y if self.cur_y else self.def_y

            oy = [self.y_quantity(v, ox[k]) for k, v in enumerate(data)]

            ix, x = min(enumerate(ox), key=lambda n: abs(p.x() - n[1]))

            text = '{} M,\n{} {}'.format(rnd(x), rnd(oy[ix]), self.y_q_label)
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

    def set_quantity(self):
        # x_axis = self.graphWidget.getPlotItem().getAxis('bottom')
        # x_axis.setScale(self.x_quantity)
        # x_axis.setLabel(f"Velocity ({self.x_q_label})")

        y_axis = self.graphWidget.getPlotItem().getAxis('left')
        y_axis.setLabel(self.y_q_label)
        y_def = [rnd(self.y_quantity(v, self.x[i])) for i, v in enumerate(self.def_y)]

        if self.cur_y:
            y_cur = [rnd(self.y_quantity(v, self.x[i])) for i, v in enumerate(self.cur_y)]
            self.set_limits(self.x, y_def + y_cur)
            self.current_plot.setData(self.x, y_cur)

        else:
            self.set_limits(self.x, y_def)
        # self.default_plot.setData(self.x, y_def)
        self.init_plot.setData(self.x, y_def)

    def reset_current_plot(self):
        self.current_plot.setData()
        self.cur_y = None
        self.current_point_text.setColor(color=(255, 255, 255))
        self.set_quantity()

    def draw_current_plot(self, current_drop):
        self.cur_y = current_drop
        self.current_point_text.setColor(color=(255, 170, 0))
        self.set_quantity()

    def draw_default_plot(self, distances, default_drop):
        self.x, self.def_y = distances, default_drop
        self.current_point_text.setColor(color=(255, 255, 255))
        self.set_quantity()

    def draw_init_plot(self, distances, default_drop):
        self.x, self.def_y = distances, default_drop
        self.current_point_text.setColor(color=(255, 255, 255))
        self.set_quantity()

    def set_cd_at_distance(self, x, y):
        self.cd_at_distance.setVisible(True)
        self.cd_at_distance.setPos((x, 0))
        self.cd_at_distance_text.setText(f'{x} m\n{rnd(self.y_quantity(y, x))} {self.y_q_label}')
        self.cd_at_distance_text.setPos(x, 0)

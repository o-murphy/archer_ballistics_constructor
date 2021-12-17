from gui.templates import Ui_DragFuncEdit
from PyQt5 import QtWidgets, QtCore
from gui.drag_func_plot import DragPlot
from gui.drop_func_plot import DropPlot
from modules import py_archer_ballistics
from modules import BConverter


TEST_DATA = [[0.00, 0.1198], [0.05, 0.1197], [0.10, 0.1196], [0.15, 0.1194], [0.20, 0.1193], [0.25, 0.1194], [0.30, 0.1194], [0.35, 0.1194], [0.40, 0.1193], [0.45, 0.1193], [0.50, 0.1194], [0.55, 0.1193], [0.60, 0.1194], [0.65, 0.1197], [0.70, 0.1202], [0.725, 0.1207], [0.75, 0.1215], [0.775, 0.1226], [0.80, 0.1242], [0.825, 0.1266], [0.85, 0.1306], [0.875, 0.1368], [0.90, 0.1464], [0.925, 0.1660], [0.95, 0.2054], [0.975, 0.2993], [1.0, 0.3803], [1.025, 0.4015], [1.05, 0.4043], [1.075, 0.4034], [1.10, 0.4014], [1.125, 0.3987], [1.15, 0.3955], [1.20, 0.3884], [1.25, 0.3810], [1.30, 0.3732], [1.35, 0.3657], [1.40, 0.3580], [1.50, 0.3440], [1.55, 0.3376], [1.60, 0.3315], [1.65, 0.3260], [1.70, 0.3209], [1.75, 0.3160], [1.80, 0.3117], [1.85, 0.3078], [1.90, 0.3042], [1.95, 0.3010], [2.00, 0.2980], [2.05, 0.2951], [2.10, 0.2922], [2.15, 0.2892], [2.20, 0.2864], [2.25, 0.2835], [2.30, 0.2807], [2.35, 0.2779], [2.40, 0.2752], [2.45, 0.2725], [2.50, 0.2697], [2.55, 0.2670], [2.60, 0.2643], [2.65, 0.2615], [2.70, 0.2588], [2.75, 0.2561], [2.80, 0.2533], [2.85, 0.2506], [2.90, 0.2479], [2.95, 0.2451], [3.00, 0.2424], [3.10, 0.2368], [3.20, 0.2313], [3.30, 0.2258], [3.40, 0.2205], [3.50, 0.2154], [3.60, 0.2106], [3.70, 0.2060], [3.80, 0.2017], [3.90, 0.1975], [4.00, 0.1935], [4.20, 0.1861], [4.40, 0.1793], [4.60, 0.1730], [4.80, 0.1672]]


rnd = BConverter.auto_rnd


class DragFuncEditDialog(QtWidgets.QDialog, Ui_DragFuncEdit):
    def __init__(self, data=None):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, True)
        self.setWindowTitle('ArcherBC - Drag Function Editor')
        self.ballistics = py_archer_ballistics.ArcherBallistics()

        self.drag_plot = DragPlot('drag_plot')
        self.set_distance_quantity()

        self.drop_plot = DropPlot('drop_plot')
        self.drop_plot.graphWidget.getPlotItem().vb.invertY(True)
        self.gridLayout.addWidget(self.drag_plot, 0, 1, 1, 2)
        self.gridLayout.addWidget(self.drop_plot, 0, 1, 1, 2)

        # self.switch_plot_drop()

        self.default_data = data if data else TEST_DATA
        self.current_data = None
        self.current_distance = None
        self.distances = []
        self.set_distances()
        self.default_drop = self.ballistics.calculate_drop(self.default_data, self.distances)
        self.current_drop = None
        self.dox, self.doy = self.parse_data(self.default_data)

        self.update_table()
        self.draw_drag_plot()

        self.PeakUp.clicked.connect(lambda: self.set_coefficient('mid', 1))
        self.PeakDown.clicked.connect(lambda: self.set_coefficient('mid', -1))
        self.Up.clicked.connect(lambda: self.set_coefficient('all', 1))
        self.Down.clicked.connect(lambda: self.set_coefficient('all', -1))
        self.EndUp.clicked.connect(lambda: self.set_coefficient('end', 1))
        self.EndDown.clicked.connect(lambda: self.set_coefficient('end', -1))

        self.buttonBox.button(QtWidgets.QDialogButtonBox.Reset).clicked.connect(self.reset)

        self.radioDrop.clicked.connect(self.switch_plot_drop)
        self.radioDrag.clicked.connect(self.switch_plot_drag)

        self.buttonBox.accepted.connect(self.accept)  # type: ignore
        self.buttonBox.rejected.connect(self.reject)  # type: ignore

        # self.calculate_bullet_drop()
        self.set_drop_table()

        self.set_hold_off_quantity()

        self.distanceQuantity.currentIndexChanged.connect(self.set_distance_quantity)
        self.holdOffQuantity.currentIndexChanged.connect(self.set_hold_off_quantity)

        self.dropTable.clicked.connect(lambda item: self.cd_at_distance(item))

    def set_distance_quantity(self):
        x_axis = self.drag_plot.graphWidget.getPlotItem().getAxis('bottom')
        self.drag_plot.x_quantity, self.drag_plot.x_q_label = 1, 'Mach'
        if self.distanceQuantity.currentIndex() == 1:
            self.drag_plot.x_quantity, self.drag_plot.x_q_label = 343, 'm/s'
        if self.distanceQuantity.currentIndex() == 2:
            self.drag_plot.x_quantity, self.drag_plot.x_q_label = 343 * 3.281, 'ft/s'
        x_axis.setScale(self.drag_plot.x_quantity)
        x_axis.setLabel(f"Velocity ({self.drag_plot.x_q_label})")

    def set_hold_off_quantity(self):
        quantity = self.holdOffQuantity.currentIndex()
        y_axis = self.drop_plot.graphWidget.getPlotItem().getAxis('left')
        if quantity == 1:
            self.drop_plot.y_q_label = 'MIL'
            self.drop_plot.q_func = BConverter.cm2mil
        elif quantity == 2:
            self.drop_plot.y_q_label = 'MOA'
            self.drop_plot.q_func = BConverter.cm2moa
        else:
            self.drop_plot.y_q_label = 'sm'
            self.drop_plot.q_func = BConverter.nothing
        y_axis.setLabel(self.drop_plot.y_q_label)

        default = [self.drop_plot.q_func(v, self.distances[k]) for k, v in enumerate(self.default_drop)]
        self.drop_plot.set_limits(self.distances, default)
        self.drop_plot.default_plot.setData(self.distances, default)

        if self.current_drop:
            current = [self.drop_plot.q_func(v, self.distances[k]) for k, v in enumerate(self.current_drop)]
            self.drop_plot.set_limits(self.distances, current + default)
            self.drop_plot.current_plot.setData(self.distances, current)

        # print(max(self.distances), min(self.distances), max(default), min(default))

    def draw_drag_plot(self):
        self.drag_plot.default_plot.setData(self.dox, self.doy)
        self.drag_plot.set_limits(self.dox, self.doy)
        self.drag_plot.set_text(self.dox[self.doy.index(max(self.doy))], max(self.doy), max(self.doy))
        self.drag_plot.peak_line.setPos((self.dox[self.doy.index(max(self.doy))], 0))
        self.drag_plot.peak_line.setVisible(True)

    def set_distances(self):
        for i in range(25, 2500, 25):
            self.distances.append(i)

    def set_drop_table(self):
        for i in range(0, 5):
            self.dropTable.insertRow(i)
            dist = QtWidgets.QTableWidgetItem()
            dist.setText(str((i+1)*100))
            self.dropTable.setItem(i, 0, dist)
            vz = QtWidgets.QTableWidgetItem()
            self.dropTable.setItem(i, 1, vz)

    def cd_at_distance(self, item=None):
        if item:
            self.current_distance = float(self.dropTable.item(item.row(), 0).text())
        self.ballistics.calculate_cd(distance=self.current_distance)

        ox, oy = self.parse_data(self.current_data)
        x, y = rnd(self.ballistics.cd_at_distance), rnd(min(oy))

        self.drag_plot.cd_at_distance.setVisible(True)
        self.drag_plot.cd_at_distance_text.setText(str(x*343))
        self.drag_plot.cd_at_distance_text.setPos(x, y)
        self.drag_plot.cd_at_distance.setPos((x, y))

        self.drop_plot.cd_at_distance.setVisible(True)
        self.drop_plot.cd_at_distance_text.setText(str(self.current_distance))
        self.drop_plot.cd_at_distance_text.setPos(rnd(self.current_distance), rnd(max(self.current_drop if self.current_drop else self.default_drop)))
        self.drop_plot.cd_at_distance.setPos((rnd(self.current_distance), rnd(max(self.current_drop if self.current_drop else self.default_drop))))

    def switch_plot_drop(self):
        self.drag_plot.setVisible(False)
        self.drop_plot.setVisible(True)
        pass

    def switch_plot_drag(self):
        self.drag_plot.setVisible(True)
        self.drop_plot.setVisible(False)
        pass

    def calculate_bullet_drop(self):
        if self.current_data:
            self.current_drop = self.ballistics.calculate_drop(self.current_data, self.distances)
        if self.current_distance:
            self.cd_at_distance()

    def update_table(self):
        for i in range(self.dragTable.columnCount()):
            self.dragTable.removeColumn(0)
        data = self.current_data if self.current_data else self.default_data
        if data:
            for k, v in enumerate(data):
                self.dragTable.insertColumn(k)
                iv = QtWidgets.QTableWidgetItem()
                iv.setText(str(rnd(v[0])))
                self.dragTable.setItem(0, k, iv)
                ii = QtWidgets.QTableWidgetItem()
                ii.setText(str(rnd(v[1])))
                self.dragTable.setItem(1, k, ii)
        self.drag_plot.current_point.setData()
        self.drag_plot.current_point_text.setText("")

    def reset(self):
        self.current_data = None  # self.default_data
        self.update_table()
        self.drag_plot.current_plot.setData()
        self.drag_plot.set_limits(self.dox, self.doy)
        self.drag_plot.set_text(self.dox[self.doy.index(max(self.doy))], max(self.doy), max(self.doy))
        self.drag_plot.current_point_text.setColor(color=(255, 255, 255))

        self.current_drop = None  # self.default_drop
        self.calculate_bullet_drop()
        self.drop_plot.current_plot.setData()
        self.drop_plot.current_point_text.setColor(color=(255, 255, 255))
        self.set_hold_off_quantity()

    def append_updates(self):
        self.update_table()
        self.drag_plot.default_plot.setData(*self.parse_data(self.default_data))
        ox, oy = self.parse_data(self.current_data)
        self.drag_plot.current_plot.setData(ox, oy)
        self.drag_plot.set_limits(ox + self.dox, oy + self.doy)
        self.drag_plot.set_text(ox[oy.index(max(oy))], max(oy), max(self.doy))
        self.drag_plot.current_point_text.setColor(color=(255, 170, 0))

        self.calculate_bullet_drop()
        # self.drop_plot.set_limits(self.distances, self.default_drop + self.current_drop)
        # self.drop_plot.current_plot.setData(self.distances, self.current_drop)
        self.drop_plot.current_point_text.setColor(color=(255, 170, 0))
        self.set_hold_off_quantity()

    @staticmethod
    def parse_data(data: list) -> dict or None:
        ox, oy = [i[0] for i in data], [i[1] for i in data]
        return ox, oy if ox and oy else None

    def set_coefficient(self, side, is_up):
        ox, oy = self.parse_data(self.current_data if self.current_data else self.default_data)
        if self.Step.value() > 0:
            max_y = max(oy)
            max_y_idx = oy.index(max_y)
            peak = ox[max_y_idx]
            step = self.Step.value() * is_up / 100
            new_data = []

            for i, x in enumerate(ox):
                if side in ['mid', 'middle']:
                    if x >= 1:
                        if x < peak:
                            x_min, x_max = ox[0], peak
                            oy[i] *= 1 + step * ((x - x_min) / (x_max - x_min))
                        elif x > peak:
                            x_min, x_max = ox[len(ox) - 1], peak
                            oy[i] *= 1 + step * ((x - x_min) / (x_max - x_min))
                        else:
                            oy[i] *= 1 + step
                elif side == 'end':
                    if x >= 1:
                        if x > peak:
                            x_max = peak
                            x_min = ox[len(ox) - 1]
                            oy[i] *= 1 + step * (1 - (x - x_min) / (x_max - x_min))
                elif side == 'all':
                    oy[i] *= 1 + step
                new_data.append([ox[i], oy[i]])
            self.current_data = new_data
            self.append_updates()

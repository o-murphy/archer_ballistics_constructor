from gui.templates import Ui_DragFuncEdit
from PyQt5 import QtWidgets
from gui.drag_func_plot import DragPlot
from modules import drop_by_drag


class DragFuncEditDialog(QtWidgets.QDialog, Ui_DragFuncEdit):
    def __init__(self, data=None):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('ArcherBC - Drag Function Editor')

        self.drag_plot = DragPlot('drag_plot')
        self.drop_plot = DragPlot('drop_plot')

        self.gridLayout.addWidget(self.drop_plot, 0, 1, 1, 4)
        self.gridLayout.addWidget(self.drag_plot, 0, 1, 1, 4)

        if not data:
            data = [[0.00, 0.1198], [0.05, 0.1197], [0.10, 0.1196], [0.15, 0.1194], [0.20, 0.1193], [0.25, 0.1194], [0.30, 0.1194], [0.35, 0.1194], [0.40, 0.1193], [0.45, 0.1193], [0.50, 0.1194], [0.55, 0.1193], [0.60, 0.1194], [0.65, 0.1197], [0.70, 0.1202], [0.725, 0.1207], [0.75, 0.1215], [0.775, 0.1226], [0.80, 0.1242], [0.825, 0.1266], [0.85, 0.1306], [0.875, 0.1368], [0.90, 0.1464], [0.925, 0.1660], [0.95, 0.2054], [0.975, 0.2993], [1.0, 0.3803], [1.025, 0.4015], [1.05, 0.4043], [1.075, 0.4034], [1.10, 0.4014], [1.125, 0.3987], [1.15, 0.3955], [1.20, 0.3884], [1.25, 0.3810], [1.30, 0.3732], [1.35, 0.3657], [1.40, 0.3580], [1.50, 0.3440], [1.55, 0.3376], [1.60, 0.3315], [1.65, 0.3260], [1.70, 0.3209], [1.75, 0.3160], [1.80, 0.3117], [1.85, 0.3078], [1.90, 0.3042], [1.95, 0.3010], [2.00, 0.2980], [2.05, 0.2951], [2.10, 0.2922], [2.15, 0.2892], [2.20, 0.2864], [2.25, 0.2835], [2.30, 0.2807], [2.35, 0.2779], [2.40, 0.2752], [2.45, 0.2725], [2.50, 0.2697], [2.55, 0.2670], [2.60, 0.2643], [2.65, 0.2615], [2.70, 0.2588], [2.75, 0.2561], [2.80, 0.2533], [2.85, 0.2506], [2.90, 0.2479], [2.95, 0.2451], [3.00, 0.2424], [3.10, 0.2368], [3.20, 0.2313], [3.30, 0.2258], [3.40, 0.2205], [3.50, 0.2154], [3.60, 0.2106], [3.70, 0.2060], [3.80, 0.2017], [3.90, 0.1975], [4.00, 0.1935], [4.20, 0.1861], [4.40, 0.1793], [4.60, 0.1730], [4.80, 0.1672]]

        self.default_data = data
        self.current_data = data

        self.update_table()

        self.dox, self.doy = self.parse_data(self.default_data)
        self.drag_plot.default_plot.setData(self.dox, self.doy)

        self.drag_plot.set_limits(self.dox, self.doy)
        self.drag_plot.set_text(self.dox[self.doy.index(max(self.doy))], max(self.doy), max(self.doy))
        self.drag_plot.peak_line.setPos((self.dox[self.doy.index(max(self.doy))], 0))

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

        self.distances = []
        self.current_drop = []
        for i in range(0, 10):
            self.tableWidget_2.insertRow(i)
            dist = QtWidgets.QTableWidgetItem()
            dist.setText(str((i+1)*100))
            self.tableWidget_2.setItem(i, 0, dist)
            self.distances.append((i+1)*100)
            vz = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setItem(i, 1, vz)
        self.calculate_bullet_drop()

        self.Calculate.clicked.connect(self.calculate_bullet_drop)

    def switch_plot_drop(self):
        self.drag_plot.setVisible(False)
        self.drop_plot.setVisible(True)
        pass

    def switch_plot_drag(self):
        self.drag_plot.setVisible(True)
        self.drop_plot.setVisible(False)
        pass

    def calculate_bullet_drop(self):
        self.current_drop.clear()
        self.current_drop = drop_by_drag.calculate(self.current_data, self.distances)
        for k, v in enumerate(self.current_drop):
            self.tableWidget_2.item(k, 1).setText(str(round(v, 2)))

    def update_table(self):
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.removeColumn(0)
        if self.current_data:
            for k, v in enumerate(self.current_data):
                self.tableWidget.insertColumn(k)
                iv = QtWidgets.QTableWidgetItem()
                iv.setText(str(round(v[0], 4)))
                self.tableWidget.setItem(0, k, iv)
                ii = QtWidgets.QTableWidgetItem()
                ii.setText(str(round(v[1], 4)))
                self.tableWidget.setItem(1, k, ii)

    def reset(self):
        self.current_data = self.default_data
        self.update_table()
        self.drag_plot.current_plot.setData()
        self.drag_plot.set_limits(self.dox, self.doy)
        self.drag_plot.set_text(self.dox[self.doy.index(max(self.doy))], max(self.doy), max(self.doy))
        self.drag_plot.current_point_text.setColor(color=(255, 255, 255))
        self.calculate_bullet_drop()

    def append_updates(self):
        self.update_table()
        self.drag_plot.default_plot.setData(*self.parse_data(self.default_data))
        ox, oy = self.parse_data(self.current_data)
        self.drag_plot.current_plot.setData(ox, oy)
        self.drag_plot.set_limits(ox + self.dox, oy + self.doy)
        self.drag_plot.set_text(ox[oy.index(max(oy))], max(oy), max(self.doy))
        self.drag_plot.current_point_text.setColor(color=(255, 170, 0))
        self.calculate_bullet_drop()

    @staticmethod
    def parse_data(data: list) -> dict or None:
        ox, oy = [i[0] for i in data], [i[1] for i in data]
        return ox, oy if ox and oy else None

    def set_coefficient(self, side, is_up):
        ox, oy = self.parse_data(self.current_data)
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

from gui.templates import Ui_DrugFuncEdit
from PyQt5 import QtWidgets
from gui.drug_func_plot import DrugPlot


class DrugFuncEditDialog(QtWidgets.QDialog, Ui_DrugFuncEdit):
    def __init__(self, data=None):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('ArcherBC - Drag Function Editor')
        self.plot = DrugPlot()
        self.gridLayout.addWidget(self.plot, 0, 0, 1, 4)

        if not data:
            data = [[0.00, 0.1198], [0.05, 0.1197], [0.10, 0.1196], [0.15, 0.1194], [0.20, 0.1193], [0.25, 0.1194], [0.30, 0.1194], [0.35, 0.1194], [0.40, 0.1193], [0.45, 0.1193], [0.50, 0.1194], [0.55, 0.1193], [0.60, 0.1194], [0.65, 0.1197], [0.70, 0.1202], [0.725, 0.1207], [0.75, 0.1215], [0.775, 0.1226], [0.80, 0.1242], [0.825, 0.1266], [0.85, 0.1306], [0.875, 0.1368], [0.90, 0.1464], [0.925, 0.1660], [0.95, 0.2054], [0.975, 0.2993], [1.0, 0.3803], [1.025, 0.4015], [1.05, 0.4043], [1.075, 0.4034], [1.10, 0.4014], [1.125, 0.3987], [1.15, 0.3955], [1.20, 0.3884], [1.25, 0.3810], [1.30, 0.3732], [1.35, 0.3657], [1.40, 0.3580], [1.50, 0.3440], [1.55, 0.3376], [1.60, 0.3315], [1.65, 0.3260], [1.70, 0.3209], [1.75, 0.3160], [1.80, 0.3117], [1.85, 0.3078], [1.90, 0.3042], [1.95, 0.3010], [2.00, 0.2980], [2.05, 0.2951], [2.10, 0.2922], [2.15, 0.2892], [2.20, 0.2864], [2.25, 0.2835], [2.30, 0.2807], [2.35, 0.2779], [2.40, 0.2752], [2.45, 0.2725], [2.50, 0.2697], [2.55, 0.2670], [2.60, 0.2643], [2.65, 0.2615], [2.70, 0.2588], [2.75, 0.2561], [2.80, 0.2533], [2.85, 0.2506], [2.90, 0.2479], [2.95, 0.2451], [3.00, 0.2424], [3.10, 0.2368], [3.20, 0.2313], [3.30, 0.2258], [3.40, 0.2205], [3.50, 0.2154], [3.60, 0.2106], [3.70, 0.2060], [3.80, 0.2017], [3.90, 0.1975], [4.00, 0.1935], [4.20, 0.1861], [4.40, 0.1793], [4.60, 0.1730], [4.80, 0.1672]]

        self.default_data = data
        self.current_data = data
        self.update_table()

        self.dox, self.doy = self.split_default_data()
        self.plot.default_plot.setData(self.dox, self.doy)

        self.plot.set_limits(max(self.dox), min(self.dox), max(self.doy), min(self.doy))
        self.plot.set_text(self.dox[self.doy.index(max(self.doy))], max(self.doy), max(self.doy))
        self.plot.set_point()

        self.PeakUp.clicked.connect(lambda: self.set_coefficient('mid', 1))
        self.PeakDown.clicked.connect(lambda: self.set_coefficient('mid', -1))
        self.Up.clicked.connect(lambda: self.set_coefficient('all', 1))
        self.Down.clicked.connect(lambda: self.set_coefficient('all', -1))
        self.EndUp.clicked.connect(lambda: self.set_coefficient('end', 1))
        self.EndDown.clicked.connect(lambda: self.set_coefficient('end', -1))

        self.buttonBox.button(QtWidgets.QDialogButtonBox.Reset).clicked.connect(self.reset)

        self.buttonBox.accepted.connect(self.accept)  # type: ignore
        self.buttonBox.rejected.connect(self.reject)  # type: ignore

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
        self.plot.current_plot.setData()
        self.plot.set_limits(max(self.dox), min(self.dox), max(self.doy), min(self.doy))
        self.plot.set_text(self.dox[self.doy.index(max(self.doy))], max(self.doy), max(self.doy))

    def append_updates(self):
        self.update_table()
        self.plot.default_plot.setData(*self.split_default_data())
        ox, oy = self.split_current_data()
        self.plot.current_plot.setData(ox, oy)
        self.plot.set_limits(max(ox), min(ox), max(oy), min(oy))
        self.plot.set_text(ox[oy.index(max(oy))], max(oy), max(self.doy))

    def split_default_data(self):
        ox, oy = [i[0] for i in self.default_data], [i[1] for i in self.default_data]
        return ox, oy

    def split_current_data(self):
        ox, oy = [i[0] for i in self.current_data], [i[1] for i in self.current_data]
        return ox, oy

    def set_coefficient(self, side, is_up):
        ox, oy = self.split_current_data()
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

    def on_ok(self):
        return self.current_data

from PyQt5 import QtWidgets, QtCore
from .templates import Ui_DragFuncEditDialog
from .drag_func_plot import DragPlot
from .drop_func_plot import DropPlot
from .drag_table import DragTable
from .bc_table import BCTable
from .drop_table_edit import DropTableEdit
from modules.py_archer_ballistics import ArcherBallistics, Profile
from modules import BConverter


TEST_DATA = [[0.00, 0.1198], [0.05, 0.1197], [0.10, 0.1196], [0.15, 0.1194], [0.20, 0.1193], [0.25, 0.1194], [0.30, 0.1194], [0.35, 0.1194], [0.40, 0.1193], [0.45, 0.1193], [0.50, 0.1194], [0.55, 0.1193], [0.60, 0.1194], [0.65, 0.1197], [0.70, 0.1202], [0.725, 0.1207], [0.75, 0.1215], [0.775, 0.1226], [0.80, 0.1242], [0.825, 0.1266], [0.85, 0.1306], [0.875, 0.1368], [0.90, 0.1464], [0.925, 0.1660], [0.95, 0.2054], [0.975, 0.2993], [1.0, 0.3803], [1.025, 0.4015], [1.05, 0.4043], [1.075, 0.4034], [1.10, 0.4014], [1.125, 0.3987], [1.15, 0.3955], [1.20, 0.3884], [1.25, 0.3810], [1.30, 0.3732], [1.35, 0.3657], [1.40, 0.3580], [1.50, 0.3440], [1.55, 0.3376], [1.60, 0.3315], [1.65, 0.3260], [1.70, 0.3209], [1.75, 0.3160], [1.80, 0.3117], [1.85, 0.3078], [1.90, 0.3042], [1.95, 0.3010], [2.00, 0.2980], [2.05, 0.2951], [2.10, 0.2922], [2.15, 0.2892], [2.20, 0.2864], [2.25, 0.2835], [2.30, 0.2807], [2.35, 0.2779], [2.40, 0.2752], [2.45, 0.2725], [2.50, 0.2697], [2.55, 0.2670], [2.60, 0.2643], [2.65, 0.2615], [2.70, 0.2588], [2.75, 0.2561], [2.80, 0.2533], [2.85, 0.2506], [2.90, 0.2479], [2.95, 0.2451], [3.00, 0.2424], [3.10, 0.2368], [3.20, 0.2313], [3.30, 0.2258], [3.40, 0.2205], [3.50, 0.2154], [3.60, 0.2106], [3.70, 0.2060], [3.80, 0.2017], [3.90, 0.1975], [4.00, 0.1935], [4.20, 0.1861], [4.40, 0.1793], [4.60, 0.1730], [4.80, 0.1672]]
test_data = {'z_d': 100, 'z_y': 0, 'z_x': 0, 'rifleName': '', 'caliberName': '.223 Remington', 'sh': 90, 'twist': 10,
             'caliberShort': '.233Rem', 'rightTwist': True, 'bulletName': '', 'weight': 69.0, 'length': 0.9,
             'diameter': 0.224, 'weightTile': '69gr', 'dragType': 1, 'bc': 0.169, 'cartridgeName': '', 'mv': 868,
             'temp': 15, 'ts': 1.55, 'z_temp': 15, 'z_angle': 0, 'z_pressure': 760, 'z_latitude': 0, 'z_humidity': 50,
             'z_azimuth': 270, 'z_powder_temp': 15}

rnd = BConverter.auto_rnd


class DragFuncEditDialog(QtWidgets.QDialog, Ui_DragFuncEditDialog):
    def __init__(self, cur_prof=None):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, True)
        self.setWindowTitle('ArcherBC - Drag Function Editor')
        self.ballistics = ArcherBallistics()

        self.bc_table = BCTable()
        self.drag_plot = DragPlot('drag_plot')
        self.drop_plot = DropPlot('drop_plot')
        self.drop_table_edit = DropTableEdit()
        self.dragTable = DragTable()

        self.cur_prof = cur_prof
        self.profile = None

        self.default_data = None
        self.current_data = None
        self.dox = None
        self.doy = None

        self.distances = []
        self.current_distance = None
        self.default_drop = None
        self.current_drop = None
        self.drop_table = None

        self.setProfile()
        self.setWidgets()

        self.setDrag()
        self.setDrops()
        self.setConnects()

    def setProfile(self):
        self.profile = Profile(self.cur_prof) if self.cur_prof else Profile(test_data)
        self.ballistics.set_profile(self.profile)
        if self.profile.DragFunc == 10 and self.profile.df_data:
            self.ballistics.set_drag_function(self.profile.df_data)
        self.ballistics.set_atmo(self.profile)
        self.ballistics.get_sound_speed()

    def setDrag(self):
        self.default_data = self.ballistics.get_drag_function()[::-1] if self.profile else TEST_DATA
        self.current_data = None
        self.dox, self.doy = self.parse_data(self.default_data)
        self.drag_plot.draw_default_plot(self.dox, self.doy)
        self.set_distance_quantity()
        self.update_drag_table()

    def setDrops(self):
        self.drop_table = self.drop_table_edit.drop_table
        self.set_distances()
        self.default_drop = [rnd(i) for i in self.ballistics.calculate_drop(self.default_data, self.distances)]
        self.drop_plot.draw_default_plot(self.distances, self.default_drop)
        self.set_hold_off_quantity()
        self.drop_table_edit.drop_table.set()

    def setWidgets(self):
        self.gridLayout.addWidget(self.bc_table, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.drag_plot, 0, 1, 1, 2)
        self.gridLayout.addWidget(self.drop_plot, 0, 1, 1, 2)
        self.gridLayout.addWidget(self.drop_table_edit, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.dragTable, 4, 0, 1, 4)
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 4)

        self.distanceQuantity.setItemData(0, 1)
        self.distanceQuantity.setItemData(1, self.ballistics.sound_speed)
        self.distanceQuantity.setItemData(2, self.ballistics.sound_speed * 3.281)

        self.holdOffQuantity.setItemData(0, BConverter.nothing)
        self.holdOffQuantity.setItemData(1, BConverter.cm2mil)
        self.holdOffQuantity.setItemData(2, BConverter.cm2moa)

    def setConnects(self):
        self.PeakUp.clicked.connect(lambda: self.set_coefficient('mid', 1))
        self.PeakDown.clicked.connect(lambda: self.set_coefficient('mid', -1))
        self.Up.clicked.connect(lambda: self.set_coefficient('all', 1))
        self.Down.clicked.connect(lambda: self.set_coefficient('all', -1))
        self.EndUp.clicked.connect(lambda: self.set_coefficient('end', 1))
        self.EndDown.clicked.connect(lambda: self.set_coefficient('end', -1))

        self.radioDrop.clicked.connect(self.switch_plot_drop)
        self.radioDrag.clicked.connect(self.switch_plot_drag)

        self.buttonBox.button(QtWidgets.QDialogButtonBox.Reset).clicked.connect(self.reset)
        self.buttonBox.accepted.connect(self.accept)  # type: ignore
        self.buttonBox.rejected.connect(self.reject)  # type: ignore

        self.distanceQuantity.currentIndexChanged.connect(self.set_distance_quantity)
        self.holdOffQuantity.currentIndexChanged.connect(self.set_hold_off_quantity)

        self.drop_table.clicked.connect(lambda item: self.cd_at_distance(item))

    def set_hold_off_quantity(self):
        self.drop_plot.y_q_label = self.holdOffQuantity.currentText()
        self.drop_plot.y_quantity = self.holdOffQuantity.currentData()
        self.drop_plot.set_quantity()

    def set_distance_quantity(self):
        self.drag_plot.x_q_label = self.distanceQuantity.currentText()
        self.drag_plot.x_quantity = self.distanceQuantity.currentData()
        self.drag_plot.set_distance_quantity()

    def set_distances(self):
        for i in range(25, 2500, 25):
            self.distances.append(i)

    """ TEMPORARY """
    def cd_at_distance(self, item=None):
        if item:
            self.current_distance = self.drop_table.cellWidget(item.row(), 0).value()
            self.ballistics.calculate_cd(distance=self.current_distance)
            ox, oy = self.parse_data(self.current_data if self.current_data else self.default_data)
            x, y = rnd(self.ballistics.cd_at_distance), rnd(min(oy))
            self.drag_plot.set_cd_at_distance(x, y)

    def switch_plot_drop(self):
        self.drag_plot.setVisible(False), self.drop_plot.setVisible(True)

    def switch_plot_drag(self):
        self.drag_plot.setVisible(True), self.drop_plot.setVisible(False)

    def calculate_bullet_drop(self):
        if self.current_data:
            self.current_drop = self.ballistics.calculate_drop(self.current_data, self.distances)
        if self.current_distance:
            self.cd_at_distance()

    def update_drag_table(self):
        self.dragTable.set(self.current_data, self.default_data)
        self.drag_plot.current_point.setData()
        self.drag_plot.current_point_text.setText("")

    def reset(self):
        self.current_data = None  # self.default_data
        self.update_drag_table()
        self.drag_plot.reset_current_plot()

        self.current_drop = None  # self.default_drop
        self.calculate_bullet_drop()
        self.drop_plot.reset_current_plot()

    def append_updates(self):
        self.ballistics.drag_function = self.current_data
        self.ballistics.set_drag_function(self.ballistics.drag_function)
        self.update_drag_table()
        self.drag_plot.draw_current_plot(self.parse_data(self.current_data)[1])

        self.calculate_bullet_drop()
        self.drop_plot.draw_custom_plot(self.current_drop)

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

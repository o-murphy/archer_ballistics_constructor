from PyQt5 import QtWidgets, QtCore, QtGui
from .templates import Ui_DragFuncEditDialog
from .drag_func_plot import DragPlot
from .drop_func_plot import DropPlot
from .drag_table import DragTable
from .bc_table import BCTable
from .drop_table_edit import DropTableEdit
from .current_atmo_dialog import CurrentAtmoDialog
from modules.py_archer_ballistics import ArcherBallistics, Profile
from modules import BConverter

from ..stylesheet import load_qss

rnd = BConverter.auto_rnd


class DragFuncEditDialog(QtWidgets.QDialog, Ui_DragFuncEditDialog):
    def __init__(self, cur_prof=None, bc_table=None):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet(load_qss('qss/dialog.qss'))

        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, True)
        self.setWindowTitle('ArcherBC - Drag Function Editor')
        self.ballistics = ArcherBallistics()

        self.bc_table = bc_table if bc_table else BCTable()
        self.drag_plot = DragPlot('drag_plot')
        self.drop_plot = DropPlot('drop_plot')
        self.drop_table_edit = DropTableEdit()
        self.dragTable = DragTable()
        self.drop_table = self.drop_table_edit.drop_table

        self.current_atmo_dlg = CurrentAtmoDialog()

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

        self.setProfile()
        self.setWidgets()

        self.setDrag()
        self.setDrops()
        self.setConnects()

    def setProfile(self):
        self.profile = Profile(self.cur_prof) if self.cur_prof else None
        self.ballistics.set_profile(self.profile)
        if self.profile.DragFunc == 10 and self.profile.df_data:
            self.ballistics.set_drag_function(self.profile.df_data)
        self.ballistics.set_atmo(self.profile)
        self.ballistics.get_sound_speed()

    def setDrag(self):
        self.default_data = self.ballistics.get_drag_function()[::-1] if self.profile else None
        self.current_data = None
        self.dox, self.doy = self.parse_data(self.default_data)
        self.drag_plot.draw_default_plot(self.dox, self.doy)
        self.set_distance_quantity()
        self.update_drag_table()

    def setDrops(self):
        self.set_distances()
        self.default_drop = [rnd(i) for i in self.ballistics.calculate_drop(self.default_data, self.distances)]
        self.drop_plot.draw_default_plot(self.distances, self.default_drop)
        self.set_hold_off_quantity()

        self.drop_table_edit.drop_table.set()
        self.custom_drop_at_distance()

    def setWidgets(self):
        spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addWidget(self.bc_table, 0, 0, 1, 1)
        self.gridLayout.addItem(spacer, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.drag_plot, 0, 1, 2, 2)
        self.gridLayout.addWidget(self.drop_plot, 0, 1, 2, 2)
        self.gridLayout.addWidget(self.drop_table_edit, 0, 3, 2, 1)
        self.gridLayout.addWidget(self.dragTable, 5, 0, 1, 4)
        self.gridLayout.addWidget(self.dragTableToolBox, 6, 1, 1, 1)
        self.gridLayout.addWidget(self.buttonBox, 7, 0, 1, 4)

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
        self.holdOffQuantity.currentIndexChanged.connect(lambda: (
            self.set_hold_off_quantity(), self.cd_at_distance()
        ))
        self.drop_table.clicked.connect(self.cd_at_distance)
        self.drop_table_edit.addRow.clicked.connect(lambda: (
            self.drop_table_edit.add_row(), self.custom_drop_at_distance()
        ))
        self.Calculate.clicked.connect(self.custom_drop_at_distance)
        self.SetConditions.clicked.connect(self.current_atmo_dialog)
        self.buttonBox.keyPressEvent = self.keyPressEvent

        self.copyTable.clicked.connect(self.copy_table)
        self.pasteTable.clicked.connect(self.paste_table)

    def keyPressEvent(self, e: QtGui.QKeyEvent) -> None:
        if e.key() == QtCore.Qt.Key_Enter:
            e.ignore()

    def custom_drop_at_distance(self):
        d = [self.drop_table.cellWidget(r, 0).value() for r in range(self.drop_table.rowCount())]
        self.ballistics.get_drop_at_distance(d)
        [self.drop_table.cellWidget(i, 1).sb.setValue(v) for i, v in enumerate(self.ballistics.drop_at_distance)]

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

    def cd_at_distance(self):
        self.current_distance = self.drop_table.cellWidget(self.drop_table.currentRow(), 0).value()
        drop = self.drop_table.cellWidget(self.drop_table.currentRow(), 1).sb.value()
        self.ballistics.calculate_cd(distance=self.current_distance)
        ox, oy = self.parse_data(self.current_data if self.current_data else self.default_data)
        x, y = rnd(self.ballistics.cd_at_distance), rnd(min(oy))
        self.drag_plot.set_cd_at_distance(x, y)
        self.drop_plot.set_cd_at_distance(self.current_distance, drop)

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

    def current_atmo_dialog(self):
        ok = self.current_atmo_dlg.exec_()
        if ok:
            atmo = self.current_atmo_dlg.get_atmo()

    def copy_table(self):
        datasheet = '\n'.join([f'{str(rnd(v)).replace(".", ",")}\t{str(rnd(i)).replace(".", ",")}' for v, i in (
            self.current_data if self.current_data else self.default_data
        )])
        cb = QtWidgets.QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(datasheet, mode=cb.Clipboard)

    # TODO:
    def paste_table(self):
        try:
            cb = QtWidgets.QApplication.clipboard()
            new_data = [
                [float(j.replace(',', '.')) for j in i.split('\t')
                 if not j == ''] for i in cb.text().split('\n') if i.split('\t') != []
            ][::-1]
            print(new_data)
            self.current_data = new_data
            self.append_updates()
        except Exception as error:
            print(error)

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

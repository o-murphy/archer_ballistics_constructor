from PyQt5 import QtWidgets, QtCore, QtGui
from .templates import Ui_DragFuncEditDialog
from .drag_func_plot import DragPlot
from .drop_func_plot import DropPlot
from .drag_table import DragTable
from ..bc_table import BCTable
from .drop_table_edit import DropTableEdit
from .current_atmo_dialog import CurrentAtmoDialog
from modules import ArcherBallistics, Profile
from modules import BConverter
from modules import State, StateDidUpdate
from modules.env_update import USER_RECENT

from ..stylesheet import load_qss

rnd = BConverter.auto_rnd

default_g1 = """
0,0	0,263
0,5	0,203
0,6	0,203
0,7	0,217
0,8	0,255
0,9	0,342
0,95	0,408
1,0	0,481
1,05	0,543
1,1	0,588
1,2	0,639
1,3	0,659
1,4	0,663
1,5	0,657
1,6	0,647
1,8	0,621
2,0	0,593
2,2	0,569
2,5	0,54
3,0	0,513
3,5	0,504
4,0	0,501
"""

DEFAULTS = {
    'default_data': None,
    'current_data': None,
    'distances': None,
    'current_distance': None,
    'default_drop': None,
    'current_drop': None,
    'rifleName': 'Template',
    'caliberName': '.308 Win',
    'sh': 90,
    'twist': 11,
    'caliberShort': '',
    'rightTwist': True,
    'bulletName': 'Hornady ELD Match',
    'weight': 178.0,
    'length': 1.3,
    'diameter': 0.308,
    'weightTile': '178gr',
    'drags': [],
    'drag_idx': -1,
    'cartridgeName': 'Template',
    'mv': 800,
    'temp': 15,
    'ts': 1.55,
    'z_pressure': 760,
    'z_angle': 0,
    'z_temp': 15,
    'z_humidity': 50,
    'z_azimuth': 270,
    'z_latitude': 0,
    'z_powder_temp': 15,
    'z_d': 100,
    'z_x': 0.0,
    'z_y': 0.0,
    'df_data': None,
    'df_type': 'Custom'
}


class DragFuncEditDialog(QtWidgets.QDialog, Ui_DragFuncEditDialog):
    def __init__(self, state: dict = None):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet(load_qss('qss/dialog.qss'))

        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, True)
        self.setWindowTitle('ArcherBC - Drag Function Editor')

        self.mbc = None

        self.state = State(self, **DEFAULTS)

        if state:
            self.setState(**state)
            self.dfComment.setText(
                self.state.df_type + ': ' + self.state.df_comment
            )
            if self.state.df_type.endswith('Multi-BC'):
                self.mbc = BCTable(self)
                # if not self.state.df_data:
                #     self.state.df_data = [
                #         [1, 1000], [0, 0], [0, 0], [0, 0], [0, 0]
                #     ]
                if self.state.df_data:
                    self.mbc.set_data(self.state.df_data)

                self.gridLayout.addWidget(self.mbc, 0, 0, 1, 1)

                self.importDF.setDisabled(True)
                self.pasteTable.setDisabled(True)


        self.onStateUpdate.connect(self.state_did_update)
        # self.onStateSet.connect(self.state_did_set)

        self.ballistics = ArcherBallistics()

        self.drag_plot = DragPlot('drag_plot')
        self.drop_plot = DropPlot('drop_plot')
        self.drop_table_edit = DropTableEdit(self)
        self.dragTable = DragTable()
        self.dragTable.readonly()

        self.drop_table = self.drop_table_edit.drop_table
        self.current_atmo_dlg = CurrentAtmoDialog()

        self.profile = Profile(self.state.__dict__)

        self.setProfile()
        self.setWidgets()

        self.dox = None
        self.doy = None

        self.updateState(
            default_data=self.ballistics.get_drag_function() if self.profile else None,
            distances=[i for i in range(25, 2500, 25)]
        )

        if state:
            self.updateState(default_drop=[rnd(i) for i in self.ballistics.calculate_drop(
                self.state.default_data, self.state.distances)])

        self.setConnects()

    def mbc_edit(self):
        mbc = self.mbc.get_data()
        self.profile.set_bc(mbc)
        self.setProfile()
        self.updateState(
            current_data=self.ballistics.get_drag_function() if self.profile else None,
            distances=[i for i in range(25, 2500, 25)]
        )
        # self.updateState(default_drop=[rnd(i) for i in self.ballistics.calculate_drop(
        #     self.state.default_data, self.state.distances)])
        self.append_updates()
        self.custom_drop_at_distance()

    def setProfile(self):
        self.ballistics.set_profile(self.profile)
        if self.profile.DragFunc == 10 and self.profile.df_data:
            self.ballistics.set_drag_function(self.profile.df_data)
        self.ballistics.set_atmo(self.profile)
        self.ballistics.get_sound_speed()

    def state_did_update(self, e):
        if isinstance(e, StateDidUpdate):
            if e.key == 'default_data':
                self.setDrag()

            if e.key == 'default_drop':
                self.setDrops()

    def setDrag(self):
        self.dox, self.doy = self.parse_data(self.state.default_data)
        self.drag_plot.draw_default_plot(self.dox, self.doy)
        self.set_distance_quantity()
        self.update_drag_table()

    def setDrops(self):
        self.drop_plot.draw_default_plot(self.state.distances, self.state.default_drop)
        self.set_hold_off_quantity()
        self.drop_table_edit.drop_table.set()
        self.custom_drop_at_distance()

    def setWidgets(self):
        # spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.gridLayout.addWidget(self.bc_table, 0, 0, 1, 1)
        # self.gridLayout.addItem(spacer, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.drag_plot, 0, 1, 2, 2)
        self.gridLayout.addWidget(self.drop_plot, 0, 1, 2, 2)
        self.gridLayout.addWidget(self.drop_table_edit, 0, 3, 2, 1)
        self.gridLayout.addWidget(self.dragTable, 5, 0, 1, 4)
        self.gridLayout.addWidget(self.dragTableToolBox, 6, 0, 1, 4)
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
        self.drop_table.tableWidget.clicked.connect(self.cd_at_distance)
        self.drop_table_edit.addRow.clicked.connect(lambda: (
            self.drop_table_edit.add_row(), self.custom_drop_at_distance()
        ))
        # self.Calculate.clicked.connect(
        #     lambda: self.setState(bcTable=self.bc_table.get_data()) if isinstance(self.bc_table, BCTable)
        #     else self.setState(bc=self.bc_table.value())
        # )
        self.SetConditions.clicked.connect(self.current_atmo_dialog)
        self.buttonBox.keyPressEvent = self.keyPressEvent

        self.copyTable.clicked.connect(self.copy_table)
        self.pasteTable.clicked.connect(self.paste_table)

        self.importDF.clicked.connect(self.import_table)
        self.exportDF.clicked.connect(self.export_table)

    def keyPressEvent(self, e: QtGui.QKeyEvent) -> None:
        if e.key() == QtCore.Qt.Key_Enter:
            e.ignore()

    def custom_drop_at_distance(self):
        d = [int(self.drop_table.tableWidget.item(r, 0).text()) for r in range(self.drop_table.tableWidget.rowCount())]
        self.ballistics.get_drop_at_distance(d)
        [self.drop_table.set_item_data(i, 1, rnd(v)) for i, v in enumerate(self.ballistics.drop_at_distance)]

    def set_hold_off_quantity(self):
        self.drop_plot.y_q_label = self.holdOffQuantity.currentText()
        self.drop_plot.y_quantity = self.holdOffQuantity.currentData()
        self.drop_plot.set_quantity()

    def set_distance_quantity(self):
        self.drag_plot.x_q_label = self.distanceQuantity.currentText()
        self.drag_plot.x_quantity = self.distanceQuantity.currentData()
        self.drag_plot.set_distance_quantity()

    """ TEMPORARY """

    def cd_at_distance(self):
        self.updateState(current_distance=self.drop_table.get_current_distance())
        drop = self.drop_table.get_current_drop()

        self.ballistics.calculate_cd(distance=self.state.current_distance)
        ox, oy = self.parse_data(self.state.current_data if self.state.current_data else self.state.default_data)
        x, y = rnd(self.ballistics.cd_at_distance), rnd(min(oy))
        self.drag_plot.set_cd_at_distance(x, y)
        self.drop_plot.set_cd_at_distance(self.state.current_distance, drop)

    def switch_plot_drop(self):
        self.drag_plot.setVisible(False), self.drop_plot.setVisible(True)

    def switch_plot_drag(self):
        self.drag_plot.setVisible(True), self.drop_plot.setVisible(False)

    def calculate_bullet_drop(self):
        if self.state.current_data:
            self.state.current_drop = self.ballistics.calculate_drop(self.state.current_data, self.state.distances)
        if self.state.current_distance:
            self.cd_at_distance()

    def update_drag_table(self):
        self.dragTable.set(self.state.current_data, self.state.default_data)
        self.drag_plot.current_point.setData()
        self.drag_plot.current_point_text.setText("")

    def reset(self):
        self.updateState(current_data=None)

        self.update_drag_table()
        self.drag_plot.reset_current_plot()

        self.updateState(current_drop=None)
        self.calculate_bullet_drop()
        self.drop_plot.reset_current_plot()

    def append_updates(self):
        self.ballistics.drag_function = self.state.current_data
        self.ballistics.set_drag_function(self.ballistics.drag_function)
        self.update_drag_table()
        self.drag_plot.draw_current_plot(
            self.parse_data(self.state.current_data)[0],
            self.parse_data(self.state.current_data)[1]
        )

        self.calculate_bullet_drop()
        self.drop_plot.draw_custom_plot(self.state.current_drop)

    def current_atmo_dialog(self):
        ok = self.current_atmo_dlg.exec_()
        if ok:
            atmo = self.current_atmo_dlg.get_atmo()

    # def copy_table(self):
    #     datasheet = '\n'.join([f'{str(rnd(v)).replace(".", ",")}\t{str(rnd(i)).replace(".", ",")}' for v, i in (
    #         self.state.current_data if self.state.current_data else self.state.default_data
    #     )])
    #     cb = QtWidgets.QApplication.clipboard()
    #     cb.clear(mode=cb.Clipboard)
    #     cb.setText(datasheet, mode=cb.Clipboard)

    def copy_table(self):
        data = self.state.current_data if self.state.current_data else self.state.default_data
        datasheet = []
        for (v, c) in data:
            datasheet.append(f"{str(v).replace(r'.', r',')}\t{str(c).replace(r'.', r',')}")
        datasheet = '\n'.join(datasheet)

        cb = QtWidgets.QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(datasheet, mode=cb.Clipboard)

    def paste_table(self):
        cb = QtWidgets.QApplication.clipboard()
        lines = cb.text().split('\n')
        pairs = [i.split('\t') for i in lines if len(i.split('\t')) == 2]
        float_pairs = [[float(i.replace(',', '.')), float(j.replace(',', '.'))] for i, j in pairs]
        self.updateState(current_data=float_pairs)
        self.dragTable.set(self.state.current_data, self.state.default_data)
        self.append_updates()

    @staticmethod
    def parse_data(data: list) -> dict or None:
        if data:
            ox, oy = [i[0] for i in data], [i[1] for i in data]
            return ox, oy if ox and oy else None
        else:
            return None

    def set_coefficient(self, side, is_up):
        ox, oy = self.parse_data(self.state.current_data if self.state.current_data else self.state.default_data)
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
            self.updateState(current_data=new_data)
            self.append_updates()

    def __getstate__(self):
        new_state = self.state.__dict__
        is_new_data = True if self.state.current_data else False

        if is_new_data:
            new_state['df_data'] = self.state.current_data
            new_state['dragType'] = 2
        else:
            new_state['df_data'] = self.state.default_data

        [new_state.pop(key) for key in ['default_data',
                                        'current_data',
                                        'distances',
                                        'current_distance',
                                        'default_drop',
                                        'current_drop']]
        return new_state

    def import_table(self):
        options = QtWidgets.QFileDialog.Options()
        fileName, fileFormat = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "QFileDialog.getOpenFileName()",
            USER_RECENT,
            "Drag function (*.drg;*.snr;*.ardrg)",
            options=options
        )
        if fileName:
            from modules import FileParse
            fp = FileParse()
            data, comment = fp.open_format(fileFormat, fileName)
            if data:
                if not self.state.default_data:
                    self.updateState(default_data=data)
                else:
                    self.updateState(current_data=data)
                self.dragTable.set(self.state.current_data, self.state.default_data)
                self.append_updates()

            self.dfComment.setText(comment.replace('\n', '')[:80])

    def export_table(self, fileName=None):
        data = self.state.current_data
        if data:

            options = QtWidgets.QFileDialog.Options()
            fileName, fileFormat = QtWidgets.QFileDialog.getSaveFileName(
                self,
                "QFileDialog.getSaveFileName()",
                rf'{USER_RECENT}\{fileName}' if fileName else rf'{USER_RECENT}\recent_',
                "Drag function (*.drg;*.snr;*.ardrg)",
                options=options
            )
            if fileName:
                from modules import FileParse
                fp = FileParse()
                result = fp.save_format(fileFormat, fileName, data, fileName)

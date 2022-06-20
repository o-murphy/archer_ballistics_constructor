from PyQt5 import QtWidgets, QtCore, QtGui

try:
    from .templates import Ui_DragFuncEditDialog
    from .drag_func_plot import DragPlot
    from .drop_func_plot import DropPlot
    from .drag_table import DragTable
    from ..bc_table import BCTable
    from .drop_table_edit import DropTableEdit
    from .current_atmo_dialog import CurrentAtmoDialog
    from .defaults import DEFAULTS
    from ..stylesheet import load_qss
    from .drag_editor_state import DragEditorState

except Exception as exception:
    from gui.drag_func_editor.templates import Ui_DragFuncEditDialog
    from gui.drag_func_editor.drag_func_plot import DragPlot
    from gui.drag_func_editor.drop_func_plot import DropPlot
    from gui.drag_func_editor.drag_table import DragTable
    from gui.bc_table import BCTable
    from gui.drag_func_editor.drop_table_edit import DropTableEdit
    from gui.drag_func_editor.current_atmo_dialog import CurrentAtmoDialog
    from gui.drag_func_editor.defaults import DEFAULTS
    from gui.stylesheet import load_qss
    from gui.drag_func_editor.drag_editor_state import DragEditorState

from modules import BConverter
from modules.env_update import USER_RECENT

rnd = BConverter.auto_rnd


class DragFuncEditDialog(QtWidgets.QDialog, Ui_DragFuncEditDialog):

    def __init__(self, state: dict = None):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet(load_qss('qss/dialog.qss'))

        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, True)
        self.setWindowTitle('ArcherBC - Drag Function Editor')
        self.dfComment.setStyleSheet("""color: orange; font-size: 14px;""")

        self.defaults = state

        self.state = DragEditorState(self, state)

        self.onStateUpdate.connect(self.state_did_update)

        self.dfType.setText(self.state.df_type + ':')
        self.dfComment.setText(self.state.df_comment)
        self.dfComment.setText(self.state.df_comment)

        self.mbc = BCTable(self)
        self.sbc = QtWidgets.QDoubleSpinBox(self)
        self.sbc.setMaximum(10)
        self.sbc.setMinimum(0.001)
        self.sbc.setDecimals(3)
        self.sbc.setSingleStep(0.001)

        spolicy = QtWidgets.QSizePolicy()
        spolicy.setVerticalPolicy(QtWidgets.QSizePolicy.Expanding)
        spolicy.setHorizontalPolicy(QtWidgets.QSizePolicy.Expanding)

        self.sbc.setSizePolicy(spolicy)

        self.calculation_mode = QtWidgets.QComboBox(self)

        self.calculation_mode.addItem('G1', 'G1')
        self.calculation_mode.addItem('G7', 'G7')
        self.calculation_mode.addItem('G1 Multi-BC', 'G1 Multi-BC')
        self.calculation_mode.addItem('G7 Multi-BC', 'G7 Multi-BC')
        self.calculation_mode.addItem('Custom drag func', 'Custom')
        self.calculation_mode.setCurrentIndex(self.calculation_mode.findData(self.state.df_type))

        self.drag_plot = DragPlot('drag_plot')
        self.drop_plot = DropPlot('drop_plot')
        self.drop_table_edit = DropTableEdit(self)
        self.dragTable = DragTable()
        self.dragTable.readonly()

        self.drop_table = self.drop_table_edit.drop_table
        self.current_atmo_dlg = CurrentAtmoDialog()
        self.setWidgets()

        self.dox = None
        self.doy = None

        self.updateState(
            default_drag_func=self.state.drag_function if self.state.profile else None,
            distances=self.state.distances_generator()
        )

        if state:
            drops = self.state.calculate_drop(self.state.default_drag_func)
            default_drop = [rnd(i) for i in drops]
            self.updateState(default_drop=default_drop)

        self.switch_calculation_mode()

        self.setConnects()

    def switch_calculation_mode(self):
        # self.updateState(df_type=self.calculation_mode.currentData())

        self.state.df_type = self.calculation_mode.currentData()

        if self.state.df_type == 'Custom':
            self.importDF.setEnabled(True)
            self.pasteTable.setEnabled(True)
            self.mbc.setDisabled(True)
            self.mbc.setVisible(False)
            self.sbc.setDisabled(True)
            self.sbc.setVisible(False)

        elif self.state.df_type.endswith('Multi-BC'):

            self.mbc.bc_table.setRowCount(5)

            if isinstance(self.state.df_data, float):
                self.state.df_data = ((self.state.mv, self.state.df_data),)

            if self.state.df_data:
                self.mbc.set_data(self.state.df_data)
            self.mbc.setEnabled(True)
            self.mbc.setVisible(True)
            self.sbc.setVisible(False)
            self.sbc.setEnabled(False)
            self.importDF.setDisabled(True)
            self.pasteTable.setDisabled(True)

        elif self.state.df_type in ['G1', 'G7']:

            if isinstance(self.state.df_data, tuple) or isinstance(self.state.df_data, list):
                self.state.mv, self.state.df_data = self.state.df_data[0]

            self.sbc.setValue(self.state.df_data)

            self.mbc.setDisabled(True)
            self.mbc.setVisible(False)
            self.sbc.setVisible(True)
            self.sbc.setEnabled(True)

            self.importDF.setDisabled(True)
            self.pasteTable.setDisabled(True)

        self.updateState()

    def mbc_edit(self):
        mbc = self.mbc.get_data()
        self.state.df_data = mbc

        print(f'\n\ndf_data: {self.state.df_data}\n\n')

        self.updateState()
        # self.append_updates()
        # self.custom_drop_at_distance()

    def sbc_changed(self, e):
        self.state.df_data = e
        self.updateState()

    def state_did_update(self, e):

        self.state.setProfile()
        self.state.current_drag_func = self.state.drag_function

        self.update_drag_table()
        self.drag_plot.draw_current_plot(*self.parse_data(self.state.current_drag_func))

        if hasattr(e, 'default_drag_func'):
            self.setDefaultDrag()

        try:
            drops = self.state.calculate_drop(self.state.current_drag_func)
            if drops:
                self.state.current_drop = [rnd(i) for i in drops]
                if self.state.current_drop:
                    self.drop_plot.draw_current_plot(self.state.current_drop)
        except TypeError as err:
            print(err)

        self.custom_drop_at_distance()

        if hasattr(e, 'default_drop'):
            self.setDefaultDrops()

        self.cd_at_distance()

    def setDefaultDrag(self):
        from calculator.calculator import DragFunctions

        if self.state.df_type in ['G1', 'G1 Multi-BC']:
            self.dox, self.doy = self.parse_data(DragFunctions.G1)
        elif self.state.df_type in ['G7', 'G7Multi-BC']:
            self.dox, self.doy = self.parse_data(DragFunctions.G7)
        else:
            self.dox, self.doy = self.parse_data(self.state.df_data)

        self.drag_plot.draw_default_plot(self.dox, self.doy)

        self.set_distance_quantity()
        self.update_drag_table()

    def setDefaultDrops(self):
        self.drop_plot.draw_default_plot(self.state.distances, self.state.default_drop)
        self.set_hold_off_quantity()
        self.drop_table_edit.drop_table.set()
        self.custom_drop_at_distance()

    def setWidgets(self):
        self.gridLayout.addWidget(self.drag_plot, 0, 1, 2, 2)
        self.gridLayout.addWidget(self.drop_plot, 0, 1, 2, 2)

        self.gridLayout.addWidget(self.mbc, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.sbc, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.calculation_mode, 1, 0)

        self.gridLayout.addWidget(self.drop_table_edit, 0, 3, 2, 1)
        self.gridLayout.addWidget(self.dragTable, 5, 0, 1, 4)
        self.gridLayout.addWidget(self.dragTableToolBox, 6, 0, 1, 4)
        self.gridLayout.addWidget(self.buttonBox, 7, 0, 1, 4)

        self.distanceQuantity.setItemData(0, 1)
        self.distanceQuantity.setItemData(1, self.state.sound_speed)
        self.distanceQuantity.setItemData(2, self.state.sound_speed * 3.281)

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

        self.SetConditions.clicked.connect(self.current_atmo_dialog)
        self.buttonBox.keyPressEvent = self.keyPressEvent

        self.copyTable.clicked.connect(self.copy_table)
        self.pasteTable.clicked.connect(self.paste_table)

        self.importDF.clicked.connect(self.import_table)
        self.exportDF.clicked.connect(self.export_table)

        self.calculation_mode.currentIndexChanged.connect(self.switch_calculation_mode)
        self.sbc.valueChanged.connect(self.sbc_changed)

    def keyPressEvent(self, e: QtGui.QKeyEvent) -> None:
        if e.key() == QtCore.Qt.Key_Enter:
            e.ignore()

    def custom_drop_at_distance(self):
        d = [self.drop_table.tableWidget.item(r, 0).text() for r in range(self.drop_table.tableWidget.rowCount())]
        d = [int(i) for i in d]

        [self.drop_table.set_item_data(i, 1, rnd(v)) for i, v in enumerate(self.state.drop_at_distance())]

    def set_hold_off_quantity(self):
        self.drop_plot.y_q_label = self.holdOffQuantity.currentText()
        self.drop_plot.y_quantity = self.holdOffQuantity.currentData()
        self.drop_plot.set_quantity()

    def set_distance_quantity(self):
        self.drag_plot.x_q_label = self.distanceQuantity.currentText()
        self.drag_plot.x_quantity = self.distanceQuantity.currentData()
        self.drag_plot.set_distance_quantity()

    def cd_at_distance(self):
        self.state.current_distance = self.drop_table.get_current_distance()
        if self.state.current_distance:
            drop = self.drop_table.get_current_drop()
            self.state.calculate_cd(distance=self.state.current_distance)
            self.drop_plot.set_cd_at_distance(self.state.current_distance, drop)

            ox, oy = self.parse_data(
                self.state.current_drag_func if self.state.current_drag_func else self.state.default_drag_func)
            x, y = rnd(self.state.get_cd_at_distance(self.state.current_distance)), rnd(min(oy))
            # self.drag_plot.set_cd_at_distance(x, y)

    def switch_plot_drop(self):
        self.drag_plot.stackUnder(self.drop_plot)

    def switch_plot_drag(self):
        self.drop_plot.stackUnder(self.drag_plot)

    def calculate_bullet_drop(self):
        if self.state.current_distance:
            self.cd_at_distance()

    def update_drag_table(self):
        self.dragTable.set(self.state.current_drag_func, self.state.default_drag_func)
        self.drag_plot.current_point.setData()
        self.drag_plot.current_point_text.setText("")

    def reset(self):
        self.drag_plot.reset_current_plot()
        self.drop_plot.reset_current_plot()
        self.updateState(self.defaults)

    def append_updates(self):
        self.state.drag_function = self.state.current_drag_func
        self.update_drag_table()
        self.drag_plot.draw_current_plot(
            self.parse_data(self.state.current_drag_func)[0],
            self.parse_data(self.state.current_drag_func)[1]
        )

        self.calculate_bullet_drop()
        self.drop_plot.draw_current_plot(self.state.calculate_drop(self.state.current_drop))

    def current_atmo_dialog(self):
        ok = self.current_atmo_dlg.exec_()
        if ok:
            atmo = self.current_atmo_dlg.get_atmo()

    def copy_table(self):
        data = self.state.current_drag_func if self.state.current_drag_func else self.state.default_drag_func
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
        self.updateState(current_drag_func=float_pairs)
        self.dragTable.set(self.state.current_drag_func, self.state.default_drag_func)
        self.append_updates()

    @staticmethod
    def parse_data(data: list) -> dict or None:
        if data:
            ox, oy = [i[0] for i in data], [i[1] for i in data]
            return ox, oy if ox and oy else None
        else:
            return None

    def set_coefficient(self, side, is_up):
        ox, oy = self.parse_data(
            self.state.current_drag_func if self.state.current_drag_func else self.state.default_drag_func)
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
            # new_data.sort(reverse=True)
            # print('reverse')
            self.updateState(current_drag_func=new_data)
            self.append_updates()

    def __getstate__(self):
        new_state = self.state.__dict__
        is_new_data = True if self.state.current_drag_func else False

        if is_new_data:
            new_state['df_data'] = self.state.current_drag_func
            new_state['dragType'] = 2
        else:
            new_state['df_data'] = self.state.default_drag_func

        [new_state.pop(key) for key in ['default_drag_func',
                                        'current_drag_func',
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
                if not self.state.default_drag_func:
                    self.updateState(default_drag_func=data)
                else:
                    self.updateState(current_drag_func=data)
                self.dragTable.set(self.state.current_drag_func, self.state.default_drag_func)
                self.append_updates()

            self.dfComment.setText(comment.replace('\n', '')[:80])

    def export_table(self, fileName=None):
        data = self.state.current_drag_func
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
                fp.save_format(fileFormat, fileName, data, fileName)


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # NATIVE DARK THEME
    # from dark_theme import DarkTheme
    # DarkTheme().setup(app)
    try:
        from .defaults import EXAMPLE_G1
    except ImportError as err:
        from gui.drag_func_editor.defaults import EXAMPLE_G7, DEFAULTS

    dialog = DragFuncEditDialog(DEFAULTS)
    dialog.show()
    dialog.exec()
    return dialog.state


if __name__ == '__main__':
    main()

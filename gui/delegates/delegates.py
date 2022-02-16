from PyQt5 import QtWidgets, QtCore


class SpinDelegate(QtWidgets.QItemDelegate):
    def setEditorData(self, editor: 'QWidget', index: QtCore.QModelIndex) -> None:
        value = index.model().data(index, QtCore.Qt.EditRole)
        editor.setValue(value) if value else None

    def setModelData(self, editor: 'QWidget', model: QtCore.QAbstractItemModel, index: QtCore.QModelIndex) -> None:
        editor.interpretText()
        value = editor.value()

        model.setData(index, value, QtCore.Qt.EditRole)

    def updateEditorGeometry(self, editor: 'QWidget', option: 'QStyleOptionViewItem', index: QtCore.QModelIndex) -> None:
        editor.setGeometry(option.rect)

    def set_props(self, editor, min, max, step, dec=None):
        editor.setMaximum(max)
        editor.setMinimum(min)
        editor.setSingleStep(step)
        if dec:
            editor.setDecimals(dec)
        return editor


class Velocity(SpinDelegate):
    def createEditor(self, parent, option, index):
        editor = QtWidgets.QDoubleSpinBox(parent)
        self.set_props(editor, 10, 0, 0.01, 2)
        return editor


class DragCoefficient(SpinDelegate):
    def createEditor(self, parent, option, index):
        editor = QtWidgets.QDoubleSpinBox(parent)
        self.set_props(editor, 1, 0, 0.0001, 4)
        return editor


class BallisticCoefficient(SpinDelegate):
    def createEditor(self, parent, option, index):
        editor = QtWidgets.QDoubleSpinBox(parent)
        self.set_props(editor, 0, 20, 0.001, 3)
        return editor

    def setModelData(self, editor: 'QWidget', model: QtCore.QAbstractItemModel, index: QtCore.QModelIndex) -> None:
        editor.interpretText()
        value = editor.value()

        model.setData(index, value, QtCore.Qt.EditRole)


class MuzzleVelocity(SpinDelegate):
    def createEditor(self, parent, option, index):
        editor = QtWidgets.QSpinBox(parent)
        self.set_props(editor, 0, 3000, 1)
        return editor


from gui.db_widgets.table_btns import SelectBtn

class ButtonDelegate(QtWidgets.QItemDelegate):

    def __init__(self, parent):
        QtWidgets.QItemDelegate.__init__(self, parent)

    def createEditor(self, parent, option, index):
        # btn = QtWidgets.QPushButton(str(index.data()), parent)
        btn = SelectBtn()
        # btn.clicked.connect(self.currentIndexChanged)
        # btn.clicked.connect(lambda *args: print('clicked', args))
        return btn

    def setEditorData(self, editor, index):
        editor.blockSignals(True)
        editor.blockSignals(False)

    def setModelData(self, editor, model, index):
        model.setData(index, editor.text())

    @QtCore.pyqtSlot()
    def currentIndexChanged(self):
        self.commitData.emit(self.sender())

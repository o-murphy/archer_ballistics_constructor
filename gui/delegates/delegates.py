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
        self.set_props(editor, 0, 10, 0.01, 2)
        return editor


class DragCoefficient(SpinDelegate):
    def createEditor(self, parent, option, index):
        editor = QtWidgets.QDoubleSpinBox(parent)
        self.set_props(editor, 0, 1, 0.0001, 4)
        return editor


class BallisticCoefficient(SpinDelegate):
    def createEditor(self, parent, option, index):
        editor = QtWidgets.QDoubleSpinBox(parent)
        self.set_props(editor, 0, 10, 0.001, 3)

        if self.parent():
            editor.editingFinished.connect(self.parent().mbc_edit)

        return editor

    def setModelData(self, editor: 'QWidget', model: QtCore.QAbstractItemModel, index: QtCore.QModelIndex) -> None:
        editor.interpretText()
        value = editor.value()

        model.setData(index, value, QtCore.Qt.EditRole)


class MuzzleVelocity(SpinDelegate):
    def createEditor(self, parent, option, index):
        editor = QtWidgets.QSpinBox(parent)
        self.set_props(editor, 0, 3000, 1)

        if self.parent():
            editor.editingFinished.connect(self.parent().mbc_edit)

        return editor


class Distance(SpinDelegate):
    def createEditor(self, parent, option, index):
        editor = QtWidgets.QSpinBox(parent)
        self.set_props(editor, 0, 10000, 1)
        editor.editingFinished.connect(self.parent().custom_drop_at_distance)
        return editor


class Drop(SpinDelegate):
    def createEditor(self, parent, option, index):
        editor = QtWidgets.QDoubleSpinBox(parent)
        editor.setDisabled(True)
        self.set_props(editor, -10000, 10000, 0.001, 3)
        return editor


class DropCorrection(SpinDelegate):
    def createEditor(self, parent, option, index):
        editor = QtWidgets.QDoubleSpinBox(parent)
        self.set_props(editor, -10000, 10000, 0.001, 3)
        return editor

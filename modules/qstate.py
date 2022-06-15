from PyQt5 import QtCore, QtWidgets


class StateDidUpdate(QtCore.QEvent):
    __name__ = 'StateDidUpdate'

    def __init__(self, key=None, value=None, *args, **kwargs):
        super(StateDidUpdate, self).__init__(QtCore.QEvent(QtCore.QEvent.Type(10001)))
        self.key = key
        self.value = value
        self.kwargs = kwargs
        for i, v in enumerate(args):
            self.__setattr__('_' + str(i), v)
        for k, v in self.kwargs.items():
            self.__setattr__(k, v)


class State(QtCore.QObject):
    onStateUpdate = QtCore.pyqtSignal(StateDidUpdate)

    def __init__(self, widget: QtWidgets.QWidget, state: dict = None, **kwargs):
        """ widget: QtWidgets.QWidget | widget that's need to be state-full """
        super(State, self).__init__()
        if state:
            kwargs.update(state)
        self.updateState(**kwargs)
        widget.updateState = self.updateState
        widget.onStateUpdate = self.onStateUpdate

    def __getstate__(self):
        return self.__dict__

    def updateState(self, state: dict = None, *args, **kwargs):
        if state:
            kwargs.update(**state)
        if kwargs:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
                # self.onStateUpdate.emit(StateDidUpdate(key, value))
            self.onStateUpdate.emit(StateDidUpdate(**kwargs))
        else:
            self.onStateUpdate.emit(StateDidUpdate())

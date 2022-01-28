from PyQt5 import QtCore, QtWidgets


class StateDidUpdate(QtCore.QEvent):
    __name__ = 'StateDidUpdate'

    def __init__(self, key=None, value=None, *args, **kwargs):
        super(StateDidUpdate, self).__init__(QtCore.QEvent(QtCore.QEvent.Type(10001)))
        self.key = key
        self.value = value
        for i, v in enumerate(args):
            self.__setattr__('_' + str(i), v)
        for k, v in kwargs.items():
            self.__setattr__(k, v)


class StateDidSet(QtCore.QEvent):
    __name__ = 'StateDidSet'

    def __init__(self, key=None, value=None, *args, **kwargs):
        super(StateDidSet, self).__init__(QtCore.QEvent(QtCore.QEvent.Type(10002)))
        self.key = key
        self.value = value
        for i, v in enumerate(args):
            self.__setattr__('_' + str(i), v)
        for k, v in kwargs.items():
            self.__setattr__(k, v)


class State(QtCore.QObject):
    onStateUpdate = QtCore.pyqtSignal(StateDidUpdate)
    onStateSet = QtCore.pyqtSignal(StateDidSet)

    def __init__(self, widget: QtWidgets.QWidget, state: dict = None, **kwargs):
        super(State, self).__init__()
        if state:
            kwargs.update(state)
            self.setState(**kwargs)

        widget.setState = self.setState
        widget.updateState = self.updateState
        widget.onStateUpdate = self.onStateUpdate
        widget.onStateSet = self.onStateSet

    def emit(self, key, value):
        self.arg_update.emit(StateDidUpdate(key, value))
        self.__setattr__(key, value)

    def setState(self, state: dict = None, **kwargs):
        if state:
            kwargs.update(state)
        for key, value in kwargs.items():
            self.onStateSet.emit(StateDidSet(key, value))
            self.__setattr__(key, value)

    def updateState(self, state: dict = None, **kwargs):
        if state:
            kwargs.update(state)
        for key, value in kwargs.items():
            self.onStateUpdate.emit(StateDidUpdate(key, value))
            self.__setattr__(key, value)

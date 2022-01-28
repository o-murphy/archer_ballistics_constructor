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
        """
        widget: QtWidgets.QWidget | widget that's need to be state-full
        """
        super(State, self).__init__()
        if state:
            kwargs.update(state)

        if kwargs:
            self.setState(**kwargs)

        widget.setState = self.setState
        widget.updateState = self.updateState
        widget.onStateUpdate = self.onStateUpdate
        widget.onStateSet = self.onStateSet

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, state):
        for key, value in state.items():
            self.onStateSet.emit(StateDidSet(key, value))
            self.__setattr__(key, value)

    def emit(self, key, value):
        self.arg_update.emit(StateDidUpdate(key, value))
        self.__setattr__(key, value)

    def setState(self, state: dict = None, **kwargs):
        if state:
            kwargs.update(state)
        if kwargs:
            for key, value in kwargs.items():
                self.onStateSet.emit(StateDidSet(key, value))
                self.__setattr__(key, value)
        else:
            self.onStateSet.emit(StateDidSet())

    def updateState(self, state: dict = None, **kwargs):
        if state:
            kwargs.update(**state)
        if kwargs:
            for key, value in kwargs.items():
                self.onStateUpdate.emit(StateDidUpdate(key, value))
                self.__setattr__(key, value)
        else:
            self.onStateUpdate.emit(StateDidUpdate())

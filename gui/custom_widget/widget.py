from PyQt5 import QtCore, QtWidgets


class StateUpdated(QtCore.QEvent):
    __name__ = 'StateUpdated'

    def __init__(self, key=None, value=None, *args, **kwargs):
        super(StateUpdated, self).__init__(QtCore.QEvent(QtCore.QEvent.Type(10001)))
        self.key = key
        self.value = value
        for i, v in enumerate(args):
            self.__setattr__('_' + str(i), v)
        for k, v in kwargs.items():
            self.__setattr__(k, v)


class State(QtCore.QObject):
    arg_update = QtCore.pyqtSignal(StateUpdated)

    def __init__(self, widget: QtWidgets.QWidget, state: dict = None, **kwargs):
        super(State, self).__init__()
        if state:
            kwargs.update(state)
        [self.__setattr__(key, value) for key, value in kwargs.items()]

        # self.widget = widget
        widget.setState = self.setState
        widget.StateUpdateHandler = self.StateUpdateHandler
        widget.onStateUpdate = self.arg_update

    # def __setattr__(self, key, value):
    #     print(key, value)
    #     # self.arg_update.emit(StateUpdated(key, value))
    #     super(State, self).__setattr__(key, value)

    def emit(self, key, value):
        self.arg_update.emit(StateUpdated(key, value))
        self.__setattr__(key, value)

    def setState(self, state: dict = None, **kwargs):
        if state:
            kwargs.update(state)
        # [self.__setattr__(key, value) for key, value in kwargs.items()]
        [self.emit(key, value) for key, value in kwargs.items()]

    def StateUpdateHandler(self, callback):
        self.arg_update.connect(callback)



class Props(State):
    def __init__(self):
        super(Props, self).__init__()

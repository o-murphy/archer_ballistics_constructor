from PyQt5 import QtCore, QtWidgets, QtGui


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
    """
        self.setter.connect(function)
    """

    setter = QtCore.pyqtSignal(object, object)

    def __init__(self, *args: object, **kwargs):
        super().__init__()
        self.set_state(*args, **kwargs)

    def set_state(self, *args, **kwargs):
        for i, v in enumerate(args):
            self.__setattr__('_' + str(i), v)

        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def __setattr__(self, key, value):
        event = StateUpdated(key, value)
        self.event(event)
        self.setter.emit(key, value)
        super().__setattr__(key, value)

    def event(self, e: StateUpdated) -> bool:
        print(e.type(), e.key, e.value)
        return True


class StateFullWidget(QtWidgets.QWidget):
    def __init__(self, state: State = None):
        super(StateFullWidget, self).__init__()
        self._state = state
        self.onStateInit()

    @property
    def state(self):
        return self._state

    # def setState(self, *args, **kwargs):
    #     self._state = value

    def onStateInit(self):
        pass

    def onStateUpdate(self):
        pass


s = StateFullWidget()
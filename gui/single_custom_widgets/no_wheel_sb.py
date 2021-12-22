from PyQt5 import QtWidgets, QtGui, QtCore


class NoWheelDoubleSpinBox(QtWidgets.QDoubleSpinBox):
    def __init__(self):
        super(NoWheelDoubleSpinBox, self).__init__()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMaximumSize(QtCore.QSize(80, 16777215))
        self.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.setWrapping(False)
        self.setFrame(True)
        self.setReadOnly(False)
        self.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.setAccelerated(False)
        self.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.setKeyboardTracking(False)
        self.setMinimum(-200.0)
        self.setMaximum(200.0)
        self.setSingleStep(0.25)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

    def wheelEvent(self, event):
        if self.hasFocus():
            super().wheelEvent(event)


class NoWheelSpinBox(QtWidgets.QSpinBox):
    def __init__(self):
        super(NoWheelSpinBox, self).__init__()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.setFont(font)
        self.setStyleSheet("")
        self.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.setPrefix("")
        self.setMaximum(10000)
        self.setSingleStep(10)
        self.setProperty("value", 100)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

    def wheelEvent(self, event):
        if self.hasFocus():
            super().wheelEvent(event)

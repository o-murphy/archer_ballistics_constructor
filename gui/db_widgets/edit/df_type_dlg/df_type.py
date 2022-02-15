from PyQt5 import QtWidgets, QtCore


class DFCombo(QtWidgets.QComboBox):
    def __init__(self):
        super(DFCombo, self).__init__()
        self.addItems(['G1', 'G7', 'G1 Multi-BC', 'G7 Multi-BC', 'Custom'])


class DFTypeDlg(QtWidgets.QDialog):
    def __init__(self):
        super(DFTypeDlg, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.combo = DFCombo()
        self.ok = QtWidgets.QPushButton('OK')
        self.cancel = QtWidgets.QPushButton('Cancel')
        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)
        self.grid.addWidget(QtWidgets.QLabel("What's type of drag_func you'll use?"), 0, 0, 1, 2)
        self.grid.addWidget(self.combo, 1, 0, 1, 2)
        self.grid.addWidget(self.ok)
        self.grid.addWidget(self.cancel)
        self.ok.clicked.connect(self.accept)
        self.cancel.clicked.connect(self.reject)

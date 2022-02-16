from PyQt5 import QtWidgets, QtCore, QtGui
from gui.stylesheet import load_qss


class DFCombo(QtWidgets.QComboBox):
    def __init__(self):
        super(DFCombo, self).__init__()
        self.addItems(['G1', 'G7', 'G1 Multi-BC', 'G7 Multi-BC', 'Custom'])


class DFTypeDlg(QtWidgets.QDialog):
    def __init__(self):
        super(DFTypeDlg, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.setStyleSheet(load_qss('qss/dialog.qss') + """
            QDialog {border: 1px solid rgb(76, 76, 76)}
        """)

        self.combo = DFCombo()

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo.sizePolicy().hasHeightForWidth())
        self.combo.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.combo.setFont(font)

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

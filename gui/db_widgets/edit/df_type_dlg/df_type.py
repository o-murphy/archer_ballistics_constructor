from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QComboBox, QDialog, QSizePolicy, QPushButton, QLabel, QGridLayout

from gui.stylesheet import load_qss


class DFCombo(QComboBox):
    def __init__(self):
        super(DFCombo, self).__init__()
        self.addItems(['G1', 'G7', 'G1 Multi-BC', 'G7 Multi-BC', 'Custom'])


class DFTypeDlg(QDialog):
    def __init__(self):
        super(DFTypeDlg, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.setStyleSheet(load_qss('qss/dialog.qss') + """
            QDialog {border: 1px solid rgb(76, 76, 76)}
        """)

        self.combo = DFCombo()

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo.sizePolicy().hasHeightForWidth())
        self.combo.setSizePolicy(sizePolicy)

        font = QFont()
        font.setPointSize(12)
        self.combo.setFont(font)

        self.ok = QPushButton('OK')
        self.cancel = QPushButton('Cancel')
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.label = QLabel()
        self.grid.addWidget(self.label, 0, 0, 1, 2)
        self.grid.addWidget(self.combo, 1, 0, 1, 2)
        self.grid.addWidget(self.ok)
        self.grid.addWidget(self.cancel)
        self.ok.clicked.connect(self.accept)
        self.cancel.clicked.connect(self.reject)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.label.setText(_translate('DFTypeDlg', "What's type of drag_func you'll use?"))

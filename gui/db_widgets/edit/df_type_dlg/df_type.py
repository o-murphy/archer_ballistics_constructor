from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtCore import QRect, QMetaObject
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QComboBox, QDialog, QSizePolicy, QLabel, QGridLayout
from PyQt5.QtWidgets import QDialogButtonBox

from gui.stylesheet import load_qss


class DFCombo(QComboBox):
    def __init__(self):
        super(DFCombo, self).__init__()
        self.setObjectName('DFCombo')
        [self.addItem(x, x) for x in ['G7', 'G1', 'G7 Multi-BC', 'G1 Multi-BC', 'Custom']]
        self.retranslateUi()

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setItemText(0, _translate('DFCombo', 'G7'))
        self.setItemText(1, _translate('DFCombo', 'G1'))
        self.setItemText(2, _translate('DFCombo', 'G7 Multi-BC'))
        self.setItemText(3, _translate('DFCombo', 'G1 Multi-BC'))
        self.setItemText(4, _translate('DFCombo', 'Custom'))


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
        
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setGeometry(QRect(0, 210, 261, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")

        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.label = QLabel()
        self.grid.addWidget(self.label, 0, 0, 1, 2)
        self.grid.addWidget(self.combo, 1, 0, 1, 2)
        self.grid.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(self.accept)  # type: ignore
        self.buttonBox.rejected.connect(self.reject)  # type: ignore

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.label.setText(_translate('DFTypeDlg', "What's type of drag_func you'll use?"))

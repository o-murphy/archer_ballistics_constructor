from PyQt5 import QtWidgets, QtCore
from .templates import Ui_customDlg
from modules.env_update import USER_RECENT
from modules import FileParse


class CustomDLG(QtWidgets.QDialog, Ui_customDlg):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.data = None

        self.comboBox.currentIndexChanged.connect(self.combo_changed)
        self.file.clicked.connect(self.import_table)

    def combo_changed(self, index):
        combo = self.comboBox.itemText(index)
        if combo == "Import by file":
            self.file.setEnabled(True)
        else:
            self.file.setDisabled(True)

    def import_table(self):
        options = QtWidgets.QFileDialog.Options()
        fileName, fileFormat = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "QFileDialog.getOpenFileName()",
            USER_RECENT,
            "Drag function (*.drg;*.snr;*.ardrg)",
            options=options
        )
        if fileName:
            fp = FileParse()
            data, comment = fp.open_format(fileFormat, fileName)
            if data:
                self.data = data
                self.label.setText(fileName)

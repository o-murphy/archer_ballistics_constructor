# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from gui.templates import Ui_FooterWidget
from modules.lpc_check import lpcRunThread, UsbStatusCode, check_lpc_driver


class FooterWidget(QtWidgets.QWidget, Ui_FooterWidget, lpcRunThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.conn_status = None
        if check_lpc_driver():
            self.setupLpcTread()
            self.autoConnect.clicked.connect(self.setup_lpc_thread)

        else:
            self.connectionStatus.setText(UsbStatusCode.DRIVER_ERROR)

    def setup_lpc_thread(self):

        if self.autoConnect.isChecked():
            self.startLpcThread()
        else:
            self.stopLpcThread()

    def updateLpcDeviceStatus(self, status):
        if hasattr(self, 'conn_status'):
            if self.conn_status != status:
                self.conn_status = status
                self.connectionStatus.setText(status)

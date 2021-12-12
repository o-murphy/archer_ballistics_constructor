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
        else:
            self.connectionStatus.setText(UsbStatusCode.DRIVER_ERROR)

    def updateLpcDeviceStatus(self, status):
        if hasattr(self, 'conn_status'):
            if self.conn_status != status:
                self.conn_status = status
                self.connectionStatus.setText(status)
                if status == UsbStatusCode.CONNECTED:
                    self.setEnabled(True)
                else:
                    self.setEnabled(False)

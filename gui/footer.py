# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from gui.templates import Ui_FooterWidget
from modules.lpc_check import lpcRunThread, UsbStatusCode, check_lpc_driver
from .app_settings import AppSettings


class FooterWidget(QtWidgets.QWidget, Ui_FooterWidget, lpcRunThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.autoConnect.setDisabled(True)

        self.conn_status = None
        if check_lpc_driver():
            self.setupLpcTread()
            # self.setup_lpc_thread()
            self.autoConnect.clicked.connect(self.setup_lpc_thread)

        else:
            self.connectionStatus.setText(UsbStatusCode.DRIVER_ERROR)

        self.Preferences.clicked.connect(self.open_app_settings)

    def open_app_settings(self):
        dlg = AppSettings()
        if dlg.exec_():
            self.window().setUnits()
            self.window().setLang()

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

# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore
from gui.templates import Ui_FooterWidget
from modules.lpc_check import lpcRunThread, UsbStatusCode, check_lpc_driver
import configparser
import os
from modules.env_update import CONFIG_PATH


class FooterWidget(QtWidgets.QWidget, Ui_FooterWidget, lpcRunThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)

        self.languages = ['en', 'ua', 'ru']
        for i, lang in enumerate(self.languages):
            self.Language.setItemData(i, lang)

        self.set_language()
        self.Language.currentIndexChanged.connect(self.update_language)

        self.autoConnect.setDisabled(True)

        self.conn_status = None
        if check_lpc_driver():
            self.setupLpcTread()
            # self.setup_lpc_thread()
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

    def update_language(self, e):
        locale = self.Language.currentData()
        config = configparser.ConfigParser()
        config.read(CONFIG_PATH)
        config.set('Locale', 'system', QtCore.QLocale.system().name().split('_')[1].lower())

        if locale != 'en':
            if os.path.isfile(f'translate/eng-{locale}.qm'):
                config.set('Locale', 'current', locale)
            else:
                locale = config['Locale']['system']
                config.set('Locale', 'current', locale)
        else:
            config.set('Locale', 'current', locale)
        with open(CONFIG_PATH, 'w') as fp:
            print(locale)
            config.write(fp)

        self.window().setLang()

    def set_language(self):
        config = configparser.ConfigParser()
        config.read(CONFIG_PATH)
        locale = config['Locale']['current']
        self.Language.setCurrentIndex(self.languages.index(locale))

# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtGui, QtCore
import sys
from modules import env_update
from gui import Ui_MainWindow
from gui import LPC_dialog
from gui import FooterWidget
from gui import EmptyProfilesTab
from gui import CatalogTab
from gui import MyTab
from gui.stylesheet import load_qss
from modules.env_update import CONFIG_PATH

import configparser
import os


class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    TODO: fix update df data for archer_ballistics.pyd
    TODO: unify API methods for each of ballistic calculator extensions
    TODO: rebuild wrong ui templates
    # TODO: rewrite "retranslateUI" methods if needed
    TODO: update transtations
    TODO: update dbwidgets for units convertor
    TODO: update dbworker filters
    TODO: clean project from unused references, libraries
    TODO: add dynamic imports of extensions
    TODO: add reticle designer extension
    TODO: add device settings extension
    TODO: add developer settings extension
    """
    def __init__(self):
        super().__init__()

        self.translator_custom = QtCore.QTranslator()
        self.translator_qt = QtCore.QTranslator()

        self.config = configparser.ConfigParser()
        self.setLang()
        self.setupDriverCheck()
        self.setupUi(self)
        self.setupWidgets()
        self.setQss()

        self.units = None
        self.setUnits()

        # self.setWindowIcon(QtGui.QIcon('Icon.png'))

    def setUnits(self):
        self.config.read(CONFIG_PATH)
        self.units = self.config['Units']
        for c in self.findChildren(QtWidgets.QWidget):
            if hasattr(c, 'setUnits'):
                c.setUnits()

    def setLang(self):
        self.config.read(CONFIG_PATH)
        if not os.path.isfile(CONFIG_PATH):
            self.config.add_section('Locale')

            self.config.set('Locale', 'system', QtCore.QLocale.system().name().split('_')[1].lower())
            self.config.set('Locale', 'current', QtCore.QLocale.system().name().split('_')[1].lower())
            with open(CONFIG_PATH, 'w') as fp:
                self.config.write(fp)

        self.locale = self.config['Locale']['current']

        app = QtCore.QCoreApplication.instance()
        app.removeTranslator(self.translator_qt)
        app.removeTranslator(self.translator_custom)

        if self.locale != 'en':
            if not os.path.isfile(f'translate/eng-{self.locale}.qm'):
                self.locale = self.config['Locale']['system']
                self.config.set('Locale', 'current', self.locale)

            with open(CONFIG_PATH, 'w') as fp:
                self.config.write(fp)
            if self.locale != 'en':

                self.translator_custom = QtCore.QTranslator()
                self.translator_custom.load(f'translate/eng-{self.locale}.qm')

                self.translator_qt = QtCore.QTranslator()
                self.translator_qt.load(f'translate/qtbase_{self.locale}.qm')

                app.installTranslator(self.translator_qt)
                app.installTranslator(self.translator_custom)
        self.retranslateUi(self)
        for c in self.findChildren(QtWidgets.QWidget):
            if hasattr(c, 'retranslateUi'):
                c.retranslateUi(c)

    def setupDriverCheck(self):
        self.lpc_dialog = LPC_dialog()

    def setupWidgets(self):
        self.profiles_tab = EmptyProfilesTab(*sys.argv)
        self.my_tab = MyTab()
        self.catalog_tab = CatalogTab()

        self.tabWidget.addTab(self.profiles_tab, QtGui.QIcon(), 'Profiles')
        self.tabWidget.addTab(self.my_tab, QtGui.QIcon(), 'Templates')
        self.tabWidget.addTab(self.catalog_tab, QtGui.QIcon(), 'Catalog')

        self.retranslate_tabs()

        footer_widget = FooterWidget(self)
        self.__setattr__('footer_widget', footer_widget)
        self.gridLayout.addWidget(self.footer_widget, 1, 0, 1, 1)

    def setQss(self):
        self.setStyleSheet(load_qss('qss/application.qss'))

    def closeEvent(self, event) -> None:
        self.custom_close(event)

    def custom_close(self, event):
        if not self.profiles_tab.is_saved:
            choice = self.profiles_tab.close_file()
            if choice == QtWidgets.QMessageBox.Cancel or not self.profiles_tab.is_saved:
                event.ignore()
            else:
                QtGui.QCloseEvent()
        else:
            QtGui.QCloseEvent()
        # if hasattr(self, 'profiles_tab'):
        #     self.profiles_tab.save_backup()
        # sys.exit()

    def retranslate_tabs(self):
        _translate = QtCore.QCoreApplication.translate
        self.tabWidget.setTabText(0, _translate("MainWindow", 'Profiles'))
        self.tabWidget.setTabText(1, _translate("MainWindow", 'Templates'))
        self.tabWidget.setTabText(2, _translate("MainWindow", 'Catalog'))


def main():
    os.chdir(os.path.dirname(__file__))

    env_update.main()
    app = QtWidgets.QApplication(sys.argv)

    # _id = QtGui.QFontDatabase.addApplicationFont("Bank Gothic Light BT.ttf")
    # fid = QtGui.QFontDatabase.applicationFontFamilies(_id)
    # font = QtGui.QFont("BankGothic Lt BT")
    # font = QtGui.QFont("Segoe UI Historic")
    # app.setFont(font)

    # NATIVE DARK THEME
    # from dark_theme import DarkTheme
    # DarkTheme().setup(app)

    window = ExampleApp()
    window.show()
    app.setWindowIcon(QtGui.QIcon('Icon.png'))
    app.exec_()


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtGui
from gui import ProfilesTab, Ui_MainWindow, FooterWidget
import sys
from modules import env_update
from gui import LPC_dialog


class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupDriverCheck()
        self.setupUi(self)
        self.setupWidgets()

        # self.setWindowIcon(QtGui.QIcon('Icon.png'))

    def setupDriverCheck(self):
        self.lpc_dialog = LPC_dialog()

    def setupWidgets(self):
        profiles_tab = ProfilesTab(self)
        self.__setattr__('profiles_tab', profiles_tab)
        self.tabWidget.addTab(self.profiles_tab, QtGui.QIcon(), 'Profiles')

        footer_widget = FooterWidget(self)
        self.__setattr__('footer_widget', footer_widget)
        self.gridLayout.addWidget(self.footer_widget)

    def closeEvent(self, event) -> None:
        if hasattr(self, 'profiles_tab'):
            self.profiles_tab.save_backup()
        sys.exit()


def main():
    env_update.main()

    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()

    app.setWindowIcon(QtGui.QIcon('Icon.png'))

    app.exec_()


if __name__ == '__main__':
    main()

    # pyinstaller -w -i=.rsrc\Icon.ico --add-data=.rsrc;.rsrc\ --add-data=drv;drv\ run.py

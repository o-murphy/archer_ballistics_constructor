from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTabWidget
from extensions import Extension
from .main import EmptyTab


class XExtension(Extension):

    def include(self):
        if self.enter_point:
            ch: QTabWidget = self.enter_point.findChild(QTabWidget, 'MainWindowTabWidget')
            tab = EmptyTab(self.enter_point)
            ch.addTab(tab, QIcon(), 'Reticles')


if __name__ == '__main__':
    pass

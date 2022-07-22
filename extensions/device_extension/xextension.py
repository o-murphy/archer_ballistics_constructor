from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTabWidget, QWidget, QGridLayout, QLabel
from extensions import Extension


class XExtension(Extension):

    def include(self):
        if self.enter_point:
            self.make_messbox()

    def make_messbox(self):
        ch: QTabWidget = self.enter_point.findChild(QTabWidget, 'MainWindowTabWidget')
        self.tab = EmptyTab()
        ch.addTab(self.tab, QIcon(), 'Device')


class EmptyTab(QWidget):
    def __init__(self, *args):
        super().__init__()

        self.gridLayout = QGridLayout()
        self.setLayout(self.gridLayout)
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText('Extension currently unavailable')
        self.layout().addWidget(self.label)


if __name__ == '__main__':
    e = XExtension()

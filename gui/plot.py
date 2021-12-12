from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.widg = QtWidgets.QWidget(self)

        self.verticalLayout = QtWidgets.QHBoxLayout(self.widg)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setSpacing(4)

        self.graphWidget = pg.PlotWidget()
        self.button = QtWidgets.QPushButton()
        self.button.setText('up')
        self.button2 = QtWidgets.QPushButton()
        self.button2.setText('down')

        self.verticalLayout.addWidget(self.graphWidget)
        self.verticalLayout.addWidget(self.button)
        self.verticalLayout.addWidget(self.button2)

        self.setCentralWidget(self.widg)

        self.nbc = 0.025
        self.nv = 15
        self.sbc = 0.350
        self.sv = 900



        # self.graphWidget.plot(self.bc, self.v)
        # plot data: x, y values
        self.plot = self.graphWidget.plot()
        self.graph_build()
        self.button.clicked.connect(self.up)
        self.button2.clicked.connect(self.down)



    def graph_build(self):
        self.bc = []
        self.v = []
        sbc = self.sbc
        nv = self.nv
        for i in range(10):
            self.bc.append(sbc + i*self.nbc)
            self.v.append(self.sv - i*nv)
            sbc += 0.005
            nv += 2

        self.plot.setData(self.v, self.bc)

    def up(self):

        self.sbc += 0.025
        self.sv += 10
        self.nv -= 1
        self.nbc += 0.025
        self.graph_build()

    def down(self):
        self.sbc -= 0.025
        self.sv -= 10
        self.nv += 1
        self.nbc -= 0.025
        self.graph_build()


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

from PyQt5 import QtWidgets


class CatalogMenu(QtWidgets.QMenu):
    def __init__(self):
        super(CatalogMenu, self).__init__()

        self.setObjectName('CatalogMenu')
        self.template = QtWidgets.QAction('Add template', self)
        self.addAction(self.template)

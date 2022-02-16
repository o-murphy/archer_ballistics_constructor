from PyQt5 import QtWidgets


class TemplatesMenu(QtWidgets.QMenu):
    def __init__(self):
        super(TemplatesMenu, self).__init__()

        self.setObjectName('TemplatesMenu')
        self.add = QtWidgets.QAction('Add', self)
        self.edit = QtWidgets.QAction('Edit', self)
        self.copy = QtWidgets.QAction('Copy', self)
        self.delete = QtWidgets.QAction('Delete', self)
        self.addActions([self.add, self.edit, self.copy])
        self.addSeparator()
        self.addAction(self.delete)

from PyQt5.QtWidgets import QAction, QMenu
from PyQt5.QtCore import QCoreApplication


class TemplatesMenu(QMenu):
    def __init__(self):
        super(TemplatesMenu, self).__init__()

        self.setObjectName('TemplatesMenu')
        self.add = QAction('Add', self)
        self.edit = QAction('Edit', self)
        self.copy = QAction('Copy', self)
        self.delete = QAction('Delete', self)

        self.retranslateUi()

        self.addActions([self.add, self.edit, self.copy])
        self.addSeparator()
        self.addAction(self.delete)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.add.setText(_translate('TemplatesMenu', 'Add'))
        self.edit.setText(_translate('TemplatesMenu', 'Edit'))
        self.copy.setText(_translate('TemplatesMenu', 'Copy'))
        self.delete.setText(_translate('TemplatesMenu', 'Delete'))

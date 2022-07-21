from PyQt5.QtWidgets import QMenu, QAction
from PyQt5.QtCore import QCoreApplication


class CatalogMenu(QMenu):
    def __init__(self):
        super(CatalogMenu, self).__init__()

        self.setObjectName('CatalogMenu')
        self.template = QAction('Add template', self)
        self.addAction(self.template)
        self.retranslateUi()

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.template.setText(_translate('CatalogMenu', 'Add template'))

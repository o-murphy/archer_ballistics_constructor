from PyQt5 import QtWidgets, QtCore
from ..toolbar import InfoTools
from dbworker import db

from ...db_widgets.tables.catalog_list import CatalogList


class Tab(QtWidgets.QWidget):
    def __init__(self):
        super(Tab, self).__init__()
        self.setStyleSheet("""QLabel {font-size: 16px;}""")

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(self.gridLayout)

        self.list = None
        self.info = None
        self.table = None
        self.tools = InfoTools()
        self.tools.addTemplate.clicked.connect(self.add_template)

    def set(self):
        if self.list and self.info:
            self.table = self.list.tableWidget
            self.gridLayout.addWidget(self.list, 0, 0, 2, 1)
            self.gridLayout.addWidget(self.info, 0, 1, 1, 1)
            self.gridLayout.addWidget(self.tools, 1, 1, 1, 1)

    def add_template(self):
        if self.info.item:
            sess = db.SessMake()

            item = sess.query(self.list.model).get(self.info.item.id)

            sess.expunge(item)
            db.make_transient(item)
            delattr(item, 'id')
            item.attrs = 'rw'
            sess.add(item)
            sess.commit()

            for table in self.window().my_tab.findChildren(CatalogList):
                table.set_data()

    def findParent(self, parent, objectName):
        if parent.objectName() != objectName:
            return self.findParent(parent.parent(), objectName)
        return parent

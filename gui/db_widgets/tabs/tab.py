from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QWidget

from ..toolbar import InfoTools
from dbworker import db

from ..tables.catalog_list import CatalogList
from ..filter import Filter


class Tab(QWidget):
    def __init__(self):
        super(Tab, self).__init__()
        self.setStyleSheet("""QLabel {font-size: 16px;}""")
        self.setObjectName('SelectorTab')

        self.gridLayout = QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setAlignment(Qt.AlignTop)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 1)
        self.setLayout(self.gridLayout)

        self.list = None
        self.info = None
        self.table = None
        self.tools = None
        self.filter_widget: Filter = None

    def enable_filter(self):
        self.filter_widget = Filter()
        self.gridLayout.addWidget(self.filter_widget, 1, 1, 1, 1)

    def enable_add_template(self):
        self.tools = InfoTools()
        self.tools.addTemplate.clicked.connect(self.add_template)
        self.gridLayout.addWidget(self.tools, 2, 1, 1, 1)

    def eventFilter(self, sender, event) -> bool:
        print(sender, event)
        super().eventFilter(sender, event)

    def set(self):
        if self.list and self.info:
            self.table = self.list.tableView
            self.gridLayout.addWidget(self.list, 0, 0, 3, 1)
            self.gridLayout.addWidget(self.info, 0, 1, 1, 1)

    def add_template(self):
        print('add', self.info.item.name)
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

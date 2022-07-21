from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QCursor, QStandardItemModel
from PyQt5.QtWidgets import QHeaderView, QWidget

from dbworker import db
from .templates import Ui_roTable
from ..edit import CatalogItemEdit


class CatalogList(QWidget, Ui_roTable):
    def __init__(self, model=None, attrs=None, editor=None):
        super(CatalogList, self).__init__()
        self.setupUi(self)

        self.data = []
        self.model = model
        self.attrs = attrs
        self.editor = editor
        self.table_model = QStandardItemModel(self)

        self.proxy_filter = None

        self.menu = None

        self.tableView.contextMenuEvent = self.context_menu
        self.tableView.installEventFilter(self)

    def set_context_menu(self, menu=None):
        if menu:
            self.menu = menu
            self.customContextMenuRequested.connect(self.context_menu)

    def context_menu(self, e):
        index = self.tableView.indexAt(e.pos())
        if self.menu:
            self.menu.popup(QCursor.pos())
            action = self.menu.exec_()
            if self.menu.objectName() == "TemplatesMenu":
                if action == self.menu.add:
                    self.new_item()
                elif action == self.menu.delete:
                    self.delete_item(index)
                elif action == self.menu.edit:
                    self.edit_item(index)
                elif action == self.menu.copy:
                    self.copy_item(index)
            elif self.menu.objectName() == "CatalogMenu":
                if action == self.menu.template:
                    tab = self.findParent(self.parent(), 'SelectorTab')
                    tab.add_template()

    def update_table(self):
        self.table_model.setRowCount(len(self.data))
        if len(self.data) > 0:
            self.table_model.setColumnCount(len(self.data[0]))

            for i, y in enumerate(self.data):
                for j, x in enumerate(y):
                    self.table_model.setItem(i, j, QStandardItem())
                    self.table_model.item(i, j).setData(x, Qt.DisplayRole)

        self.tableView.setModel(self.table_model)

        if self.proxy_filter:
            self.proxy_filter()

    def set_header(self):
        header = self.tableView.horizontalHeader()
        header.setSectionHidden(0, True)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        for i in range(2, header.count()):
            header.setSectionResizeMode(i, QHeaderView.ResizeToContents)

    def viewport_row(self):
        cursor = self.tableView.mapFromGlobal(QCursor().pos())
        return self.tableView.indexAt(cursor)

    def set_data(self):
        self.data = []
        sess = db.SessMake()
        if self.model:
            if self.attrs:
                items = sess.query(self.model).filter_by(attrs=self.attrs).all()
            else:
                items = sess.query(self.model).all()
            self.parse_data(items)
            self.update_table()

    def parse_data(self, items):
        self.data = []
        for i in items:
            self.data.append(i.__dict__)

    def copy_item(self, index):
        index = self.tableView.model().index(index.row(), 0)
        if index:
            item_data = self.tableView.model().itemData(index)
            if item_data:
                sess = db.SessMake()
                item = sess.query(self.model).get(item_data[0])
                dlg = CatalogItemEdit(self.editor(item, 'copy'))
                if dlg.exec_():
                    dlg.get()
                self.set_data()

    def edit_item(self, index):
        index = self.tableView.model().index(index.row(), 0)
        if index:
            item_data = self.tableView.model().itemData(index)
            if item_data:
                sess = db.SessMake()
                item = sess.query(self.model).get(item_data[0])
                dlg = CatalogItemEdit(self.editor(item, 'edit'))
                if dlg.exec_():
                    dlg.get()
                self.set_data()

    def delete_item(self, index):
        index = self.tableView.model().index(index.row(), 0)
        if index:
            item_data = self.tableView.model().itemData(index)
            print(item_data)
            if item_data:
                sess = db.SessMake()
                item = sess.query(self.model).get(item_data[0])
                print(item)
                sess.delete(item)
                sess.commit()
                self.set_data()

    def new_item(self):
        dlg = CatalogItemEdit(self.editor())
        if dlg.exec_():
            dlg.get()
        self.set_data()
    #
    # def edit_dialog(self):
    #     pass
    #
    # def sel_cur(self):
    #     pass
    #
    def findParent(self, parent, objectName):
        if parent.objectName() != objectName:
            return self.findParent(parent.parent(), objectName)
        return parent

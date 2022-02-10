from PyQt5 import QtWidgets
from .templates import Ui_catalogTemplateList
from .catalog_list import CatalogList
from .templateBtns import TemplateBtns

from dbworker import db
from dbworker.models import *


class CatalogTemplateList(CatalogList, Ui_catalogTemplateList):
    def __init__(self):
        super(CatalogTemplateList, self).__init__()
        self.setupUi(self)
        # self.editor = CatalogRifle

        self.data = []
        self.setupTable()
        self.set_data()

    def setupTable(self):
        header = self.tableWidget.horizontalHeader()
        header.setSectionHidden(0, True)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        for i in range(2, header.count()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

        # self.tableWidget.doubleClicked.connect(self.edit_item)
        # self.tableWidget.viewport().installEventFilter(self)

    def update_table(self):
        print('here will be query to db')

        self.tableWidget.setRowCount(len(self.data))
        for i, y in enumerate(self.data):

            for j, x in enumerate(y):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(x)))
            t_btn = TemplateBtns()
            del_btn = t_btn.delBtn
            create_btn = t_btn.createProfile

            del_btn.clicked.connect(self.delete_item)
            create_btn.clicked.connect(self.new_profile)

            self.tableWidget.setCellWidget(i, self.tableWidget.columnCount() - 1, t_btn)

    def set_data(self):
        self.data = []
        sess = db.SessMake()
        templates = sess.query(Template).all()
        for i in templates:
            self.data.append([i.id, i.name, i.rifle.name, i.cartridge.name, i.drag_func.drag_type])
        self.update_table()

    def delete_item(self):
        id = int(self.tableWidget.item(self.viewport_row(), 0).text())
        sess = db.SessMake()
        t = sess.query(Template).get(id)
        sess.delete(t)
        sess.commit()
        self.set_data()

    def new_profile(self):
        pass
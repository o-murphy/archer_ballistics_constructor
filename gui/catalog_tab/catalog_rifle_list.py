from .templates import Ui_catalogRifleList
from .catalog_list import CatalogList
from .catalog_rifle import CatalogRifle
from .catalog_item_edit import CatalogItemEdit

from dbworker import db


class CatalogRifleList(CatalogList, Ui_catalogRifleList):
    def __init__(self):
        super(CatalogRifleList, self).__init__()
        self.setupUi(self)
        self.editor = CatalogRifle

        self.data = []
        self.setupTable()
        self.set_data()
        self.update_table()

    def set_data(self):
        self.data = []
        rifles = db.get_rifles()
        for i in rifles:
            self.data.append([i.id, i.name, i.caliber.name, i.sh, i.twist])

    def copy_item(self):
        id = int(self.tableWidget.item(self.viewport_row(), 0).text())
        rifle = db.get_rifle(id)
        new_rifle = rifle.__dict__
        new_rifle['diameter'] = rifle.caliber.diameter.diameter

        edit = CatalogItemEdit('Rifle', self.editor(rifle))
        if edit.exec_():
            new_rifle.update(edit.get_data())
            db.add_rifle(**new_rifle)
        self.set_data()
        self.update_table()

    def edit_item(self):
        id = int(self.tableWidget.item(self.viewport_row(), 0).text())
        rifle = db.get_rifle(id)
        edit = CatalogItemEdit('Rifle', self.editor(rifle))
        if edit.exec_():
            db.update_rifle(id, edit.get_data())
        self.set_data()
        self.update_table()

    def delete_item(self):
        id = int(self.tableWidget.item(self.viewport_row(), 0).text())
        db.delete_rifle(id)
        self.set_data()
        self.update_table()


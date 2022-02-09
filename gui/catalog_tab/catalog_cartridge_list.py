from .templates import Ui_catalogCartridgeList
from .catalog_list import CatalogList
from .catalog_cartridge import CatalogCartridge
from .catalog_item_edit import CatalogItemEdit

from dbworker import db
from dbworker.models import *


class CatalogCartridgeList(CatalogList, Ui_catalogCartridgeList):
    def __init__(self):
        super(CatalogCartridgeList, self).__init__()
        self.setupUi(self)
        self.editor = CatalogCartridge

        self.data = []
        self.setupTable()
        self.set_data()

    def set_data(self):
        self.data = []
        sess = db.SessMake()
        cartridges = sess.query(Cartridge).all()
        for i in cartridges:
            self.data.append([i.id, i.name, i.caliber.name, i.bullet.name, i.mv])
        self.update_table()

    def edit_dialog(self):
        item = self.tableWidget.item(self.viewport_row(), 0)
        id = int(item.text()) if item else None
        sess = db.SessMake()
        c = sess.query(Cartridge).get(id) if id else None
        if id:
            edit = CatalogItemEdit('Rifle edit', self.editor(c))
        else:
            edit = CatalogItemEdit('Rifle edit', self.editor())
        if edit.exec_():
            ret = edit.get()
            ret.id = id
            ret.c = c
            ret.sess = sess

            return ret

    def new_item(self):
        ret = self.edit_dialog()

        if ret:
            cartridge = Cartridge(ret.n, ret.v, ret.t, ret.tss, ret.cb, ret.b)
            ret.sess.add(cartridge)
            ret.sess.commit()
            self.set_data()

    def copy_item(self):
        ret = self.edit_dialog()

        if ret:
            cartridge = Cartridge(ret.n, ret.v, ret.t, ret.tss, ret.cb, ret.b)
            ret.sess.add(cartridge)
            ret.sess.commit()
            self.set_data()

    def edit_item(self):
        ret = self.edit_dialog()
        if ret:
            c: Cartridge = ret.c
            c.name = ret.n
            c.mv = ret.v
            c.temp = ret.t
            c.ts = ret.tss
            c.caliber_id = ret.cb
            c.bullet_id = ret.b
            ret.sess.commit()
            self.set_data()

    def delete_item(self):
        item = self.tableWidget.item(self.viewport_row(), 0)
        id = int(item.text()) if item else None
        sess = db.SessMake()
        c = sess.query(Cartridge).get(id) if id else None
        if c:
            sess.delete(c)
            sess.commit()
            self.set_data()



    # def copy_item(self):
    #     id = int(self.tableWidget.item(self.viewport_row(), 0).text())
    #     cartridge = db.get_cartridge(id)
    #
    #     edit = CatalogItemEdit('Rifle', self.editor(cartridge))
    #     if edit.exec_():
    #         new_cartridge = cartridge.__dict__
    #         new_data = edit.get_data()
    #         new_cartridge.update(new_data)
    #         new_cartridge['diameter'] = cartridge.caliber.diameter.diameter
    #         new_cartridge['name'] = new_data['cartridgeName']
    #         new_cartridge['caliberName'] = cartridge.caliber.name
    #
    #         db.add_cartridge(**new_cartridge)
    #     self.set_data()
    #     self.update_table()
    #
    # def edit_item(self):
    #     id = int(self.tableWidget.item(self.viewport_row(), 0).text())
    #     cartridge = db.get_cartridge(id)
    #     edit = CatalogItemEdit('Cartridge', self.editor(cartridge))
    #     if edit.exec_():
    #         new_cartridge = edit.get_data()
    #         new_cartridge['diameter'] = cartridge.caliber.diameter.diameter
    #         new_cartridge['name'] = new_cartridge['cartridgeName']
    #         new_cartridge['caliberName'] = cartridge.caliber.name
    #
    #         db.update_cartridge(id, new_cartridge)
    #     self.set_data()
    #     self.update_table()
    #
    # def delete_item(self):
    #     id = int(self.tableWidget.item(self.viewport_row(), 0).text())
    #     db.delete_cartridge(id)
    #     self.set_data()
    #     self.update_table()

from .templates import Ui_catalogBulletList
from .catalog_list import CatalogList
from .catalog_bullet import CatalogBullet
from .catalog_item_edit import CatalogItemEdit

from dbworker import db
from dbworker.models import *


class CatalogBulletList(CatalogList, Ui_catalogBulletList):
    def __init__(self):
        super(CatalogBulletList, self).__init__()
        self.setupUi(self)
        self.editor = CatalogBullet

        self.data = []
        self.setupTable()
        self.set_data()

    def set_data(self):
        self.data = []
        sess = db.SessMake()
        bullets = sess.query(Bullet).all()
        for i in bullets:
            self.data.append([i.id, i.name, i.weight, i.length, i.diameter.diameter, i.bc])
        self.update_table()

    def edit_dialog(self):
        item = self.tableWidget.item(self.viewport_row(), 0)
        id = int(item.text()) if item else None
        sess = db.SessMake()
        r = sess.query(Bullet).get(id) if id else None
        if id:
            edit = CatalogItemEdit('Rifle edit', self.editor(r))
        else:
            edit = CatalogItemEdit('Rifle edit', self.editor())
        if edit.exec_():
            ret = edit.get()
            # ret.id = id
            # ret.r = r
            # ret.sess = sess
            # return ret

    def new_item(self):
        ret = self.edit_dialog()
        #
        # if ret:
        #     d = ret.sess.query(Diameter).filter_by(diameter=ret.c).first()
        #     ret.sess.add(Rifle(ret.n, c.id, ret.s, ret.t, ret.ir, ret.tl))
        #     ret.sess.commit()
        # self.set_data()

    # def copy_item(self):
    #     id = int(self.tableWidget.item(self.viewport_row(), 0).text())
    #     bullet = db.get_bullet(id)
    #
    #     edit = CatalogItemEdit('Bullet', self.editor(bullet))
    #     if edit.exec_():
    #         new_bullet = bullet.__dict__
    #         new_data = edit.get_data()
    #         new_bullet.update(new_data)
    #         new_bullet['dfdata'] = new_data['df_data']
    #         new_bullet['multiBC'] = new_data
    #
    #
    #         db.add_bullet(**new_bullet)
    #     self.set_data()
    #     self.update_table()
    #
    # def edit_item(self):
    #     id = int(self.tableWidget.item(self.viewport_row(), 0).text())
    #     bullet = db.get_bullet(id)
    #     edit = CatalogItemEdit('Cartridge', self.editor(bullet))
    #     if edit.exec_():
    #         new_bullet = edit.get_data()
    #
    #         db.update_bullet(id, new_bullet)
    #     self.set_data()
    #     self.update_table()
    #
    # def delete_item(self):
    #     id = int(self.tableWidget.item(self.viewport_row(), 0).text())
    #     db.delete_bullet(id)
    #     self.set_data()
    #     self.update_table()


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
            self.data.append([i.id, i.name, i.weight, i.length, i.diameter.diameter])
        self.update_table()

    def edit_dialog(self):
        item = self.tableWidget.item(self.viewport_row(), 0)
        id = int(item.text()) if item else None
        sess = db.SessMake()
        b = sess.query(Bullet).get(id) if id else None
        df = sess.query(DragFunc).filter_by(bullet_id=id).all()
        if id:
            edit = CatalogItemEdit('Rifle edit', self.editor(b, df))
        else:
            edit = CatalogItemEdit('Rifle edit', self.editor())
        if edit.exec_():
            ret = edit.get()
            ret.id = id
            ret.b = b
            ret.sess = sess
            d = ret.sess.query(Diameter).filter_by(diameter=ret.d).first()
            if not d:
                d = Diameter(ret.d)
                ret.sess.add(d)
                sess.commit()
            ret.d = d
            return ret

    # def update_drag(self):

    def new_item(self):
        ret = self.edit_dialog()
        if ret:
            bullet = Bullet(ret.n, ret.w, ret.ln, ret.d.id)
            ret.sess.add(bullet)
            ret.sess.commit()

            drags = ret.sess.query(DragFunc).filter_by(bullet_id=bullet.id).all()
            for df in drags:
                ret.sess.delete(df)
            for df in ret.df:
                ret.sess.add(DragFunc(*df, bullet_id=bullet.id))
                ret.sess.commit()

            self.set_data()

    def edit_item(self):
        ret = self.edit_dialog()
        if ret:
            b: Bullet = ret.b
            b.name = ret.n
            b.weight = ret.w
            b.length = ret.ln
            b.diameter_id = ret.d.id
            ret.sess.commit()
            self.set_data()

            drags = ret.sess.query(DragFunc).filter_by(bullet_id=ret.id).all()
            for df in drags:
                ret.sess.delete(df)
            for df in ret.df:
                ret.sess.add(DragFunc(*df, bullet_id=ret.id))
                ret.sess.commit()

            self.set_data()

    def delete_item(self):
        id = int(self.tableWidget.item(self.viewport_row(), 0).text())
        sess = db.SessMake()
        b = sess.query(Bullet).get(id)

        drags = sess.query(DragFunc).filter_by(bullet_id=id).all()
        for df in drags:
            sess.delete(df)

        sess.delete(b)
        sess.commit()
        self.set_data()

        #     c = ret.sess.query(Caliber).filter_by(name=ret.c).first()
        #     r: Rifle = ret.r
        #     r.name = ret.n
        #     r.caliber_id = c.id
        #     r.sh = ret.s
        #     r.twist = ret.t
        #     r.is_right = ret.ir
        #     r.tile = ret.tl
        #     ret.sess.commit()
        #     self.set_data()

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


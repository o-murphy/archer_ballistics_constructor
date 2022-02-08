from .templates import Ui_catalogRifleList
from .catalog_list import CatalogList
from .catalog_rifle import CatalogRifle
from .catalog_item_edit import CatalogItemEdit

from dbworker import db
from dbworker.models import *


class CatalogRifleList(CatalogList, Ui_catalogRifleList):
    def __init__(self):
        super(CatalogRifleList, self).__init__()
        self.setupUi(self)
        self.editor = CatalogRifle

        self.data = []
        self.setupTable()
        self.set_data()

    def set_data(self):
        self.data = []
        sess = db.SessMake()
        rifles = sess.query(Rifle).all()
        for i in rifles:
            self.data.append([i.id, i.name, i.caliber.name, i.sh, i.twist])
        self.update_table()

    def edit_dialog(self):
        item = self.tableWidget.item(self.viewport_row(), 0)
        id = int(item.text()) if item else None
        sess = db.SessMake()
        r = sess.query(Rifle).get(id) if id else None
        if id:
            edit = CatalogItemEdit('Rifle edit', self.editor(r))
        else:
            edit = CatalogItemEdit('Rifle edit', self.editor())
        if edit.exec_():
            ret = edit.get()
            ret.id = id
            ret.r = r
            ret.sess = sess
            return ret

    def new_item(self):
        ret = self.edit_dialog()

        if ret:
            c = ret.sess.query(Caliber).filter_by(name=ret.c).first()
            ret.sess.add(Rifle(ret.n, c.id, ret.s, ret.t, ret.ir, ret.tl))
            ret.sess.commit()
        self.set_data()

    def copy_item(self):
        ret = self.edit_dialog()

        if ret:
            c = ret.sess.query(Caliber).filter_by(name=ret.c).first()
            ret.sess.add(Rifle(ret.n, c.id, ret.s, ret.t, ret.ir, ret.tl))
            ret.sess.commit()
        self.set_data()

    def edit_item(self):
        ret = self.edit_dialog()
        if ret:
            c = ret.sess.query(Caliber).filter_by(name=ret.c).first()
            r: Rifle = ret.r
            r.name = ret.n
            r.caliber_id = c.id
            r.sh = ret.s
            r.twist = ret.t
            r.is_right = ret.ir
            r.tile = ret.tl
            ret.sess.commit()
            self.set_data()

    def delete_item(self):
        id = int(self.tableWidget.item(self.viewport_row(), 0).text())
        sess = db.SessMake()
        r = sess.query(Rifle).get(id)
        sess.delete(r)
        sess.commit()
        self.set_data()

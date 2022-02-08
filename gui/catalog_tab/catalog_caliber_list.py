from .catalog_list import CatalogList
from .templates import Ui_catalogCaliberList
from .caliber_edit import CaliberEdit
from .catalog_item_edit import CatalogItemEdit

from dbworker import db
from dbworker.models import *


class CatalogCaliberList(CatalogList, Ui_catalogCaliberList):
    def __init__(self):
        super(CatalogCaliberList, self).__init__()
        self.setupUi(self)

        self.data = []
        self.setupTable()
        self.set_data()

    def set_data(self):
        self.data = []

        sess = db.SessMake()
        calibers = sess.query(Caliber).all()

        for i in calibers:
            self.data.append([i.id, i.name, i.diameter.diameter])
        self.update_table()

    def edit_dialog(self):
        item = self.tableWidget.item(self.viewport_row(), 0)
        id = int(item.text()) if item else None
        sess = db.SessMake()
        c = sess.query(Caliber).get(id) if id else None
        if id:
            edit = CatalogItemEdit('Caliber edit', CaliberEdit(c.name, c.diameter.diameter))
        else:
            edit = CaliberEdit()
        if edit.exec_():
            ret = edit.get()
            ret.id = id
            ret.c = c
            ret.sess = sess

            d = sess.query(Diameter).filter_by(diameter=ret.d).first()
            if not d:
                d = Diameter(ret.d)
                sess.add(d)
                sess.commit()
            ret.d = d
            return ret

    def new_item(self):
        ret = self.edit_dialog()
        if ret:
            ret.sess.add(Caliber(ret.n, ret.d.id))
            ret.sess.commit()
        self.set_data()

    def edit_item(self):
        ret = self.edit_dialog()
        if ret:
            ret.c.name = ret.n
            ret.c.diameter_id = ret.d.id
            ret.sess.commit()

            self.set_data()

    def copy_item(self):
        ret = self.edit_dialog()
        if ret:
            new_c = Caliber(ret.n, ret.d.id)
            ret.sess.add(new_c)
            ret.sess.commit()
        self.set_data()

    def delete_item(self):
        id = int(self.tableWidget.item(self.viewport_row(), 0).text())
        sess = db.SessMake()
        c = sess.query(Caliber).get(id)
        r = sess.query(Rifle).filter_by(caliber_id=c.id).first()
        if not r:
            d = sess.query(Diameter).filter_by(diameter=c.diameter.diameter).all()
            if d:
                for i in d:
                    sess.delete(i)
            sess.delete(c)
            sess.commit()
            self.set_data()

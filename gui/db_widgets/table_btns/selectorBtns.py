from PyQt5 import QtWidgets
from .templates import Ui_selectorBtns
from dbworker import db
from ..edit import CatalogItemEdit


class SelectBtn(QtWidgets.QWidget, Ui_selectorBtns):
    def __init__(self, model=None, editor=None):
        super(SelectBtn, self).__init__()
        self.setupUi(self)
        self.model = model
        self.editor = editor

    def delete(self, id):
        sess = db.SessMake()
        item = sess.query(self.model).get(id)
        sess.delete(item)
        sess.commit()

    def edit(self, id):
        sess = db.SessMake()
        item = sess.query(self.model).get(id)
        dlg = CatalogItemEdit(self.editor(item, 'edit'))
        if dlg.exec_():
            dlg.get()

    def copy(self, id):
        sess = db.SessMake()
        item = sess.query(self.model).get(id)
        dlg = CatalogItemEdit(self.editor(item, 'copy'))
        if dlg.exec_():
            dlg.get()

    def new(self):
        dlg = CatalogItemEdit(self.editor())
        if dlg.exec_():
            dlg.get()

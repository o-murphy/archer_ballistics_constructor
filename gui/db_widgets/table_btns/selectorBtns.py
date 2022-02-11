from PyQt5 import QtWidgets
from .templates import Ui_selectorBtns
from dbworker import db


class SelectBtn(QtWidgets.QWidget, Ui_selectorBtns):
    def __init__(self, ):
        super(SelectBtn, self).__init__()
        self.setupUi(self)

    def delete(self, model, id):
        sess = db.SessMake()
        item = sess.query(model).get(id)
        sess.delete(item)
        sess.commit()

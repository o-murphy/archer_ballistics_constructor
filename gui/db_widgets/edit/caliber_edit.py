from PyQt5 import QtWidgets
from .templates import Ui_caliberEdit
from dbworker import db
from dbworker.models import Caliber, Diameter


class CaliberEdit(QtWidgets.QDialog, Ui_caliberEdit):
    def __init__(self):
        super(CaliberEdit, self).__init__()
        self.setupUi(self)

    def get(self):
        sess = db.SessMake()
        diam = sess.query(Diameter).filter_by(diameter=self.diameter.value()).first()
        if not diam:
            diam = Diameter(self.diameter.value())
            sess.add(diam)
            sess.commit()
        cal = Caliber(self.name.text(), diam.id)
        sess.add(cal)
        sess.commit()
        return cal.id

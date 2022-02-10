from PyQt5 import QtWidgets
from .templates import Ui_templateInfo
from dbworker import db
from dbworker.models import *


class TemplateInfo(QtWidgets.QWidget, Ui_templateInfo):
    def __init__(self, id):
        super(TemplateInfo, self).__init__()
        self.setupUi(self)

        sess = db.SessMake()

        self.template = sess.query(Template).get(id)

        self.rifle = sess.query(Rifle).get(self.template.rifle_id)

        self.rifleName.setText(self.rifle.name)
        self.sh.setText(str(self.rifle.sh))
        self.twist.setText(
            f'1:{self.rifle.twist} Right' if self.rifle.is_right else f'1:{self.rifle.twist} Left'
        )
        self.caliberShort.setText(self.rifle.tile)

        self.cartridge = sess.query(Cartridge).get(self.template.cartridge_id)

        self.cartridgeName.setText(self.cartridge.name)
        self.mv.setText(str(self.cartridge.mv))
        self.temp.setText(str(self.cartridge.temp))
        self.ts.setText(str(self.cartridge.ts))
        self.bullet.setText(self.cartridge.bullet.name + ', ' + str(self.cartridge.bullet.weight) + ' gr')
        self.caliber.setText(
            self.cartridge.caliber.name + ', d:  ' + str(self.cartridge.caliber.diameter.diameter) + ' inch')

        drags = sess.query(DragFunc).filter_by(bullet_id=self.cartridge.bullet.id)

        for df in drags:
            self.drag_func.addItem(df.drag_type + ' ' + df.comment, df.id)

        cur_drag = sess.query(DragFunc).get(self.template.drag_func_id)
        self.drag_func.setCurrentText(
            cur_drag.drag_type + ' ' + cur_drag.comment
        )

        self.drag_func.currentIndexChanged.connect(self.update_template)

    def update_template(self):
        sess = db.SessMake()
        template = sess.query(Template).get(self.template.id)
        template.drag_func_id = self.drag_func.currentData()
        sess.commit()
        catalog_tab = self.findParent(self.parent(), 'catalogTab')
        catalog_tab.selector.template_list.set_data()

    def findParent(self, parent, objectName):
        if parent.objectName() != objectName:
            return self.findParent(parent.parent(), objectName)
        return parent
from PyQt5 import QtWidgets, QtGui
from dbworker import db


class CatalogList(QtWidgets.QWidget):
    def __init__(self, model=None, attrs=None):
        super(CatalogList, self).__init__()
        self.tableWidget: QtWidgets.QTableWidget = None
        self.data = []
        self.model = model
        self.attrs = attrs

    def setupTable(self):
        header = self.tableWidget.horizontalHeader()
        header.setSectionHidden(0, True)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        for i in range(2, header.count()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

    def update_table(self):
        self.tableWidget.setRowCount(len(self.data))
        for i, y in enumerate(self.data):
            for j, x in enumerate(y):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(x)))

    def viewport_row(self):
        cursor = self.tableWidget.viewport().mapFromGlobal(QtGui.QCursor().pos())
        return self.tableWidget.indexAt(cursor).row()

    def set_data(self):
        self.data = []
        sess = db.SessMake()
        if self.model:
            if self.attrs:
                items = sess.query(self.model).filter_by(attrs=self.attrs).all()
            else:
                items = sess.query(self.model).all()
            self.parse_data(items)
            self.update_table()

    def parse_data(self, items):
        self.data = []
        for i in items:
            self.data.append(i.__dict__)

    def copy_item(self):
        pass

    def edit_item(self):
        pass

    def delete_item(self):
        pass

    def new_item(self):
        pass

    def edit_dialog(self):
        pass

    def sel_cur(self):
        pass

    def findParent(self, parent, objectName):
        if parent.objectName() != objectName:
            return self.findParent(parent.parent(), objectName)
        return parent

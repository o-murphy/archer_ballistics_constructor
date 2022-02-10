from PyQt5 import QtWidgets, QtGui, QtCore
from .selectorBtns import SelectBtn


class CatalogList(QtWidgets.QWidget):
    def __init__(self):
        super(CatalogList, self).__init__()
        self.tableWidget: QtWidgets.QTableWidget = None

    def setupTable(self):
        header = self.tableWidget.horizontalHeader()
        header.setSectionHidden(0, True)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        for i in range(2, header.count()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

        self.tableWidget.doubleClicked.connect(self.edit_item)
        self.tableWidget.viewport().installEventFilter(self)
        self.tableWidget.clicked.connect(self.sel_cur)

    def eventFilter(self, watched, event):
        if watched == self.tableWidget.viewport() and event.type() == QtCore.QEvent.MouseButtonDblClick:
            if not self.tableWidget.item(self.viewport_row(), 0):
                self.new_item()
        return QtWidgets.QWidget.eventFilter(self, watched, event)

    def update_table(self):
        print('here will be query to db')

        self.tableWidget.setRowCount(len(self.data))
        for i, y in enumerate(self.data):

            for j, x in enumerate(y):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(x)))
            sel_btn = SelectBtn()
            edit_btn = sel_btn.editBtn
            del_btn = sel_btn.delBtn
            copy_btn = sel_btn.copyBtn
            edit_btn.clicked.connect(self.edit_item)
            del_btn.clicked.connect(self.delete_item)
            copy_btn.clicked.connect(self.copy_item)

            self.tableWidget.setCellWidget(i, self.tableWidget.columnCount() - 1, sel_btn)

    def viewport_row(self):
        cursor = self.tableWidget.viewport().mapFromGlobal(QtGui.QCursor().pos())
        return self.tableWidget.indexAt(cursor).row()

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

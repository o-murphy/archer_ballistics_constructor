from PyQt5 import QtWidgets, QtGui
from .catalog_item_edit import CatalogItemEdit
from .selectorBtns import SelectBtn


# class DeleteButton(QtWidgets.QPushButton):
#     def __init__(self, parent=None):
#         super(DeleteButton, self).__init__(parent)
#         self.setText('Del')


class EditButton(QtWidgets.QPushButton):
    def __init__(self, parent):
        super(EditButton, self).__init__(parent)
        self.setText('Edit')


class CopyButton(QtWidgets.QPushButton):
    def __init__(self, parent):
        super(CopyButton, self).__init__(parent)
        self.setText('Copy')


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

        self.tableWidget.currentCellChanged.connect(self.row_changed)
        self.tableWidget.doubleClicked.connect(self.double_clicked)

    def double_clicked(self, index):
        id = self.tableWidget.item(index.row(), 0).text()
        print('here will added to constructor', id)

    def row_changed(self, row, col, prow, pcol):
        id = self.tableWidget.item(row, 0).text()
        print('here will be query to db to draw info about', id)

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
        id = int(self.tableWidget.item(self.viewport_row(), 0).text())
        print('here will be create copy of item in db', id)

    def edit_item(self):
        id = int(self.tableWidget.item(self.viewport_row(), 0).text())
        print('here will be query to db to get', id)

        edit = CatalogItemEdit('Rifle', self.editor(temp_data))
        if edit.exec_():
            temp_data = edit.get_data()
            print('here will be query to db to edit', id)

    def delete_item(self):
        id = int(self.tableWidget.item(self.viewport_row(), 0).text())
        self.tableWidget.removeRow(self.viewport_row())
        print('here will be deleted', id)

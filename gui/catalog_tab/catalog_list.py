from PyQt5 import QtWidgets
from .catalog_item_edit import CatalogItemEdit
from .catalog_rifle import CatalogRifle


class DeleteButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super(DeleteButton, self).__init__(parent)
        self.setText('Del')


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

    def setupTable(self):
        self.data = [
            [101, 'WWWWWWWWWWWWWWWWWWWW', 'b', 'c', 'd'], [102, 2, 'b', 'c', 'd'], [103, 4, 'b', 'c', 'd']
        ]

        header = self.tableWidget.horizontalHeader()
        header.setSectionHidden(0, True)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        for i in range(2, header.count()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

        self.update_table()
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
                print(x)
            edit_btn = EditButton(self)
            del_btn = DeleteButton(self)
            copy_btn = CopyButton(self)
            edit_btn.clicked.connect(self.edit_item)
            del_btn.clicked.connect(self.delete_item)
            copy_btn.clicked.connect(self.copy_item)

            self.tableWidget.setCellWidget(i, self.tableWidget.columnCount()-3, copy_btn)
            self.tableWidget.setCellWidget(i, self.tableWidget.columnCount()-2, edit_btn)
            self.tableWidget.setCellWidget(i, self.tableWidget.columnCount()-1, del_btn)

    def copy_item(self):
        current_row = self.tableWidget.currentRow()
        id = int(self.tableWidget.item(current_row, 0).text())
        print('here will be create copy of item in db', id)

    def edit_item(self):
        current_row = self.tableWidget.currentRow()
        id = int(self.tableWidget.item(current_row, 0).text())
        print('here will be query to db to get', id)

        temp_data = {
            "rifleName": "G7 template",
            "caliberName": ".224 Remington",
            "sh": 90,
            "twist": 10,
            "caliberShort": ".224",
            "rightTwist": True,
        }

        edit = CatalogItemEdit('Rifle', CatalogRifle(temp_data))
        if edit.exec_():
            temp_data = edit.get_data()
            print('here will be query to db to edit', id)

    def delete_item(self):
        current_row = self.tableWidget.currentRow()
        id = int(self.tableWidget.item(current_row, 0).text())
        self.tableWidget.removeRow(current_row)
        print('here will be deleted', id)

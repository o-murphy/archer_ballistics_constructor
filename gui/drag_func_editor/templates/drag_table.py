from PyQt5 import QtCore, QtWidgets


class Ui_DragTable(QtWidgets.QTableWidget):
    def setupUI(self):
        self.setEnabled(True)
        self.setMaximumSize(QtCore.QSize(16777215, 80))
        self.setWordWrap(True)
        self.setObjectName("dragTable")
        self.setColumnCount(0)
        self.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.setVerticalHeaderItem(1, item)
        self.horizontalHeader().setVisible(False)
        self.horizontalHeader().setDefaultSectionSize(60)
        self.horizontalHeader().setMinimumSectionSize(28)
        self.verticalHeader().setDefaultSectionSize(28)
        self.verticalHeader().setMinimumSectionSize(28)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Ui_DragTable):
        _translate = QtCore.QCoreApplication.translate
        Ui_DragTable.setWindowTitle(_translate("Ui_DragTable", "Form"))
        item = self.verticalHeaderItem(0)
        item.setText(_translate("Ui_DragTable", "x"))
        item = self.verticalHeaderItem(1)
        item.setText(_translate("Ui_DragTable", "y"))

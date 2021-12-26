from PyQt5 import QtCore, QtWidgets


class Ui_DropTable(QtWidgets.QTableWidget):
    def setupUi(self):
        self.setGeometry(QtCore.QRect(20, 20, 200, 302))
        self.setMinimumSize(QtCore.QSize(200, 0))
        self.setMaximumSize(QtCore.QSize(200, 16777215))
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.setObjectName("dropTable")
        self.setColumnCount(3)
        self.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(2, item)
        self.horizontalHeader().setDefaultSectionSize(60)
        self.horizontalHeader().setMinimumSectionSize(50)
        self.verticalHeader().setVisible(False)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.horizontalHeaderItem(0)
        item.setText(_translate("Form", "dist"))
        item = self.horizontalHeaderItem(1)
        item.setText(_translate("Form", "hold off"))
        item = self.horizontalHeaderItem(2)
        item.setText(_translate("Form", "correction"))

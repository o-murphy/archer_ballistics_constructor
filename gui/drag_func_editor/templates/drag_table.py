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

        self.setStyleSheet("""
            QScrollBar:horizontal {
                    background-color: rgb(51, 51, 51); /*#2A2929;*/
                    height: 14px;
                    margin: 6px 15px 6px 15px;
                    border: 1px transparent #2A2929;
                    border-radius: 6px;
                }
            QScrollBar:horizontal:hover {
                background-color: rgb(51, 51, 51); /*#2A2929;*/
                height: 14px;
                margin: 3px 15px 3px 15px;
                border: 1px transparent #2A2929;
                border-radius: 6px;
            }

            QScrollBar::handle:horizontal
            {
                background-color: rgb(78, 78, 78);         /* #605F5F; */
                min-width: 5px;
                border-radius: 4px;
            }

            QScrollBar::handle:horizontal:hover
            {
                background-color: rgb(78, 78, 78);         /* #605F5F; */
                min-width: 5px;
                border-radius: 4px;
            }

            QScrollBar::sub-line:horizontal
            {
                margin: 0px 0px 0px 4px;
        		border: 1px solid rgb(51, 51, 51);
        		border-top-left-radius: 5px;
        		border-bottom-left-radius: 5px;
        		background-color: rgb(51, 51, 51);
        		color: white;
                height: 8px;
                width: 5px;
                subcontrol-position: left;
                subcontrol-origin: margin;
            }

            QScrollBar::add-line:horizontal
            {
                margin: 0px 4px 0px 0px;
        		border: 1px solid rgb(51, 51, 51);
        		border-top-right-radius: 5px;
        		border-bottom-right-radius: 5px;
        		background-color: rgb(51, 51, 51);
        		color: white;
                height: 8px;
                width: 5px;
                subcontrol-position: right;
                subcontrol-origin: margin;
            }


            QScrollBar::sub-line:horizontal:hover,QScrollBar::sub-line:horizontal:on
            {
                margin: 0px 0px 0px 4px;
        		border: 1px solid rgb(51, 51, 51); /*rgb(78, 78, 78);*/
        		border-top-left-radius: 5px;
        		border-bottom-left-radius: 5px;
        		background-color: rgb(78, 78, 78);
        		color: white;
                height: 8px;
                width: 5px;
                subcontrol-position: left;
                subcontrol-origin: margin;
            }



            QScrollBar::add-line:horizontal:hover, QScrollBar::add-line:horizontal:on
            {
                margin: 0px 4px 0px 0px;
        		border: 1px solid rgb(51, 51, 51);
        		border-top-right-radius: 5px;
        		border-bottom-right-radius: 5px;
        		background-color: rgb(78, 78, 78);
        		color: white;
                height: 8px;
                width: 5px;
                subcontrol-position: right;
                subcontrol-origin: margin;
            }

            QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal
            {
            			        background: none;

            }

            QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
            {
                background: none;
            }

                """)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.verticalHeaderItem(0)
        item.setText(_translate("Form", "x"))
        item = self.verticalHeaderItem(1)
        item.setText(_translate("Form", "y"))

from PyQt5 import QtWidgets, QtCore
from .templates import Ui_DragTable
from modules.converter import BConverter

rnd = BConverter.auto_rnd


class DragTable(Ui_DragTable):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.setStyleSheet("""
        


QScrollBar:horizontal {
        background-color: #2A2929;
        height: 16px;
        margin: 3px 15px 3px 15px;
        border: 1px transparent #2A2929;
        border-radius: 4px;
    }
    QScrollBar::handle:horizontal
    {
        background-color: rgb(78, 78, 78);         /* #605F5F; */
        min-height: 5px;
        border-radius: 4px;
    }

    QScrollBar::sub-line:horizontal
    {
        margin: 0px 0px 0px 2px;
		border: 1px solid rgb(78, 78, 78);
		border-top-left-radius: 5px;
		border-bottom-left-radius: 5px;
		background-color: rgb(78, 78, 78);
		color: white;
        height: 8px;
        width: 8px;
        subcontrol-position: left;
        subcontrol-origin: margin;
    }

    QScrollBar::add-line:horizontal
    {
        margin: 0px 2px 0px 0px;
		border: 1px solid rgb(78, 78, 78);
		border-top-right-radius: 5px;
		border-bottom-right-radius: 5px;
		background-color: rgb(78, 78, 78);
		color: white;
        height: 8px;
        width: 8px;
        subcontrol-position: right;
        subcontrol-origin: margin;
    }


    QScrollBar::sub-line:horizontal:hover,QScrollBar::sub-line:horizontal:on
    {
		margin: 0px 0px 0px 2px;
       	border: 1px solid rgb(78, 78, 78);
		border-top-left-radius: 5px;
		border-bottom-left-radius: 5px;
		background-color: rgb(78, 78, 78);
        height: 8px;
        width: 8px;
        subcontrol-position: left;
        subcontrol-origin: margin;
    }



    QScrollBar::add-line:horizontal:hover, QScrollBar::add-line:horizontal:on
    {
		margin: 0px 2px 0px 0px;
		border: 1px solid rgb(78, 78, 78);
		border-top-right-radius: 5px;
		border-bottom-right-radius: 5px;
		background-color: rgb(78, 78, 78);
        height: 8px;
        width: 8px;
		subcontrol-position: right;
        subcontrol-origin: margin;
    }

    QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
    {
			        background: none;
    }

    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
    {
        background: none;

    }

        """)

    def set(self, current_data, default_data):
        for i in range(self.columnCount()):
            self.removeColumn(0)
        data = current_data if current_data else default_data
        if data:
            for k, v in enumerate(data):
                self.insertColumn(k)
                iv = QtWidgets.QTableWidgetItem()
                ivw = QtWidgets.QLineEdit()
                ivw.setEnabled(False)
                ivw.setText(str(rnd(v[0])))
                self.setItem(0, k, iv)
                self.setCellWidget(0, k, ivw)

                ii = QtWidgets.QTableWidgetItem()
                iiw = QtWidgets.QLineEdit()
                iiw.setEnabled(False)
                iiw.setText(str(rnd(v[1])))
                self.setItem(1, k, ii)
                self.setCellWidget(1, k, iiw)

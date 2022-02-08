from .templates import Ui_catalogCartridgeList
from .catalog_list import CatalogList
from .catalog_cartridge import CatalogCartridge
from .catalog_item_edit import CatalogItemEdit

from dbworker import db


class CatalogCartridgeList(CatalogList, Ui_catalogCartridgeList):
    def __init__(self):
        super(CatalogCartridgeList, self).__init__()
        self.setupUi(self)
        self.editor = CatalogCartridge

        self.data = []
        self.setupTable()
        # self.set_data()
        self.update_table()

    def set_data(self):
        self.data = []
        cartridges = db.get_cartridges()
        for i in cartridges:
            self.data.append([i.id, i.name, i.caliber.name, i.mv, i.temp])

    def copy_item(self):
        id = int(self.tableWidget.item(self.viewport_row(), 0).text())
        cartridge = db.get_cartridge(id)

        edit = CatalogItemEdit('Rifle', self.editor(cartridge))
        if edit.exec_():
            new_cartridge = cartridge.__dict__
            new_data = edit.get_data()
            new_cartridge.update(new_data)
            new_cartridge['diameter'] = cartridge.caliber.diameter.diameter
            new_cartridge['name'] = new_data['cartridgeName']
            new_cartridge['caliberName'] = cartridge.caliber.name

            db.add_cartridge(**new_cartridge)
        self.set_data()
        self.update_table()

    def edit_item(self):
        id = int(self.tableWidget.item(self.viewport_row(), 0).text())
        cartridge = db.get_cartridge(id)
        edit = CatalogItemEdit('Cartridge', self.editor(cartridge))
        if edit.exec_():
            new_cartridge = edit.get_data()
            new_cartridge['diameter'] = cartridge.caliber.diameter.diameter
            new_cartridge['name'] = new_cartridge['cartridgeName']
            new_cartridge['caliberName'] = cartridge.caliber.name

            db.update_cartridge(id, new_cartridge)
        self.set_data()
        self.update_table()

    def delete_item(self):
        id = int(self.tableWidget.item(self.viewport_row(), 0).text())
        db.delete_cartridge(id)
        self.set_data()
        self.update_table()

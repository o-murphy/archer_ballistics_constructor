from ..tables import CatalogRifleList
from ..info import CatalogRifleInfo
from .tab import Tab
from dbworker import db
from dbworker.models import *


class RiflesTab(Tab):
    def __init__(self):
        super(RiflesTab, self).__init__()
        self.list = CatalogRifleList()
        self.info = CatalogRifleInfo()
        self.set()

    def add_template(self):
        sess = db.SessMake()

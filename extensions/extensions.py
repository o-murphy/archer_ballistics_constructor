import importlib
import os
from pathlib import Path
from PyQt5.QtWidgets import QMainWindow

import logging

logging.basicConfig(level=logging.INFO, filename="extension_importer.log")
log = logging.getLogger('xextension importer')


class Extend(object):
    def __init__(self, enter_point):
        self.enter_point = enter_point
        self.find_extensions()

    def find_extensions(self):
        edir = Path(__file__ + r'\extensions').parent.parent
        for i, each in enumerate(os.listdir(edir)):
            p = Path(str(edir) + fr'\{each}')
            if p.is_dir():
                try:
                    lib = importlib.import_module('extensions.' + p.name, package=str(p))
                    log.info(f'{p.name} import OK')
                    extension = lib.XExtension(self.enter_point)
                    log.info(f'{extension} loads OK')
                    extension.include()
                except ImportError as error:
                    log.warning(error)
                except AttributeError as error:
                    log.warning(error)
                except Exception as error:
                    log.warning(error)

    def import_extension(self):
        pass


class Extension(object):
    def __init__(self, enter_point: QMainWindow = None):
        self.enter_point = enter_point

    def include(self):
        pass


if __name__ == '__main__':
    e = Extend()

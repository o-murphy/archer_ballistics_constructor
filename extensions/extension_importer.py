import importlib
import os
from pathlib import Path
from PyQt5.QtWidgets import QMainWindow, QWidget
from modules.env_update import USER_ARCHERBC

import logging

logging.basicConfig(level=logging.INFO,
                    filename=f"{USER_ARCHERBC}/x_importer.log",
                    filemode='w',
                    format='%(asctime)s [%(name)-10s] %(levelname)-8s %(message)s')
log = logging.getLogger('x_importer')


class Extension(object):
    def __init__(self, enter_point: [QWidget, QMainWindow] = None):
        self.enter_point = enter_point

    def include(self):
        pass


class ExtendAll(object):
    def __init__(self, enter_point: [QWidget, QMainWindow] = None):
        self.enter_point = enter_point
        self.find_extensions()

    def find_extensions(self):
        edir = Path(__file__ + r'\extensions').parent.parent
        for i, each in enumerate(os.listdir(edir)):
            p = Path(str(edir) + fr'\{each}')
            if p.is_dir() and not str(p).endswith('__pycache__'):
                lib = None
                try:
                    lib = importlib.import_module('extensions.' + p.name, package=str(p))
                    log.info(f'[{lib.__name__}]\timport OK')
                    extension = lib.XExtension(self.enter_point)
                    log.info(f'[{lib.__name__}.{type(extension).__name__}]\tload OK')
                    extension.include()
                except ImportError as error:
                    log.warning(error)
                except AttributeError as error:
                    if lib:
                        log.warning(f'[{lib.__name__}]\t{error.__class__.__name__}:\t{error}')
                    else:
                        log.warning(f'[RuntimeWarning]\t{error.__class__.__name__}:\t{error}')

                except Exception as error:
                    if lib:
                        log.warning(f'[{lib.__name__}]\t{error.__class__.__name__}:\t{error}')
                    else:
                        log.warning(f'[RuntimeWarning]\t{error.__class__.__name__}:\t{error}')

    def import_extension(self):
        pass


if __name__ == '__main__':
    pass

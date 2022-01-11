# -*- coding: utf-8 -*-

import os
import shutil


USER_PATH = rf'{os.environ["HOMEDRIVE"]}{os.environ["HOMEPATH"]}'
USER_DOCS = rf'{USER_PATH}\Documents'

USER_ARCHERBC = rf'{USER_DOCS}\ArcherBC'
USER_RECENT = rf'{USER_ARCHERBC}\Recent'
USER_BACKUP = rf'{USER_ARCHERBC}\Backup'
MK_DIRS = [USER_ARCHERBC, USER_RECENT, USER_BACKUP]

USER_TEMP = rf'{USER_ARCHERBC}\temp'
RM_DIRS = [USER_TEMP]

CONFIG_PATH = rf'{USER_ARCHERBC}\settings.ini'


def main():
    for dir in MK_DIRS:
        if not os.path.isdir(dir):
            os.mkdir(dir)
    for dir in RM_DIRS:
        if os.path.isdir(dir):
            shutil.rmtree(dir)


if __name__ == '__main__':
    main()

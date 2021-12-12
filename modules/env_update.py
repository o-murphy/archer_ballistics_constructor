# -*- coding: utf-8 -*-

import os


USER_PATH = rf'{os.environ["HOMEDRIVE"]}{os.environ["HOMEPATH"]}'
USER_DOCS = rf'{USER_PATH}\Documents'
USER_ARCHERBC = rf'{USER_DOCS}\ArcherBC'
USER_RECENT = rf'{USER_ARCHERBC}\Recent'
USER_BACKUP = rf'{USER_ARCHERBC}\Backup'


def main():
    # if 'ArcherBC' not in os.listdir(USER_DOCS):
    if not os.path.isdir(USER_ARCHERBC):
        os.mkdir(USER_ARCHERBC)
    # if 'Recent' not in os.listdir(USER_ARCHERBC):
    if not os.path.isdir(USER_RECENT):
        os.mkdir(USER_RECENT)
    # if 'Backup' not in os.listdir(USER_ARCHERBC):
    if not os.path.isdir(USER_BACKUP):
        os.mkdir(USER_BACKUP)


if __name__ == '__main__':
    main()

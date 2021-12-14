from PyQt5 import QtWidgets, QtGui
import sys
import os
from gui import Ui_ArcheBCUpdate
import urllib.request
from modules import env_update
import json
from modules.get_file_props import getFileProperties as get_file_props


class UpdaterApp(QtWidgets.QMainWindow, Ui_ArcheBCUpdate):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.current_file = None
        self.get_current_executable()

        self.current_v = None
        self.get_current_ver()

        self.download_url = None
        self.download_filename = None
        self.buttonBox.setVisible(False)
        self.check_updates()

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def get_current_executable(self):
        if os.path.isfile(r'archerbc.py'):
            self.current_file = r'archerbc.py'
        elif os.path.isfile('archerbc.exe'):
            self.current_file = r'archerbc.exe'

    def get_current_ver(self):
        props = get_file_props(self.current_file)
        if props:
            if props['StringFileInfo']:
                self.current_v = props['StringFileInfo']['ProductVersion']

    # when push button is pressed, this method is called
    def Handle_Progress(self, blocknum, blocksize, totalsize):
        readed_data = blocknum * blocksize  # calculate the progress
        if totalsize > 0:
            download_percentage = readed_data * 100 / totalsize
            self.progressBar.setValue(int(download_percentage))
            QtWidgets.QApplication.processEvents()

    def Download(self):
        self.label.setText('Downloading update,\nplease wait...')
        env_update.main()

        if not os.path.isdir(rf'{env_update.USER_ARCHERBC}\temp'):
            os.mkdir(rf'{env_update.USER_ARCHERBC}\temp')

        down_url = self.download_url
        save_loc = rf'{env_update.USER_TEMP}\{self.download_filename}'  # specify save location
        urllib.request.urlretrieve(down_url, save_loc, self.Handle_Progress)  # Downloading using urllib

        os.system(rf'{save_loc} /verysilent')
        env_update.main()

    def check_updates(self):
        branch_url = 'https://api.github.com/repos/o-murphy/archer_ballistics_constructor/releases'
        try:
            response = urllib.request.urlopen(branch_url)
            if response.getcode() == 200:
                j = json.loads(response.read().decode("utf-8"))
                last_release = j[len(j)-1]
                last_v = last_release['tag_name']
                if last_v != self.current_v:
                    self.download_url = last_release['assets'][0]['browser_download_url']
                    self.download_filename = last_release['assets'][0]['name']

            if self.download_url:
                self.label.setText('New version of ArcherBC found,\ndo you want to update?')
                self.buttonBox.setVisible(True)
            else:
                self.reject()
        except:
            self.reject()

    def accept(self):
        self.buttonBox.setVisible(False)
        self.Download()
        self.reject()

    def reject(self):
        if self.current_file == r'archerbc.py':
            os.system(fr'start venv\Scripts\python.exe {self.current_file}')
        elif self.current_file == 'archerbc.exe':
            os.system(fr'start {self.current_file}')
        sys.exit()

    def closeEvent(self, event) -> None:
        self.reject()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = UpdaterApp()
    window.show()
    app.setWindowIcon(QtGui.QIcon('Icon.png'))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

pyinstaller -y -i=.rsrc\Icon.ico --add-data=.rsrc;.rsrc\ --add-data=drv;drv\ archerbc.py --version-file=version.txt -w
pyinstaller -y -i=.rsrc\Icon.ico archerbc_updater.py -w
"%ProgramFiles(x86)%\INNOSE~1\ISCC.exe" /Qp installer64_relative.iss
AcherBC_setup.exe /verysilent
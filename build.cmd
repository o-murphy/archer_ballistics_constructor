pyinstaller -y -w --clean -i=.rsrc\Icon.ico --version-file=version.txt --add-data=.rsrc;.rsrc\ --add-data=drv;drv\ archerbc.py
pyinstaller -y -w --clean -i=.rsrc\Icon.ico --version-file=uversion.txt archerbc_updater.py
"%ProgramFiles(x86)%\INNOSE~1\ISCC.exe" /Qp installer64_relative.iss
AcherBC_setup.exe /verysilent
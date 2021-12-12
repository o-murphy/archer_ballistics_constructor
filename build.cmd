pyinstaller -y -i=.rsrc\Icon.ico --add-data=.rsrc;.rsrc\ --add-data=drv;drv\ run.py
"%ProgramFiles(x86)%\INNOSE~1\ISCC.exe" /Qp installer64_relative.iss
AcherBC_setup.exe /verysilent
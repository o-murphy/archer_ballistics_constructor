def try_qt():
    import sys
    print(sys.version)

    try:
        from PyQt5 import QtWidgets, QtCore, QtGui
        print(QtWidgets, QtCore, QtGui)
        print('sucsess')
    except Exception as err:
        print(err)
        while True:
            continue
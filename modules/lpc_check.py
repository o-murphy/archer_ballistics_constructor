# -*- coding: utf-8 -*-

from PyQt5 import QtCore
import os
import win32com.client
import subprocess


class UsbStatusCode:
    DRIVER_ERROR = 'Driver not installed'
    DFU_NOT_CONNECTED = 'No DFU device found'
    MULTIPLE_DFU = 'Multiple DFU devices found'
    CONNECTED = 'Successfully Connected'


class lpcRunThread(object):

    def setupLpcTread(self):
        self.thread = QtCore.QThread()
        self.lpc_device_handler = lpcDeviceHandler()
        self.lpc_device_handler.moveToThread(self.thread)
        self.lpc_device_handler.newLpcDeviceStatus.connect(self.updateLpcDeviceStatus)
        self.thread.started.connect(self.lpc_device_handler.run)
        # self.thread.start()

    def startLpcThread(self):
        self.lpc_device_handler.cont = True
        self.thread.start()

    def stopLpcThread(self):
        self.lpc_device_handler.cont = False
        self.thread.exit()
        pass

    @QtCore.pyqtSlot(str)
    def updateLpcDeviceStatus(self, status):
        if hasattr(self, 'objectName'):
            print(status, self.objectName())


class lpcDeviceHandler(QtCore.QObject):
    running = False
    cont = True
    newLpcDeviceStatus = QtCore.pyqtSignal(str)  # *args
    __VID = 0x1FC9
    __PID = 0x000C
    __dev = None

    def run(self):
        while self.cont:
            self.newLpcDeviceStatus.emit(str(self.check()))
            QtCore.QThread.msleep(100)

    @staticmethod
    def check():
        wmi = win32com.client.GetObject("winmgmts:")
        lpc_devices = [
            usb.Dependent.split('\\')[6] for usb in wmi.InstancesOf("Win32_USBControllerDevice")
            if usb.Dependent.split('\\')[6] == 'VID_1FC9&PID_000C'
        ]
        try:
            if not lpc_devices:
                raise ValueError(UsbStatusCode.DFU_NOT_CONNECTED)
            if len(lpc_devices) > 1:
                raise ValueError(UsbStatusCode.MULTIPLE_DFU)
        except ValueError as error:
            return error
        return UsbStatusCode.CONNECTED

def check_lpc_driver():
    try:
        if os.path.isfile(os.environ['PROGRAMFILES'] + r'\NXP\LPC Driver Installer\lpcdevice\lpcdevice.cat'):
            return True
        else:
            raise FileNotFoundError
    except FileNotFoundError:
        return False

def install_lpc_driver():
    if os.path.isfile(r'drv\lpc_driver_setup.exe'):
        subprocess.call(r'drv\lpc_driver_setup.exe /qr', shell=True)
    else:
        pass


if __name__ == '__main__':
    check_lpc_driver()
    pass

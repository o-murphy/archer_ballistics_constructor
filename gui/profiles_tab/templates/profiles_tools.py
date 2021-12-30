# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_templates\profiles_tools.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_profilesTools(object):
    def setupUi(self, profilesTools):
        profilesTools.setObjectName("profilesTools")
        profilesTools.resize(424, 30)
        profilesTools.setMinimumSize(QtCore.QSize(0, 30))
        profilesTools.setMaximumSize(QtCore.QSize(424, 16777215))
        self.gridLayout = QtWidgets.QGridLayout(profilesTools)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.upProfile = QtWidgets.QPushButton(profilesTools)
        self.upProfile.setMinimumSize(QtCore.QSize(30, 30))
        self.upProfile.setMaximumSize(QtCore.QSize(30, 30))
        self.upProfile.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui_templates\\../.rsrc/res/drawable/arrowupbtn21a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.upProfile.setIcon(icon)
        self.upProfile.setObjectName("upProfile")
        self.gridLayout.addWidget(self.upProfile, 0, 0, 1, 1)
        self.downProfile = QtWidgets.QPushButton(profilesTools)
        self.downProfile.setMinimumSize(QtCore.QSize(30, 30))
        self.downProfile.setMaximumSize(QtCore.QSize(30, 30))
        self.downProfile.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui_templates\\../.rsrc/res/drawable/arrowdownbtn21a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downProfile.setIcon(icon1)
        self.downProfile.setObjectName("downProfile")
        self.gridLayout.addWidget(self.downProfile, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.newFile = QtWidgets.QPushButton(profilesTools)
        self.newFile.setMinimumSize(QtCore.QSize(30, 30))
        self.newFile.setMaximumSize(QtCore.QSize(30, 30))
        self.newFile.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui_templates\\../.rsrc/res/drawable/copybtn21a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newFile.setIcon(icon2)
        self.newFile.setIconSize(QtCore.QSize(20, 20))
        self.newFile.setCheckable(False)
        self.newFile.setChecked(False)
        self.newFile.setObjectName("newFile")
        self.gridLayout.addWidget(self.newFile, 0, 3, 1, 1)
        self.saveButton = QtWidgets.QPushButton(profilesTools)
        self.saveButton.setMinimumSize(QtCore.QSize(30, 30))
        self.saveButton.setMaximumSize(QtCore.QSize(30, 30))
        self.saveButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui_templates\\../.rsrc/res/drawable/savebtn_menu21a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon3)
        self.saveButton.setIconSize(QtCore.QSize(20, 20))
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 0, 4, 1, 1)
        self.saveAsButton = QtWidgets.QPushButton(profilesTools)
        self.saveAsButton.setMinimumSize(QtCore.QSize(30, 30))
        self.saveAsButton.setMaximumSize(QtCore.QSize(30, 30))
        self.saveAsButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ui_templates\\../.rsrc/res/drawable/saveasbtn_menu21a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveAsButton.setIcon(icon4)
        self.saveAsButton.setIconSize(QtCore.QSize(20, 20))
        self.saveAsButton.setCheckable(False)
        self.saveAsButton.setChecked(False)
        self.saveAsButton.setObjectName("saveAsButton")
        self.gridLayout.addWidget(self.saveAsButton, 0, 5, 1, 1)
        self.openFile = QtWidgets.QPushButton(profilesTools)
        self.openFile.setMinimumSize(QtCore.QSize(30, 30))
        self.openFile.setMaximumSize(QtCore.QSize(30, 30))
        self.openFile.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("ui_templates\\../.rsrc/res/drawable/openbtn_menu21a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openFile.setIcon(icon5)
        self.openFile.setIconSize(QtCore.QSize(20, 20))
        self.openFile.setCheckable(False)
        self.openFile.setChecked(False)
        self.openFile.setObjectName("openFile")
        self.gridLayout.addWidget(self.openFile, 0, 6, 1, 1)
        self.closeFile = QtWidgets.QPushButton(profilesTools)
        self.closeFile.setMinimumSize(QtCore.QSize(30, 30))
        self.closeFile.setMaximumSize(QtCore.QSize(30, 30))
        self.closeFile.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("ui_templates\\../.rsrc/res/drawable/exitbtn_menu21a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeFile.setIcon(icon6)
        self.closeFile.setIconSize(QtCore.QSize(20, 20))
        self.closeFile.setCheckable(False)
        self.closeFile.setChecked(False)
        self.closeFile.setObjectName("closeFile")
        self.gridLayout.addWidget(self.closeFile, 0, 7, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 9, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 8, 1, 1)
        self.newProfileButton = QtWidgets.QPushButton(profilesTools)
        self.newProfileButton.setMinimumSize(QtCore.QSize(30, 30))
        self.newProfileButton.setMaximumSize(QtCore.QSize(30, 30))
        self.newProfileButton.setWhatsThis("")
        self.newProfileButton.setAccessibleDescription("")
        self.newProfileButton.setStyleSheet("QPushButton {color: white;}\n"
"QPushButton::QToolTip {color: black}")
        self.newProfileButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("ui_templates\\../.rsrc/res/drawable/addbtn_menu21a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newProfileButton.setIcon(icon7)
        self.newProfileButton.setIconSize(QtCore.QSize(25, 25))
        self.newProfileButton.setObjectName("newProfileButton")
        self.gridLayout.addWidget(self.newProfileButton, 0, 9, 1, 1)
        self.removeProfileButton = QtWidgets.QPushButton(profilesTools)
        self.removeProfileButton.setMinimumSize(QtCore.QSize(30, 30))
        self.removeProfileButton.setMaximumSize(QtCore.QSize(30, 30))
        self.removeProfileButton.setIconSize(QtCore.QSize(25, 25))
        self.removeProfileButton.setObjectName("removeProfileButton")
        self.gridLayout.addWidget(self.removeProfileButton, 0, 10, 1, 1)
        self.clearAllProfiles = QtWidgets.QPushButton(profilesTools)
        self.clearAllProfiles.setMinimumSize(QtCore.QSize(30, 30))
        self.clearAllProfiles.setMaximumSize(QtCore.QSize(30, 30))
        self.clearAllProfiles.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("ui_templates\\../.rsrc/res/drawable/deletebtn21a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearAllProfiles.setIcon(icon8)
        self.clearAllProfiles.setIconSize(QtCore.QSize(20, 20))
        self.clearAllProfiles.setObjectName("clearAllProfiles")
        self.gridLayout.addWidget(self.clearAllProfiles, 0, 11, 1, 1)
        self.saveProfileButton = QtWidgets.QPushButton(profilesTools)
        self.saveProfileButton.setMinimumSize(QtCore.QSize(30, 30))
        self.saveProfileButton.setMaximumSize(QtCore.QSize(30, 30))
        self.saveProfileButton.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("ui_templates\\../.rsrc/res/drawable-hdpi-v4/bookmarksbtn_menu21a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveProfileButton.setIcon(icon9)
        self.saveProfileButton.setIconSize(QtCore.QSize(20, 20))
        self.saveProfileButton.setCheckable(False)
        self.saveProfileButton.setObjectName("saveProfileButton")
        self.gridLayout.addWidget(self.saveProfileButton, 0, 12, 1, 1)

        self.retranslateUi(profilesTools)
        QtCore.QMetaObject.connectSlotsByName(profilesTools)

    def retranslateUi(self, profilesTools):
        _translate = QtCore.QCoreApplication.translate
        profilesTools.setWindowTitle(_translate("profilesTools", "Form"))
        self.upProfile.setToolTip(_translate("profilesTools", "<font color=black>Move up (CTRL+Up)</font>"))
        self.upProfile.setShortcut(_translate("profilesTools", "Ctrl+Up"))
        self.downProfile.setToolTip(_translate("profilesTools", "<font color=black>Move down (CTRL+Up)</font>"))
        self.downProfile.setShortcut(_translate("profilesTools", "Ctrl+Up"))
        self.newFile.setToolTip(_translate("profilesTools", "<font color=black>New File (CTRL+Shift+N)</font>"))
        self.newFile.setShortcut(_translate("profilesTools", "Ctrl+Shift+N"))
        self.saveButton.setToolTip(_translate("profilesTools", "<font color=black>Save File (CTRL+S)</font>"))
        self.saveButton.setShortcut(_translate("profilesTools", "Ctrl+S"))
        self.saveAsButton.setToolTip(_translate("profilesTools", "<font color=black>Save file as... (CTRL+Shift+S)</font>"))
        self.saveAsButton.setShortcut(_translate("profilesTools", "Ctrl+Shift+S"))
        self.openFile.setToolTip(_translate("profilesTools", "<font color=black>Open File (CTRL+O)</font>"))
        self.openFile.setShortcut(_translate("profilesTools", "Ctrl+O"))
        self.closeFile.setToolTip(_translate("profilesTools", "<font color=black>Close File (CTRL+Shift+C)</font>"))
        self.closeFile.setShortcut(_translate("profilesTools", "Ctrl+Shift+C"))
        self.newProfileButton.setToolTip(_translate("profilesTools", "<font color=black>Add Profile (CTRL+N)</font>"))
        self.newProfileButton.setShortcut(_translate("profilesTools", "Ctrl+N"))
        self.removeProfileButton.setToolTip(_translate("profilesTools", "<font color=black>Remove Profile (CTRL+Del)</font>"))
        self.removeProfileButton.setText(_translate("profilesTools", "—"))
        self.removeProfileButton.setShortcut(_translate("profilesTools", "Ctrl+Del"))
        self.clearAllProfiles.setToolTip(_translate("profilesTools", "<font color=black>Remove All Profiles (CTRL+Shift+Del)</font>"))
        self.clearAllProfiles.setShortcut(_translate("profilesTools", "Ctrl+Shift+Del"))
        self.saveProfileButton.setToolTip(_translate("profilesTools", "<font color=black>Save to database</font>"))

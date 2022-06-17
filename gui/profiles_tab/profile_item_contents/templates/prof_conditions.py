# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_templates\prof_conditions.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_conditions(object):
    def setupUi(self, conditions):
        conditions.setObjectName("conditions")
        conditions.resize(518, 250)
        self.gridLayout = QtWidgets.QGridLayout(conditions)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(conditions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_84 = QtWidgets.QLabel(self.groupBox)
        self.label_84.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_84.setFont(font)
        self.label_84.setObjectName("label_84")
        self.gridLayout_6.addWidget(self.label_84, 5, 0, 1, 1)
        self.widget_42 = QtWidgets.QWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_42.sizePolicy().hasHeightForWidth())
        self.widget_42.setSizePolicy(sizePolicy)
        self.widget_42.setMinimumSize(QtCore.QSize(180, 0))
        self.widget_42.setMaximumSize(QtCore.QSize(180, 16777215))
        self.widget_42.setObjectName("widget_42")
        self.horizontalLayout_58 = QtWidgets.QHBoxLayout(self.widget_42)
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName("horizontalLayout_58")
        self.z_pressure = QtWidgets.QSpinBox(self.widget_42)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.z_pressure.sizePolicy().hasHeightForWidth())
        self.z_pressure.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.z_pressure.setFont(font)
        self.z_pressure.setStyleSheet("")
        self.z_pressure.setMaximum(1100)
        self.z_pressure.setProperty("value", 760)
        self.z_pressure.setObjectName("z_pressure")
        self.horizontalLayout_58.addWidget(self.z_pressure)
        self.gridLayout_6.addWidget(self.widget_42, 3, 1, 1, 1)
        self.widget_44 = QtWidgets.QWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_44.sizePolicy().hasHeightForWidth())
        self.widget_44.setSizePolicy(sizePolicy)
        self.widget_44.setMinimumSize(QtCore.QSize(180, 0))
        self.widget_44.setMaximumSize(QtCore.QSize(180, 16777215))
        self.widget_44.setObjectName("widget_44")
        self.horizontalLayout_60 = QtWidgets.QHBoxLayout(self.widget_44)
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName("horizontalLayout_60")
        self.z_angle = QtWidgets.QSpinBox(self.widget_44)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.z_angle.sizePolicy().hasHeightForWidth())
        self.z_angle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.z_angle.setFont(font)
        self.z_angle.setStyleSheet("")
        self.z_angle.setMaximum(359)
        self.z_angle.setProperty("value", 0)
        self.z_angle.setObjectName("z_angle")
        self.horizontalLayout_60.addWidget(self.z_angle)
        self.gridLayout_6.addWidget(self.widget_44, 5, 1, 1, 1)
        self.widget_39 = QtWidgets.QWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_39.sizePolicy().hasHeightForWidth())
        self.widget_39.setSizePolicy(sizePolicy)
        self.widget_39.setMinimumSize(QtCore.QSize(180, 0))
        self.widget_39.setMaximumSize(QtCore.QSize(180, 16777215))
        self.widget_39.setObjectName("widget_39")
        self.horizontalLayout_55 = QtWidgets.QHBoxLayout(self.widget_39)
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")
        self.z_temp = QtWidgets.QSpinBox(self.widget_39)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.z_temp.sizePolicy().hasHeightForWidth())
        self.z_temp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.z_temp.setFont(font)
        self.z_temp.setStyleSheet("")
        self.z_temp.setProperty("showGroupSeparator", False)
        self.z_temp.setMinimum(-60)
        self.z_temp.setProperty("value", 15)
        self.z_temp.setObjectName("z_temp")
        self.horizontalLayout_55.addWidget(self.z_temp)
        self.gridLayout_6.addWidget(self.widget_39, 0, 1, 1, 1)
        self.widget_41 = QtWidgets.QWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_41.sizePolicy().hasHeightForWidth())
        self.widget_41.setSizePolicy(sizePolicy)
        self.widget_41.setMinimumSize(QtCore.QSize(180, 0))
        self.widget_41.setMaximumSize(QtCore.QSize(180, 16777215))
        self.widget_41.setObjectName("widget_41")
        self.horizontalLayout_57 = QtWidgets.QHBoxLayout(self.widget_41)
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName("horizontalLayout_57")
        self.z_humidity = QtWidgets.QSpinBox(self.widget_41)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.z_humidity.sizePolicy().hasHeightForWidth())
        self.z_humidity.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.z_humidity.setFont(font)
        self.z_humidity.setStyleSheet("")
        self.z_humidity.setMaximum(100)
        self.z_humidity.setProperty("value", 50)
        self.z_humidity.setObjectName("z_humidity")
        self.horizontalLayout_57.addWidget(self.z_humidity)
        self.gridLayout_6.addWidget(self.widget_41, 2, 1, 1, 1)
        self.widget_45 = QtWidgets.QWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_45.sizePolicy().hasHeightForWidth())
        self.widget_45.setSizePolicy(sizePolicy)
        self.widget_45.setMinimumSize(QtCore.QSize(180, 0))
        self.widget_45.setMaximumSize(QtCore.QSize(180, 16777215))
        self.widget_45.setObjectName("widget_45")
        self.horizontalLayout_61 = QtWidgets.QHBoxLayout(self.widget_45)
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName("horizontalLayout_61")
        self.z_azimuth = QtWidgets.QSpinBox(self.widget_45)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.z_azimuth.sizePolicy().hasHeightForWidth())
        self.z_azimuth.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.z_azimuth.setFont(font)
        self.z_azimuth.setStyleSheet("")
        self.z_azimuth.setMaximum(359)
        self.z_azimuth.setProperty("value", 270)
        self.z_azimuth.setObjectName("z_azimuth")
        self.horizontalLayout_61.addWidget(self.z_azimuth)
        self.gridLayout_6.addWidget(self.widget_45, 6, 1, 1, 1)
        self.widget_43 = QtWidgets.QWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_43.sizePolicy().hasHeightForWidth())
        self.widget_43.setSizePolicy(sizePolicy)
        self.widget_43.setMinimumSize(QtCore.QSize(180, 0))
        self.widget_43.setMaximumSize(QtCore.QSize(180, 16777215))
        self.widget_43.setObjectName("widget_43")
        self.horizontalLayout_59 = QtWidgets.QHBoxLayout(self.widget_43)
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName("horizontalLayout_59")
        self.z_latitude = QtWidgets.QSpinBox(self.widget_43)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.z_latitude.sizePolicy().hasHeightForWidth())
        self.z_latitude.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.z_latitude.setFont(font)
        self.z_latitude.setStyleSheet("")
        self.z_latitude.setMaximum(359)
        self.z_latitude.setProperty("value", 0)
        self.z_latitude.setObjectName("z_latitude")
        self.horizontalLayout_59.addWidget(self.z_latitude)
        self.gridLayout_6.addWidget(self.widget_43, 4, 1, 1, 1)
        self.widget_40 = QtWidgets.QWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_40.sizePolicy().hasHeightForWidth())
        self.widget_40.setSizePolicy(sizePolicy)
        self.widget_40.setMinimumSize(QtCore.QSize(180, 0))
        self.widget_40.setMaximumSize(QtCore.QSize(180, 16777215))
        self.widget_40.setObjectName("widget_40")
        self.horizontalLayout_56 = QtWidgets.QHBoxLayout(self.widget_40)
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName("horizontalLayout_56")
        self.z_powder_temp = QtWidgets.QSpinBox(self.widget_40)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.z_powder_temp.sizePolicy().hasHeightForWidth())
        self.z_powder_temp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.z_powder_temp.setFont(font)
        self.z_powder_temp.setStyleSheet("")
        self.z_powder_temp.setMinimum(-60)
        self.z_powder_temp.setProperty("value", 15)
        self.z_powder_temp.setObjectName("z_powder_temp")
        self.horizontalLayout_56.addWidget(self.z_powder_temp)
        self.gridLayout_6.addWidget(self.widget_40, 1, 1, 1, 1)
        self.label_83 = QtWidgets.QLabel(self.groupBox)
        self.label_83.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_83.setFont(font)
        self.label_83.setObjectName("label_83")
        self.gridLayout_6.addWidget(self.label_83, 4, 0, 1, 1)
        self.label_85 = QtWidgets.QLabel(self.groupBox)
        self.label_85.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_85.setFont(font)
        self.label_85.setObjectName("label_85")
        self.gridLayout_6.addWidget(self.label_85, 6, 0, 1, 1)
        self.label_82 = QtWidgets.QLabel(self.groupBox)
        self.label_82.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_82.setFont(font)
        self.label_82.setObjectName("label_82")
        self.gridLayout_6.addWidget(self.label_82, 3, 0, 1, 1)
        self.label_81 = QtWidgets.QLabel(self.groupBox)
        self.label_81.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_81.setFont(font)
        self.label_81.setObjectName("label_81")
        self.gridLayout_6.addWidget(self.label_81, 2, 0, 1, 1)
        self.label_80 = QtWidgets.QLabel(self.groupBox)
        self.label_80.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_80.setFont(font)
        self.label_80.setObjectName("label_80")
        self.gridLayout_6.addWidget(self.label_80, 1, 0, 1, 1)
        self.label_79 = QtWidgets.QLabel(self.groupBox)
        self.label_79.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_79.setFont(font)
        self.label_79.setObjectName("label_79")
        self.gridLayout_6.addWidget(self.label_79, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(conditions)
        QtCore.QMetaObject.connectSlotsByName(conditions)

    def retranslateUi(self, conditions):
        _translate = QtCore.QCoreApplication.translate
        conditions.setWindowTitle(_translate("conditions", "Form"))
        self.groupBox.setTitle(_translate("conditions", "Zeroing conditions "))
        self.label_84.setText(_translate("conditions", "Angle:"))
        self.z_pressure.setSuffix(_translate("conditions", " mmHg"))
        self.z_angle.setSuffix(_translate("conditions", "°"))
        self.z_temp.setSuffix(_translate("conditions", " °C"))
        self.z_humidity.setSuffix(_translate("conditions", " %"))
        self.z_azimuth.setSuffix(_translate("conditions", "°"))
        self.z_latitude.setSuffix(_translate("conditions", "°"))
        self.z_powder_temp.setSuffix(_translate("conditions", " °C"))
        self.label_83.setText(_translate("conditions", "Latitude"))
        self.label_85.setText(_translate("conditions", "Azimuth:"))
        self.label_82.setText(_translate("conditions", "Pressure:"))
        self.label_81.setText(_translate("conditions", "Humidity:"))
        self.label_80.setText(_translate("conditions", "Powder Temperature:"))
        self.label_79.setText(_translate("conditions", "Temperature:"))
import res_rc

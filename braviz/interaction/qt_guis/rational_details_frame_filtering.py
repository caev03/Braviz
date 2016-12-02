# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\braviz\braviz\interaction\qt_guis\rational_details_frame_filtering.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_rational_details(object):
    def setupUi(self, rational_details):
        rational_details.setObjectName(_fromUtf8("rational_details"))
        rational_details.resize(419, 231)
        rational_details.setFrameShape(QtGui.QFrame.NoFrame)
        rational_details.setFrameShadow(QtGui.QFrame.Raised)
        self.gridLayout = QtGui.QGridLayout(rational_details)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.optimum_val = QtGui.QSpinBox(rational_details)
        self.optimum_val.setMaximum(100)
        self.optimum_val.setObjectName(_fromUtf8("optimum_val"))
        self.gridLayout.addWidget(self.optimum_val, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(rational_details)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 6, 4, 1, 1)
        self.label_6 = QtGui.QLabel(rational_details)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.th_spin = QtGui.QDoubleSpinBox(rational_details)
        self.th_spin.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.th_spin.setObjectName(_fromUtf8("th_spin"))
        self.gridLayout.addWidget(self.th_spin, 6, 5, 1, 1)
        self.label_2 = QtGui.QLabel(rational_details)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 4, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.optimum_real_value = QtGui.QLabel(rational_details)
        self.optimum_real_value.setObjectName(_fromUtf8("optimum_real_value"))
        self.gridLayout.addWidget(self.optimum_real_value, 2, 3, 1, 1)
        self.label_3 = QtGui.QLabel(rational_details)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.horizontalSlider = QtGui.QSlider(rational_details)
        self.horizontalSlider.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setPageStep(10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtGui.QSlider.NoTicks)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.gridLayout.addWidget(self.horizontalSlider, 4, 0, 1, 7)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 8, 0, 1, 1)
        self.label = QtGui.QLabel(rational_details)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.minimum_val = QtGui.QDoubleSpinBox(rational_details)
        self.minimum_val.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.minimum_val.setMaximum(9999.0)
        self.minimum_val.setObjectName(_fromUtf8("minimum_val"))
        self.gridLayout.addWidget(self.minimum_val, 1, 1, 1, 1)
        self.maximum_val = QtGui.QDoubleSpinBox(rational_details)
        self.maximum_val.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.maximum_val.setMaximum(9999999.0)
        self.maximum_val.setObjectName(_fromUtf8("maximum_val"))
        self.gridLayout.addWidget(self.maximum_val, 1, 5, 1, 1)
        self.label_4 = QtGui.QLabel(rational_details)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)
        self.operation_combo = QtGui.QComboBox(rational_details)
        self.operation_combo.setObjectName(_fromUtf8("operation_combo"))
        self.operation_combo.addItem(_fromUtf8(""))
        self.operation_combo.addItem(_fromUtf8(""))
        self.operation_combo.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.operation_combo, 6, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 0, 1, 1)
        self.label_2.setBuddy(self.maximum_val)
        self.label.setBuddy(self.minimum_val)

        self.retranslateUi(rational_details)
        QtCore.QObject.connect(self.optimum_val, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.horizontalSlider.setValue)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.optimum_val.setValue)
        QtCore.QMetaObject.connectSlotsByName(rational_details)

    def retranslateUi(self, rational_details):
        rational_details.setWindowTitle(_translate("rational_details", "Frame", None))
        self.optimum_val.setSuffix(_translate("rational_details", "%", None))
        self.label_5.setText(_translate("rational_details", "Threshold:", None))
        self.label_6.setText(_translate("rational_details", "Operation:", None))
        self.label_2.setToolTip(_translate("rational_details", "Select the expected maximum value for this variable", None))
        self.label_2.setText(_translate("rational_details", "Maximum", None))
        self.optimum_real_value.setText(_translate("rational_details", "0", None))
        self.label_3.setToolTip(_translate("rational_details", "Select the optimal value for this value, the value that would be considered \"good\"", None))
        self.label_3.setText(_translate("rational_details", "Optimum", None))
        self.label.setToolTip(_translate("rational_details", "Select the expected minimum value for this variable", None))
        self.label.setText(_translate("rational_details", "Minimum", None))
        self.label_4.setText(_translate("rational_details", " = ", None))
        self.operation_combo.setItemText(0, _translate("rational_details", ">", None))
        self.operation_combo.setItemText(1, _translate("rational_details", "<", None))
        self.operation_combo.setItemText(2, _translate("rational_details", "=", None))


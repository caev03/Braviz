# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\braviz\braviz\interaction\qt_guis\ortho_measure_start.ui'
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

class Ui_OpenMeasureApp(object):
    def setupUi(self, OpenMeasureApp):
        OpenMeasureApp.setObjectName(_fromUtf8("OpenMeasureApp"))
        OpenMeasureApp.setWindowModality(QtCore.Qt.ApplicationModal)
        OpenMeasureApp.resize(400, 300)
        OpenMeasureApp.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(OpenMeasureApp)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(OpenMeasureApp)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.load_roi_button = QtGui.QPushButton(self.frame)
        self.load_roi_button.setObjectName(_fromUtf8("load_roi_button"))
        self.gridLayout.addWidget(self.load_roi_button, 1, 2, 1, 1)
        self.new_roi_button = QtGui.QPushButton(self.frame)
        self.new_roi_button.setObjectName(_fromUtf8("new_roi_button"))
        self.gridLayout.addWidget(self.new_roi_button, 0, 2, 1, 1)
        self.load_scenario = QtGui.QPushButton(self.frame)
        self.load_scenario.setObjectName(_fromUtf8("load_scenario"))
        self.gridLayout.addWidget(self.load_scenario, 2, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(OpenMeasureApp)
        QtCore.QMetaObject.connectSlotsByName(OpenMeasureApp)

    def retranslateUi(self, OpenMeasureApp):
        OpenMeasureApp.setWindowTitle(_translate("OpenMeasureApp", "Measure", None))
        self.load_roi_button.setText(_translate("OpenMeasureApp", "Load Measure", None))
        self.new_roi_button.setText(_translate("OpenMeasureApp", "New Measure", None))
        self.load_scenario.setText(_translate("OpenMeasureApp", "Load Scenario", None))


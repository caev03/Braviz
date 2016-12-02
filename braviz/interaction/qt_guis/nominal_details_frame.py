# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\braviz\braviz\interaction\qt_guis\nominal_details_frame.ui'
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

class Ui_nominal_details_frame(object):
    def setupUi(self, nominal_details_frame):
        nominal_details_frame.setObjectName(_fromUtf8("nominal_details_frame"))
        nominal_details_frame.setFrameShape(QtGui.QFrame.NoFrame)
        nominal_details_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.verticalLayout = QtGui.QVBoxLayout(nominal_details_frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labels_names_table = QtGui.QTableView(nominal_details_frame)
        self.labels_names_table.setObjectName(_fromUtf8("labels_names_table"))
        self.labels_names_table.horizontalHeader().setStretchLastSection(True)
        self.labels_names_table.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.labels_names_table)

        self.retranslateUi(nominal_details_frame)
        QtCore.QMetaObject.connectSlotsByName(nominal_details_frame)

    def retranslateUi(self, nominal_details_frame):
        pass


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\braviz\braviz\interaction\qt_guis\multiple_rois.ui'
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

class Ui_MultipleRoisDialog(object):
    def setupUi(self, MultipleRoisDialog):
        MultipleRoisDialog.setObjectName(_fromUtf8("MultipleRoisDialog"))
        MultipleRoisDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        MultipleRoisDialog.resize(400, 300)
        MultipleRoisDialog.setSizeGripEnabled(True)
        MultipleRoisDialog.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(MultipleRoisDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableView = QtGui.QTableView(MultipleRoisDialog)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableView)
        self.buttonBox = QtGui.QDialogButtonBox(MultipleRoisDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(MultipleRoisDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), MultipleRoisDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), MultipleRoisDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(MultipleRoisDialog)

    def retranslateUi(self, MultipleRoisDialog):
        MultipleRoisDialog.setWindowTitle(_translate("MultipleRoisDialog", "Multiple Rois", None))


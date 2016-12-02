# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\braviz\braviz\interaction\qt_guis\load_sub_sample_dialog.ui'
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

class Ui_LoadSampleDialog(object):
    def setupUi(self, LoadSampleDialog):
        LoadSampleDialog.setObjectName(_fromUtf8("LoadSampleDialog"))
        LoadSampleDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        LoadSampleDialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(LoadSampleDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.Layout = QtGui.QFrame(LoadSampleDialog)
        self.Layout.setFrameShape(QtGui.QFrame.NoFrame)
        self.Layout.setFrameShadow(QtGui.QFrame.Raised)
        self.Layout.setObjectName(_fromUtf8("Layout"))
        self.gridLayout = QtGui.QGridLayout(self.Layout)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableView = QtGui.QTableView(self.Layout)
        self.tableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.Layout)
        self.buttonBox = QtGui.QDialogButtonBox(LoadSampleDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(LoadSampleDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), LoadSampleDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), LoadSampleDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LoadSampleDialog)

    def retranslateUi(self, LoadSampleDialog):
        LoadSampleDialog.setWindowTitle(_translate("LoadSampleDialog", "Select Sub Sample", None))


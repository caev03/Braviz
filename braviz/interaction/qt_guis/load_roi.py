# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\braviz\braviz\interaction\qt_guis\load_roi.ui'
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

class Ui_LoadRoiDialog(object):
    def setupUi(self, LoadRoiDialog):
        LoadRoiDialog.setObjectName(_fromUtf8("LoadRoiDialog"))
        LoadRoiDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        LoadRoiDialog.resize(400, 300)
        LoadRoiDialog.setSizeGripEnabled(True)
        LoadRoiDialog.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(LoadRoiDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableView = QtGui.QTableView(LoadRoiDialog)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableView)
        self.buttonBox = QtGui.QDialogButtonBox(LoadRoiDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Open)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(LoadRoiDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), LoadRoiDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), LoadRoiDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LoadRoiDialog)

    def retranslateUi(self, LoadRoiDialog):
        LoadRoiDialog.setWindowTitle(_translate("LoadRoiDialog", "Load ROI", None))

